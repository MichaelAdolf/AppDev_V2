PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
lib/features/jarvis/ui/home_screen.dart:150:11: Error: 'await' can only be used in 'async' or 'async*' methods.
          await JarvisWakewordControl.start();
          ^^^^^
Target kernel_snapshot_program failed: Exception


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:compileFlutterBuildDebug'.
> Process 'command 'C:\Users\Michael\flutter\bin\flutter.bat'' finished with non-zero exit value 1

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to generate a Build Scan (Powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 11s
Running Gradle task 'assembleDebug'...                             11,8s
Error: Gradle task assembleDebug failed with exit code 1
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             19,3s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,9s
I/FlutterActivityAndFragmentDelegate(23059): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(23059): Beginning load of flutter...
D/FlutterJNI(23059): flutter (null) was loaded normally!
I/flutter (23059): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(23059): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              110ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:52380/FEbFCUtYcEs=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:52380/FEbFCUtYcEs=/devtools/?uri=ws://127.0.0.1:52380/FEbFCUtYcEs=/ws
D/FlutterRenderer(23059): Width is zero. 0,0
I/mple.jarvis_app(23059): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(23059): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xec3ea3f5df40e1a5
I/UnisocBufferQueueHelper(23059): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006ec5ddcd20, size:88
I/mple.jarvis_app(23059): createUnisocBufferQueueHelperFactory success, get instance 0xb400006ec5ddcd20
I/mple.jarvis_app(23059): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006e0ca17b40, size:296, enable:0
I/mple.jarvis_app(23059): createUnisocFrameRecordFactory success, get instance 0xb400006e0ca17b40
D/FlutterJNI(23059): Sending viewport metrics to the engine.
W/libc    (23059): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(23059): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(23059): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23059): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(23059): register: id=23b000007fc, handle=0xb400006f25b71fa0, importpid=23059
W/libc    (23059): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(23059): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc(23059): register: id=23b000007fc, handle=0xb400006f25b72320, importpid=23059
D/mali_gralloc(23059): unregister: id=23b000007fc, handle=0xb400006f25b72320, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b000007fd, handle=0xb400006f25b72320, importpid=23059
D/mali_gralloc(23059): register: id=23b000007fd, handle=0xb400006f25b72400, importpid=23059
D/mali_gralloc(23059): unregister: id=23b000007fd, handle=0xb400006f25b72400, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b000007fe, handle=0xb400006f25b72400, importpid=23059
D/mali_gralloc(23059): register: id=23b000007fe, handle=0xb400006f25b724e0, importpid=23059
D/mali_gralloc(23059): unregister: id=23b000007fe, handle=0xb400006f25b724e0, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b000007ff, handle=0xb400006f25b724e0, importpid=23059
D/mali_gralloc(23059): register: id=23b000007ff, handle=0xb400006f25b725c0, importpid=23059
D/mali_gralloc(23059): unregister: id=23b000007ff, handle=0xb400006f25b725c0, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b00000800, handle=0xb400006f25b725c0, importpid=23059
D/mali_gralloc(23059): register: id=23b00000800, handle=0xb400006f25b726a0, importpid=23059
D/mali_gralloc(23059): unregister: id=23b00000800, handle=0xb400006f25b726a0, base=0x0, importpid=23059, clone_count=1
W/Choreographer(23059): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(23059): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(23059): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(23059): Connected to TTS engine
I/TextToSpeech(23059): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_SERVICE(23059): Foreground Service läuft
I/Choreographer(23059): Skipped 86 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(23059): register: id=23b00000801, handle=0xb400006e06750da0, importpid=23059
I/HWUI    (23059): Davey! duration=1504ms; Flags=1, FrameTimelineVsyncId=5528785, IntendedVsync=26251155917985, Vsync=26252588972793, InputEventId=0, HandleInputStart=26252603519529, AnimationStart=26252603524952, PerformTraversalsStart=26252603527914, DrawStart=26252609701760, FrameDeadline=26251172584652, FrameInterval=26252602801414, FrameStartTime=16663428, SyncQueued=26252614433683, SyncStart=26252614567145, IssueDrawCommandsStart=26252615680452, SwapBuffers=26252637348645, FrameCompleted=26252660823491, DequeueBufferDuration=5447000, QueueBufferDuration=1147347, GpuCompleted=26252637348645, SwapBuffersCompleted=26252660823491, DisplayPresentTime=7382880253521260137, CommandSubmissionCompleted=26252637348645, 
D/ProfileInstaller(23059): Installing profile for com.example.jarvis_app
D/JARVIS_TTS(23059): Android TTS bereit
W/Choreographer(23059): Already have a pending vsync event.  There should only be one at a time.
D/FlutterJNI(23059): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
W/mple.jarvis_app(23059): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(23059): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(23059): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(23059): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
D/JARVIS_WS(23059): WebSocket verbunden
I/flutter (23059): [VOICE] Ergebnis: sage | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/TTS     (23059): Utterance ID has started: eda62917-f8c6-41b5-8af6-e87cb348e4aa
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/TTS     (23059): Utterance ID has completed: eda62917-f8c6-41b5-8af6-e87cb348e4aa
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: okay jarvis ok jarvis
D/JARVIS_WAKEWORD(23059): Wakeword erkannt
W/mple.jarvis_app(23059): type=1400 audit(0.0:3969): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
W/libc    (23059): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(23059): WakeLock aktiviert
D/JARVIS_WAKEWORD(23059): sendWakewordToFlutter
I/flutter (23059): [JARVIS BRIDGE] wakewordDetected
I/flutter (23059): [JARVIS BRIDGE] null
I/flutter (23059): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (23059): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (23059): [JARVIS] Wakeword Trigger empfangen
I/flutter (23059): [JARVIS] Controller State: JarvisState.idle
I/flutter (23059): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
D/mali_gralloc(23059): register: id=23b0000080e, handle=0xb400006e0cbc51c0, importpid=23059
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(23059): Listening gestartet
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis: dann | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir doch | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir doch auch | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir doch auch etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir doch auch etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir doch auch etwas zu nichts | final=false
I/flutter (23059): [VOICE] Ergebnis: dann sage mir doch auch etwas zu nichts | final=true
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: warum kannst du mir nichts zu nichts sagen warum kannst du mir nicht zum licht sagen warum kannst du mir nichts zum licht sagen
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: okay jarvis okay service
D/JARVIS_WAKEWORD(23059): Wakeword erkannt
W/libc    (23059): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(23059): type=1400 audit(0.0:3971): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(23059): WakeLock aktiviert
D/JARVIS_WAKEWORD(23059): sendWakewordToFlutter
I/flutter (23059): [JARVIS BRIDGE] wakewordDetected
I/flutter (23059): [JARVIS BRIDGE] null
I/flutter (23059): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (23059): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (23059): [JARVIS] Wakeword Trigger empfangen
I/flutter (23059): [JARVIS] Controller State: JarvisState.error
I/flutter (23059): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(23059): Listening gestartet
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis:  | final=false
I/flutter (23059): [VOICE] Ergebnis: sage | final=false
I/flutter (23059): [VOICE] Ergebnis: sage | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter (23059): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/TTS     (23059): Utterance ID has started: c6623849-5e18-4486-9e0a-bd7f8d9cec75
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/TTS     (23059): Utterance ID has completed: c6623849-5e18-4486-9e0a-bd7f8d9cec75
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: okay jarvis ok jarvis
D/JARVIS_WAKEWORD(23059): Wakeword erkannt
W/libc    (23059): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(23059): type=1400 audit(0.0:3973): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(23059): WakeLock aktiviert
D/JARVIS_WAKEWORD(23059): sendWakewordToFlutter
I/flutter (23059): [JARVIS BRIDGE] wakewordDetected
I/flutter (23059): [JARVIS BRIDGE] null
I/flutter (23059): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (23059): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (23059): [JARVIS] Wakeword Trigger empfangen
I/flutter (23059): [JARVIS] Controller State: JarvisState.idle
I/flutter (23059): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(23059): Listening gestartet
I/flutter (23059): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
I/flutter (23059): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](23059): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(23059): unregister: id=23b000007fe, handle=0xb400006f25b72400, base=0x0, importpid=23059, clone_count=0
D/mali_gralloc(23059): unregister: id=23b000007ff, handle=0xb400006f25b724e0, base=0x0, importpid=23059, clone_count=0
D/mali_gralloc(23059): unregister: id=23b00000800, handle=0xb400006f25b725c0, base=0x0, importpid=23059, clone_count=0
D/mali_gralloc(23059): unregister: id=23b000007fd, handle=0xb400006f25b72320, base=0x0, importpid=23059, clone_count=0
D/mali_gralloc(23059): unregister: id=23b000007fc, handle=0xb400006f25b71fa0, base=0x0, importpid=23059, clone_count=0
D/mali_gralloc(23059): unregister: id=23b0000080e, handle=0xb400006e0cbc51c0, base=0x0, importpid=23059, clone_count=0
D/mali_gralloc(23059): unregister: id=23b00000801, handle=0xb400006e06750da0, base=0x0, importpid=23059, clone_count=0
I/flutter (23059): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (23059): [Jarvis] Lifecycle: AppLifecycleState.paused
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Fehler: 7
I/flutter (23059): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (23059): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(23059): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23059): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23059): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(23059): register: id=23b00000850, handle=0xb400006f25b71d00, importpid=23059
D/mali_gralloc(23059): register: id=23b00000850, handle=0xb400006f25b71fa0, importpid=23059
D/mali_gralloc(23059): unregister: id=23b00000850, handle=0xb400006f25b71fa0, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b00000851, handle=0xb400006f25b71fa0, importpid=23059
D/mali_gralloc(23059): register: id=23b00000851, handle=0xb400006f25b72320, importpid=23059
D/mali_gralloc(23059): unregister: id=23b00000851, handle=0xb400006f25b72320, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b00000852, handle=0xb400006f25b72320, importpid=23059
D/mali_gralloc(23059): register: id=23b00000852, handle=0xb400006f25b72400, importpid=23059
D/mali_gralloc(23059): unregister: id=23b00000852, handle=0xb400006f25b72400, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b00000853, handle=0xb400006f25b72400, importpid=23059
D/mali_gralloc(23059): register: id=23b00000853, handle=0xb400006f25b724e0, importpid=23059
D/mali_gralloc(23059): unregister: id=23b00000853, handle=0xb400006f25b724e0, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b00000854, handle=0xb400006f25b724e0, importpid=23059
D/mali_gralloc(23059): register: id=23b00000854, handle=0xb400006f25b725c0, importpid=23059
D/mali_gralloc(23059): unregister: id=23b00000854, handle=0xb400006f25b725c0, base=0x0, importpid=23059, clone_count=1
D/mali_gralloc(23059): register: id=23b00000855, handle=0xb400006f25b70800, importpid=23059
D/mali_gralloc(23059): register: id=23b00000856, handle=0xb400006f25b72a20, importpid=23059
I/flutter (23059): [Jarvis] Lifecycle: AppLifecycleState.resumed
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: okay jarvis okay tschüss okay schatz
D/JARVIS_WAKEWORD(23059): Wakeword erkannt
W/libc    (23059): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(23059): type=1400 audit(0.0:3977): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(23059): WakeLock aktiviert
D/JARVIS_WAKEWORD(23059): sendWakewordToFlutter
I/flutter (23059): [JARVIS BRIDGE] wakewordDetected
I/flutter (23059): [JARVIS BRIDGE] null
I/flutter (23059): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (23059): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (23059): [JARVIS] Wakeword Trigger empfangen
I/flutter (23059): [JARVIS] Controller State: JarvisState.idle
I/flutter (23059): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
D/mali_gralloc(23059): register: id=23b0000085b, handle=0xb400006e0cbc5000, importpid=23059
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(23059): Listening gestartet
I/flutter (23059): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: ja jarvis ja chavez ja chave
D/JARVIS_WAKEWORD(23059): Wakeword erkannt
W/libc    (23059): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(23059): type=1400 audit(0.0:3979): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(23059): WakeLock aktiviert
D/JARVIS_WAKEWORD(23059): sendWakewordToFlutter
I/flutter (23059): [JARVIS BRIDGE] wakewordDetected
I/flutter (23059): [JARVIS BRIDGE] null
I/flutter (23059): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (23059): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (23059): [JARVIS] Wakeword Trigger empfangen
I/flutter (23059): [JARVIS] Controller State: JarvisState.idle
I/flutter (23059): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(23059): Listening gestartet
I/flutter (23059): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für Wakeword
D/JARVIS_WAKEWORD(23059): Sprache erkannt
D/JARVIS_WAKEWORD(23059): Sprachende
D/JARVIS_WAKEWORD(23059): Erkannt: hallo jarvis hallo chavez hallo chave
D/JARVIS_WAKEWORD(23059): Wakeword erkannt
W/libc    (23059): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(23059): type=1400 audit(0.0:3980): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(23059): WakeLock aktiviert
D/JARVIS_WAKEWORD(23059): sendWakewordToFlutter
I/flutter (23059): [JARVIS BRIDGE] wakewordDetected
I/flutter (23059): [JARVIS BRIDGE] null
I/flutter (23059): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (23059): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (23059): [JARVIS] Wakeword Trigger empfangen
I/flutter (23059): [JARVIS] Controller State: JarvisState.idle
I/flutter (23059): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(23059): Wakeword STOP
I/flutter (23059): [JARVIS] Wakeword gestoppt
I/flutter (23059): [VOICE] listen() wird gestartet
I/flutter (23059): [VOICE] verfügbar: true
I/flutter (23059): [VOICE] SpeechToText aktiv
I/flutter (23059): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(23059): Listening gestartet
I/flutter (23059): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(23059): Listening gestartet
D/JARVIS_WAKEWORD(23059): Bereit für WakewordPS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
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
