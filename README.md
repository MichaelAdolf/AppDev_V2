package com.example.jarvis_app

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log

class JarvisBackgroundService : Service() {

    override fun onCreate() {
        super.onCreate()

        Log.d(
            "JARVIS_SERVICE",
            "Background Service gestartet"
        )
    }

    override fun onStartCommand(
        intent: Intent?,
        flags: Int,
        startId: Int
    ): Int {

        Log.d(
            "JARVIS_SERVICE",
            "Background Service läuft"
        )

        return START_STICKY
    }

    override fun onDestroy() {

        Log.d(
            "JARVIS_SERVICE",
            "Background Service beendet"
        )

        super.onDestroy()
    }

    override fun onBind(
        intent: Intent?
    ): IBinder? {
        return null
    }
}
