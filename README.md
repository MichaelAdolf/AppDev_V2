Future<bool> startListening({
  required Function(String text) onFinalResult,
  Function(String text)? onPartialResult,
}) async {

  debugPrint(
    '[VOICE] listen() wird gestartet',
  );

  final available =
      await _speech.initialize();

  debugPrint(
    '[VOICE] verfügbar: $available',
  );

  if (!available) {

    debugPrint(
      '[VOICE] SpeechToText nicht verfügbar',
    );

    return false;
  }

  await _speech.listen(
    localeId: 'de_DE',
    partialResults: true,
    listenMode: ListenMode.confirmation,
    onResult: (result) {

      final text =
          result.recognizedWords.trim();

      debugPrint(
        '[VOICE] Ergebnis: $text | final=${result.finalResult}',
      );

      if (text.isEmpty) {
        return;
      }

      if (result.finalResult) {

        onFinalResult(text);

      } else {

        onPartialResult?.call(text);
      }
    },
  );

  debugPrint(
    '[VOICE] SpeechToText aktiv',
  );

  return true;
}
