package com.example.jarvis_app

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.Service
import android.content.Intent
import android.os.Build
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.os.PowerManager
import android.util.Log
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.Response
import okhttp3.WebSocket
import okhttp3.WebSocketListener
import java.util.concurrent.TimeUnit

class JarvisForegroundService : Service() {

    companion object {
        private const val CHANNEL_ID =
            "jarvis_runtime_channel"

        private const val NOTIFICATION_ID =
            1001

        private const val NODE_RED_WS_URL =
            "ws://192.168.178.47:1880/endpoint/ws/jarvis-router"
    }

    private val mainHandler =
        Handler(Looper.getMainLooper())

    private var webSocket: WebSocket? = null

    private var reconnectRunnable: Runnable? = null

    private val client: OkHttpClient =
        OkHttpClient.Builder()
            .pingInterval(
                20,
                TimeUnit.SECONDS
            )
            .retryOnConnectionFailure(true)
            .build()

    override fun onCreate() {
        super.onCreate()

        createNotificationChannel()
        startAsForegroundService()
        connectWebSocket()
    }

    override fun onStartCommand(
        intent: Intent?,
        flags: Int,
        startId: Int
    ): Int {
        Log.d(
            "JARVIS_SERVICE",
            "Foreground Service läuft"
        )

        return START_STICKY
    }

    override fun onDestroy() {
        Log.d(
            "JARVIS_SERVICE",
            "Foreground Service beendet"
        )

        reconnectRunnable?.let {
            mainHandler.removeCallbacks(it)
        }

        webSocket?.close(
            1000,
            "Service beendet"
        )

        webSocket = null

        super.onDestroy()
    }

    override fun onBind(
        intent: Intent?
    ): IBinder? {
        return null
    }

    private fun startAsForegroundService() {
        val notification =
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                Notification.Builder(
                    this,
                    CHANNEL_ID
                )
                    .setContentTitle("Jarvis aktiv")
                    .setContentText(
                        "Jarvis Runtime läuft"
                    )
                    .setSmallIcon(
                        android.R.drawable.ic_dialog_info
                    )
                    .build()
            } else {
                Notification.Builder(this)
                    .setContentTitle("Jarvis aktiv")
                    .setContentText(
                        "Jarvis Runtime läuft"
                    )
                    .setSmallIcon(
                        android.R.drawable.ic_dialog_info
                    )
                    .build()
            }

        startForeground(
            NOTIFICATION_ID,
            notification
        )
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

    private fun connectWebSocket() {
        Log.d(
            "JARVIS_WS",
            "Verbinde mit $NODE_RED_WS_URL"
        )

        val request =
            Request.Builder()
                .url(NODE_RED_WS_URL)
                .build()

        webSocket =
            client.newWebSocket(
                request,
                object : WebSocketListener() {

                    override fun onOpen(
                        webSocket: WebSocket,
                        response: Response
                    ) {
                        Log.d(
                            "JARVIS_WS",
                            "WebSocket verbunden"
                        )
                    }

                    override fun onMessage(
                        webSocket: WebSocket,
                        text: String
                    ) {
                        Log.d(
                            "JARVIS_WS",
                            "Nachricht empfangen: $text"
                        )

                        handleNodeRedEvent(text)
                    }

                    override fun onFailure(
                        webSocket: WebSocket,
                        t: Throwable,
                        response: Response?
                    ) {
                        Log.d(
                            "JARVIS_WS",
                            "WebSocket Fehler: ${t.message}"
                        )

                        scheduleReconnect()
                    }

                    override fun onClosed(
                        webSocket: WebSocket,
                        code: Int,
                        reason: String
                    ) {
                        Log.d(
                            "JARVIS_WS",
                            "WebSocket geschlossen: $reason"
                        )

                        scheduleReconnect()
                    }
                }
            )
    }

    private fun scheduleReconnect() {
        reconnectRunnable?.let {
            mainHandler.removeCallbacks(it)
        }

        reconnectRunnable =
            Runnable {
                connectWebSocket()
            }

        mainHandler.postDelayed(
            reconnectRunnable!!,
            3000
        )
    }

    private fun handleNodeRedEvent(
        payload: String
    ) {
        Log.d(
            "JARVIS_EVENT",
            "Node-RED Event wird verarbeitet"
        )

        wakeDeviceBriefly()

        MainActivity.openAndDeliverEvent(
            this,
            payload
        )
    }

    @Suppress("DEPRECATION")
    private fun wakeDeviceBriefly() {
        try {
            val powerManager =
                getSystemService(
                    POWER_SERVICE
                ) as PowerManager

            val wakeLock =
                powerManager.newWakeLock(
                    PowerManager.SCREEN_BRIGHT_WAKE_LOCK or
                        PowerManager.ACQUIRE_CAUSES_WAKEUP,
                    "jarvis:node_red_event"
                )

            wakeLock.acquire(10_000)

            Log.d(
                "JARVIS_WAKE",
                "WakeLock aktiviert"
            )
        } catch (e: Exception) {
            Log.d(
                "JARVIS_WAKE",
                "WakeLock Fehler: ${e.message}"
            )
        }
    }
}
