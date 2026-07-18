private fun speakMessage(
    payload: String
) {

    try {

        val json =
            JSONObject(payload)

        val message =
            json.optString(
                "message",
                ""
            )

        if (message.isBlank()) {
            return
        }

        Log.d(
            "JARVIS_TTS",
            "Sprache: $message"
        )

        tts?.speak(
            message,
            TextToSpeech.QUEUE_FLUSH,
            null,
            "jarvis_event"
        )

    } catch (e: Exception) {

        Log.d(
            "JARVIS_TTS",
            "Fehler: ${e.message}"
        )
    }
}
