package com.example.jarvis_app

import android.os.Build
import android.os.Bundle
import android.view.WindowManager
import io.flutter.embedding.android.FlutterActivity
import android.content.Intent
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {
    companion object {

        const val CHANNEL_NAME =
            "jarvis/background"

        var currentInstance:
            MainActivity? = null

        fun sendEventToFlutter(
            event: String
        ) {
            android.util.Log.d(
                "JARVIS_BRIDGE",
                "Sende Event: $event"
            )

            currentInstance?.channel?.invokeMethod(
                "backgroundEvent",
                event
            )
        }

    }

    private lateinit var channel: MethodChannel

    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)

        currentInstance = this

        val serviceIntent = 
            Intent(
                this,
                JarvisForegroundService::class.java
            )

        startService(
            Intent(
                this,
                JarvisBackgroundService::class.java
            )
        )

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
    }

    override fun configureFlutterEngine( 
        flutterEngine: io.flutter.embedding.engine.FlutterEngine 
    ) {

        super.configureFlutterEngine(
            flutterEngine
        )

        channel = MethodChannel(
            flutterEngine
                .dartExecutor
                .binaryMessenger,
            CHANNEL_NAME
        )
    }
}
