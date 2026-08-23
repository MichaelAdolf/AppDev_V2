Future<void> _playCurrentResponse(
  HaResponse response,
) async {
  if (_isSpeaking) {
    return;
  }

  _isSpeaking = true;

  debugPrint(
    '[JARVIS] Speech Mode: ${_speechOutput.mode.name}',
  );

  debugPrint(
    '[JARVIS] Response Text: ${response.message}',
  );

  debugPrint(
    '[JARVIS] Audio URL: ${response.audioUrl}',
  );

  await JarvisWakewordControl.stop();

  try {
    final completed = await _speechOutput.output(
      response,
    );

    if (!mounted || !completed) {
      return;
    }

    controller.onSpeechFinished();
  } catch (error) {
    debugPrint(
      '[JARVIS] Sprachausgabe fehlgeschlagen: $error',
    );

    if (mounted) {
      controller.onSpeechFinished();
    }
  } finally {
    _isSpeaking = false;

    if (
        mounted &&
        _wakewordEnabled &&
        controller.state == JarvisState.idle) {
      await JarvisWakewordControl.start();
    }
  }
}
