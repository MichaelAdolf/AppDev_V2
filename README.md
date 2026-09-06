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
