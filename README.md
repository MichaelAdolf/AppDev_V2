companion object {

    const val CHANNEL_NAME =
        "jarvis/background"

    var currentInstance:
        MainActivity? = null

    fun sendEventToFlutter(
        event: String
    ) {

        currentInstance?.channel?.invokeMethod(
            "backgroundEvent",
            event
        )
    }
}

private lateinit var channel:
    MethodChannel
