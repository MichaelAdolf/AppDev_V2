fun sendWakewordToFlutter() {

    Log.d(
        "JARVIS_WAKEWORD",
        "sendWakewordToFlutter"
    )

    val activity = currentInstance

    if (activity == null) {

        Log.d(
            "JARVIS_WAKEWORD",
            "Flutter Activity fehlt - Wakeword gepuffert"
        )

        pendingWakeword = true
        return
    }

    if (activity.channel == null) {

        Log.d(
            "JARVIS_WAKEWORD",
            "MethodChannel fehlt - Wakeword gepuffert"
        )

        pendingWakeword = true
        return
    }

    activity.runOnUiThread {
        activity.channel?.invokeMethod(
            "wakewordDetected",
            null
        )
    }
}
``
