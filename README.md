Future<void> _startNativeWakewordSafely() async {
  if (!_wakewordEnabled) {
    return;
  }

  if (_isStartingNativeWakeword) {
    return;
  }

  _isStartingNativeWakeword = true;

  try {
    // Hier deinen vorhandenen MethodChannel-Aufruf verwenden.
    //
    // Beispiel:
    // await _platform.invokeMethod('startWakeword');

    await _startNativeWakeword();
  } catch (error, stackTrace) {
    debugPrint(
      'HomeScreen: '
      'Native Wakeword konnte nicht gestartet werden: $error',
    );
    debugPrintStack(stackTrace: stackTrace);
  } finally {
    _isStartingNativeWakeword = false;
  }
}
