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

  // ───────────────────────── INIT ─────────────────────────

  Future<void> initialize() async {
    _haConnected = await _ha.ping();
    notifyListeners();
  }

  Future<void> interrupt() async {
    await _conversation.interrupt();

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
        if (_state == JarvisState.speaking) {
          _conversation.interrupt();
        }
        
        handleTextInput(input ?? 'licht an');
        break;

      case JarvisEvent.voiceStarted:
        if (!isBusy) {
          _setState(JarvisState.listening);
        }
        // später: Mic aktiv, UI Feedback
        break;

      case JarvisEvent.voiceStopped:
        if (state == JarvisState.listening) {
          _setState(JarvisState.thinking);
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
      await _conversation.interrupt();

      _lastResponse = result;
      _responseText = result.message;
      _liveTranscript = 'EXTERNAL TRIGGER: ${source.toUpperCase()}';

      _addHistoryEntry(
        text: result.message, 
        isUser: false
      );

      if (result.success) {
        if (source == 'android-service') {
          _setState(JarvisState.idle);
        } else {
          _setState(JarvisState.speaking);
        }
      } else {
        _setState(JarvisState.error);
      }
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

  Future<void> _handleIntent(JarvisIntent intent) async {
    try {
      await _conversation.interrupt();
      _setState(JarvisState.thinking);
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
    }
  }

  // ───────────────────────── STATE HELPER ─────────────────────────

  void _setState(JarvisState state) {
    _state = state;
    notifyListeners();
  }
}