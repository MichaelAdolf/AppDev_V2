import 'dart:async';

import 'package:flutter/material.dart';
import '../../../core/jarvis_state.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_intent.dart';
import '../../../core/ha_response.dart';
import '../../../services/home_assistant_service.dart';
import '../../../core/jarvis_intent_parser.dart';
import '../../../services/conversation_service.dart';
import '../../../core/conversation_entry.dart';

class JarvisController extends ChangeNotifier {
  final HomeAssistantService _ha;
  final ConversationService _conversation;

  JarvisController({
    required HomeAssistantService homeAssistantService,
    JarvisIntentParser? parser,
  })  : _ha = homeAssistantService,
        _conversation = ConversationService(ha: homeAssistantService);

  // ───────────────────────── STATE ─────────────────────────

  JarvisState _state = JarvisState.idle;
  String _responseText = '';
  String _liveTranscript = '';
  bool _haConnected = false;
  HaResponse? _lastResponse;
  final List<ConversationEntry> _history = [];
  int _interactionSequence = 0;
  int? _activeInteractionId;

  bool _isDisposed = false;

  static const Duration _defaultRequestTimeout = Duration(seconds: 15);

  // ───────────────────────── GETTERS ─────────────────────────

  JarvisState get state => _state;
  String get responseText => _responseText;
  String get liveTranscript => _liveTranscript;
  bool get haConnected => _haConnected;

  HaResponse? get lastResponse => _lastResponse;
  List<ConversationEntry> get history => List.unmodifiable(_history);

  bool get isBusy =>
    _state == JarvisState.listening || 
    _state == JarvisState.thinking || 
    _state == JarvisState.speaking;

  String get stateLabel => _state.name.toUpperCase();

  String get haStatusText =>
      _haConnected ? 'Home Assistant Online' : 'Home Assistant Offline';

  int? get activeInteractionId => _activeInteractionId;

  bool get hasActiveInteraction => _activeInteractionId != null;

  // ───────────────────────── INIT ─────────────────────────

  Future<void> initialize() async {
    _haConnected = await _ha.ping();
    notifyListeners();
  }

  Future<void> interrupt() async {
    _responseText = '';
    _liveTranscript = '';
    _setState(JarvisState.idle);
  }

  void updateLiveTranscript(String text) {
    _liveTranscript = text;
    notifyListeners();
  }

  void clearLiveTranscript() {
    _liveTranscript = '';
    notifyListeners();
  }

  void _addHistoryEntry({required String text, required bool isUser}) {
    final trimmedText = text.trim();
    if (trimmedText.isEmpty) return;
    _history.add(ConversationEntry(text: trimmedText, isUser: isUser));

    if (_history.length > 6) {
      _history.removeAt(0);
    }
    notifyListeners();
  }

  int _beginInteraction() {
    _interactionSequence += 1;
    _activeInteractionId = _interactionSequence;

    debugPrint(
      'JarvisController: '
      'Interaktion $_activeInteractionId gestartet',
    );

    return _interactionSequence;
  }

  bool _isInteractionCurrent(int interactionId) {
    return !_isDisposed &&
        _activeInteractionId == interactionId;
  }

  void _finishInteraction(int interactionId) {
    if (_activeInteractionId != interactionId) {
      return;
    }

    debugPrint(
      'JarvisController: '
      'Interaktion $interactionId abgeschlossen',
    );

    _activeInteractionId = null;
  }

  void _invalidateActiveInteraction() {
    final previousInteractionId = _activeInteractionId;

    _interactionSequence += 1;
    _activeInteractionId = null;

    if (previousInteractionId != null) {
      debugPrint(
        'JarvisController: '
        'Interaktion $previousInteractionId ungültig gemacht',
      );
    }
  }
  // ───────────────────────── INPUT ─────────────────────────

  void handleTextInput(String input) {
    if (_state == JarvisState.speaking || _state == JarvisState.thinking) {
      // Interrupt erlaubt
    }else if (isBusy) {
      return;
    }

    _liveTranscript = input;

    _addHistoryEntry(
      text: input, 
      isUser: true,
    );

    final intent = JarvisIntent(type: IntentType.unknown, rawText: input);
    _handleIntent(intent);
  }

  void handleEvent(JarvisEvent event, {String? input}) {
    switch (event) {
      case JarvisEvent.userTapped:
        handleTextInput(input ?? 'licht an');
        // später: Mic aktiv, UI Feedback
        break;

      case JarvisEvent.voiceStarted:
        if (!isBusy) {
          _setState(JarvisState.listening);
        }
        // später: Mic aktiv, UI Feedback
        break;

      case JarvisEvent.voiceStopped:
        if (state == JarvisState.listening) {
          debugPrint('JarvisController: Spracheingabe beendet');
        }
        // später: Speech-to-text finalize
        break;

      case JarvisEvent.intentReceived:
        // optional Logging / Debug
        break;

      case JarvisEvent.commandReceived:
        // später: HA Input verarbeitet
        break;

      case JarvisEvent.commandExecuted:
        _setState(JarvisState.speaking);
        // später: Erfolg / Feedback
        break;

      case JarvisEvent.error:
        _responseText = input ?? 'Ein unbekannter Fehler ist aufgetreten';
        _setState(JarvisState.error);
        // später: UI Error State
        break;
    }
  }

  void onSpeechFinished() async {
    _responseText = '';
    _liveTranscript = '';
    _setState(JarvisState.idle);
  }

  Future<void> handleExternalResponse(
    HaResponse result, {
      String source = 'external',
  }) async {
    try {
      _lastResponse = result;
      _responseText = result.message;
      _liveTranscript = 'EXTERNAL TRIGGER: ${source.toUpperCase()}';

      _addHistoryEntry(
        text: result.message, 
        isUser: false
      );

      if (result.success) {
          _setState(JarvisState.speaking);
      } else {
        _setState(JarvisState.error);
      };
    } catch (e) {
      _responseText = 'Extetrnal trigger error: $e';

      _addHistoryEntry(
        text: 'Extetrnal trigger error: $e', 
        isUser: false,
      );

      _setState(JarvisState.error);
    }
  }

  // ───────────────────────── CORE FLOW ─────────────────────────

  Future<void> _handleIntent(/* dein bestehender Intent-Typ */ intent) async {
    final interactionId = _beginInteraction();

    _setState(JarvisState.thinking);

    try {
      final response = await _conversation
          .execute(intent)
          .timeout(_defaultRequestTimeout);

      if (!_isInteractionCurrent(interactionId)) {
        debugPrint(
          'JarvisController: '
          'Response für veraltete Interaktion '
          '$interactionId wird verworfen',
        );
        return;
      }

      final result = await _conversation.execute(intent);
      
      _lastResponse = result;
      _responseText = result.message;
      
      _addHistoryEntry(
        text: result.message, 
        isUser: false,
      );

      if (result.success) {
        _setState(JarvisState.speaking);

      } else {
        _setState(JarvisState.error);
      }
    } catch (e) {
      _responseText = 'Error: $e';

      _addHistoryEntry(
        text: 'Error: $e', 
        isUser: false,
      );

      _setState(JarvisState.error);
      _processCurrentResponse(
            interactionId: interactionId,
            response: response,
          );
        } on TimeoutException {
          if (!_isInteractionCurrent(interactionId)) {
            return;
          }

          debugPrint(
            'JarvisController: '
            'Timeout für Interaktion $interactionId',
          );

          _handleRequestTimeout(interactionId);
        } catch (error, stackTrace) {
          if (!_isInteractionCurrent(interactionId)) {
            debugPrint(
              'JarvisController: '
              'Fehler einer veralteten Interaktion '
              '$interactionId wird ignoriert: $error',
            );
            return;
          }

          debugPrint(
            'JarvisController: '
            'Fehler in Interaktion $interactionId: $error',
          );
          debugPrintStack(stackTrace: stackTrace);

          _handleRequestError(
            interactionId: interactionId,
            error: error,
          );
        }
      }

  // ───────────────────────── STATE HELPER ─────────────────────────

  void _setState(JarvisState state) {
    _state = state;
    notifyListeners();
  }

  void _processCurrentResponse({
    required int interactionId,
    required HaResponse response,
  }) {
    if (!_isInteractionCurrent(interactionId)) {
      return;
    }

    lastResponse = response;

    // Hier deinen bestehenden History-Eintrag beibehalten.
    //
    // Beispiel:
    // _conversationHistory.add(
    //   ConversationEntry.assistant(response.message),
    // );

    if (response.success) {
      _setState(JarvisState.speaking);
      return;
    }

    _finishInteraction(interactionId);
    _setState(JarvisState.error);
  }

  void _handleRequestTimeout(int interactionId) {
    if (!_isInteractionCurrent(interactionId)) {
      return;
    }

    _finishInteraction(interactionId);

    lastUserText = lastUserText;

    // Verwende hier deinen bereits vorhandenen Mechanismus
    // für eine lokale Fehlerantwort.
    //
    // Falls HaResponse einen passenden Konstruktor besitzt:
    //
    // lastResponse = HaResponse(
    //   success: false,
    //   message: 'Die Verarbeitung hat zu lange gedauert.',
    // );
    //
    // Passe den Konstruktor an dein tatsächliches Modell an.

    _setState(JarvisState.error);
  }

  void _handleRequestError({
    required int interactionId,
    required Object error,
  }) {
    if (!_isInteractionCurrent(interactionId)) {
      return;
    }

    _finishInteraction(interactionId);

    // Hier deinen bisherigen Catch-Fehlerpfad verwenden.
    //
    // Beispiel:
    // lastResponse = HaResponse(
    //   success: false,
    //   message: 'Die Anfrage konnte nicht verarbeitet werden.',
    // );

    _setState(JarvisState.error);
  }

  void completeSpeaking() {
    final interactionId = _activeInteractionId;

    if (interactionId != null) {
      _finishInteraction(interactionId);
    }

    if (_isDisposed) {
      return;
    }

    _setState(JarvisState.idle);
  }
}