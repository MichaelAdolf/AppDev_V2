import 'package:flutter/material.dart';
import 'dart:async';

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
    if (controller.state == JarvisState.speaking) {
      await _speechOutput.stop();

      _isSpeaking = false;

      await controller.interrupt();
      await _startVoiceInput();

      return;
    }

    if (controller.isBusy) {
      return;
    }

    await _startVoiceInput();
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