private fun restartWakewordListener() {

    mainHandler.postDelayed(
        {
            try {
                speechRecognizer?.cancel()
                startWakewordRecognition()
            } catch (e: Exception) {
                Log.d(
                    "JARVIS_WAKEWORD",
                    "Restart Fehler: ${e.message}"
                )
            }
        },
        1000
    )
}
