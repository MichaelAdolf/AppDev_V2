PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             19,2s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           7,2s
I/FlutterActivityAndFragmentDelegate(14537): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(14537): Beginning load of flutter...
D/FlutterJNI(14537): flutter (null) was loaded normally!
I/flutter (14537): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(14537): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              127ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:62528/WYlwsHlkfEg=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:62528/WYlwsHlkfEg=/devtools/?uri=ws://127.0.0.1:62528/WYlwsHlkfEg=/ws
D/FlutterRenderer(14537): Width is zero. 0,0
I/mple.jarvis_app(14537): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(14537): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x4d5ddc78bdad968d
I/UnisocBufferQueueHelper(14537): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006f25a65a80, size:88
I/mple.jarvis_app(14537): createUnisocBufferQueueHelperFactory success, get instance 0xb400006f25a65a80
I/mple.jarvis_app(14537): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f259add80, size:296, enable:0
I/mple.jarvis_app(14537): createUnisocFrameRecordFactory success, get instance 0xb400006f259add80
D/FlutterJNI(14537): Sending viewport metrics to the engine.
W/libc    (14537): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(14537): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(14537): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(14537): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(14537): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(14537): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(14537): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(14537): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(14537): register: id=23b000004f3, handle=0xb400006f25974780, importpid=14537
W/libc    (14537): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(14537): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc(14537): register: id=23b000004f3, handle=0xb400006f25974b00, importpid=14537
D/mali_gralloc(14537): unregister: id=23b000004f3, handle=0xb400006f25974b00, base=0x0, importpid=14537, clone_count=1
D/mali_gralloc(14537): register: id=23b000004f4, handle=0xb400006f25974b00, importpid=14537
D/mali_gralloc(14537): register: id=23b000004f4, handle=0xb400006f25974be0, importpid=14537
D/mali_gralloc(14537): unregister: id=23b000004f4, handle=0xb400006f25974be0, base=0x0, importpid=14537, clone_count=1
D/mali_gralloc(14537): register: id=23b000004f5, handle=0xb400006f25974be0, importpid=14537
D/mali_gralloc(14537): register: id=23b000004f5, handle=0xb400006f25974cc0, importpid=14537
D/mali_gralloc(14537): unregister: id=23b000004f5, handle=0xb400006f25974cc0, base=0x0, importpid=14537, clone_count=1
D/mali_gralloc(14537): register: id=23b000004f6, handle=0xb400006f25974cc0, importpid=14537
D/mali_gralloc(14537): register: id=23b000004f6, handle=0xb400006f25974da0, importpid=14537
D/mali_gralloc(14537): unregister: id=23b000004f6, handle=0xb400006f25974da0, base=0x0, importpid=14537, clone_count=1
D/mali_gralloc(14537): register: id=23b000004f7, handle=0xb400006f25974da0, importpid=14537
D/mali_gralloc(14537): register: id=23b000004f7, handle=0xb400006f25974e80, importpid=14537
D/mali_gralloc(14537): unregister: id=23b000004f7, handle=0xb400006f25974e80, base=0x0, importpid=14537, clone_count=1
W/Choreographer(14537): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(14537): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(14537): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(14537): Connected to TTS engine
I/TextToSpeech(14537): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_SERVICE(14537): Foreground Service läuft
D/JARVIS_WS(14537): WebSocket verbunden
I/Choreographer(14537): Skipped 73 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(14537): register: id=23b000004f8, handle=0xb400006e038f0040, importpid=14537
I/HWUI    (14537): Davey! duration=1282ms; Flags=1, FrameTimelineVsyncId=982538, IntendedVsync=11384370759668, Vsync=11385587426359, InputEventId=0, HandleInputStart=11385599465894, AnimationStart=11385599470971, PerformTraversalsStart=11385599473817, DrawStart=11385620173971, FrameDeadline=11384387426335, FrameInterval=11385598582509, FrameStartTime=16666667, SyncQueued=11385624535932, SyncStart=11385625258624, IssueDrawCommandsStart=11385627332586, SwapBuffers=11385651629817, FrameCompleted=11385654075740, DequeueBufferDuration=6495692, QueueBufferDuration=667500, GpuCompleted=11385654075740, SwapBuffersCompleted=11385652456663, DisplayPresentTime=0, CommandSubmissionCompleted=11385651629817, 
D/JARVIS_TTS(14537): Android TTS bereit
D/ProfileInstaller(14537): Installing profile for com.example.jarvis_app
D/FlutterJNI(14537): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
I/mple.jarvis_app(14537): Background concurrent mark compact GC freed 10MB AllocSpace bytes, 3(60KB) LOS objects, 49% free, 2850KB/5700KB, paused 594us,5.855ms total 50.315ms
W/mple.jarvis_app(14537): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(14537): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(14537): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(14537): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Partial Wakeword erkannt: hey jarvis
D/JARVIS_WAKEWORD(14537): Wakeword erkannt
W/libc    (14537): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(14537): type=1400 audit(0.0:3124): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14537): WakeLock aktiviert
D/JARVIS_WAKEWORD(14537): sendWakewordToFlutter
I/flutter (14537): [JARVIS BRIDGE] wakewordDetected
I/flutter (14537): [JARVIS BRIDGE] null
I/flutter (14537): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14537): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
D/JARVIS_WAKEWORD(14537): Erkannt: hey jarvis hey chavez ey jarvis
D/JARVIS_WAKEWORD(14537): Wakeword erkannt
W/libc    (14537): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(14537): type=1400 audit(0.0:3125): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14537): WakeLock aktiviert
D/JARVIS_WAKEWORD(14537): sendWakewordToFlutter
I/flutter (14537): [JARVIS BRIDGE] wakewordDetected
I/flutter (14537): [JARVIS BRIDGE] null
I/flutter (14537): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14537): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (14537): [JARVIS] Wakeword Trigger empfangen
I/flutter (14537): [JARVIS] Wakeword Trigger empfangen
D/mali_gralloc(14537): register: id=23b00000511, handle=0xb400006f25972640, importpid=14537
D/JARVIS_WAKEWORD(14537): Wakeword STOP
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Erkannt: sage mir etwas zum licht trage mir etwas zum licht frage mir etwas zum licht
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Erkannt: sage mir etwas zum licht zeige mir etwas zum licht frage mir etwas zum licht
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Partial Wakeword erkannt: hey jarvis
D/JARVIS_WAKEWORD(14537): Wakeword erkannt
W/libc    (14537): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(14537): type=1400 audit(0.0:3126): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14537): WakeLock aktiviert
D/JARVIS_WAKEWORD(14537): sendWakewordToFlutter
I/flutter (14537): [JARVIS BRIDGE] wakewordDetected
I/flutter (14537): [JARVIS BRIDGE] null
I/flutter (14537): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14537): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (14537): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Erkannt: hey jarvis hey schatz
D/JARVIS_WAKEWORD(14537): Wakeword erkannt
W/libc    (14537): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(14537): WakeLock aktiviert
D/JARVIS_WAKEWORD(14537): sendWakewordToFlutter
I/flutter (14537): [JARVIS BRIDGE] wakewordDetected
I/flutter (14537): [JARVIS BRIDGE] null
I/flutter (14537): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14537): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
W/mple.jarvis_app(14537): type=1400 audit(0.0:3127): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
I/flutter (14537): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Sprache erkannt
D/JARVIS_WAKEWORD(14537): Sprachende
D/JARVIS_WAKEWORD(14537): Erkannt: was ist mit dem licht was ist mit
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
D/JARVIS_WAKEWORD(14537): Fehler: 7
D/JARVIS_WAKEWORD(14537): Listening gestartet
D/JARVIS_WAKEWORD(14537): Bereit für Wakeword
