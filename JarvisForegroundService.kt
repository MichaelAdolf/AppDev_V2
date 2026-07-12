package com.example.jarvis_app

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.Intent
import android.os.Build
import android.os.IBinder

class JarvisForegroundService : Service() {

    companion object {
        private const val CHANNEL_ID =
            "jarvis_runtime_channel"

        private const val NOTIFICATION_ID = 1001
    }

    override fun onCreate() {
        super.onCreate()

        createNotificationChannel()

        val notification =
            Notification.Builder(this, CHANNEL_ID)
                .setContentTitle("Jarvis aktiv")
                .setContentText(
                    "Jarvis Runtime läuft"
                )
                .setSmallIcon(
                    android.R.drawable.ic_dialog_info
                )
                .build()

        startForeground(
            NOTIFICATION_ID,
            notification
        )
    }

    override fun onStartCommand(
        intent: Intent?,
        flags: Int,
        startId: Int
    ): Int {
        android.util.Log.d(
            "JARVIS_BRIDGE",
            "EVENT wird ausgelöst"
        )

        MainActivity.sendEventToFlutter(
            "Hallo aus Android Service"
        )

        return START_STICKY
    }

    override fun onBind(
        intent: Intent?
    ): IBinder? {
        return null
    }

    private fun createNotificationChannel() {

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {

            val channel =
                NotificationChannel(
                    CHANNEL_ID,
                    "Jarvis Runtime",
                    NotificationManager.IMPORTANCE_LOW
                )

            val manager =
                getSystemService(
                    NotificationManager::class.java
                )

            manager.createNotificationChannel(
                channel
            )
        }
    }
}