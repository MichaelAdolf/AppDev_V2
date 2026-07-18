package com.example.jarvis_app

import android.content.Context 
import android.content.Intent 
import android.os.Build 
import android.os.Bundle 
import android.util.Log 
import android.view.WindowManager 
import io.flutter.embedding.android.FlutterActivity 
import io.flutter.embedding.engine.FlutterEngine 
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {

companion object {

    const val CHANNEL_NAME = "jarvis/background"

    private const val EXTRA_JARVIS_EVENT =
        "jarvis_event"

    var currentInstance: MainActivity? = null

    private var pendingEvent: String? = null

    private var pendingWakeword: Boolean = false

    fun openAndDeliverEvent(
        context: Context,
        event: String
    ) {
        Log.d(
            "JARVIS_BRIDGE",
            "openAndDeliverEvent"
        )

        pendingEvent = event

        val intent = Intent(
            context,
            MainActivity::class.java
        ).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP)
            addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP)
            addFlags(Intent.FLAG_ACTIVITY_REORDER_TO_FRONT)
            addFlags(Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED)
            putExtra(EXTRA_JARVIS_EVENT, event)
        }

        Log.d("JARVIS_BRIDGE", "Bridge Activity in Vordergrund")
        context.startActivity(intent)
    }

    fun sendEventToFlutter(
        event: String
    ) {
        Log.d(
            "JARVIS_BRIDGE",
            "currentInstance = ${currentInstance != null}"
        )

        val activity = currentInstance

        if (activity == null) {
            Log.d(
                "JARVIS_BRIDGE",
                "Flutter Activity fehlt - Event gepuffert"
            )

            pendingEvent = event
            return
        }

        if (activity.channel == null) {
            Log.d(
                "JARVIS_BRIDGE",
                "MethodChannel fehlt - Event gepuffert"
            )

            pendingEvent = event
            return
        }

        Log.d(
            "JARVIS_BRIDGE",
            "Sende Event an Flutter"
        )

        activity.runOnUiThread {
            activity.channel?.invokeMethod(
                "backgroundEvent",
                event
            )
        }
    }

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
}

private var channel: MethodChannel? = null

override fun onCreate(
    savedInstanceState: Bundle?
) {
    super.onCreate(savedInstanceState)

    currentInstance = this

    window.addFlags(
        WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
    )

    val serviceIntent = Intent(
        this,
        JarvisForegroundService::class.java
    )

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        startForegroundService(serviceIntent)
    } else {
        startService(serviceIntent)
    }

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O_MR1) {
        setShowWhenLocked(true)
        setTurnScreenOn(true)
    } else {
        window.addFlags(
            WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED
                or WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON
                or WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
        )
    }

    handleIncomingIntent(intent)
}

override fun onNewIntent(
    intent: Intent
) {
    super.onNewIntent(intent)

    setIntent(intent)
    handleIncomingIntent(intent)
}

override fun configureFlutterEngine(
    flutterEngine: FlutterEngine
) {
    super.configureFlutterEngine(flutterEngine)

    channel = MethodChannel(
        flutterEngine
            .dartExecutor
            .binaryMessenger,
        CHANNEL_NAME
    )

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

    Log.d(
        "JARVIS_BRIDGE",
        "MethodChannel erstellt"
    )

    flushPendingEvent()
}

override fun onDestroy() {
    if (currentInstance == this) {
        currentInstance = null
    }

    super.onDestroy()
}

private fun handleIncomingIntent(
    intent: Intent?
) {
    val event = intent
        ?.getStringExtra(EXTRA_JARVIS_EVENT)

    if (event != null) {
        Log.d(
            "JARVIS_BRIDGE",
            "Intent Event empfangen"
        )

        pendingEvent = event
        flushPendingEvent()
    }
}

private fun flushPendingEvent() {

    if (channel == null) {
        Log.d(
            "JARVIS_BRIDGE",
            "Flush nicht möglich - Channel fehlt"
        )

        return
    }

    val event = pendingEvent

    if (event != null) {
        Log.d(
            "JARVIS_BRIDGE",
            "Gepuffertes Event wird gesendet"
        )

        pendingEvent = null

        channel?.invokeMethod(
            "backgroundEvent",
            event
        )
    }
    
    if (pendingWakeword) {
        Log.d(
            "JARVIS_WAKEWORD",
            "Gepuffertes Wakeword wird gesendet"
        )
        
        pendingWakeword = false

        channel?.invokeMethod(
            "wakewordDetected",
            null
        )
    }
}

}