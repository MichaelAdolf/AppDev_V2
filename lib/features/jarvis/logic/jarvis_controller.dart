import 'package:flutter/material.dart';
import '../../../services/audio_service.dart';
import '../../../core/jarvis_state.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_intent.dart';
import '../../../core/ha_response.dart';
import '../../../services/home_assistant_service.dart';
import '../../../core/jarvis_intent_parser.dart';
import '../../../services/conversation_service.dart';

class JarvisController extends ChangeNotifier {
  final HomeAssistantService _ha;
  final JarvisIntentParser _parser;
  final ConversationService _conversation;

  JarvisController({
    required HomeAssistantService homeAssistantService,
    JarvisIntentParser? parser,
  })  : _ha = homeAssistantService,
        _parser = parser ?? JarvisIntentParser(),
        _conversation = ConversationService(ha: homeAssistantService);

  // ───────────────────────── STATE ─────────────────────────

  JarvisState _state = JarvisState.idle;
  String _responseText = '';
  bool _haConnected = false;
  HaResponse? _lastResponse;

  // ───────────────────────── GETTERS ─────────────────────────

  JarvisState get state => _state;
  String get responseText => _responseText;
  bool get haConnected => _haConnected;

  HaResponse? get lastResponse => _lastResponse;

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

  Future<void>? _currentSpeech;

  Future<void> interrupt() async {
    await _conversation.interrupt();

    _responseText = '';

    _setState(JarvisState.idle);
  }

  // ───────────────────────── INPUT ─────────────────────────

  void handleTextInput(String input) {
    if (_state == JarvisState.speaking || _state == JarvisState.thinking) {
      // Interrupt erlaubt
    }else if (isBusy) {
      return;
    }

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

  void onSpeechFinished() {
    _responseText = '';
    _setState(JarvisState.idle);
  }

  // ───────────────────────── CORE FLOW ─────────────────────────

  Future<void> _handleIntent(JarvisIntent intent) async {
    try {
      await _conversation.interrupt();

      _setState(JarvisState.listening);

      await Future.delayed(const Duration(seconds: 2));

      _setState(JarvisState.thinking);

      final result = await _conversation.execute(intent);

      _lastResponse = result;
      _responseText = result.message;

      if (result.success) {
        _setState(JarvisState.speaking);

      } else {
        _setState(JarvisState.error);
      }
    } catch (e) {
      _responseText = 'Error: $e';
      _setState(JarvisState.error);
    }
  }

  Future<HaResponse> _sendIntentToHA(JarvisIntent intent) {
    return _ha.sendIntent(intent);
  }

  // ───────────────────────── STATE HELPER ─────────────────────────

  void _setState(JarvisState state) {
    _state = state;
    notifyListeners();
  }
}