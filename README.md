import 'dart:async';

import 'package:flutter/material.dart';

import '../../../core/conversation_entry.dart';
import '../../../core/ha_response.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_intent.dart';
import '../../../core/jarvis_intent_parser.dart';
import '../../../core/jarvis_state.dart';
import '../../../services/conversation_service.dart';
import '../../../services/home_assistant_service.dart';

class JarvisController extends ChangeNotifier {
  final HomeAssistantService _ha;
  final ConversationService _conversation;

  JarvisController({
    required HomeAssistantService homeAssistantService,
    JarvisIntentParser? parser,
  })  : _ha = homeAssistantService,
        _conversation = ConversationService(ha: homeAssistantService);

  JarvisState _state = JarvisState.idle;
  String _responseText = '';
  String _liveTranscript = '';
  bool _haConnected = false;
  HaResponse? _lastResponse;
  final List<ConversationEntry> _history = <ConversationEntry>[];

  int _interactionSequence = 0;
  int? _activeInteractionId;
  bool _isDisposed = false;

  static const Duration _defaultRequestTimeout = Duration(seconds: 15);

  JarvisState get state => _state;
  String get responseText => _responseText;
  String get liveTranscript => _liveTranscript;
  bool get haConnected => _haConnected;
  HaResponse? get lastResponse => _lastResponse;
  List<ConversationEntry> get history => List.unmodifiable(_history);
  int? get activeInteractionId => _activeInteractionId;
  bool get hasActiveInteraction => _activeInteractionId != null;

  bool get isBusy =>
      _state == JarvisState.listening ||
      _state == JarvisState.thinking ||
      _state == JarvisState.speaking;

  String get stateLabel => _state.name.toUpperCase();
  String get haStatusText =>
      _haConnected ? 'Home Assistant Online' : 'Home Assistant Offline';

  Future<void> initialize() async {
    if (_isDisposed) return;
    _haConnected = await _ha.ping();
    _notifySafely();
  }

  Future<void> interrupt({bool clearLastResponse = true}) async {
    _invalidateActiveInteraction();
    _responseText = '';
    _liveTranscript = '';
    if (clearLastResponse) _lastResponse = null;
    _setState(JarvisState.idle);
  }

  void updateLiveTranscript(String text) {
    if (_isDisposed) return;
    _liveTranscript = text;
    _notifySafely();
  }

  void clearLiveTranscript() {
    if (_isDisposed) return;
    _liveTranscript = '';
    _notifySafely();
  }

  void handleTextInput(String input) {
    if (_isDisposed) return;

    final text = input.trim();
    if (text.isEmpty) return;

    // Ein finaler STT-Text kommt regulär noch im Zustand listening an.
    // Andere aktive Requests werden vor einer neuen Interaktion entwertet.
    if (_state == JarvisState.thinking || _state == JarvisState.speaking) {
      _invalidateActiveInteraction();
    }

    _liveTranscript = text;
    _addHistoryEntry(text: text, isUser: true);

    final intent = JarvisIntent(
      type: IntentType.unknown,
      rawText: text,
    );
    unawaited(_handleIntent(intent));
  }

  void handleEvent(JarvisEvent event, {String? input}) {
    if (_isDisposed) return;

    switch (event) {
      case JarvisEvent.userTapped:
        if (input != null && input.trim().isNotEmpty) {
          handleTextInput(input);
        }
        break;
      case JarvisEvent.voiceStarted:
        if (!isBusy) _setState(JarvisState.listening);
        break;
      case JarvisEvent.voiceStopped:
        if (_state == JarvisState.listening) {
          debugPrint('JarvisController: Spracheingabe beendet');
        }
        break;
      case JarvisEvent.intentReceived:
      case JarvisEvent.commandReceived:
        break;
      case JarvisEvent.commandExecuted:
        if (_lastResponse != null) _setState(JarvisState.speaking);
        break;
      case JarvisEvent.error:
        _invalidateActiveInteraction();
        _responseText = input ?? 'Ein unbekannter Fehler ist aufgetreten';
        _setState(JarvisState.error);
        break;
    }
  }

  Future<void> handleExternalResponse(
    HaResponse result, {
    String source = 'external',
  }) async {
    if (_isDisposed) return;

    _invalidateActiveInteraction();
    final interactionId = _beginInteraction();

    _lastResponse = result;
    _responseText = result.message;
    _liveTranscript = 'EXTERNAL TRIGGER: ${source.toUpperCase()}';
    _addHistoryEntry(text: result.message, isUser: false);

    if (result.success) {
      _setState(JarvisState.speaking);
    } else {
      _finishInteraction(interactionId);
      _setState(JarvisState.error);
    }
  }

  Future<void> _handleIntent(JarvisIntent intent) async {
    final interactionId = _beginInteraction();
    _setState(JarvisState.thinking);

    try {
      final response = await _conversation
          .execute(intent)
          .timeout(_defaultRequestTimeout);

      if (!_isInteractionCurrent(interactionId)) {
        debugPrint(
          'JarvisController: Response für veraltete Interaktion '
          '$interactionId wird verworfen',
        );
        return;
      }

      _processCurrentResponse(
        interactionId: interactionId,
        response: response,
      );
    } on TimeoutException {
      if (!_isInteractionCurrent(interactionId)) return;
      debugPrint('JarvisController: Timeout für Interaktion $interactionId');
      _handleRequestTimeout(interactionId);
    } catch (error, stackTrace) {
      if (!_isInteractionCurrent(interactionId)) {
        debugPrint(
          'JarvisController: Fehler einer veralteten Interaktion '
          '$interactionId wird ignoriert: $error',
        );
        return;
      }

      debugPrint('JarvisController: Fehler in Interaktion $interactionId: $error');
      debugPrintStack(stackTrace: stackTrace);
      _handleRequestError(interactionId: interactionId, error: error);
    }
  }

  void _processCurrentResponse({
    required int interactionId,
    required HaResponse response,
  }) {
    if (!_isInteractionCurrent(interactionId)) return;

    _lastResponse = response;
    _responseText = response.message;
    _addHistoryEntry(text: response.message, isUser: false);

    if (response.success) {
      _setState(JarvisState.speaking);
    } else {
      _finishInteraction(interactionId);
      _setState(JarvisState.error);
    }
  }

  void _handleRequestTimeout(int interactionId) {
    if (!_isInteractionCurrent(interactionId)) return;
    _finishInteraction(interactionId);
    _responseText =
        'Die Verarbeitung hat zu lange gedauert. Bitte versuche es erneut.';
    _addHistoryEntry(text: _responseText, isUser: false);
    _setState(JarvisState.error);
  }

  void _handleRequestError({
    required int interactionId,
    required Object error,
  }) {
    if (!_isInteractionCurrent(interactionId)) return;
    _finishInteraction(interactionId);
    _responseText = 'Die Anfrage konnte nicht verarbeitet werden.';
    _addHistoryEntry(text: _responseText, isUser: false);
    _setState(JarvisState.error);
  }

  void completeSpeaking() {
    final interactionId = _activeInteractionId;
    if (interactionId != null) _finishInteraction(interactionId);
    if (_isDisposed) return;
    _responseText = '';
    _liveTranscript = '';
    _setState(JarvisState.idle);
  }

  void onSpeechFinished() => completeSpeaking();

  void _addHistoryEntry({required String text, required bool isUser}) {
    final trimmedText = text.trim();
    if (trimmedText.isEmpty || _isDisposed) return;

    _history.add(ConversationEntry(text: trimmedText, isUser: isUser));
    if (_history.length > 6) _history.removeAt(0);
    _notifySafely();
  }

  int _beginInteraction() {
    _interactionSequence += 1;
    _activeInteractionId = _interactionSequence;
    debugPrint('JarvisController: Interaktion $_activeInteractionId gestartet');
    return _interactionSequence;
  }

  bool _isInteractionCurrent(int interactionId) =>
      !_isDisposed && _activeInteractionId == interactionId;

  void _finishInteraction(int interactionId) {
    if (_activeInteractionId != interactionId) return;
    debugPrint('JarvisController: Interaktion $interactionId abgeschlossen');
    _activeInteractionId = null;
  }

  void _invalidateActiveInteraction() {
    final previousInteractionId = _activeInteractionId;
    _interactionSequence += 1;
    _activeInteractionId = null;
    if (previousInteractionId != null) {
      debugPrint(
        'JarvisController: Interaktion $previousInteractionId ungültig gemacht',
      );
    }
  }

  void _setState(JarvisState state) {
    if (_isDisposed) return;
    if (_state == state) return;
    _state = state;
    _notifySafely();
  }

  void _notifySafely() {
    if (!_isDisposed) notifyListeners();
  }

  @override
  void dispose() {
    if (_isDisposed) return;
    _invalidateActiveInteraction();
    _isDisposed = true;
    super.dispose();
  }
}
