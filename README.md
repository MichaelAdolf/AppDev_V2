PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              9,4s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,1s
I/FlutterActivityAndFragmentDelegate( 7570): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 7570): Beginning load of flutter...
D/FlutterJNI( 7570): flutter (null) was loaded normally!
I/flutter ( 7570): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 7570): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              168ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:60350/9WCoivJUpcY=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:60350/9WCoivJUpcY=/devtools/?uri=ws://127.0.0.1:60350/9WCoivJUpcY=/ws
I/mple.jarvis_app( 7570): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer( 7570): Width is zero. 0,0
I/mple.jarvis_app( 7570): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x42a48a813e9e33af
I/UnisocBufferQueueHelper( 7570): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006e0a120840, size:88
I/mple.jarvis_app( 7570): createUnisocBufferQueueHelperFactory success, get instance 0xb400006e0a120840
I/mple.jarvis_app( 7570): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25b6cd80, size:296, enable:0
I/mple.jarvis_app( 7570): createUnisocFrameRecordFactory success, get instance 0xb400006f25b6cd80
D/FlutterJNI( 7570): Sending viewport metrics to the engine.
W/libc    ( 7570): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 7570): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 7570): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 7570): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 7570): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 7570): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 7570): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 7570): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 7570): register: id=23b00000beb, handle=0xb400006f25b2c4e0, importpid=7570
W/libc    ( 7570): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 7570): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 7570): register: id=23b00000beb, handle=0xb400006f25b2c860, importpid=7570
D/mali_gralloc( 7570): unregister: id=23b00000beb, handle=0xb400006f25b2c860, base=0x0, importpid=7570, clone_count=1
D/mali_gralloc( 7570): register: id=23b00000bec, handle=0xb400006f25b2c860, importpid=7570
D/mali_gralloc( 7570): register: id=23b00000bec, handle=0xb400006f25b2c940, importpid=7570
D/mali_gralloc( 7570): unregister: id=23b00000bec, handle=0xb400006f25b2c940, base=0x0, importpid=7570, clone_count=1
D/mali_gralloc( 7570): register: id=23b00000bed, handle=0xb400006f25b2c940, importpid=7570
D/mali_gralloc( 7570): register: id=23b00000bed, handle=0xb400006f25b2ca20, importpid=7570
D/mali_gralloc( 7570): unregister: id=23b00000bed, handle=0xb400006f25b2ca20, base=0x0, importpid=7570, clone_count=1
D/mali_gralloc( 7570): register: id=23b00000bee, handle=0xb400006f25b2ca20, importpid=7570
D/mali_gralloc( 7570): register: id=23b00000bee, handle=0xb400006f25b2cb00, importpid=7570
D/mali_gralloc( 7570): unregister: id=23b00000bee, handle=0xb400006f25b2cb00, base=0x0, importpid=7570, clone_count=1
D/mali_gralloc( 7570): register: id=23b00000bef, handle=0xb400006f25b2cb00, importpid=7570
D/mali_gralloc( 7570): register: id=23b00000bef, handle=0xb400006f25b2cbe0, importpid=7570
D/mali_gralloc( 7570): unregister: id=23b00000bef, handle=0xb400006f25b2cbe0, base=0x0, importpid=7570, clone_count=1
W/Choreographer( 7570): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 7570): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 7570): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 7570): Connected to TTS engine
I/TextToSpeech( 7570): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 7570): RECORD_AUDIO Permission fehlt
D/JARVIS_SERVICE( 7570): Foreground Service läuft
I/Choreographer( 7570): Skipped 58 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 7570): register: id=23b00000bf0, handle=0xb400006e02c45f60, importpid=7570
D/JARVIS_WS( 7570): WebSocket verbunden
I/HWUI    ( 7570): Davey! duration=1009ms; Flags=1, FrameTimelineVsyncId=6157171, IntendedVsync=33255326824001, Vsync=33256293490687, InputEventId=0, HandleInputStart=33256294367904, AnimationStart=33256294370366, PerformTraversalsStart=33256294371789, DrawStart=33256297281712, FrameDeadline=33255343490668, FrameInterval=33256294000328, FrameStartTime=16666667, SyncQueued=33256299983481, SyncStart=33256300148097, IssueDrawCommandsStart=33256300955866, SwapBuffers=33256334999058, FrameCompleted=33256336818597, DequeueBufferDuration=2417500, QueueBufferDuration=401270, GpuCompleted=33256336818597, SwapBuffersCompleted=33256335515904, DisplayPresentTime=0, CommandSubmissionCompleted=33256334999058, 
D/JARVIS_TTS( 7570): Android TTS bereit
I/flutter ( 7570): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/FlutterJNI( 7570): Sending viewport metrics to the engine.
D/ProfileInstaller( 7570): Installing profile for com.example.jarvis_app
I/flutter ( 7570): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 7570): [Jarvis] App resumed -> voice neu initialisieren
I/mple.jarvis_app( 7570): Background concurrent mark compact GC freed 10MB AllocSpace bytes, 3(60KB) LOS objects, 49% free, 2894KB/5724KB, paused 282us,7.660ms total 55.463ms
W/mple.jarvis_app( 7570): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 7570): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 7570): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 7570): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD( 7570): Listening gestartet
D/JARVIS_WAKEWORD( 7570): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7570): Sprache erkannt
D/JARVIS_WAKEWORD( 7570): Sprachende
D/JARVIS_WAKEWORD( 7570): Erkannt: okay tschüss
D/JARVIS_WAKEWORD( 7570): Listening gestartet
D/JARVIS_WAKEWORD( 7570): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7570): Sprache erkannt
D/JARVIS_WAKEWORD( 7570): Sprachende
D/JARVIS_WAKEWORD( 7570): Erkannt: okay jarvis
D/JARVIS_WAKEWORD( 7570): Wakeword erkannt
W/libc    ( 7570): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 7570): type=1400 audit(0.0:21176): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 7570): WakeLock aktiviert
D/JARVIS_WAKEWORD( 7570): sendWakewordToFlutter
I/flutter ( 7570): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 7570): [JARVIS BRIDGE] null
I/flutter ( 7570): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 7570): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 7570): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 7570): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 7570): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 7570): Wakeword STOP
D/mali_gralloc( 7570): register: id=23b00000bfe, handle=0xb400006f25b2ab80, importpid=7570
I/flutter ( 7570): [JARVIS] Wakeword gestoppt
I/flutter ( 7570): [VOICE] listen() wird gestartet
I/flutter ( 7570): [VOICE] verfügbar: true
I/flutter ( 7570): [VOICE] SpeechToText aktiv
I/flutter ( 7570): [JARVIS] startListening verlassen
I/flutter ( 7570): [VOICE] Ergebnis:  | final=false
I/flutter ( 7570): [VOICE] Ergebnis:  | final=false
I/flutter ( 7570): [VOICE] Ergebnis:  | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage mir etwas | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage mir etwas zum | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage mir etwas zum Licht | final=false
I/flutter ( 7570): [VOICE] Ergebnis: sage mir etwas zum Licht | final=true
D/TTS     ( 7570): Utterance ID has started: 27c8096b-b28f-4773-9f8c-0781e557cc8d
D/TTS     ( 7570): Utterance ID has completed: 27c8096b-b28f-4773-9f8c-0781e557cc8d
D/JARVIS_WAKEWORD( 7570): Mikrofon gehört Flutter
D/JARVIS_WAKEWORD( 7570): Wakeword STOP
I/flutter ( 7570): [JARVIS] Wakeword gestoppt
I/flutter ( 7570): [VOICE] listen() wird gestartet
I/flutter ( 7570): [VOICE] verfügbar: true
I/flutter ( 7570): [VOICE] SpeechToText aktiv
I/flutter ( 7570): [JARVIS] startListening verlassen
I/flutter ( 7570): [VOICE] Ergebnis:  | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage mir | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage mir etwas | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage mir etwas | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage mir etwas zum | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage mir etwas zum Licht | final=false
I/flutter ( 7570): [VOICE] Ergebnis: okay sage mir etwas zum Licht | final=true
D/TTS     ( 7570): Utterance ID has started: 7d3c56dc-0456-4c83-b560-993109dbab60
D/TTS     ( 7570): Utterance ID has completed: 7d3c56dc-0456-4c83-b560-993109dbab60
D/JARVIS_WAKEWORD( 7570): Mikrofon gehört Flutter
