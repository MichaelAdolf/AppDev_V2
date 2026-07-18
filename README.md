PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             18,7s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           7,2s
I/FlutterActivityAndFragmentDelegate(20617): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(20617): Beginning load of flutter...
D/FlutterJNI(20617): flutter (null) was loaded normally!
I/flutter (20617): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(20617): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              656ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:53297/J60b6CqT3Jo=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:53297/J60b6CqT3Jo=/devtools/?uri=ws://127.0.0.1:53297/J60b6CqT3Jo=/ws
I/mple.jarvis_app(20617): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer(20617): Width is zero. 0,0
I/mple.jarvis_app(20617): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x2e027a2106ef7ad9
I/UnisocBufferQueueHelper(20617): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006e093587e0, size:88
I/mple.jarvis_app(20617): createUnisocBufferQueueHelperFactory success, get instance 0xb400006e093587e0
I/mple.jarvis_app(20617): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25934d80, size:296, enable:0
I/mple.jarvis_app(20617): createUnisocFrameRecordFactory success, get instance 0xb400006f25934d80
D/FlutterJNI(20617): Sending viewport metrics to the engine.
W/libc    (20617): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(20617): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(20617): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(20617): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(20617): register: id=23b00000775, handle=0xb400006f1ebe34e0, importpid=20617
W/libc    (20617): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(20617): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc(20617): register: id=23b00000775, handle=0xb400006f1ebe3860, importpid=20617
D/mali_gralloc(20617): unregister: id=23b00000775, handle=0xb400006f1ebe3860, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b00000776, handle=0xb400006f1ebe3860, importpid=20617
D/mali_gralloc(20617): register: id=23b00000776, handle=0xb400006f1ebe3940, importpid=20617
D/mali_gralloc(20617): unregister: id=23b00000776, handle=0xb400006f1ebe3940, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b00000777, handle=0xb400006f1ebe3940, importpid=20617
D/mali_gralloc(20617): register: id=23b00000777, handle=0xb400006f1ebe3a20, importpid=20617
D/mali_gralloc(20617): unregister: id=23b00000777, handle=0xb400006f1ebe3a20, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b00000778, handle=0xb400006f1ebe3a20, importpid=20617
D/mali_gralloc(20617): register: id=23b00000778, handle=0xb400006f1ebe3b00, importpid=20617
D/mali_gralloc(20617): unregister: id=23b00000778, handle=0xb400006f1ebe3b00, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b00000779, handle=0xb400006f1ebe3b00, importpid=20617
D/mali_gralloc(20617): register: id=23b00000779, handle=0xb400006f1ebe3be0, importpid=20617
D/mali_gralloc(20617): unregister: id=23b00000779, handle=0xb400006f1ebe3be0, base=0x0, importpid=20617, clone_count=1
W/Choreographer(20617): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(20617): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(20617): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(20617): Connected to TTS engine
I/TextToSpeech(20617): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_SERVICE(20617): Foreground Service läuft
D/JARVIS_WS(20617): WebSocket verbunden
I/Choreographer(20617): Skipped 61 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(20617): register: id=23b0000077a, handle=0xb400006e03f00120, importpid=20617
I/HWUI    (20617): Davey! duration=1049ms; Flags=1, FrameTimelineVsyncId=5445784, IntendedVsync=24953239879001, Vsync=24954256545688, InputEventId=0, HandleInputStart=24954266220496, AnimationStart=24954266223458, PerformTraversalsStart=24954266224958, DrawStart=24954269946112, FrameDeadline=24953256545668, FrameInterval=24954265798150, FrameStartTime=16666667, SyncQueued=24954273412189, SyncStart=24954273782381, IssueDrawCommandsStart=24954275581112, SwapBuffers=24954287727266, FrameCompleted=24954289524804, DequeueBufferDuration=2972193, QueueBufferDuration=897731, GpuCompleted=24954289524804, SwapBuffersCompleted=24954288820727, DisplayPresentTime=3347130489146469989, CommandSubmissionCompleted=24954287727266, 
D/JARVIS_TTS(20617): Android TTS bereit
D/FlutterJNI(20617): Sending viewport metrics to the engine.
D/ProfileInstaller(20617): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Wakeword STOP
I/flutter (20617): [JARVIS] Wakeword gestoppt
W/mple.jarvis_app(20617): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(20617): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(20617): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(20617): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (20617): [VOICE] listen() wird gestartet
I/flutter (20617): [VOICE] verfügbar: true
I/flutter (20617): [VOICE] SpeechToText aktiv
I/flutter (20617): [JARVIS] startListening verlassen
I/flutter (20617): [VOICE] Ergebnis:  | final=false
I/flutter (20617): [VOICE] Ergebnis:  | final=false
I/flutter (20617): [VOICE] Ergebnis:  | final=false
I/flutter (20617): [VOICE] Ergebnis: sage | final=false
I/flutter (20617): [VOICE] Ergebnis: sage | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir etwas über | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir etwas über das | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir etwas über das Licht | final=false
I/flutter (20617): [VOICE] Ergebnis: sage mir etwas über das Licht | final=true
D/TTS     (20617): Utterance ID has started: d008dbb0-c7d0-46b4-bfb7-76d69c7d65a1
D/TTS     (20617): Utterance ID has completed: d008dbb0-c7d0-46b4-bfb7-76d69c7d65a1
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Sprache erkannt
D/JARVIS_WAKEWORD(20617): Sprachende
D/JARVIS_WAKEWORD(20617): Erkannt: schau mal nicht schlecht
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Sprache erkannt
D/JARVIS_WAKEWORD(20617): Sprachende
D/JARVIS_WAKEWORD(20617): Erkannt: okay jarvis
D/JARVIS_WAKEWORD(20617): Wakeword erkannt
W/libc    (20617): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(20617): type=1400 audit(0.0:3920): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(20617): WakeLock aktiviert
D/JARVIS_WAKEWORD(20617): sendWakewordToFlutter
I/flutter (20617): [JARVIS BRIDGE] wakewordDetected
I/flutter (20617): [JARVIS BRIDGE] null
I/flutter (20617): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (20617): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (20617): [JARVIS] Wakeword Trigger empfangen
I/flutter (20617): [JARVIS] Controller State: JarvisState.idle
I/flutter (20617): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(20617): Wakeword STOP
I/flutter (20617): [JARVIS] Wakeword gestoppt
I/flutter (20617): [VOICE] listen() wird gestartet
I/flutter (20617): [VOICE] verfügbar: true
I/flutter (20617): [VOICE] SpeechToText aktiv
D/mali_gralloc(20617): register: id=23b00000787, handle=0xb400006e09225000, importpid=20617
I/flutter (20617): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(20617): Listening gestartet
I/flutter (20617): [VOICE] Ergebnis:  | final=false
I/flutter (20617): [VOICE] Ergebnis:  | final=false
I/flutter (20617): [VOICE] Ergebnis: wie | final=false
I/flutter (20617): [VOICE] Ergebnis: wie | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es mit | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es mit dem | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es mit dem Licht | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es mit dem Licht aus | final=false
I/flutter (20617): [VOICE] Ergebnis: wie schaut es mit dem Licht aus | final=true
D/TTS     (20617): Utterance ID has started: 48ccdfc1-2d3c-4ccc-ae2f-b5121a471498
D/TTS     (20617): Utterance ID has completed: 48ccdfc1-2d3c-4ccc-ae2f-b5121a471498
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
I/flutter (20617): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](20617): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(20617): unregister: id=23b00000778, handle=0xb400006f1ebe3a20, base=0x0, importpid=20617, clone_count=0
D/mali_gralloc(20617): unregister: id=23b00000779, handle=0xb400006f1ebe3b00, base=0x0, importpid=20617, clone_count=0
I/flutter (20617): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (20617): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(20617): unregister: id=23b00000775, handle=0xb400006f1ebe34e0, base=0x0, importpid=20617, clone_count=0
D/mali_gralloc(20617): unregister: id=23b00000777, handle=0xb400006f1ebe3940, base=0x0, importpid=20617, clone_count=0
D/mali_gralloc(20617): unregister: id=23b00000776, handle=0xb400006f1ebe3860, base=0x0, importpid=20617, clone_count=0
D/mali_gralloc(20617): unregister: id=23b00000787, handle=0xb400006e09225000, base=0x0, importpid=20617, clone_count=0
D/mali_gralloc(20617): unregister: id=23b0000077a, handle=0xb400006e03f00120, base=0x0, importpid=20617, clone_count=0
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
I/flutter (20617): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (20617): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(20617): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(20617): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(20617): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(20617): register: id=23b0000079d, handle=0xb400006f1ebe1d40, importpid=20617
D/mali_gralloc(20617): register: id=23b0000079d, handle=0xb400006f1ebe1e20, importpid=20617
D/mali_gralloc(20617): unregister: id=23b0000079d, handle=0xb400006f1ebe1e20, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b0000079e, handle=0xb400006f1ebe1e20, importpid=20617
D/mali_gralloc(20617): register: id=23b0000079e, handle=0xb400006f1ebe1fe0, importpid=20617
D/mali_gralloc(20617): unregister: id=23b0000079e, handle=0xb400006f1ebe1fe0, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b0000079f, handle=0xb400006f1ebe1fe0, importpid=20617
D/mali_gralloc(20617): register: id=23b0000079f, handle=0xb400006f1ebe2d00, importpid=20617
D/mali_gralloc(20617): unregister: id=23b0000079f, handle=0xb400006f1ebe2d00, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b000007a0, handle=0xb400006f1ebe2d00, importpid=20617
D/mali_gralloc(20617): register: id=23b000007a0, handle=0xb400006f1ebe3080, importpid=20617
D/mali_gralloc(20617): unregister: id=23b000007a0, handle=0xb400006f1ebe3080, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b000007a1, handle=0xb400006f1ebe3080, importpid=20617
D/mali_gralloc(20617): register: id=23b000007a1, handle=0xb400006f1ebe34e0, importpid=20617
D/mali_gralloc(20617): unregister: id=23b000007a1, handle=0xb400006f1ebe34e0, base=0x0, importpid=20617, clone_count=1
D/mali_gralloc(20617): register: id=23b000007a2, handle=0xb400006f1ebe1020, importpid=20617
D/mali_gralloc(20617): register: id=23b000007a3, handle=0xb400006f1ebe3cc0, importpid=20617
I/flutter (20617): [Jarvis] Lifecycle: AppLifecycleState.resumed
D/JARVIS_WAKEWORD(20617): Sprache erkannt
D/JARVIS_WAKEWORD(20617): Sprachende
D/JARVIS_WAKEWORD(20617): Erkannt: okay jarvis okay schatz okay jabbis
D/JARVIS_WAKEWORD(20617): Wakeword erkannt
W/libc    (20617): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(20617): type=1400 audit(0.0:3923): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(20617): WakeLock aktiviert
D/JARVIS_WAKEWORD(20617): sendWakewordToFlutter
I/flutter (20617): [JARVIS BRIDGE] wakewordDetected
I/flutter (20617): [JARVIS BRIDGE] null
I/flutter (20617): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (20617): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (20617): [JARVIS] Wakeword Trigger empfangen
I/flutter (20617): [JARVIS] Controller State: JarvisState.idle
I/flutter (20617): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(20617): Wakeword STOP
I/flutter (20617): [JARVIS] Wakeword gestoppt
I/flutter (20617): [VOICE] listen() wird gestartet
I/flutter (20617): [VOICE] verfügbar: true
I/flutter (20617): [VOICE] SpeechToText aktiv
I/flutter (20617): [JARVIS] startListening verlassen
D/mali_gralloc(20617): register: id=23b000007a4, handle=0xb400006f20d573c0, importpid=20617
D/JARVIS_WAKEWORD(20617): Listening gestartet
I/flutter (20617): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Sprache erkannt
D/JARVIS_WAKEWORD(20617): Sprachende
D/JARVIS_WAKEWORD(20617): Erkannt: 123 1 2 3 zwei drei
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Sprache erkannt
D/JARVIS_WAKEWORD(20617): Sprachende
D/JARVIS_WAKEWORD(20617): Erkannt: hallo jarvis hallo chavez hallo charvis
D/JARVIS_WAKEWORD(20617): Wakeword erkannt
W/libc    (20617): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(20617): WakeLock aktiviert
D/JARVIS_WAKEWORD(20617): sendWakewordToFlutter
I/flutter (20617): [JARVIS BRIDGE] wakewordDetected
I/flutter (20617): [JARVIS BRIDGE] null
I/flutter (20617): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (20617): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (20617): [JARVIS] Wakeword Trigger empfangen
I/flutter (20617): [JARVIS] Controller State: JarvisState.thinking
I/flutter (20617): [JARVIS] Controller Busy: true
I/flutter (20617): [JARVIS] Wakeword ignoriert - Controller Busy
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Sprache erkannt
D/JARVIS_WAKEWORD(20617): Sprachende
D/JARVIS_WAKEWORD(20617): Erkannt: sage mir etwas zu den tagesinformationen sage mir etwas zu den tageseinformationen
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
D/JARVIS_WAKEWORD(20617): Listening gestartet
D/JARVIS_WAKEWORD(20617): Bereit für Wakeword
D/JARVIS_WAKEWORD(20617): Fehler: 7
