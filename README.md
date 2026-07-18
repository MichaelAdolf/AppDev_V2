channel?.setMethodCallHandler { call, result ->

    when (call.method) {

        "stopWakeword" -> {

            JarvisForegroundService.instance
                ?.stopWakewordListener()

            result.success(null)
        }

        "startWakeword" -> {

            JarvisForegroundService.instance
                ?.startWakewordListener()

            result.success(null)
        }

        else -> result.notImplemented()
    }
}
