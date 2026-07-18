PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             19,0s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,0s
I/FlutterActivityAndFragmentDelegate( 3299): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 3299): Beginning load of flutter...
D/FlutterJNI( 3299): flutter (null) was loaded normally!
I/flutter ( 3299): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 3299): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              102ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:55110/M7c_Hjozl7o=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:55110/M7c_Hjozl7o=/devtools/?uri=ws://127.0.0.1:55110/M7c_Hjozl7o=/ws
D/FlutterRenderer( 3299): Width is zero. 0,0
I/mple.jarvis_app( 3299): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app( 3299): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x7f7ea7ee6af63d2b
I/UnisocBufferQueueHelper( 3299): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006ec5dfeba0, size:88
I/mple.jarvis_app( 3299): createUnisocBufferQueueHelperFactory success, get instance 0xb400006ec5dfeba0
I/mple.jarvis_app( 3299): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25b73c40, size:296, enable:0
I/mple.jarvis_app( 3299): createUnisocFrameRecordFactory success, get instance 0xb400006f25b73c40
D/FlutterJNI( 3299): Sending viewport metrics to the engine.
W/libc    ( 3299): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 3299): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 3299): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 3299): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 3299): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 3299): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 3299): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 3299): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 3299): register: id=23b0000071c, handle=0xb400006f25b346a0, importpid=3299
W/libc    ( 3299): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 3299): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 3299): register: id=23b0000071c, handle=0xb400006f25b34a20, importpid=3299
D/mali_gralloc( 3299): unregister: id=23b0000071c, handle=0xb400006f25b34a20, base=0x0, importpid=3299, clone_count=1
D/mali_gralloc( 3299): register: id=23b0000071d, handle=0xb400006f25b34a20, importpid=3299
D/mali_gralloc( 3299): register: id=23b0000071d, handle=0xb400006f25b34b00, importpid=3299
D/mali_gralloc( 3299): unregister: id=23b0000071d, handle=0xb400006f25b34b00, base=0x0, importpid=3299, clone_count=1
D/mali_gralloc( 3299): register: id=23b0000071e, handle=0xb400006f25b34b00, importpid=3299
D/mali_gralloc( 3299): register: id=23b0000071e, handle=0xb400006f25b34be0, importpid=3299
D/mali_gralloc( 3299): unregister: id=23b0000071e, handle=0xb400006f25b34be0, base=0x0, importpid=3299, clone_count=1
D/mali_gralloc( 3299): register: id=23b0000071f, handle=0xb400006f25b34be0, importpid=3299
D/mali_gralloc( 3299): register: id=23b0000071f, handle=0xb400006f25b34cc0, importpid=3299
D/mali_gralloc( 3299): unregister: id=23b0000071f, handle=0xb400006f25b34cc0, base=0x0, importpid=3299, clone_count=1
D/mali_gralloc( 3299): register: id=23b00000720, handle=0xb400006f25b34cc0, importpid=3299
D/mali_gralloc( 3299): register: id=23b00000720, handle=0xb400006f25b34da0, importpid=3299
D/mali_gralloc( 3299): unregister: id=23b00000720, handle=0xb400006f25b34da0, base=0x0, importpid=3299, clone_count=1
W/Choreographer( 3299): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 3299): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 3299): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 3299): Connected to TTS engine
I/TextToSpeech( 3299): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 3299): Listening gestartet
D/JARVIS_SERVICE( 3299): Foreground Service läuft
D/JARVIS_WS( 3299): WebSocket verbunden
I/Choreographer( 3299): Skipped 57 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 3299): register: id=23b00000721, handle=0xb400006e045f2040, importpid=3299
I/HWUI    ( 3299): Davey! duration=977ms; Flags=1, FrameTimelineVsyncId=2595163, IntendedVsync=18031659418001, Vsync=18032609418020, InputEventId=0, HandleInputStart=18032615822986, AnimationStart=18032615827101, PerformTraversalsStart=18032615829409, DrawStart=18032620769255, FrameDeadline=18031676084668, FrameInterval=18032614994139, FrameStartTime=16666667, SyncQueued=18032622831370, SyncStart=18032623194639, IssueDrawCommandsStart=18032624078139, SwapBuffers=18032635627139, FrameCompleted=18032636852870, DequeueBufferDuration=2490000, QueueBufferDuration=813653, GpuCompleted=18032636827024, SwapBuffersCompleted=18032636852870, DisplayPresentTime=7594879245753807719, CommandSubmissionCompleted=18032635627139, 
D/JARVIS_TTS( 3299): Android TTS bereit
D/FlutterJNI( 3299): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD( 3299): Bereit für Wakeword
D/ProfileInstaller( 3299): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD( 3299): Fehler: 7
D/JARVIS_WAKEWORD( 3299): Listening gestartet
D/JARVIS_WAKEWORD( 3299): Bereit für Wakeword
D/JARVIS_WAKEWORD( 3299): Sprache erkannt
D/JARVIS_WAKEWORD( 3299): Sprachende
D/JARVIS_WAKEWORD( 3299): Erkannt: okay jarvis ok jarvis okay chavez
D/JARVIS_WAKEWORD( 3299): Wakeword erkannt
W/libc    ( 3299): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 3299): type=1400 audit(0.0:3605): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.google.android.gms
D/JARVIS_WAKE( 3299): WakeLock aktiviert
D/JARVIS_WAKEWORD( 3299): sendWakewordToFlutter
I/flutter ( 3299): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 3299): [JARVIS BRIDGE] null
I/flutter ( 3299): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 3299): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
W/mple.jarvis_app( 3299): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 3299): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 3299): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 3299): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter ( 3299): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 3299): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 3299): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 3299): Wakeword STOP
I/flutter ( 3299): [JARVIS] Wakeword gestoppt
I/flutter ( 3299): [VOICE] listen() wird gestartet
I/flutter ( 3299): [VOICE] verfügbar: true
D/mali_gralloc( 3299): register: id=23b00000726, handle=0xb400006f20d57580, importpid=3299
I/flutter ( 3299): [VOICE] SpeechToText aktiv
I/flutter ( 3299): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD( 3299): Listening gestartet
D/JARVIS_WAKEWORD( 3299): Bereit für Wakeword
D/JARVIS_WAKEWORD( 3299): Sprache erkannt
D/JARVIS_WAKEWORD( 3299): Sprachende
W/mple.jarvis_app( 3299): type=1400 audit(0.0:3606): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.google.android.gms
D/JARVIS_WAKEWORD( 3299): Erkannt: okay jarvis ok jarvis
D/JARVIS_WAKEWORD( 3299): Wakeword erkannt
W/libc    ( 3299): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE( 3299): WakeLock aktiviert
D/JARVIS_WAKEWORD( 3299): sendWakewordToFlutter
I/flutter ( 3299): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 3299): [JARVIS BRIDGE] null
I/flutter ( 3299): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 3299): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
D/JARVIS_WAKEWORD( 3299): Restart blockiert
I/flutter ( 3299): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 3299): [JARVIS] Controller State: JarvisState.listening
I/flutter ( 3299): [JARVIS] Controller Busy: true
I/flutter ( 3299): [JARVIS] Wakeword ignoriert - Controller Busy
