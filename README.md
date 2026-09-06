Future<void> _handleErrorState() async {
  _thinkingFeedbackService.cancel();
  await _speechOutputService.stop();

  if (_wakewordEnabled) {
    await _startNativeWakewordSafely();
  }
}
