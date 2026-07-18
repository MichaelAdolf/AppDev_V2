package com.example.jarvis_app

import android.Manifest
import android.app.Notification 
import android.app.NotificationChannel 
import android.app.NotificationManager 
import android.app.Service 
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build 
import android.os.Handler 
import android.os.IBinder 
import android.os.Looper 
import android.os.PowerManager 
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.util.Log
import androidx.core.content.ContextCompat
import okhttp3.OkHttpClient 
import okhttp3.Request 
import okhttp3.Response 
import okhttp3.WebSocket 
import okhttp3.WebSocketListener 
import java.util.concurrent.TimeUnit
import java.util.Locale
import org.json.JSONObject

class JarvisForegroundService : Service() {

companion object {
    private const val CHANNEL_ID =
        "jarvis_runtime_channel"

    private const val NOTIFICATION_ID =
        1001

    private const val NODE_RED_WS_URL =
        "ws://192.168.178.47:1880/endpoint/ws/jarvis-router"

    var instance: JarvisForegroundService? = null
}

private val mainHandler =
    Handler(Looper.getMainLooper())

private var webSocket: WebSocket? = null
private var tts: TextToSpeech? = null

private var speechRecognizer: SpeechRecognizer? = null
private var wakewordActive: Boolean = false
private var wakewordRestartAllowed: Boolean = true
private val wakewordText = "jarvis"
private var lastWakewordTimestamp: Long = 0

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
    instance = this
    super.onCreate()

    createNotificationChannel()
    startAsForegroundService()

    tts = TextToSpeech(
        applicationContext
    ){ status ->

        if (status == TextToSpeech.SUCCESS) {
            tts?.language =
                Locale.GERMAN
            tts?.setSpeechRate(
                1.0f
            )

            Log.d(
                "JARVIS_TTS",
                "Android TTS bereit"
            )
        }

    }

    connectWebSocket()
    startWakewordListener()
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

    tts?.stop()
    tts?.shutdown()
    tts = null

    speechRecognizer?.destroy()
    speechRecognizer = null
    wakewordActive = false

    if (instance == this) {
        instance = null
    }

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
    speakMessage(payload)

    Log.d("JARVIS_EVENT", "Activity wird geöffnet")

    val launchIntent = 
        packageManager.getLaunchIntentForPackage( 
            packageName
        )

    launchIntent?.apply {

    addFlags(
        Intent.FLAG_ACTIVITY_NEW_TASK
    )

    addFlags(
        Intent.FLAG_ACTIVITY_REORDER_TO_FRONT
    )

    addFlags(
        Intent.FLAG_ACTIVITY_SINGLE_TOP
    )

    startActivity(this)

    }

    MainActivity.openAndDeliverEvent(
        this,
        payload
    )
}

private fun speakMessage( 
    payload: String 
) {
    try {

        val json =
            JSONObject(payload)

        val message =
            json.optString(
                "message",
                ""
            )

        if (message.isBlank()) {
            return
        }

        Log.d(
            "JARVIS_TTS",
            "Sprache: $message"
        )

        tts?.speak(
            message,
            TextToSpeech.QUEUE_FLUSH,
            null,
            "jarvis_event"
        )

    } catch (e: Exception) {

        Log.d(
            "JARVIS_TTS",
            "Fehler: ${e.message}"
        )
    }
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

fun startWakewordListener() {
    wakewordRestartAllowed = true
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
    
    speechRecognizer?.destroy()

    speechRecognizer = null

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

fun stopWakewordListener() {
    Log.d(
        "JARVIS_WAKEWORD",
        "Wakeword STOP"
    )

    wakewordActive = false
    wakewordRestartAllowed = false

    try{
        speechRecognizer?.cancel()

        speechRecognizer?.destroy()

        speechRecognizer = null

    } catch (_: Exception) {

    }
}

private fun startWakewordRecognition() {

    val intent =
        Intent(
            RecognizerIntent.ACTION_RECOGNIZE_SPEECH
        ).apply {
            putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )

            putExtra(
                RecognizerIntent.EXTRA_LANGUAGE,
                "de-DE"
            )

            putExtra(
                RecognizerIntent.EXTRA_PARTIAL_RESULTS,
                true
            )

            putExtra(
                RecognizerIntent.EXTRA_MAX_RESULTS,
                3
            )
        }

    try {
        speechRecognizer?.startListening(intent)

        Log.d(
            "JARVIS_WAKEWORD",
            "Listening gestartet"
        )
    } catch (e: Exception) {
        Log.d(
            "JARVIS_WAKEWORD",
            "Start Fehler: ${e.message}"
        )

        restartWakewordListener()
    }
}

private fun restartWakewordListener() {

    if (!wakewordRestartAllowed){
        Log.d(
            "JARVIS_WAKEWORD",
            "Restart blockiert"
        )
        return
    }

    mainHandler.postDelayed(
        {
            try {
                speechRecognizer?.cancel()
                startWakewordRecognition()
            } catch (e: Exception) {
                Log.d(
                    "JARVIS_WAKEWORD",
                    "Restart Fehler: ${e.message}"
                )
            }
        },
        1000
    )
}

private fun onWakewordDetected() {
    
    val now = System.currentTimeMillis()

    if (
        now - lastWakewordTimestamp <
        3000
    ) {

        Log.d(
            "JARVIS_WAKEWORD",
            "Wakeword Cooldown aktiv"
        )
        return
    }
    lastWakewordTimestamp = now

    Log.d(
        "JARVIS_WAKEWORD",
        "Wakeword erkannt"
    )

    wakeDeviceBriefly()

    speakWakewordAck()

    MainActivity.sendWakewordToFlutter()

}

private fun speakWakewordAck() {

try {
    tts?.speak(
        "Ja?",
        android.speech.tts.TextToSpeech.QUEUE_FLUSH,
        null,
        "jarvis_wakeword_ack"
    )
} catch (e: Exception) {
    Log.d(
        "JARVIS_WAKEWORD",
        "TTS Fehler: ${e.message}"
    )
}

}

}