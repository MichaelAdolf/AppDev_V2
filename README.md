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
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,5s
I/FlutterActivityAndFragmentDelegate( 5978): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 5978): Beginning load of flutter...
D/FlutterJNI( 5978): flutter (null) was loaded normally!
I/flutter ( 5978): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 5978): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              245ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:62685/P-Sy4FxY16A=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:62685/P-Sy4FxY16A=/devtools/?uri=ws://127.0.0.1:62685/P-Sy4FxY16A=/ws
D/FlutterRenderer( 5978): Width is zero. 0,0
I/mple.jarvis_app( 5978): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app( 5978): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x2fb240c8190994c1
I/UnisocBufferQueueHelper( 5978): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006ec5c266c0, size:88
I/mple.jarvis_app( 5978): createUnisocBufferQueueHelperFactory success, get instance 0xb400006ec5c266c0
I/mple.jarvis_app( 5978): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25b43c40, size:296, enable:0
I/mple.jarvis_app( 5978): createUnisocFrameRecordFactory success, get instance 0xb400006f25b43c40
D/FlutterJNI( 5978): Sending viewport metrics to the engine.
W/libc    ( 5978): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 5978): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 5978): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 5978): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 5978): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 5978): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 5978): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 5978): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 5978): register: id=23b00000755, handle=0xb400006f1ebe34e0, importpid=5978
W/libc    ( 5978): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 5978): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 5978): register: id=23b00000755, handle=0xb400006f1ebe3860, importpid=5978
D/mali_gralloc( 5978): unregister: id=23b00000755, handle=0xb400006f1ebe3860, base=0x0, importpid=5978, clone_count=1
D/mali_gralloc( 5978): register: id=23b00000756, handle=0xb400006f1ebe3860, importpid=5978
D/mali_gralloc( 5978): register: id=23b00000756, handle=0xb400006f1ebe3940, importpid=5978
D/mali_gralloc( 5978): unregister: id=23b00000756, handle=0xb400006f1ebe3940, base=0x0, importpid=5978, clone_count=1
D/mali_gralloc( 5978): register: id=23b00000757, handle=0xb400006f1ebe3940, importpid=5978
D/mali_gralloc( 5978): register: id=23b00000757, handle=0xb400006f1ebe3a20, importpid=5978
D/mali_gralloc( 5978): unregister: id=23b00000757, handle=0xb400006f1ebe3a20, base=0x0, importpid=5978, clone_count=1
D/mali_gralloc( 5978): register: id=23b00000758, handle=0xb400006f1ebe3a20, importpid=5978
D/mali_gralloc( 5978): register: id=23b00000758, handle=0xb400006f1ebe3b00, importpid=5978
D/mali_gralloc( 5978): unregister: id=23b00000758, handle=0xb400006f1ebe3b00, base=0x0, importpid=5978, clone_count=1
D/mali_gralloc( 5978): register: id=23b00000759, handle=0xb400006f1ebe3b00, importpid=5978
D/mali_gralloc( 5978): register: id=23b00000759, handle=0xb400006f1ebe3be0, importpid=5978
D/mali_gralloc( 5978): unregister: id=23b00000759, handle=0xb400006f1ebe3be0, base=0x0, importpid=5978, clone_count=1
W/Choreographer( 5978): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 5978): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 5978): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 5978): Connected to TTS engine
I/TextToSpeech( 5978): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 5978): Listening gestartet
D/JARVIS_SERVICE( 5978): Foreground Service läuft
I/Choreographer( 5978): Skipped 54 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 5978): register: id=23b0000075a, handle=0xb400006e04ca6e80, importpid=5978
D/JARVIS_WS( 5978): WebSocket verbunden
I/HWUI    ( 5978): Davey! duration=929ms; Flags=1, FrameTimelineVsyncId=2872126, IntendedVsync=18792209339673, Vsync=18793111121151, InputEventId=0, HandleInputStart=18793125366326, AnimationStart=18793125368865, PerformTraversalsStart=18793125370134, DrawStart=18793129072826, FrameDeadline=18792226006340, FrameInterval=18793124988557, FrameStartTime=16699657, SyncQueued=18793130835365, SyncStart=18793130907095, IssueDrawCommandsStart=18793131685557, SwapBuffers=18793137498749, FrameCompleted=18793138925788, DequeueBufferDuration=1687808, QueueBufferDuration=978577, GpuCompleted=18793138827057, SwapBuffersCompleted=18793138925788, DisplayPresentTime=0, CommandSubmissionCompleted=18793137498749, 
D/JARVIS_TTS( 5978): Android TTS bereit
D/FlutterJNI( 5978): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD( 5978): Bereit für Wakeword
D/ProfileInstaller( 5978): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD( 5978): Fehler: 7
D/JARVIS_WAKEWORD( 5978): Listening gestartet
D/JARVIS_WAKEWORD( 5978): Bereit für Wakeword
D/JARVIS_WAKEWORD( 5978): Fehler: 7
D/JARVIS_WAKEWORD( 5978): Listening gestartet
D/JARVIS_WAKEWORD( 5978): Bereit für Wakeword
D/JARVIS_WAKEWORD( 5978): Sprache erkannt
D/JARVIS_WAKEWORD( 5978): Sprachende
D/JARVIS_WAKEWORD( 5978): Erkannt: ich erzähle dir jetzt mal etwas
D/JARVIS_WAKEWORD( 5978): Listening gestartet
D/JARVIS_WAKEWORD( 5978): Bereit für Wakeword
W/mple.jarvis_app( 5978): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 5978): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 5978): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 5978): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD( 5978): Fehler: 7
D/JARVIS_WAKEWORD( 5978): Listening gestartet
D/JARVIS_WAKEWORD( 5978): Bereit für Wakeword
D/JARVIS_WAKEWORD( 5978): Sprache erkannt
D/JARVIS_WAKEWORD( 5978): Sprachende
D/JARVIS_WAKEWORD( 5978): Erkannt: okay jarvis ok jarvis
D/JARVIS_WAKEWORD( 5978): Wakeword erkannt
W/libc    ( 5978): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 5978): type=1400 audit(0.0:3673): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 5978): WakeLock aktiviert
D/JARVIS_WAKEWORD( 5978): sendWakewordToFlutter
I/flutter ( 5978): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 5978): [JARVIS BRIDGE] null
I/flutter ( 5978): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 5978): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 5978): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 5978): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 5978): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 5978): Wakeword STOP
I/flutter ( 5978): [JARVIS] Wakeword gestoppt
I/flutter ( 5978): [VOICE] listen() wird gestartet
I/flutter ( 5978): [VOICE] verfügbar: true
D/mali_gralloc( 5978): register: id=23b0000076b, handle=0xb400006f20d56320, importpid=5978
I/flutter ( 5978): [VOICE] SpeechToText aktiv
I/flutter ( 5978): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD( 5978): Listening gestartet
