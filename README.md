import 'dart:async';

import 'package:flutter/material.dart';

import '../../../core/ha_response.dart';
import '../../../core/jarvis_event.dart';
import '../../../core/jarvis_state.dart';
import '../../../core/speech_output_mode.dart';
import '../../../services/jarvis_wakeword_bus.dart';
import '../../../services/jarvis_wakeword_control.dart';
import '../../../services/speech_output_service.dart';
import '../../../services/voice_service.dart';
import '../logic/jarvis_controller.dart';
import '../services/thinking_feedback_service.dart';
import '../widgets/ambient_connections.dart';
import '../widgets/ambient_particles.dart';
import '../widgets/background_grid.dart';
import '../widgets/conversation_timeline.dart';
import '../widgets/hud_overlay.dart';
import '../widgets/hud_panel.dart';
import '../widgets/jarvis_circle.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({
    super.key,
    required this.controller,
  });

  final JarvisController controller;

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
    with WidgetsBindingObserver {
  final VoiceService _voice = VoiceService();
  final ThinkingFeedbackService _thinkingFeedbackService =
      ThinkingFeedbackService();

  StreamSubscription? _wakewordSubscription;
  late final JarvisController controller;
  late final VoidCallback _controllerListener;
  late final SpeechOutputService _speechOutput;

  JarvisState? _previousJarvisState;
  int? _observedInteractionId;
  bool _isSpeaking = false;
  bool _wakewordEnabled = true;
  bool _isInterrupting = false;
  bool _isStartingNativeWakeword = false;
  SpeechOutputMode _speechOutputMode = SpeechOutputMode.appTts;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);

    controller = widget.controller;
    _speechOutput = SpeechOutputService(initialMode: _speechOutputMode);
    _controllerListener = _handleControllerChanged;
    controller.addListener(_controllerListener);

    unawaited(controller.initialize());
    unawaited(_voice.initialize());

    _wakewordSubscription = JarvisWakewordBus.stream.listen((_) async {
      if (!_wakewordEnabled) return;

      debugPrint('[JARVIS] Wakeword Trigger empfangen');
      if (controller.isBusy) {
        debugPrint('[JARVIS] Wakeword ignoriert - Controller Busy');
        return;
      }
      await _startVoiceInput();
    });
  }

  @override
  void dispose() {
    _thinkingFeedbackService.dispose();
    _wakewordSubscription?.cancel();
    controller.removeListener(_controllerListener);
    WidgetsBinding.instance.removeObserver(this);
    unawaited(_speechOutput.stop());
    unawaited(_voice.stopListening());
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    unawaited(_handleLifecycleChange(state));
  }

  Future<void> _handleLifecycleChange(AppLifecycleState state) async {
    debugPrint('[JARVIS] Lifecycle: $state');

    if (state == AppLifecycleState.paused) {
      _thinkingFeedbackService.cancel();
      await _voice.stopListening();
      await _speechOutput.stop();
      await controller.interrupt();
      await JarvisWakewordControl.stop();
      _isSpeaking = false;
      return;
    }

    if (state == AppLifecycleState.resumed) {
      await _voice.stopListening();
      await _voice.initialize();
      await _startNativeWakewordSafely();
    }
  }

  Future<void> _startVoiceInput() async {
    await JarvisWakewordControl.stop();
    debugPrint('[JARVIS] Wakeword-Stop angefordert');

    await Future<void>.delayed(const Duration(milliseconds: 1200));
    if (!mounted) return;

    final started = await _voice.startListening(
      onPartialResult: controller.updateLiveTranscript,
      onFinalResult: (text) async {
        await _voice.stopListening();
        controller.handleEvent(JarvisEvent.voiceStopped);
        controller.handleTextInput(text);
      },
    );

    if (!started) {
      debugPrint('[JARVIS] STT konnte nicht gestartet werden');
      await controller.interrupt();
      await _startNativeWakewordSafely();
      return;
    }

    controller.handleEvent(JarvisEvent.voiceStarted);
    unawaited(_handleListeningTimeout());
  }

  Future<void> _handleListeningTimeout() async {
    await Future<void>.delayed(const Duration(seconds: 12));
    if (!mounted || controller.state != JarvisState.listening) return;

    debugPrint('[JARVIS] Listening Timeout');
    await _voice.cancelListening();
    await _speechOutput.stop();
    controller.clearLiveTranscript();
    await controller.interrupt();
    await _startNativeWakewordSafely();
  }

  Future<void> _onMicPressed() async {
    final state = controller.state;

    if (state == JarvisState.listening) {
      await _voice.stopListening();
      await controller.interrupt();
      await _startNativeWakewordSafely();
      return;
    }

    if (state == JarvisState.thinking ||
        state == JarvisState.speaking ||
        state == JarvisState.error) {
      await _interruptCurrentInteraction(restartWakeword: false);
    }

    await _startVoiceInput();
  }

  Future<void> _interruptCurrentInteraction({
    bool restartWakeword = true,
  }) async {
    if (_isInterrupting) return;
    _isInterrupting = true;

    try {
      _thinkingFeedbackService.cancel();
      await _speechOutput.stop();
      await _voice.stopListening();
      await controller.interrupt();
      _isSpeaking = false;

      if (restartWakeword) await _startNativeWakewordSafely();
    } catch (error, stackTrace) {
      debugPrint('HomeScreen: Fehler beim Unterbrechen: $error');
      debugPrintStack(stackTrace: stackTrace);
    } finally {
      _isInterrupting = false;
    }
  }

  Future<void> _startNativeWakewordSafely() async {
    if (!_wakewordEnabled || _isStartingNativeWakeword) return;
    _isStartingNativeWakeword = true;

    try {
      await JarvisWakewordControl.start();
    } catch (error, stackTrace) {
      debugPrint('HomeScreen: Wakeword konnte nicht gestartet werden: $error');
      debugPrintStack(stackTrace: stackTrace);
    } finally {
      _isStartingNativeWakeword = false;
    }
  }

  Future<void> _toggleWakeword() async {
    setState(() => _wakewordEnabled = !_wakewordEnabled);
    if (_wakewordEnabled) {
      await _startNativeWakewordSafely();
    } else {
      await JarvisWakewordControl.stop();
    }
  }

  void _toggleSpeechOutputMode() {
    final newMode = _speechOutputMode == SpeechOutputMode.appTts
        ? SpeechOutputMode.nodeRedAudio
        : SpeechOutputMode.appTts;
    setState(() => _speechOutputMode = newMode);
    _speechOutput.setMode(newMode);
  }

  void _handleControllerChanged() {
    if (!mounted) return;

    final currentState = controller.state;
    final currentInteractionId = controller.activeInteractionId;
    final stateChanged = currentState != _previousJarvisState;
    final interactionChanged =
        currentInteractionId != _observedInteractionId;

    if (stateChanged || interactionChanged) {
      _previousJarvisState = currentState;
      _observedInteractionId = currentInteractionId;

      switch (currentState) {
        case JarvisState.thinking:
          _handleThinkingState(currentInteractionId);
          break;
        case JarvisState.speaking:
          _thinkingFeedbackService.cancel();
          final response = controller.lastResponse;
          if (!_isSpeaking && response != null && response.message.trim().isNotEmpty) {
            unawaited(_playCurrentResponse(response));
          }
          break;
        case JarvisState.error:
          _thinkingFeedbackService.cancel();
          unawaited(_handleErrorState());
          break;
        case JarvisState.idle:
        case JarvisState.listening:
          _thinkingFeedbackService.cancel();
          break;
      }
    }

    setState(() {});
  }

  void _handleThinkingState(int? interactionId) {
    if (interactionId == null) return;

    _thinkingFeedbackService.schedule(
      interactionId: interactionId,
      delay: const Duration(milliseconds: 350),
      onPlay: () async {
        if (!mounted ||
            controller.state != JarvisState.thinking ||
            controller.activeInteractionId != interactionId) {
          return;
        }
        debugPrint(
          'HomeScreen: Thinking-Feedback wäre jetzt für '
          'Interaktion $interactionId gestartet',
        );
      },
    );
  }

  Future<void> _handleErrorState() async {
    await _speechOutput.stop();
    await _startNativeWakewordSafely();
  }

  Future<void> _playCurrentResponse(HaResponse response) async {
    if (_isSpeaking) return;
    _isSpeaking = true;
    await JarvisWakewordControl.stop();

    try {
      final completed = await _speechOutput.output(response);
      if (!mounted || !completed) return;
      controller.completeSpeaking();
    } catch (error, stackTrace) {
      debugPrint('[JARVIS] Sprachausgabe fehlgeschlagen: $error');
      debugPrintStack(stackTrace: stackTrace);
      if (mounted) await controller.interrupt(clearLastResponse: false);
    } finally {
      _isSpeaking = false;
      if (mounted && controller.state == JarvisState.idle) {
        await _startNativeWakewordSafely();
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
          const Positioned.fill(child: BackgroundGrid()),
          const Positioned.fill(
            child: IgnorePointer(child: AmbientParticles()),
          ),
          const Positioned.fill(child: AmbientConnections()),
          const Positioned.fill(child: HudOverlay()),
          Positioned(
            left: 20,
            top: 60,
            child: HudPanel(
              title: 'SYSTEM',
              indicatorColor:
                  controller.haConnected ? Colors.greenAccent : Colors.redAccent,
              lines: [
                controller.haConnected ? 'HA ONLINE' : 'HA OFFLINE',
                'NODE-RED ONLINE',
                'STATE ${controller.state.name.toUpperCase()}',
              ],
            ),
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
                GestureDetector(
                  onTap: _onMicPressed,
                  child: JarvisCircle(state: controller.state),
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
                if (controller.liveTranscript.isNotEmpty &&
                    controller.state != JarvisState.speaking)
                  const SizedBox(height: 18),
              ],
            ),
          ),
          Positioned(
            right: 20,
            top: 200,
            child: GestureDetector(
              onTap: _toggleWakeword,
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                width: 50,
                height: 50,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: _wakewordEnabled
                      ? const Color(0xFF002D72)
                      : Colors.black,
                  border: Border.all(color: Colors.cyanAccent, width: 2),
                  boxShadow: _wakewordEnabled
                      ? [
                          BoxShadow(
                            color: Colors.blueAccent.withOpacity(0.7),
                            blurRadius: 20,
                            spreadRadius: 3,
                          ),
                        ]
                      : [],
                ),
                child: Icon(
                  Icons.mic,
                  color: _wakewordEnabled ? Colors.cyanAccent : Colors.grey,
                  size: 34,
                ),
              ),
            ),
          ),
          Positioned(
            left: 0,
            right: 0,
            bottom: 24,
            child: ConversationTimeline(entries: controller.history),
          ),
          Positioned(
            left: 20,
            top: 180,
            child: GestureDetector(
              onTap: _toggleSpeechOutputMode,
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                width: 50,
                height: 50,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: _speechOutputMode == SpeechOutputMode.nodeRedAudio
                      ? const Color(0xFF002D72)
                      : Colors.black,
                  border: Border.all(color: Colors.cyanAccent, width: 2),
                  boxShadow:
                      _speechOutputMode == SpeechOutputMode.nodeRedAudio
                          ? [
                              BoxShadow(
                                color: Colors.blueAccent.withOpacity(0.7),
                                blurRadius: 20,
                                spreadRadius: 3,
                              ),
                            ]
                          : [],
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
