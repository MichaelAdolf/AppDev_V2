import 'package:flutter/material.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_state.dart';
import '../../../services/audio_service.dart';
import '../logic/jarvis_controller.dart';
import '../widgets/jarvis_circle.dart';
import '../../../services/voice_service.dart';
import '../widgets/background_grid.dart';
import '../widgets/speech_waveform.dart';
import '../widgets/hud_panel.dart';
import '../widgets/ambient_particles.dart';
import '../widgets/conversation_timeline.dart';
import '../widgets/hud_overlay.dart';
import '../widgets/ambient_connections.dart';

class HomeScreen extends StatefulWidget {
  final JarvisController controller;
  
  const HomeScreen({
    super.key,
    required this.controller,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _isSpeaking = false;
  
  late final JarvisController controller;
  late final VoidCallback _controllerListener;
  
  final VoiceService _voice = VoiceService();

  @override
  void initState() {
    super.initState();

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
          onComplete: () {
            _isSpeaking = false;
            controller.onSpeechFinished();
          },
        );
      }

      setState(() {});
    };

    controller.addListener(_controllerListener);
    controller.initialize();
    _voice.initialize();
  }

  @override
  void dispose() {
    controller.removeListener(_controllerListener);
    super.dispose();
  }

  Future<void> _startVoiceInput() async {
    controller.handleEvent(
      JarvisEvent.voiceStarted,
    );

    await _voice.startListening(
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
                
                if (controller.state == JarvisState.speaking)
                  const Padding(
                    padding: EdgeInsets.only(
                      top: 18,
                    ),
                    child: SpeechWaveform(
                      color: Colors.greenAccent,
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