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
import '../../../services/thinking_feedback_service.dart';
import '../widgets/ambient_connections.dart';
import '../widgets/ambient_particles.dart';
import '../widgets/background_grid.dart';
import '../widgets/conversation_timeline.dart';
import '../widgets/hud_overlay.dart';
import '../widgets/hud_panel.dart';
import '../widgets/jarvis_circle.dart';
import '../widgets/jarvis_layout.dart';

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
    unawaited(_thinkingFeedbackService.dispose());
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
      await _thinkingFeedbackService.forceStop();
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
      final activeThinking = _thinkingSequence;
      if (activeThinking != null) {
        await activeThinking;
      }
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

  Future<void>? _thinkingSequence;

  void _handleControllerChanged() {
    if (!mounted) return;

    final currentState = controller.state;
    final currentInteractionId = controller.activeInteractionId;
    final stateChanged = currentState != _previousJarvisState;
    final interactionChanged = currentInteractionId != _observedInteractionId;

    _previousJarvisState = currentState;
    _observedInteractionId = currentInteractionId;

    if (currentState == JarvisState.thinking &&
        currentInteractionId != null &&
        (stateChanged || interactionChanged || controller.responseReady)) {
      _startThinkingSequence(currentInteractionId);
    } else if (currentState == JarvisState.speaking) {
      final response = controller.lastResponse;
      if (!_isSpeaking && response != null && response.message.trim().isNotEmpty) {
        unawaited(_playCurrentResponse(response));
      }
    } else if (currentState == JarvisState.error) {
      unawaited(_handleErrorState());
    }

    setState(() {});
  }

  void _startThinkingSequence(int interactionId) {
    if (_thinkingSequence != null ||
        _thinkingFeedbackService.activeInteractionId == interactionId) {
      return;
    }

    final selectedMode = _speechOutputMode;
    _thinkingSequence = _runThinkingSequence(
      interactionId,
      selectedMode,
    ).whenComplete(() => _thinkingSequence = null);
  }

  Future<void> _runThinkingSequence(
    int interactionId,
    SpeechOutputMode selectedMode,
  ) async {
    await JarvisWakewordControl.stop();
    await _thinkingFeedbackService.play(
      interactionId: interactionId,
      mode: selectedMode,
    );

    if (!mounted || controller.activeInteractionId != interactionId) return;

    // Falls die Berechnung länger als die Phrase dauert, warten wir hier auf
    // responseReady. Der Controller bleibt dabei korrekt im State thinking.
    while (mounted &&
        controller.activeInteractionId == interactionId &&
        !controller.responseReady) {
      await Future<void>.delayed(const Duration(milliseconds: 40));
    }

    if (!mounted || controller.activeInteractionId != interactionId) return;
    controller.releasePendingTransition(interactionId);
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
      body: Stack(children: [
        const Positioned.fill(child: RepaintBoundary(child: BackgroundGrid())),
        const Positioned.fill(child: RepaintBoundary(child: IgnorePointer(child: AmbientParticles()))),
        const Positioned.fill(child: RepaintBoundary(child: AmbientConnections())),
        const Positioned.fill(child: HudOverlay()),
        SafeArea(child: LayoutBuilder(builder: (context, constraints) {
          final layout = JarvisLayout.from(constraints);
          return Center(child: ConstrainedBox(
            constraints: BoxConstraints(maxWidth: layout.maxContentWidth),
            child: Padding(
              padding: EdgeInsets.fromLTRB(layout.outerPadding, 4, layout.outerPadding, layout.outerPadding),
              child: layout.usesLandscapeComposition
                  ? _buildLandscapeLayout(layout)
                  : _buildPortraitLayout(layout),
            ),
          ));
        })),
      ]),
    );
  }

  Widget _buildPortraitLayout(JarvisLayout layout) {
    final topHeight = layout.isCompact ? 124.0 : 132.0;
    final contextHeight = layout.isCompact ? 108.0 : 116.0;
    return Column(children: [
      Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Expanded(child: _systemPanel(layout, topHeight)),
        SizedBox(width: layout.panelGap),
        Expanded(child: _voicePanel(layout, topHeight)),
      ]),
      SizedBox(height: layout.gap + 8),
      Expanded(child: Center(child: _buildHero(layout))),
      SizedBox(height: layout.gap),
      Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Expanded(child: _commandPanel(layout, contextHeight)),
        SizedBox(width: layout.panelGap),
        Expanded(child: _entityPanel(layout, contextHeight)),
      ]),
      SizedBox(height: layout.gap),
      ConversationTimeline(entries: controller.history,
        height: layout.conversationHeight, compact: layout.isCompact),
    ]);
  }

  Widget _buildLandscapeLayout(JarvisLayout layout) {
    final ph=(layout.viewport.height*.19).clamp(92.0,118.0).toDouble();
    return Column(children: [
      Expanded(child: Row(crossAxisAlignment: CrossAxisAlignment.center, children: [
        Expanded(flex:3, child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          _systemPanel(layout,ph), SizedBox(height:layout.gap), _commandPanel(layout,ph)])),
        SizedBox(width:layout.gap*1.5),
        Expanded(flex:5, child:Center(child:_buildHero(layout))),
        SizedBox(width:layout.gap*1.5),
        Expanded(flex:3, child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          _voicePanel(layout,ph), SizedBox(height:layout.gap), _entityPanel(layout,ph)])),
      ])),
      SizedBox(height:layout.gap),
      ConversationTimeline(entries:controller.history,height:layout.conversationHeight,compact:true),
    ]);
  }

  Widget _systemPanel(JarvisLayout l,double h)=>HudPanel(height:h,compact:l.isCompact||l.usesLandscapeComposition,
    title:'SYSTEM',indicatorColor:controller.haConnected?Colors.greenAccent:Colors.redAccent,
    lines:[controller.haConnected?'HA ONLINE':'HA OFFLINE','NODE-RED ONLINE','STATE ${controller.state.name.toUpperCase()}']);
  Widget _voicePanel(JarvisLayout l,double h)=>HudPanel(height:h,compact:l.isCompact||l.usesLandscapeComposition,
    title:'VOICE',indicatorColor:_voiceHudColor(),lines:['LANG : de-DE','STATE : ${controller.state.name.toUpperCase()}',
    'AUDIO : ${_speechOutputMode.displayName}',controller.state==JarvisState.listening?'INPUT : ACTIVE':'INPUT : READY']);
  Widget _commandPanel(JarvisLayout l,double h)=>HudPanel(height:h,compact:l.isCompact||l.usesLandscapeComposition,
    title:'COMMAND',lines:[controller.liveTranscript.isEmpty?'WAITING...':controller.liveTranscript]);
  Widget _entityPanel(JarvisLayout l,double h)=>HudPanel(height:h,compact:l.isCompact||l.usesLandscapeComposition,
    title:'ENTITY',lines:[controller.lastResponse?.entity??'-',controller.lastResponse?.state??'-']);

  Widget _buildHero(JarvisLayout l)=>FittedBox(fit:BoxFit.scaleDown,child:Column(mainAxisSize:MainAxisSize.min,children:[
    Row(mainAxisSize:MainAxisSize.min,crossAxisAlignment:CrossAxisAlignment.end,children:[
      Padding(padding:EdgeInsets.only(bottom:l.controlSize*.08),child:_control(l,Icons.volume_up,
        _speechOutputMode==SpeechOutputMode.nodeRedAudio,_toggleSpeechOutputMode,.56)),
      SizedBox(width:l.gap+(l.usesLandscapeComposition?6:10)),
      GestureDetector(onTap:_onMicPressed,child:RepaintBoundary(child:JarvisCircle(state:controller.state,size:l.orbSize))),
      SizedBox(width:l.gap+(l.usesLandscapeComposition?6:10)),
      Padding(padding:EdgeInsets.only(bottom:l.controlSize*.08),child:_control(l,Icons.mic,_wakewordEnabled,_toggleWakeword,.62)),
    ]),
    SizedBox(height:l.usesLandscapeComposition?2:l.gap*.7),
    Text('J.A.R.V.I.S',maxLines:1,style:TextStyle(color:Colors.cyanAccent,fontSize:l.titleFontSize,
      letterSpacing:l.usesLandscapeComposition?5:8)),
  ]));

  Widget _control(JarvisLayout l,IconData icon,bool active,VoidCallback tap,double factor)=>GestureDetector(
    onTap:tap,child:AnimatedContainer(duration:const Duration(milliseconds:250),width:l.controlSize,height:l.controlSize,
      decoration:BoxDecoration(shape:BoxShape.circle,color:active?const Color(0xFF002D72):Colors.black,
        border:Border.all(color:Colors.cyanAccent,width:2),boxShadow:active?[BoxShadow(
          color:Colors.blueAccent.withValues(alpha:.55),blurRadius:14,spreadRadius:2)]:const []),
      child:Icon(icon,color:active?Colors.cyanAccent:Colors.grey,size:l.controlSize*factor)));
}
