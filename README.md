PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             26,3s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,5s
I/FlutterActivityAndFragmentDelegate(31466): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(31466): Beginning load of flutter...
D/FlutterJNI(31466): flutter (null) was loaded normally!
I/flutter (31466): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(31466): Width is zero. 0,0
D/FlutterRenderer(31466): Width is zero. 0,0
D/FlutterJNI(31466): Sending viewport metrics to the engine.
D/FlutterJNI(31466): Sending viewport metrics to the engine.
Syncing files to device 25028RN03Y...                              153ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:50529/Y2c8ro_aQ4E=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:50529/Y2c8ro_aQ4E=/devtools/?uri=ws://127.0.0.1:50529/Y2c8ro_aQ4E=/ws
I/TextToSpeech(31466): Connected to TTS engine
I/TextToSpeech(31466): Setting up the connection to TTS engine...
D/ProfileInstaller(31466): Installing profile for com.example.jarvis_app
I/flutter (31466): [Jarvis WebSocket] WebSocket verbunden
I/Choreographer(31466): Skipped 125 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(31466): register: id=23b00000210, handle=0xb400007053ffd820, importpid=31466
I/HWUI    (31466): Davey! duration=2117ms; Flags=1, FrameTimelineVsyncId=279202, IntendedVsync=8201037001423, Vsync=8203120890548, InputEventId=0, HandleInputStart=8203135669901, AnimationStart=8203135672208, PerformTraversalsStart=8203135673362, DrawStart=8203138490824, FrameDeadline=8201053668090, FrameInterval=8203134785170, FrameStartTime=16671113, SyncQueued=8203139588131, SyncStart=8203139651477, IssueDrawCommandsStart=8203140498401, SwapBuffers=8203151670516, FrameCompleted=8203154140785, DequeueBufferDuration=2613884, QueueBufferDuration=721769, GpuCompleted=8203154140785, SwapBuffersCompleted=8203152563862, DisplayPresentTime=0, CommandSubmissionCompleted=8203151670516, 
I/mple.jarvis_app(31466): Background concurrent mark compact GC freed 8076KB AllocSpace bytes, 9(180KB) LOS objects, 49% free, 2703KB/5407KB, paused 479us,6.790ms total 37.351ms
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (31466): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](31466): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(31466): unregister: id=23b0000020d, handle=0xb4000071626e8440, base=0x0, importpid=31466, clone_count=0
I/flutter (31466): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (31466): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(31466): unregister: id=23b00000210, handle=0xb400007053ffd820, base=0x0, importpid=31466, clone_count=0
D/mali_gralloc(31466): unregister: id=23b0000020e, handle=0xb4000071626e8520, base=0x0, importpid=31466, clone_count=0
D/mali_gralloc(31466): unregister: id=23b0000020f, handle=0xb4000071626e8600, base=0x0, importpid=31466, clone_count=0
D/mali_gralloc(31466): unregister: id=23b0000020c, handle=0xb4000071626e8360, base=0x0, importpid=31466, clone_count=0
D/mali_gralloc(31466): unregister: id=23b0000020b, handle=0xb4000071626e7fe0, base=0x0, importpid=31466, clone_count=0
I/ActivityThread(31466): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 8311729
I/ActivityThread(31466): assets removed: [/data/resource-cache/com.android.systemui-neutral-Flma.frro, /data/resource-cache/com.android.systemui-accent-KeQk.frro, /data/resource-cache/com.android.systemui-dynamic-TvKY.frro]
I/ActivityThread(31466): assets added: [/data/resource-cache/com.android.systemui-neutral-gKw0.frro, /data/resource-cache/com.android.systemui-accent-E5lO.frro, /data/resource-cache/com.android.systemui-dynamic-sxzj.frro]
D/JARVIS_SERVICE(31466): Background Service beendet
I/flutter (31466): [Jarvis WebSocket] WebSocket getrennt
I/flutter (31466): [Jarvis WebSocket] WebSocket verbunden
I/flutter (31466): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(31466): Disconnected from TTS engine
W/WindowOnBackDispatcher(31466): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@4c42fc9
I/FlutterActivityAndFragmentDelegate(31466): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter (31466): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(31466): Sucessfully bound to com.google.android.tts
D/FlutterRenderer(31466): Width is zero. 0,0
D/FlutterRenderer(31466): Width is zero. 0,0
D/FlutterJNI(31466): Sending viewport metrics to the engine.
E/mali_gralloc(31466): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(31466): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(31466): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(31466): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(31466): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(31466): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(31466): register: id=23b00000220, handle=0xb40000716ea08a60, importpid=31466
D/mali_gralloc(31466): register: id=23b00000220, handle=0xb40000716ea08b40, importpid=31466
D/mali_gralloc(31466): unregister: id=23b00000220, handle=0xb40000716ea08b40, base=0x0, importpid=31466, clone_count=1
D/mali_gralloc(31466): register: id=23b00000221, handle=0xb40000716ea08b40, importpid=31466
D/mali_gralloc(31466): register: id=23b00000221, handle=0xb40000716ea08c20, importpid=31466
D/mali_gralloc(31466): unregister: id=23b00000221, handle=0xb40000716ea08c20, base=0x0, importpid=31466, clone_count=1
D/mali_gralloc(31466): register: id=23b00000222, handle=0xb40000716ea08c20, importpid=31466
D/mali_gralloc(31466): register: id=23b00000222, handle=0xb40000716ea08d00, importpid=31466
D/mali_gralloc(31466): unregister: id=23b00000222, handle=0xb40000716ea08d00, base=0x0, importpid=31466, clone_count=1
D/mali_gralloc(31466): register: id=23b00000223, handle=0xb40000716ea08d00, importpid=31466
D/mali_gralloc(31466): register: id=23b00000223, handle=0xb40000716ea08de0, importpid=31466
D/mali_gralloc(31466): unregister: id=23b00000223, handle=0xb40000716ea08de0, base=0x0, importpid=31466, clone_count=1
D/mali_gralloc(31466): register: id=23b00000224, handle=0xb40000716ea08de0, importpid=31466
D/mali_gralloc(31466): register: id=23b00000224, handle=0xb40000716ea08ec0, importpid=31466
D/mali_gralloc(31466): unregister: id=23b00000224, handle=0xb40000716ea08ec0, base=0x0, importpid=31466, clone_count=1
W/Choreographer(31466): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_SERVICE(31466): Background Service gestartet
D/JARVIS_SERVICE(31466): Background Service läuft
D/FlutterJNI(31466): Sending viewport metrics to the engine.
I/TextToSpeech(31466): Connected to TTS engine
I/TextToSpeech(31466): Setting up the connection to TTS engine...
W/mple.jarvis_app(31466): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-Flma.frro' with 3 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-KeQk.frro' with 3 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-TvKY.frro' with 3 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(31466): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (31466): [Jarvis WebSocket] WebSocket verbunden
I/Choreographer(31466): Skipped 125 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(31466): register: id=23b00000225, handle=0xb4000071626e5420, importpid=31466
