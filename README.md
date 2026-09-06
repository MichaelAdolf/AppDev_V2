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
