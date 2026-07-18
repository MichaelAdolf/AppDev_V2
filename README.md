private fun speakWakewordAck() {

    try {
        tts?.speak(
            "Ja?",
            android.speech.tts.TextToSpeech.QUEUE_FLUSH,
            null,
            "jarvis_wakeword_ack"
        )
    } catch (e: Exception) {
        Log.d(
            "JARVIS_WAKEWORD",
            "TTS Fehler: ${e.message}"
        )
    }
}
