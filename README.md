if (
    controller.state == JarvisState.speaking &&
    !_isSpeaking &&
    controller.responseText.isNotEmpty) {

  _isSpeaking = true;

  if (_audioMode == AudioOutputMode.local) {

    AudioService.speak(
      controller.responseText,
      onComplete: () async {
        _isSpeaking = false;
        controller.onSpeechFinished();

        if (_wakewordEnabled) {
          await JarvisWakewordControl.start();
        }
      },
    );

  } else {

    final audioUrl =
        controller.lastResponse?.audioUrl;

    if (
        audioUrl != null &&
        audioUrl.isNotEmpty) {

      debugPrint(
        '[JARVIS] REMOTE Audio: $audioUrl',
      );

      AudioService.playRemoteUrl(
        audioUrl,
        onComplete: () async {

          _isSpeaking = false;

          controller.onSpeechFinished();

          if (_wakewordEnabled) {
            await JarvisWakewordControl.start();
          }
        },
      );

    } else {

      debugPrint(
        '[JARVIS] Keine audioUrl vorhanden -> Fallback',
      );

      AudioService.speak(
        controller.responseText,
        onComplete: () async {

          _isSpeaking = false;

          controller.onSpeechFinished();

          if (_wakewordEnabled) {
            await JarvisWakewordControl.start();
          }
        },
      );
    }
  }
}

setState(() {});
