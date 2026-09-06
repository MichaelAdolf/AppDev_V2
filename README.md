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
