Future<void> _toggleWakeword() async {

  setState(() {
    _wakewordEnabled = !_wakewordEnabled;
  });

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
