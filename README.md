private fun startWakewordListener() {

    if (wakewordActive) {
        return
    }

    if (!SpeechRecognizer.isRecognitionAvailable(this)) {
        Log.d(
            "JARVIS_WAKEWORD",
            "SpeechRecognizer nicht verfügbar"
        )

        return
    }

    val hasPermission =
        ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.RECORD_AUDIO
        ) == PackageManager.PERMISSION_GRANTED

    if (!hasPermission) {
        Log.d(
            "JARVIS_WAKEWORD",
            "RECORD_AUDIO Permission fehlt"
        )

        return
    }

    wakewordActive = true

    speechRecognizer =
        SpeechRecognizer.createSpeechRecognizer(this)

    speechRecognizer?.setRecognitionListener(
        object : RecognitionListener {

            override fun onReadyForSpeech(
                params: Bundle?
            ) {
                Log.d(
                    "JARVIS_WAKEWORD",
                    "Bereit für Wakeword"
                )
            }

            override fun onBeginningOfSpeech() {
                Log.d(
                    "JARVIS_WAKEWORD",
                    "Sprache erkannt"
                )
            }

            override fun onRmsChanged(
                rmsdB: Float
            ) {
            }

            override fun onBufferReceived(
                buffer: ByteArray?
            ) {
            }

            override fun onEndOfSpeech() {
                Log.d(
                    "JARVIS_WAKEWORD",
                    "Sprachende"
                )
            }

            override fun onError(
                error: Int
            ) {
                Log.d(
                    "JARVIS_WAKEWORD",
                    "Fehler: $error"
                )

                restartWakewordListener()
            }

            override fun onResults(
                results: Bundle?
            ) {
                val matches =
                    results?.getStringArrayList(
                        SpeechRecognizer.RESULTS_RECOGNITION
                    )

                val text =
                    matches
                        ?.joinToString(" ")
                        ?.lowercase(Locale.GERMAN)
                        ?: ""

                Log.d(
                    "JARVIS_WAKEWORD",
                    "Erkannt: $text"
                )

                if (text.contains(wakewordText)) {
                    onWakewordDetected()
                }

                restartWakewordListener()
            }

            override fun onPartialResults(
                partialResults: Bundle?
            ) {
                val matches =
                    partialResults?.getStringArrayList(
                        SpeechRecognizer.RESULTS_RECOGNITION
                    )

                val text =
                    matches
                        ?.joinToString(" ")
                        ?.lowercase(Locale.GERMAN)
                        ?: ""

                if (text.contains(wakewordText)) {
                    Log.d(
                        "JARVIS_WAKEWORD",
                        "Partial Wakeword erkannt: $text"
                    )

                    onWakewordDetected()
                }
            }

            override fun onEvent(
                eventType: Int,
                params: Bundle?
            ) {
            }
        }
    )

    startWakewordRecognition()
}
