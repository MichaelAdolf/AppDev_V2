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
  JarvisController({
    required HomeAssistantService homeAssistantService,
    JarvisIntentParser? parser,
  })  : _ha = homeAssistantService,
        _conversation = ConversationService(ha: homeAssistantService);

  final HomeAssistantService _ha;
  final ConversationService _conversation;

  JarvisState _state = JarvisState.idle;
  String _responseText = '';
  String _liveTranscript = '';
  bool _haConnected = false;
  HaResponse? _lastResponse;
  final List<ConversationEntry> _history = <ConversationEntry>[];

  int _interactionSequence = 0;
  int? _activeInteractionId;
  bool _responseReady = false;
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
  bool get responseReady => _responseReady;

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
    _responseReady = false;
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

    if (_state == JarvisState.thinking || _state == JarvisState.speaking) {
      _invalidateActiveInteraction();
    }

    _responseReady = false;
    _lastResponse = null;
    _liveTranscript = text;
    _addHistoryEntry(text: text, isUser: true);

    final intent = JarvisIntent(type: IntentType.unknown, rawText: text);
    unawaited(_handleIntent(intent));
  }

  void handleEvent(JarvisEvent event, {String? input}) {
    if (_isDisposed) return;
    switch (event) {
      case JarvisEvent.userTapped:
        if (input != null && input.trim().isNotEmpty) handleTextInput(input);
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
      case JarvisEvent.commandExecuted:
        break;
      case JarvisEvent.error:
        _invalidateActiveInteraction();
        _responseReady = false;
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
    _beginInteraction();
    _lastResponse = result;
    _responseText = result.message;
    _liveTranscript = 'EXTERNAL TRIGGER: ${source.toUpperCase()}';
    _responseReady = true;
    _addHistoryEntry(text: result.message, isUser: false);
    _setState(JarvisState.thinking);
    _notifySafely();
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
      _storePendingResponse(interactionId, response);
    } on TimeoutException {
      if (!_isInteractionCurrent(interactionId)) return;
      _storePendingResponse(
        interactionId,
        const HaResponse(
          success: false,
          intent: 'timeout',
          entity: '',
          state: 'timeout',
          message:
              'Die Verarbeitung hat zu lange gedauert. Bitte versuche es erneut.',
        ),
      );
    } catch (error, stackTrace) {
      if (!_isInteractionCurrent(interactionId)) return;
      debugPrint('JarvisController: Fehler in Interaktion $interactionId: $error');
      debugPrintStack(stackTrace: stackTrace);
      _storePendingResponse(
        interactionId,
        const HaResponse(
          success: false,
          intent: 'error',
          entity: '',
          state: 'error',
          message: 'Die Anfrage konnte nicht verarbeitet werden.',
        ),
      );
    }
  }

  void _storePendingResponse(int interactionId, HaResponse response) {
    if (!_isInteractionCurrent(interactionId)) return;
    _lastResponse = response;
    _responseText = response.message;
    _responseReady = true;
    _addHistoryEntry(text: response.message, isUser: false);
    _notifySafely();
  }

  /// Darf erst nach vollständig beendeter Thinking-Phrase aufgerufen werden.
  void releasePendingTransition(int interactionId) {
    if (!_isInteractionCurrent(interactionId) || !_responseReady) return;
    final response = _lastResponse;
    if (response == null) return;

    _responseReady = false;
    if (response.success) {
      _setState(JarvisState.speaking);
    } else {
      _finishInteraction(interactionId);
      _setState(JarvisState.error);
    }
  }

  void completeSpeaking() {
    final interactionId = _activeInteractionId;
    if (interactionId != null) _finishInteraction(interactionId);
    if (_isDisposed) return;
    _responseText = '';
    _liveTranscript = '';
    _responseReady = false;
    _setState(JarvisState.idle);
  }

  void onSpeechFinished() => completeSpeaking();

  void _addHistoryEntry({required String text, required bool isUser}) {
    final trimmed = text.trim();
    if (trimmed.isEmpty || _isDisposed) return;
    _history.add(ConversationEntry(text: trimmed, isUser: isUser));
    if (_history.length > 6) _history.removeAt(0);
    _notifySafely();
  }

  int _beginInteraction() {
    _interactionSequence += 1;
    _activeInteractionId = _interactionSequence;
    debugPrint('JarvisController: Interaktion $_activeInteractionId gestartet');
    return _interactionSequence;
  }

  bool _isInteractionCurrent(int id) =>
      !_isDisposed && _activeInteractionId == id;

  void _finishInteraction(int id) {
    if (_activeInteractionId != id) return;
    _activeInteractionId = null;
    debugPrint('JarvisController: Interaktion $id abgeschlossen');
  }

  void _invalidateActiveInteraction() {
    final previous = _activeInteractionId;
    _interactionSequence += 1;
    _activeInteractionId = null;
    if (previous != null) {
      debugPrint('JarvisController: Interaktion $previous ungültig gemacht');
    }
  }

  void _setState(JarvisState state) {
    if (_isDisposed || _state == state) return;
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
