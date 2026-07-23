static Future<void> playRemoteUrl(
  String url, {
  VoidCallback? onComplete,
}) async {

  try {

    await _player.stop();

    await _player.setUrl(url);

    await _player.play();

    _player.playerStateStream.listen(
      (state) {

        if (
          state.processingState ==
              ProcessingState.completed
        ) {

          onComplete?.call();
        }
      },
    );

  } catch (e) {

    debugPrint(
      '[AUDIO] Remote Fehler: $e',
    );

    rethrow;
  }
}
