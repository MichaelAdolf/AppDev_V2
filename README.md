private fun startWakewordRecognition() {

    val intent =
        Intent(
            RecognizerIntent.ACTION_RECOGNIZE_SPEECH
        ).apply {
            putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )

            putExtra(
                RecognizerIntent.EXTRA_LANGUAGE,
                "de-DE"
            )

            putExtra(
                RecognizerIntent.EXTRA_PARTIAL_RESULTS,
                true
            )

            putExtra(
                RecognizerIntent.EXTRA_MAX_RESULTS,
                3
            )
        }

    try {
        speechRecognizer?.startListening(intent)

        Log.d(
            "JARVIS_WAKEWORD",
            "Listening gestartet"
        )
    } catch (e: Exception) {
        Log.d(
            "JARVIS_WAKEWORD",
            "Start Fehler: ${e.message}"
        )

        restartWakewordListener()
    }
}
