PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
e: file:///D:/Users/Michael/Dokumente/16_AppDev/jarvis_app/android/app/src/main/kotlin/com/example/jarvis_app/JarvisForegroundService.kt:666:9 Argument type mismatch: actual type is 'Runnable?', but 'Runnable' was expected.

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:compileDebugKotlin'.
> A failure occurred while executing org.jetbrains.kotlin.compilerRunner.GradleCompilerRunnerWithWorkers$GradleKotlinCompilerWorkAction
   > Compilation error. See log for more details

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to generate a Build Scan (Powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 7s
Running Gradle task 'assembleDebug'...                              7,7s
Error: Gradle task assembleDebug failed with exit code 1
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              7,8s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,1s
I/FlutterActivityAndFragmentDelegate(29287): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(29287): Beginning load of flutter...
D/FlutterJNI(29287): flutter (null) was loaded normally!
I/flutter (29287): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(29287): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              107ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:58426/gZydohj3sf4=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:58426/gZydohj3sf4=/devtools/?uri=ws://127.0.0.1:58426/gZydohj3sf4=/ws
D/FlutterRenderer(29287): Width is zero. 0,0
I/mple.jarvis_app(29287): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x6a984605450893ad
I/UnisocBufferQueueHelper(29287): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006e0c99d780, size:88
I/mple.jarvis_app(29287): createUnisocBufferQueueHelperFactory success, get instance 0xb400006e0c99d780
I/mple.jarvis_app(29287): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25b0fec0, size:296, enable:0
I/mple.jarvis_app(29287): createUnisocFrameRecordFactory success, get instance 0xb400006f25b0fec0
I/mple.jarvis_app(29287): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterJNI(29287): Sending viewport metrics to the engine.
W/libc    (29287): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(29287): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(29287): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29287): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(29287): register: id=23b00000a0b, handle=0xb400006f1ec08400, importpid=29287
W/libc    (29287): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(29287): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc(29287): register: id=23b00000a0b, handle=0xb400006f1ec08780, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a0b, handle=0xb400006f1ec08780, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a0c, handle=0xb400006f1ec08780, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a0c, handle=0xb400006f1ec08860, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a0c, handle=0xb400006f1ec08860, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a0d, handle=0xb400006f1ec08860, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a0d, handle=0xb400006f1ec08940, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a0d, handle=0xb400006f1ec08940, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a0e, handle=0xb400006f1ec08940, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a0e, handle=0xb400006f1ec08a20, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a0e, handle=0xb400006f1ec08a20, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a0f, handle=0xb400006f1ec08a20, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a0f, handle=0xb400006f1ec08b00, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a0f, handle=0xb400006f1ec08b00, base=0x0, importpid=29287, clone_count=1
W/Choreographer(29287): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(29287): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(29287): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(29287): Connected to TTS engine
I/TextToSpeech(29287): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_SERVICE(29287): Foreground Service läuft
I/Choreographer(29287): Skipped 64 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(29287): register: id=23b00000a10, handle=0xb400006e081ddf60, importpid=29287
D/JARVIS_WS(29287): WebSocket verbunden
I/HWUI    (29287): Davey! duration=1101ms; Flags=1, FrameTimelineVsyncId=5757883, IntendedVsync=28090180200001, Vsync=28091249074945, InputEventId=0, HandleInputStart=28091264544753, AnimationStart=28091264548868, PerformTraversalsStart=28091264551137, DrawStart=28091269603560, FrameDeadline=28090196866668, FrameInterval=28091263921945, FrameStartTime=16701171, SyncQueued=28091271481253, SyncStart=28091271610522, IssueDrawCommandsStart=28091272426599, SwapBuffers=28091280282522, FrameCompleted=28091282184714, DequeueBufferDuration=2155154, QueueBufferDuration=975616, GpuCompleted=28091281298676, SwapBuffersCompleted=28091282184714, DisplayPresentTime=7599383958533334121, CommandSubmissionCompleted=28091280282522, 
D/JARVIS_TTS(29287): Android TTS bereit
D/FlutterJNI(29287): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/ProfileInstaller(29287): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
W/mple.jarvis_app(29287): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(29287): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(29287): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(29287): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: okay jarvis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4054): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
D/mali_gralloc(29287): register: id=23b00000a21, handle=0xb400006f1ec06480, importpid=29287
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis: sage | final=false
I/flutter (29287): [VOICE] Ergebnis: sage | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/TTS     (29287): Utterance ID has started: fbe74f62-ce86-4068-b5ab-c269141724f1
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4056): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.speaking
I/flutter (29287): [JARVIS] Controller Busy: true
I/flutter (29287): [JARVIS] Wakeword ignoriert - Controller Busy
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/TTS     (29287): Utterance ID has completed: fbe74f62-ce86-4068-b5ab-c269141724f1
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet turnunterricht
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet turnunterricht
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet turnunterricht
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: leid living unterstrichboden wurde über den jarvis router verarbeitet turnunterricht
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
W/mple.jarvis_app(29287): type=1400 audit(0.0:4058): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKEWORD(29287): Erkannt: okay tschüss okay jarvis okay charles
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis: wie | final=false
I/flutter (29287): [VOICE] Ergebnis: wie | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit den | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit den | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit den | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit den tagesinformationen aus | final=false
I/flutter (29287): [VOICE] Ergebnis: wie schaut es mit den tagesinformationen aus | final=true
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WS(29287): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 18:20. Draußen sind es aktuell 25 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(29287): Node-RED Event wird verarbeitet
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(29287): type=1400 audit(0.0:4060): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_TTS(29287): Sprache: Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 18:20. Draußen sind es aktuell 25 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT(29287): Activity wird geöffnet
D/JARVIS_BRIDGE(29287): openAndDeliverEvent
D/JARVIS_BRIDGE(29287): Bridge Activity in Vordergrund
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (29287): [Jarvis] App resumed -> voice neu initialisieren
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE(29287): Intent Event empfangen
D/JARVIS_BRIDGE(29287): Gepuffertes Event wird gesendet
I/flutter (29287): [JARVIS BRIDGE] backgroundEvent
I/flutter (29287): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 18:20. Draußen sind es aktuell 25 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (29287): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Samstag, der achtzehnter Juli 2026. Die aktuelle Uhrzeit ist 18:20. Draußen sind es aktuell 25 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (29287): [Jarvis] App resumed -> voice neu initialisieren
D/FlutterJNI(29287): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: guten abend heute ist samstag der 18 juli 2026 die aktuelle uhrzeit ist 18:20 uhr draußen sind es aktuell 25 grad bei leicht bewölktem guten abend heute ist samstag der 18 juli 2026 die aktuelle uhrzeit ist 18:20 uhr draußen sind es aktuell 25° bei leicht bewölktem guten abend heute ist samstag der 18 juli 2026 die aktuelle uhrzeit ist 18:20 uhr draußen sind es aktuell 25 grad bei leicht bewölkt
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis: sage | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter (29287): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/TTS     (29287): Utterance ID has started: 7afb3e3c-0206-40fc-8163-1b818776e0f4
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/TTS     (29287): Utterance ID has completed: 7afb3e3c-0206-40fc-8163-1b818776e0f4
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay jarvis ok jarvis okay chavez
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/mple.jarvis_app(29287): type=1400 audit(0.0:4062): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis: was | final=false
I/flutter (29287): [VOICE] Ergebnis: was | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert wenn | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert wenn ich | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert wenn ich | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert wenn ich nichts | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert wenn ich nichts sage | final=false
I/flutter (29287): [VOICE] Ergebnis: was passiert wenn ich nichts sage | final=true
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay jarvis okay ciao bis okay jarres
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/mple.jarvis_app(29287): type=1400 audit(0.0:4064): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.error
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: zeige mir etwas zum licht zeige mir was zum licht
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay jarvis ok jarvis okay jarvist
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4065): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis: Informationen | final=false
I/flutter (29287): [VOICE] Ergebnis: Informationen bitte | final=false
I/flutter (29287): [VOICE] Ergebnis: Informationen bitte | final=false
I/flutter (29287): [VOICE] Ergebnis: Informationen bitte zum | final=false
I/flutter (29287): [VOICE] Ergebnis: Informationen bitte zum Licht | final=false
I/flutter (29287): [VOICE] Ergebnis: Informationen bitte zum Licht | final=true
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/TTS     (29287): Utterance ID has started: 3daa0f9b-d8d4-4dd5-a35f-c2e02fad1fd1
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Partial Wakeword erkannt: okay jarvis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/mple.jarvis_app(29287): type=1400 audit(0.0:4067): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.speaking
I/flutter (29287): [JARVIS] Controller Busy: true
I/flutter (29287): [JARVIS] Wakeword ignoriert - Controller Busy
D/TTS     (29287): Utterance ID has completed: 3daa0f9b-d8d4-4dd5-a35f-c2e02fad1fd1
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay jarvis okay charles ok jarvis
D/JARVIS_WAKEWORD(29287): Wakeword Cooldown aktiv
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay jarvis ok jarvis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4068): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay jarvis ok jarvis okay chavez
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4070): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis:  | final=false
I/flutter (29287): [VOICE] Ergebnis: lass | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal einen | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal einen Fehler | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal einen Fehler reinbringen | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal einen Fehler reinbringen | final=false
I/flutter (29287): [VOICE] Ergebnis: lass uns mal einen Fehler reinbringen | final=true
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay tschüss okay jarvis okay ciao bis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4071): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](29287): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(29287): unregister: id=23b00000a0b, handle=0xb400006f1ec08400, base=0x0, importpid=29287, clone_count=0
D/mali_gralloc(29287): unregister: id=23b00000a0c, handle=0xb400006f1ec08780, base=0x0, importpid=29287, clone_count=0
D/mali_gralloc(29287): unregister: id=23b00000a0d, handle=0xb400006f1ec08860, base=0x0, importpid=29287, clone_count=0
D/mali_gralloc(29287): unregister: id=23b00000a21, handle=0xb400006f1ec06480, base=0x0, importpid=29287, clone_count=0
D/mali_gralloc(29287): unregister: id=23b00000a10, handle=0xb400006e081ddf60, base=0x0, importpid=29287, clone_count=0
D/mali_gralloc(29287): unregister: id=23b00000a0f, handle=0xb400006f1ec08a20, base=0x0, importpid=29287, clone_count=0
D/mali_gralloc(29287): unregister: id=23b00000a0e, handle=0xb400006f1ec08940, base=0x0, importpid=29287, clone_count=0
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.paused
I/flutter (29287): [Jarvis] App pausiert
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Fehler: 7
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(29287): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29287): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29287): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(29287): register: id=23b00000a9b, handle=0xb400006f1ec077c0, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a9b, handle=0xb400006f1ec08160, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a9b, handle=0xb400006f1ec08160, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a9c, handle=0xb400006f1ec08160, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a9c, handle=0xb400006f1ec08400, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a9c, handle=0xb400006f1ec08400, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a9d, handle=0xb400006f1ec08860, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a9d, handle=0xb400006f1ec08940, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a9d, handle=0xb400006f1ec08940, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a9e, handle=0xb400006f1ec08940, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a9e, handle=0xb400006f1ec08a20, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a9e, handle=0xb400006f1ec08a20, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000a9f, handle=0xb400006f1ec08a20, importpid=29287
D/mali_gralloc(29287): register: id=23b00000a9f, handle=0xb400006f1ec08b00, importpid=29287
D/mali_gralloc(29287): unregister: id=23b00000a9f, handle=0xb400006f1ec08b00, base=0x0, importpid=29287, clone_count=1
D/mali_gralloc(29287): register: id=23b00000aa0, handle=0xb400006f20d57ac0, importpid=29287
D/mali_gralloc(29287): register: id=23b00000aa1, handle=0xb400006e0cb500e0, importpid=29287
I/flutter (29287): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (29287): [Jarvis] App resumed -> voice neu initialisieren
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: okay tschüss okay jarvis okay ciao bis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(29287): type=1400 audit(0.0:4076): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
D/mali_gralloc(29287): register: id=23b00000aa2, handle=0xb400006f20d56320, importpid=29287
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Sprache erkannt
D/JARVIS_WAKEWORD(29287): Sprachende
D/JARVIS_WAKEWORD(29287): Erkannt: licht hallo jarvis nicht hallo jarvis
D/JARVIS_WAKEWORD(29287): Wakeword erkannt
W/mple.jarvis_app(29287): type=1400 audit(0.0:4078): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
W/libc    (29287): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(29287): WakeLock aktiviert
D/JARVIS_WAKEWORD(29287): sendWakewordToFlutter
I/flutter (29287): [JARVIS BRIDGE] wakewordDetected
I/flutter (29287): [JARVIS BRIDGE] null
I/flutter (29287): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (29287): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (29287): [JARVIS] Wakeword Trigger empfangen
I/flutter (29287): [JARVIS] Controller State: JarvisState.idle
I/flutter (29287): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
D/JARVIS_WAKEWORD(29287): Wakeword STOP
I/flutter (29287): [JARVIS] Wakeword gestoppt
I/flutter (29287): [VOICE] listen() wird gestartet
I/flutter (29287): [VOICE] verfügbar: true
I/flutter (29287): [VOICE] SpeechToText aktiv
I/flutter (29287): [JARVIS] startListening verlassen
I/flutter (29287): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(29287): Listening gestartet
D/JARVIS_WAKEWORD(29287): Bereit für Wakeword
