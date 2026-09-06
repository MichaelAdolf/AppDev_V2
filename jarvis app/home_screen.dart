import 'package:flutter/material.dart';
import 'dart:async';
import '../services/thinking_feedback_service.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_state.dart';
import '../../../core/ha_response.dart';
import '../logic/jarvis_controller.dart';
import '../widgets/jarvis_circle.dart';
import '../../../services/voice_service.dart';
import '../widgets/background_grid.dart';
import '../widgets/hud_panel.dart';
import '../widgets/ambient_particles.dart';
import '../widgets/conversation_timeline.dart';
import '../widgets/hud_overlay.dart';
import '../widgets/ambient_connections.dart';
import '../../../services/jarvis_wakeword_bus.dart';
import '../../../services/jarvis_wakeword_control.dart';
import 'package:flutter/widgets.dart';
import '../../../core/speech_output_mode.dart';
import '../../../services/speech_output_service.dart';

class HomeScreen extends StatefulWidget {
  final JarvisController controller;
  final ThinkingFeedbackService _thinkingFeedbackService = ThinkingFeedbackService();
  
  jarvisState? _previousJarvisState;
  int? _observedInteractionId;
  bool _isInterrupting = false;

  const HomeScreen({
    super.key,
    required this.controller,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with WidgetsBindingObserver{
  StreamSubscription? _wakewordSubscription;

  bool _isSpeaking = false;
  bool _wakewordEnabled = true;
  SpeechOutputMode _speechOutputMode = SpeechOutputMode.appTts;

  late final JarvisController controller;
  late final VoidCallback _controllerListener;
  late final SpeechOutputService _speechOutput;
  
  final VoiceService _voice = VoiceService();

  @override
  void initState() {
    super.initState();

    WidgetsBinding.instance.addObserver(this);

    controller = widget.controller;

    _speechOutput = SpeechOutputService(
      initialMode: _speechOutputMode,
    );
    
    _controllerListener = _handleControllerChanged;
    
    controller.addListener(_controllerListener);
    controller.initialize();
    _voice.initialize();

    _wakewordSubscription = JarvisWakewordBus.stream.listen(
      (_) async {
        
        if (!_wakewordEnabled)
        {
          return;
        }

        debugPrint(
          '[JARVIS] Wakeword Trigger empfangen',
        );

        debugPrint(
          '[JARVIS] Controller State: ${controller.state}',
        );

        debugPrint(
          '[JARVIS] Controller Busy: ${controller.isBusy}',
        );

        if (controller.isBusy) {
          debugPrint(
            '[JARVIS] Wakeword ignoriert - Controller Busy',
          );
          return;
        }
        await _startVoiceInput();
      },
    );
  }

  @override
  void dispose() {
    _wakewordSubscription?.cancel();
    
    controller.removeListener(_controllerListener);
    
    WidgetsBinding.instance.removeObserver(this);

    unawaited(_speechOutput.stop());
    unawaited(_voice.stopListening());

    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(
    AppLifecycleState state,
  ) async {
    debugPrint(
      '[Jarvis] Lifecycle: $state',
    );

    if (
      state == AppLifecycleState.paused
      ) {
        debugPrint(
          '[Jarvis] App pausiert',
        );

        await _voice.stopListening();
        await _speechOutput.stop();
        await controller.interrupt();
        await JarvisWakewordControl.stop();

        _isSpeaking = false;
      }

    if (
      state == AppLifecycleState.resumed
      ) {
        debugPrint(
          '[Jarvis] App resumed -> voice neu initialisieren',
        );

        await _voice.stopListening();
        await _voice.initialize();
        if (_wakewordEnabled) {
          await JarvisWakewordControl.start();
        }
      }
  }

  Future<void> _startVoiceInput() async {
    await JarvisWakewordControl.stop();

    debugPrint(
      '[JARVIS] Wakeword-Stop angefordert',
    );

    await Future<void>.delayed(
      const Duration(milliseconds: 1200),
    );

    debugPrint(
      '[JARVIS] Mikrofon wird an Flutter übergeben',
    );

    final started = await _voice.startListening(
      onPartialResult: (text) {
        debugPrint(
          '[JARVIS] Partial STT: $text',
        );

        controller.updateLiveTranscript(text);
      },
      onFinalResult: (text) async {
        debugPrint(
          '[JARVIS] Final STT: $text',
        );

        await _voice.stopListening();

        controller.handleEvent(
          JarvisEvent.voiceStopped,
        );

        controller.handleTextInput(text);
      },
    );

    debugPrint(
      '[JARVIS] VoiceService gestartet: $started',
    );

    if (!started) {
      debugPrint(
        '[JARVIS] STT konnte nicht gestartet werden',
      );

      await controller.interrupt();

      if (_wakewordEnabled) {
        await JarvisWakewordControl.start();
      }

      return;
    }

    controller.handleEvent(
      JarvisEvent.voiceStarted,
    );

    Future<void>.delayed(
      const Duration(seconds: 12),
      () async {
        if (!mounted) {
          return;
        }

        if (controller.state != JarvisState.listening) {
          return;
        }

        debugPrint(
          '[JARVIS] Listening Timeout',
        );

        await _voice.cancelListening();
        await _speechOutput.stop();

        controller.clearLiveTranscript();

        await controller.interrupt();

        if (_wakewordEnabled) {
          await JarvisWakewordControl.start();
        }
      },
    );
  }

  void _onMicPressed() async {
    final state = controller.state;

    if (controller.state == JarvisState.listening) {
      await _voiceservice.stopListening();
      return;
    }

    if (state == JarvisState.thinking || 
        state == JarvisState.speaking ||
        state == JarvisState.error) {
      await _interruptCurrentInteraction(
        restartWakeword: false,
      );  
    }
    await _startListening();
  }

  @override
  void dispose()
    _thinkingFeedbackService.dispose();
    _controller.removeListener(_onControllerChanged);

    // Deine bestehende Dispose-Logik bleibt erhalten
    //
    //_speechOutpoutService.dispose();
    //_voiceService.dispose();
    //_controller.dispose();

    super.dispose();
  }

  Future _toggleWakeword() async {

    setState(() { _wakewordEnabled = !_wakewordEnabled; });

    if (_wakewordEnabled) {

    await JarvisWakewordControl.start();

    debugPrint(
      '[JARVIS] Wakeword aktiviert',
    );

    } else {

    await JarvisWakewordControl.stop();

    debugPrint(
      '[JARVIS] Wakeword deaktiviert',
    );
    } 
  }

  void _toggleSpeechOutputMode() {
    final newMode = 
      _speechOutputMode == SpeechOutputMode.appTts
        ? SpeechOutputMode.nodeRedAudio
        : SpeechOutputMode.appTts;

    setState(() {
      _speechOutputMode = newMode;
      }
    );

    _speechOutput.setMode(newMode);

    debugPrint(
      '[JARVIS] Speech Output Mode: ${newMode.name}'
    );
  }

  void _handleControllerChanged() {
    if (!mounted) {
      return;
    }

    final response = controller.lastResponse;

    final shouldStartSpeech =
        controller.state == JarvisState.speaking &&
        !_isSpeaking &&
        response != null &&
        response.message.trim().isNotEmpty;

    if (shouldStartSpeech) {
      unawaited(
        _playCurrentResponse(response),
      );
    }

    setState(() {});
  }

  Future<void> _interruptCurrentInteraction({
    bool restartWakeword = true,
  }) async {
    if (_isInterrupting) {
      return;
    }

    _isInterrupting = true;

    try {
      _thinkingFeedbackService.cancel();

      await _speechOutputService.stop();

      // Falls dein Voice-Service stopListening() statt stop() verwendet,
      // hier den tatsächlichen Methodennamen einsetzen.
      await _voiceService.stopListening();

      _controller.interrupt();

      if (restartWakeword && _wakewordEnabled) {
        await _startNativeWakewordSafely();
      }
    } catch (error, stackTrace) {
      debugPrint(
        'HomeScreen: '
        'Fehler beim Unterbrechen der Interaktion: $error',
      );
      debugPrintStack(stackTrace: stackTrace);
    } finally {
      _isInterrupting = false;
    }
  }

  Future<void> _startNativeWakewordSafely() async {
    if (!_wakewordEnabled) {
      return;
    }

    if (_isStartingNativeWakeword) {
      return;
    }

    _isStartingNativeWakeword = true;

    try {
      // Hier deinen vorhandenen MethodChannel-Aufruf verwenden.
      //
      // Beispiel:
      // await _platform.invokeMethod('startWakeword');

      await _startNativeWakeword();
    } catch (error, stackTrace) {
      debugPrint(
        'HomeScreen: '
        'Native Wakeword konnte nicht gestartet werden: $error',
      );
      debugPrintStack(stackTrace: stackTrace);
    } finally {
      _isStartingNativeWakeword = false;
    }
  }

  void _onControllerChanged() {
    if (!mounted) {
      return;
    }

    final currentState = _controller.state;
    final currentInteractionId = _controller.activeInteractionId;

    final stateChanged =
        currentState != _previousJarvisState;

    final interactionChanged =
        currentInteractionId != _observedInteractionId;

    if (!stateChanged && !interactionChanged) {
      return;
    }

    _previousJarvisState = currentState;
    _observedInteractionId = currentInteractionId;

    switch (currentState) {
      case JarvisState.thinking:
        _handleThinkingState(currentInteractionId);
        break;

      case JarvisState.speaking:
        _handleSpeakingState();
        break;

      case JarvisState.error:
        _handleErrorState();
        break;

      case JarvisState.idle:
        _handleIdleState();
        break;

      case JarvisState.listening:
        _thinkingFeedbackService.cancel();
        break;
    }

    setState(() {});
  }

  void _handleThinkingState(int? interactionId) {
    if (interactionId == null) {
      return;
    }

    _thinkingFeedbackService.schedule(
      interactionId: interactionId,
      delay: const Duration(milliseconds: 350),
      onPlay: () async {
        if (_controller.state != JarvisState.thinking) {
          return;
        }

        if (_controller.activeInteractionId != interactionId) {
          return;
        }

        debugPrint(
          'HomeScreen: '
          'Thinking-Feedback wäre jetzt für '
          'Interaktion $interactionId gestartet',
        );

        // Sprint 2:
        // Hier wird später "Ich prüfe das" abgespielt.
      },
    );
  }

  Future<void> _handleSpeakingState() async {
    _thinkingFeedbackService.cancel();

    final response = _controller.lastResponse;

    if (response == null) {
      _controller.interrupt();
      return;
    }

    try {
      await _speechOutputService.output(response);

      if (!mounted) {
        return;
      }

      if (_controller.state == JarvisState.speaking) {
        _controller.completeSpeaking();

        if (_wakewordEnabled) {
          await _startNativeWakewordSafely();
        }
      }
    } catch (error, stackTrace) {
      debugPrint(
        'HomeScreen: '
        'Fehler bei der Sprachausgabe: $error',
      );
      debugPrintStack(stackTrace: stackTrace);

      await _interruptCurrentInteraction();
    }
  }

  Future<void> _handleErrorState() async {
    _thinkingFeedbackService.cancel();
    await _speechOutputService.stop();

    if (_wakewordEnabled) {
      await _startNativeWakewordSafely();
    }
  }

  void _handleIdleState() {
    _thinkingFeedbackService.cancel();
  }

  Future<void> _playCurrentResponse(
    HaResponse response,
  ) async {
    if (_isSpeaking) {
      return;
    }

    _isSpeaking = true;

    debugPrint(
      '[JARVIS] Speech Mode: ${_speechOutput.mode.name}',
    );

    debugPrint(
      '[JARVIS] Response Text: ${response.message}',
    );

    debugPrint(
      '[JARVIS] Audio URL: ${response.audioUrl}',
    );

    await JarvisWakewordControl.stop();

    try {
      final completed = await _speechOutput.output(
        response,
      );

      if (!mounted || !completed) {
        return;
      }

      controller.onSpeechFinished();
    } catch (error) {
      debugPrint(
        '[JARVIS] Sprachausgabe fehlgeschlagen: $error',
      );

      if (mounted) {
        controller.onSpeechFinished();
      }
    } finally {
      _isSpeaking = false;

      if (
          mounted &&
          _wakewordEnabled &&
          controller.state == JarvisState.idle) {
        await JarvisWakewordControl.start();
      }
    }
  }

  Color _voiceHudColor() {
    switch (controller.state) {
      case JarvisState.idle:
        return Colors.cyanAccent;
      case JarvisState.listening:
        return Colors.greenAccent;
      case JarvisState.thinking:
        return Colors.yellowAccent;
      case JarvisState.speaking:
        return Colors.greenAccent;
      case JarvisState.error:
        return Colors.redAccent;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(
        children: [

          const Positioned.fill(
            child: BackgroundGrid(),
          ),

          const Positioned.fill(
            child: IgnorePointer(
              child: AmbientParticles(),
            )
          ),

          const Positioned.fill(
            child: AmbientConnections(),
          ),

          const Positioned.fill(
            child: HudOverlay(),
          ),

          Positioned(
            left: 20,
            top: 60,
            child: HudPanel(
              title: 'SYSTEM',
              indicatorColor: controller.haConnected 
                ? Colors.greenAccent 
                : Colors.redAccent,
              lines: [
                controller.haConnected
                    ? 'HA ONLINE'
                    : 'HA OFFLINE',
                'NODE-RED ONLINE',
                'STATE ${controller.state.name.toUpperCase()}',
              ],
            )
          ),

          Positioned(
            right: 20,
            top: 60,
            child: HudPanel(
              title: 'VOICE',
              indicatorColor: _voiceHudColor(),
              lines: [
                'LANG : de-DE',
                'STATE : ${controller.state.name.toUpperCase()}',
                'AUDIO : ${_speechOutputMode.displayName}',
                controller.state == JarvisState.listening
                    ? 'INPUT : ACTIVE'
                    : 'INPUT : READY',
              ],
            ),
          ),

          Positioned(
            left: 20,
            bottom: 170,
            child: HudPanel(
              title: 'COMMAND',
              lines: [
                controller.liveTranscript.isEmpty
                    ? 'WAITING...'
                    : controller.liveTranscript,
              ],
            ),
          ),

          Positioned(
            right: 20,
            bottom: 170,
            child: HudPanel(
              title: 'ENTITY',
              lines: [
                controller.lastResponse?.entity ?? '-',
                controller.lastResponse?.state ?? '-',
              ],
            ),
          ),

          Align(
            alignment: const Alignment(0, -0.3),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [

                // JARVIS KREIS
                GestureDetector(
                  onTap: _onMicPressed,
                  child: JarvisCircle(
                    state: controller.state,
                  ),
                ),

                const SizedBox(height: 10),

                const Text(
                  'J.A.R.V.I.S',
                  style: TextStyle(
                    color: Colors.cyanAccent,
                    fontSize: 32,
                    letterSpacing: 8,
                  ),
                ),

                const SizedBox(height: 20),

                if (controller.liveTranscript.isNotEmpty && controller.state != JarvisState.speaking)
                const SizedBox(height: 18),
                // RESPONSE TEXT
              ],
            ),
          ),
          Positioned(
            right: 20,
            top: 200,
            child: GestureDetector(
              onTap: _toggleWakeword,
              child: AnimatedContainer(
                duration: const Duration(
                  milliseconds: 250,
                ),
                width: 50,
                height: 50,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: _wakewordEnabled
                    ? const Color(0xFF002D72)
                    : Colors.black,
                  border: Border.all(
                    color: Colors.cyanAccent,
                    width: 2,
                    ),
                  boxShadow: _wakewordEnabled
                    ? [
                      BoxShadow(
                        color: Colors.blueAccent
                        .withOpacity(0.7),
                        blurRadius: 20,
                        spreadRadius: 3,
                        ),
                    ]
                    :[],
                ),
                child: Icon(
                  Icons.mic,
                  color: _wakewordEnabled
                    ? Colors.cyanAccent
                    : Colors.grey,
                  size: 34,
                ),
              ),
            ),
          ),
          Positioned(
            left: 0,
            right: 0,
            bottom: 24,
            child: ConversationTimeline(
              entries: controller.history,
            ),
          ),
          Positioned(
            left: 20,
            top: 180,
            child: GestureDetector(
              onTap: _toggleSpeechOutputMode,
              child: AnimatedContainer(
                duration: const Duration(
                  milliseconds: 250,
                ),
                width: 50,
                height: 50,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: _speechOutputMode == SpeechOutputMode.nodeRedAudio
                    ? const Color(0xFF002D72)
                    : Colors.black,
                  border: Border.all(
                    color: Colors.cyanAccent,
                    width: 2,
                    ),
                  boxShadow: _speechOutputMode == SpeechOutputMode.nodeRedAudio
                    ? [
                      BoxShadow(
                        color: Colors.blueAccent
                        .withOpacity(0.7),
                        blurRadius: 20,
                        spreadRadius: 3,
                        ),
                    ]
                    :[],
                ),
                child: Icon(
                  Icons.volume_up,
                  color: _speechOutputMode == SpeechOutputMode.nodeRedAudio
                    ? Colors.cyanAccent
                    : Colors.grey,
                  size: 30,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}