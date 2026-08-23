Future<void> _startVoiceInput() async {
  await JarvisWakewordControl.stop();

  debugPrint(
    '[JARVIS] Wakeword-Stop angefordert',
  );

  await Future<void>.delayed(
    const Duration(milliseconds: 1200),
  );

  debugPrint(
    '[JARVIS] Mikrofon wird an Flutter übergeben',
  );

  final started = await _voice.startListening(
    onPartialResult: (text) {
      debugPrint(
        '[JARVIS] Partial STT: $text',
      );

      controller.updateLiveTranscript(text);
    },
    onFinalResult: (text) async {
      debugPrint(
        '[JARVIS] Final STT: $text',
      );

      await _voice.stopListening();

      controller.handleEvent(
        JarvisEvent.voiceStopped,
      );

      controller.handleTextInput(text);
    },
  );

  debugPrint(
    '[JARVIS] VoiceService gestartet: $started',
  );

  if (!started) {
    debugPrint(
      '[JARVIS] STT konnte nicht gestartet werden',
    );

    await controller.interrupt();

    if (_wakewordEnabled) {
      await JarvisWakewordControl.start();
    }

    return;
  }

  controller.handleEvent(
    JarvisEvent.voiceStarted,
  );

  Future<void>.delayed(
    const Duration(seconds: 12),
    () async {
      if (!mounted) {
        return;
      }

      if (controller.state != JarvisState.listening) {
        return;
      }

      debugPrint(
        '[JARVIS] Listening Timeout',
      );

      await _voice.cancelListening();
      await _speechOutput.stop();

      controller.clearLiveTranscript();

      await controller.interrupt();

      if (_wakewordEnabled) {
        await JarvisWakewordControl.start();
      }
    },
  );
}
