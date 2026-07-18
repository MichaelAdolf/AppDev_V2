PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              7,0s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,7s
I/FlutterActivityAndFragmentDelegate( 9378): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 9378): Beginning load of flutter...
D/FlutterJNI( 9378): flutter (null) was loaded normally!
I/flutter ( 9378): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 9378): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              131ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:63164/Z5qYxby-xpg=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:63164/Z5qYxby-xpg=/devtools/?uri=ws://127.0.0.1:63164/Z5qYxby-xpg=/ws
I/mple.jarvis_app( 9378): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer( 9378): Width is zero. 0,0
I/mple.jarvis_app( 9378): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x3db63448b7a1c68d
I/UnisocBufferQueueHelper( 9378): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006e09c68720, size:88
I/mple.jarvis_app( 9378): createUnisocBufferQueueHelperFactory success, get instance 0xb400006e09c68720
I/mple.jarvis_app( 9378): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f259f1c40, size:296, enable:0
I/mple.jarvis_app( 9378): createUnisocFrameRecordFactory success, get instance 0xb400006f259f1c40
D/FlutterJNI( 9378): Sending viewport metrics to the engine.
W/libc    ( 9378): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 9378): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 9378): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9378): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9378): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9378): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9378): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9378): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 9378): register: id=23b00000c10, handle=0xb400006f259b85c0, importpid=9378
W/libc    ( 9378): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 9378): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 9378): register: id=23b00000c10, handle=0xb400006f259b8940, importpid=9378
D/mali_gralloc( 9378): unregister: id=23b00000c10, handle=0xb400006f259b8940, base=0x0, importpid=9378, clone_count=1
D/mali_gralloc( 9378): register: id=23b00000c11, handle=0xb400006f259b8940, importpid=9378
D/mali_gralloc( 9378): register: id=23b00000c11, handle=0xb400006f259b8a20, importpid=9378
D/mali_gralloc( 9378): unregister: id=23b00000c11, handle=0xb400006f259b8a20, base=0x0, importpid=9378, clone_count=1
D/mali_gralloc( 9378): register: id=23b00000c12, handle=0xb400006f259b8a20, importpid=9378
D/mali_gralloc( 9378): register: id=23b00000c12, handle=0xb400006f259b8b00, importpid=9378
D/mali_gralloc( 9378): unregister: id=23b00000c12, handle=0xb400006f259b8b00, base=0x0, importpid=9378, clone_count=1
D/mali_gralloc( 9378): register: id=23b00000c13, handle=0xb400006f259b8b00, importpid=9378
D/mali_gralloc( 9378): register: id=23b00000c13, handle=0xb400006f259b8be0, importpid=9378
D/mali_gralloc( 9378): unregister: id=23b00000c13, handle=0xb400006f259b8be0, base=0x0, importpid=9378, clone_count=1
D/mali_gralloc( 9378): register: id=23b00000c14, handle=0xb400006f259b8be0, importpid=9378
D/mali_gralloc( 9378): register: id=23b00000c14, handle=0xb400006f259b8cc0, importpid=9378
D/mali_gralloc( 9378): unregister: id=23b00000c14, handle=0xb400006f259b8cc0, base=0x0, importpid=9378, clone_count=1
W/Choreographer( 9378): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 9378): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 9378): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 9378): Connected to TTS engine
I/TextToSpeech( 9378): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_SERVICE( 9378): Foreground Service läuft
I/Choreographer( 9378): Skipped 55 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 9378): register: id=23b00000c15, handle=0xb400006e037b2be0, importpid=9378
D/JARVIS_WS( 9378): WebSocket verbunden
I/HWUI    ( 9378): Davey! duration=930ms; Flags=1, FrameTimelineVsyncId=6403999, IntendedVsync=33860218223694, Vsync=33861133739504, InputEventId=0, HandleInputStart=33861135423818, AnimationStart=33861135426164, PerformTraversalsStart=33861135427433, DrawStart=33861138441087, FrameDeadline=33860234890361, FrameInterval=33861135067933, FrameStartTime=16645742, SyncQueued=33861139492356, SyncStart=33861139554280, IssueDrawCommandsStart=33861140398010, SwapBuffers=33861147249741, FrameCompleted=33861148764280, DequeueBufferDuration=1677500, QueueBufferDuration=817461, GpuCompleted=33861148764280, SwapBuffersCompleted=33861148214664, DisplayPresentTime=7809597357345302627, CommandSubmissionCompleted=33861147249741, 
D/JARVIS_TTS( 9378): Android TTS bereit
D/FlutterJNI( 9378): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/ProfileInstaller( 9378): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Erkannt: hey schatz
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
W/mple.jarvis_app( 9378): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 9378): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 9378): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 9378): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Erkannt: okay jarvis
D/JARVIS_WAKEWORD( 9378): Wakeword erkannt
W/libc    ( 9378): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9378): type=1400 audit(0.0:21215): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9378): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9378): sendWakewordToFlutter
I/flutter ( 9378): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9378): [JARVIS BRIDGE] null
I/flutter ( 9378): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9378): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9378): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 9378): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 9378): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 9378): Wakeword STOP
D/mali_gralloc( 9378): register: id=23b00000c1a, handle=0xb400006f20d57740, importpid=9378
I/flutter ( 9378): [JARVIS] Wakeword gestoppt
I/flutter ( 9378): [VOICE] listen() wird gestartet
I/flutter ( 9378): [VOICE] verfügbar: true
I/flutter ( 9378): [VOICE] SpeechToText aktiv
I/flutter ( 9378): [JARVIS] startListening verlassen
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/TTS     ( 9378): Utterance ID has started: db627aac-ae35-41cd-a711-8c87b95a37e2
D/TTS     ( 9378): Utterance ID has completed: db627aac-ae35-41cd-a711-8c87b95a37e2
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Erkannt: okay jarvis
D/JARVIS_WAKEWORD( 9378): Wakeword erkannt
W/libc    ( 9378): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9378): type=1400 audit(0.0:21217): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9378): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9378): sendWakewordToFlutter
I/flutter ( 9378): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9378): [JARVIS BRIDGE] null
I/flutter ( 9378): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9378): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9378): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 9378): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 9378): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 9378): Wakeword STOP
I/flutter ( 9378): [JARVIS] Wakeword gestoppt
I/flutter ( 9378): [VOICE] listen() wird gestartet
I/flutter ( 9378): [VOICE] verfügbar: true
I/flutter ( 9378): [VOICE] SpeechToText aktiv
I/flutter ( 9378): [JARVIS] startListening verlassen
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/TTS     ( 9378): Utterance ID has started: 54a55d69-5dac-4035-b283-c26d1fe0cbbb
D/TTS     ( 9378): Utterance ID has completed: 54a55d69-5dac-4035-b283-c26d1fe0cbbb
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Wakeword STOP
I/flutter ( 9378): [JARVIS] Wakeword gestoppt
I/flutter ( 9378): [VOICE] listen() wird gestartet
I/flutter ( 9378): [VOICE] verfügbar: true
I/flutter ( 9378): [VOICE] SpeechToText aktiv
I/flutter ( 9378): [JARVIS] startListening verlassen
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/TTS     ( 9378): Utterance ID has started: f7d7a3cd-e3dc-40ce-bd6c-b3f2bb4e2fa3
D/TTS     ( 9378): Utterance ID has completed: f7d7a3cd-e3dc-40ce-bd6c-b3f2bb4e2fa3
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Erkannt: okay jarvis
D/JARVIS_WAKEWORD( 9378): Wakeword erkannt
W/libc    ( 9378): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9378): type=1400 audit(0.0:21220): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9378): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9378): sendWakewordToFlutter
I/flutter ( 9378): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9378): [JARVIS BRIDGE] null
I/flutter ( 9378): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9378): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9378): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 9378): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 9378): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 9378): Wakeword STOP
I/flutter ( 9378): [JARVIS] Wakeword gestoppt
I/flutter ( 9378): [VOICE] listen() wird gestartet
I/flutter ( 9378): [VOICE] verfügbar: true
I/flutter ( 9378): [VOICE] SpeechToText aktiv
I/flutter ( 9378): [JARVIS] startListening verlassen
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage | final=false
I/flutter ( 9378): [VOICE] Ergebnis: sage | final=true
D/JARVIS_WAKEWORD( 9378): Wakeword STOP
I/flutter ( 9378): [JARVIS] Wakeword gestoppt
I/flutter ( 9378): [VOICE] listen() wird gestartet
I/flutter ( 9378): [VOICE] verfügbar: true
I/flutter ( 9378): [VOICE] SpeechToText aktiv
I/flutter ( 9378): [JARVIS] startListening verlassen
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis:  | final=false
I/flutter ( 9378): [VOICE] Ergebnis: tagesinformation | final=false
I/flutter ( 9378): [VOICE] Ergebnis: tagesinformation | final=false
I/flutter ( 9378): [VOICE] Ergebnis: tagesinformation | final=true
D/JARVIS_WS( 9378): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:33. Draußen sind es aktuell 22 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT( 9378): Node-RED Event wird verarbeitet
W/libc    ( 9378): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...( 9378): type=1400 audit(0.0:21222): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9378): WakeLock aktiviert
D/JARVIS_TTS( 9378): Sprache: Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:33. Draußen sind es aktuell 22 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT( 9378): Activity wird geöffnet
D/JARVIS_BRIDGE( 9378): openAndDeliverEvent
D/JARVIS_BRIDGE( 9378): Bridge Activity in Vordergrund
I/flutter ( 9378): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter ( 9378): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 9378): [Jarvis] App resumed -> voice neu initialisieren
I/flutter ( 9378): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE( 9378): Intent Event empfangen
D/JARVIS_BRIDGE( 9378): Gepuffertes Event wird gesendet
I/flutter ( 9378): [JARVIS BRIDGE] backgroundEvent
I/flutter ( 9378): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:33. Draußen sind es aktuell 22 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter ( 9378): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:33. Draußen sind es aktuell 22 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter ( 9378): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 9378): [Jarvis] App resumed -> voice neu initialisieren
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/FlutterJNI( 9378): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Erkannt: guten abend heute ist samstag der 18 juli 2026 die aktuelle uhrzeit ist 20:33 uhr draußen sind es aktuell 22 grad bei leicht bewölktem himmel du hast
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Fehler: 7
D/JARVIS_WAKEWORD( 9378): Listening gestartet
D/JARVIS_WAKEWORD( 9378): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9378): Sprache erkannt
D/JARVIS_WAKEWORD( 9378): Sprachende
D/JARVIS_WAKEWORD( 9378): Fehler: 7
