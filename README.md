PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             20,8s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,1s
I/FlutterActivityAndFragmentDelegate( 1918): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 1918): Beginning load of flutter...
D/FlutterJNI( 1918): flutter (null) was loaded normally!
I/flutter ( 1918): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 1918): Width is zero. 0,0
Syncing files to device 25028RN03Y...                               97ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:59484/ittQ_ENvN10=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:59484/ittQ_ENvN10=/devtools/?uri=ws://127.0.0.1:59484/ittQ_ENvN10=/ws
I/Choreographer( 1918): Skipped 221 frames!  The application may be doing too much work on its main thread.
D/FlutterRenderer( 1918): Width is zero. 0,0
I/mple.jarvis_app( 1918): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app( 1918): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xf882cacf3470c1fb
I/UnisocBufferQueueHelper( 1918): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006f25b6d700, size:88
I/mple.jarvis_app( 1918): createUnisocBufferQueueHelperFactory success, get instance 0xb400006f25b6d700
I/mple.jarvis_app( 1918): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25a6ec40, size:296, enable:0
I/mple.jarvis_app( 1918): createUnisocFrameRecordFactory success, get instance 0xb400006f25a6ec40
D/FlutterJNI( 1918): Sending viewport metrics to the engine.
W/libc    ( 1918): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 1918): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 1918): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 1918): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1918): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1918): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 1918): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1918): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 1918): register: id=23b00000704, handle=0xb400006f25a354e0, importpid=1918
W/libc    ( 1918): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 1918): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 1918): register: id=23b00000704, handle=0xb400006f25a35860, importpid=1918
D/mali_gralloc( 1918): unregister: id=23b00000704, handle=0xb400006f25a35860, base=0x0, importpid=1918, clone_count=1
D/mali_gralloc( 1918): register: id=23b00000705, handle=0xb400006f25a35860, importpid=1918
D/mali_gralloc( 1918): register: id=23b00000705, handle=0xb400006f25a35940, importpid=1918
D/mali_gralloc( 1918): unregister: id=23b00000705, handle=0xb400006f25a35940, base=0x0, importpid=1918, clone_count=1
D/mali_gralloc( 1918): register: id=23b00000706, handle=0xb400006f25a35940, importpid=1918
D/mali_gralloc( 1918): register: id=23b00000706, handle=0xb400006f25a35a20, importpid=1918
D/mali_gralloc( 1918): unregister: id=23b00000706, handle=0xb400006f25a35a20, base=0x0, importpid=1918, clone_count=1
D/mali_gralloc( 1918): register: id=23b00000707, handle=0xb400006f25a35a20, importpid=1918
D/mali_gralloc( 1918): register: id=23b00000707, handle=0xb400006f25a35b00, importpid=1918
D/mali_gralloc( 1918): unregister: id=23b00000707, handle=0xb400006f25a35b00, base=0x0, importpid=1918, clone_count=1
D/mali_gralloc( 1918): register: id=23b00000708, handle=0xb400006f25a35b00, importpid=1918
D/mali_gralloc( 1918): register: id=23b00000708, handle=0xb400006f25a35be0, importpid=1918
D/mali_gralloc( 1918): unregister: id=23b00000708, handle=0xb400006f25a35be0, base=0x0, importpid=1918, clone_count=1
I/TextToSpeech( 1918): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 1918): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 1918): Connected to TTS engine
I/TextToSpeech( 1918): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 1918): Listening gestartet
D/JARVIS_SERVICE( 1918): Foreground Service läuft
D/JARVIS_WS( 1918): WebSocket verbunden
I/Choreographer( 1918): Skipped 68 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 1918): register: id=23b00000709, handle=0xb400006e05fafc60, importpid=1918
I/HWUI    ( 1918): Davey! duration=1164ms; Flags=1, FrameTimelineVsyncId=2384334, IntendedVsync=17497152844001, Vsync=17498286177357, InputEventId=0, HandleInputStart=17498295387022, AnimationStart=17498295391175, PerformTraversalsStart=17498295393675, DrawStart=17498300554906, FrameDeadline=17497169510668, FrameInterval=17498294473099, FrameStartTime=16666667, SyncQueued=17498304165906, SyncStart=17498304264214, IssueDrawCommandsStart=17498305286252, SwapBuffers=17498316312060, FrameCompleted=17498317573675, DequeueBufferDuration=2104461, QueueBufferDuration=1060769, GpuCompleted=17498317389368, SwapBuffersCompleted=17498317573675, DisplayPresentTime=1028191643986679876, CommandSubmissionCompleted=17498316312060, 
D/JARVIS_TTS( 1918): Android TTS bereit
D/FlutterJNI( 1918): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD( 1918): Bereit für Wakeword
D/ProfileInstaller( 1918): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD( 1918): Sprache erkannt
D/JARVIS_WAKEWORD( 1918): Fehler: 7
D/JARVIS_WAKEWORD( 1918): Listening gestartet
D/JARVIS_WAKEWORD( 1918): Bereit für Wakeword
I/mple.jarvis_app( 1918): Background concurrent mark compact GC freed 10MB AllocSpace bytes, 3(60KB) LOS objects, 49% free, 2838KB/5676KB, paused 668us,6.299ms total 61.474ms
W/mple.jarvis_app( 1918): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 1918): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 1918): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 1918): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD( 1918): Sprache erkannt
D/JARVIS_WAKEWORD( 1918): Sprachende
D/JARVIS_WAKEWORD( 1918): Erkannt: okay schatz okay jarvis okay ciao bis
D/JARVIS_WAKEWORD( 1918): Wakeword erkannt
W/libc    ( 1918): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 1918): type=1400 audit(0.0:3570): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 1918): WakeLock aktiviert
D/JARVIS_WAKEWORD( 1918): sendWakewordToFlutter
I/flutter ( 1918): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 1918): [JARVIS BRIDGE] null
I/flutter ( 1918): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 1918): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 1918): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 1918): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 1918): [JARVIS] Controller Busy: false
I/flutter ( 1918): [JARVIS] _startVoiceInput START
D/JARVIS_WAKEWORD( 1918): Wakeword STOP
I/flutter ( 1918): [JARVIS] Wakeword gestoppt
I/flutter ( 1918): [VOICE] listen() wird gestartet
D/mali_gralloc( 1918): register: id=23b00000712, handle=0xb400006f25a32d80, importpid=1918
I/flutter ( 1918): [VOICE] SpeechToText active
D/JARVIS_WAKEWORD( 1918): Listening gestartet
D/JARVIS_WAKEWORD( 1918): Bereit für Wakeword
D/JARVIS_WAKEWORD( 1918): Sprache erkannt
D/JARVIS_WAKEWORD( 1918): Sprachende
D/JARVIS_WAKEWORD( 1918): Erkannt: gebe mir informationen zum licht gebe mir information zum licht gebe mehr informationen zum licht
D/JARVIS_WAKEWORD( 1918): Restart blockiert
