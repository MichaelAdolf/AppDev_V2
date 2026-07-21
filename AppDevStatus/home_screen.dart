import 'package:flutter/material.dart';
import 'package:meta/meta.dart';
import 'dart:async';

import '../../../core/constants.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_state.dart';
import '../../../services/audio_service.dart';
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
  
  late final JarvisController controller;
  late final VoidCallback _controllerListener;
  
  final VoiceService _voice = VoiceService();

  @override
  void initState() {
    super.initState();

    WidgetsBinding.instance.addObserver(this);

    controller = widget.controller;
    
    _controllerListener = () {
      if (!mounted) return;

      //Audio hier triggern, NICHT im Controller
      if (controller.state == JarvisState.speaking && 
          !_isSpeaking && 
          controller.responseText.isNotEmpty) {

        _isSpeaking = true;

        AudioService.speak(
          controller.responseText,
          onComplete: () async {
            _isSpeaking = false;
            controller.onSpeechFinished();

            if (_wakewordEnabled) {
              await JarvisWakewordControl.start();
            }
          },
        );
      }

      setState(() {});
    };

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
        await controller.interrupt();
        await JarvisWakewordControl.stop();
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

    await Future.delayed(
      const Duration(milliseconds: 500)
    );

    debugPrint(
      '[JARVIS] Wakeword gestoppt',
    );

    final started = await _voice.startListening(
      onPartialResult: (text) {
        controller.updateLiveTranscript(text);
      },

      onFinalResult: (text) {
        
        controller.handleEvent(
          JarvisEvent.voiceStopped,
        );
        
        controller.handleTextInput(text);
      },
    );

    debugPrint(
      '[JARVIS] startListening verlassen',
    );

    if (started) {
      controller.handleEvent(
        JarvisEvent.voiceStarted,
      );
      Future.delayed(
        const Duration(seconds: 12),
        () async {
          if (
            controller.state ==
            JarvisState.listening
          ) {
            debugPrint(
              '[JARVIS] Listening Timeout',
            );

            await _voice.stopListening();

            controller.clearLiveTranscript();

            await controller.interrupt();

            if (_wakewordEnabled) {
              await JarvisWakewordControl.start();
            }
            }
          }
          );
    } else {
      debugPrint(
        '[JARVIS] STT konnte nicht gestartet werden',
      );
      if (_wakewordEnabled) {
        await JarvisWakewordControl.start();
      }
    }
  }

  void _onMicPressed() async {
    if (controller.state == JarvisState.speaking) {
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
            top: 180,
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
        ],
      ),
    );
  }
}