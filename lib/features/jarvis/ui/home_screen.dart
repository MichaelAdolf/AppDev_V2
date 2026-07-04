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
  

  Color _micColor() {
    switch (controller.state) {
      case JarvisState.idle:
        return Colors.white24;

      case JarvisState.listening:
        return Colors.blueAccent;

      case JarvisState.thinking:
        return Colors.orangeAccent;

      case JarvisState.speaking:
        return Colors.greenAccent;

      case JarvisState.error:
        return Colors.redAccent;
    }
  }

  IconData _micIcon() {
    switch (controller.state) {
      case JarvisState.listening:
        return Icons.mic;

      case JarvisState.thinking:
        return Icons.sync;

      case JarvisState.speaking:
        return Icons.volume_up;

      case JarvisState.error:
        return Icons.error;

      case JarvisState.idle:
        return Icons.mic_none;
    }
  }

  String _statusText() {
    switch (controller.state) {
      case JarvisState.idle:
        return 'Tap to send command';

      case JarvisState.listening:
        return 'Listening...';

      case JarvisState.thinking:
        return 'Sending to Home Assistant...';

      case JarvisState.speaking:
        return 'Jarvis spricht ...';

      case JarvisState.error:
        return 'Error';
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
          Positioned(
            left: 20,
            top: 120,
            child: HudPanel(
              title: 'SYSTEM',
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
            top: 120,
            child: HudPanel(
              title: 'VOICE',
              lines: [
                'de-DE',
                controller.state.name.toUpperCase(),
                controller.state == JarvisState.listening
                    ? 'MIC ACTIVE'
                    : 'MIC IDLE',
              ],
            ),
          ),

          Positioned(
            left: 20,
            bottom: 180,
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
            bottom: 180,
            child: HudPanel(
              title: 'ENTITY',
              lines: [
                controller.lastResponse?.entity ?? '-',
                controller.lastResponse?.state ?? '-',
              ],
            ),
          ),

          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // HA STATUS

                Container(
                  margin: const EdgeInsets.only(
                    bottom: 25,
                  ),
                  padding: const EdgeInsets.symmetric(
                    horizontal: 14,
                    vertical: 8,
                  ),
                  decoration: BoxDecoration(
                    borderRadius:
                        BorderRadius.circular(20),
                    color: controller.haConnected
                        ? Colors.green.withValues(
                            alpha: 0.15,
                          )
                        : Colors.red.withValues(
                            alpha: 0.15,
                          ),
                    border: Border.all(
                      color: controller.haConnected
                          ? Colors.greenAccent
                          : Colors.redAccent,
                    ),
                  ),
                  child: Row(
                    mainAxisSize:
                        MainAxisSize.min,
                    children: [
                      Icon(
                        controller.haConnected
                            ? Icons.cloud_done
                            : Icons.cloud_off,
                        color: controller.haConnected
                            ? Colors.greenAccent
                            : Colors.redAccent,
                        size: 18,
                      ),

                      const SizedBox(width: 8),

                      Text(
                        controller.haStatusText,
                        style: TextStyle(
                          color:
                              controller.haConnected
                                  ? Colors.greenAccent
                                  : Colors.redAccent,
                        ),
                      ),
                    ],
                  ),
                ),

                // JARVIS KREIS

                JarvisCircle(
                  state: controller.state,
                ),
                
                if (controller.state == JarvisState.listening)
                  const Padding(
                    padding: EdgeInsets.only(
                      top: 18,
                    ),
                    child: SpeechWaveform(
                      color: Colors.greenAccent,
                    ),
                  ),

                const SizedBox(height: 30),

                const Text(
                  'JARVIS',
                  style: TextStyle(
                    color: Colors.cyanAccent,
                    fontSize: 32,
                    letterSpacing: 8,
                  ),
                ),

                const SizedBox(height: 10),

                Text(
                  controller.stateLabel,
                  style: const TextStyle(
                    color: Colors.white70,
                    fontSize: 16,
                  ),
                ),

                const SizedBox(height: 10),

                Text(
                  _statusText(),
                  style: const TextStyle(
                    color: Colors.white38,
                  ),
                ),

                const SizedBox(height: 20),

                if (controller.liveTranscript.isNotEmpty && controller.state != JarvisState.speaking)
                Container(
                  margin:
                      const EdgeInsets.symmetric(
                    horizontal: 32,
                  ),
                  padding:
                      const EdgeInsets.symmetric(
                    horizontal: 16,
                    vertical: 10,
                  ),
                  decoration: BoxDecoration(
                    color: Colors.cyanAccent.withValues(
                      alpha: 0.08,
                    ),
                    borderRadius: BorderRadius.circular(14),
                  ),
                  child: Text(
                    '"${controller.liveTranscript}"',
                    textAlign:
                        TextAlign.center,
                    style: const TextStyle(
                      color:Colors.cyanAccent,
                      fontSize: 15,
                      letterSpacing: 0.5,
                    ),
                  ),
                ),

                if (controller.liveTranscript.isNotEmpty && controller.state != JarvisState.speaking)
                const SizedBox(height: 18),
                // RESPONSE TEXT

                if (controller.responseText.isNotEmpty)
                  Container(
                    margin:
                        const EdgeInsets.symmetric(
                      horizontal: 30,
                    ),
                    padding:
                        const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: Colors.greenAccent,
                      ),
                      borderRadius:
                          BorderRadius.circular(
                        12,
                      ),
                    ),
                    child: Text(
                      controller.responseText,
                      textAlign:
                          TextAlign.center,
                      style: const TextStyle(
                        color:
                            Colors.greenAccent,
                      ),
                    ),
                  ),

                // HA RESPONSE DETAILS

                if (controller.lastResponse != null)
                  Padding(
                    padding:
                        const EdgeInsets.only(
                      top: 10,
                    ),
                    child: Text(
                      '${controller.lastResponse!.entity} → ${controller.lastResponse!.state}',
                      style: const TextStyle(
                        color: Colors.white54,
                        fontSize: 13,
                      ),
                    ),
                  ),
              ],
            ),
          ),

          Positioned(
            bottom: 60,
            left: 0,
            right: 0,
            child: Center(
              child: GestureDetector(
                onTap: _onMicPressed,
                child: Container(
                  width: 70,
                  height: 70,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: _micColor(),
                    boxShadow: [
                      BoxShadow(
                        color: _micColor()
                            .withValues(
                          alpha: 0.4,
                        ),
                        blurRadius: 20,
                        spreadRadius: 2,
                      ),
                    ],
                  ),
                  child: Icon(
                    _micIcon(),
                    color: Colors.white,
                    size: 32,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}