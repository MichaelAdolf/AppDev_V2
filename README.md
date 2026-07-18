private fun onWakewordDetected() {

    Log.d(
        "JARVIS_WAKEWORD",
        "Wakeword erkannt"
    )

    wakeDeviceBriefly()

    speakWakewordAck()

    MainActivity.sendWakewordToFlutter()
}
