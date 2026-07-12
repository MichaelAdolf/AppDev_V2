PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             73,9s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,8s
I/FlutterActivityAndFragmentDelegate(29330): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(29330): Beginning load of flutter...
D/FlutterJNI(29330): flutter (null) was loaded normally!
I/flutter (29330): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(29330): Width is zero. 0,0
D/FlutterRenderer(29330): Width is zero. 0,0
D/FlutterJNI(29330): Sending viewport metrics to the engine.
Syncing files to device 25028RN03Y...                              129ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:51209/lzXt28SR9Sk=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:51209/lzXt28SR9Sk=/devtools/?uri=ws://127.0.0.1:51209/lzXt28SR9Sk=/ws
W/DisplayEventDispatcher(29330): Vsync time out! vsyncScheduleDelay=930ms
W/Choreographer(29330): Already have a pending vsync event.  There should only be one at a time.
W/Choreographer(29330): Already have a pending vsync event.  There should only be one at a time.
I/Choreographer(29330): Skipped 58 frames!  The application may be doing too much work on its main thread.
D/FlutterJNI(29330): Sending viewport metrics to the engine.
D/ProfileInstaller(29330): Installing profile for com.example.jarvis_app
I/TextToSpeech(29330): Connected to TTS engine
I/TextToSpeech(29330): Setting up the connection to TTS engine...
I/flutter (29330): [Jarvis WebSocket] WebSocket verbunden
I/mple.jarvis_app(29330): Background concurrent mark compact GC freed 7979KB AllocSpace bytes, 13(580KB) LOS objects, 49% free, 2663KB/5327KB, paused 529us,5.441ms total 48.519ms
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/Choreographer(29330): Skipped 155 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(29330): register: id=23b000001dc, handle=0xb400007167a01ac0, importpid=29330
I/HWUI    (29330): Davey! duration=2652ms; Flags=1, FrameTimelineVsyncId=240114, IntendedVsync=7015541886677, Vsync=7018126221827, InputEventId=0, HandleInputStart=7018143492556, AnimationStart=7018143495171, PerformTraversalsStart=7018143496671, DrawStart=7018147953364, FrameDeadline=7015558553344, FrameInterval=7018142601364, FrameStartTime=16673130, SyncQueued=7018150252556, SyncStart=7018150346210, IssueDrawCommandsStart=7018151364479, SwapBuffers=7018193064594, FrameCompleted=7018194579902, DequeueBufferDuration=4600039, QueueBufferDuration=563654, GpuCompleted=7018194579902, SwapBuffersCompleted=7018193769440, DisplayPresentTime=-6196104287201262623, CommandSubmissionCompleted=7018193064594, 
I/flutter (29330): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter (29330): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (29330): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](29330): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(29330): unregister: id=23b000001da, handle=0xb40000716eb1a280, base=0x0, importpid=29330, clone_count=0
I/flutter (29330): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (29330): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(29330): unregister: id=23b000001dc, handle=0xb400007167a01ac0, base=0x0, importpid=29330, clone_count=0
D/mali_gralloc(29330): unregister: id=23b000001db, handle=0xb40000716eb1a360, base=0x0, importpid=29330, clone_count=0
D/mali_gralloc(29330): unregister: id=23b000001d7, handle=0xb40000716eb19d40, base=0x0, importpid=29330, clone_count=0
D/mali_gralloc(29330): unregister: id=23b000001d9, handle=0xb40000716eb1a1a0, base=0x0, importpid=29330, clone_count=0
D/mali_gralloc(29330): unregister: id=23b000001d8, handle=0xb40000716eb1a0c0, base=0x0, importpid=29330, clone_count=0
I/ActivityThread(29330): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 7050232
I/ActivityThread(29330): assets removed: [/data/resource-cache/com.android.systemui-neutral-RYyD.frro, /data/resource-cache/com.android.systemui-accent-RPNR.frro, /data/resource-cache/com.android.systemui-dynamic-gJHf.frro]
I/ActivityThread(29330): assets added: [/data/resource-cache/com.android.systemui-neutral-Flma.frro, /data/resource-cache/com.android.systemui-accent-KeQk.frro, /data/resource-cache/com.android.systemui-dynamic-TvKY.frro]
I/flutter (29330): [Jarvis WebSocket] WebSocket getrennt
I/flutter (29330): [Jarvis WebSocket] WebSocket verbunden
I/flutter (29330): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(29330): Disconnected from TTS engine
W/WindowOnBackDispatcher(29330): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@4c42fc9
I/FlutterActivityAndFragmentDelegate(29330): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter (29330): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(29330): Sucessfully bound to com.google.android.tts
D/FlutterRenderer(29330): Width is zero. 0,0
D/FlutterRenderer(29330): Width is zero. 0,0
D/FlutterJNI(29330): Sending viewport metrics to the engine.
E/mali_gralloc(29330): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(29330): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29330): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29330): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(29330): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(29330): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(29330): register: id=23b000001f1, handle=0xb40000716eb1a440, importpid=29330
D/mali_gralloc(29330): register: id=23b000001f1, handle=0xb40000716eb1a520, importpid=29330
D/mali_gralloc(29330): unregister: id=23b000001f1, handle=0xb40000716eb1a520, base=0x0, importpid=29330, clone_count=1
D/mali_gralloc(29330): register: id=23b000001f2, handle=0xb40000716eb1a520, importpid=29330
D/mali_gralloc(29330): register: id=23b000001f2, handle=0xb40000716eb1a600, importpid=29330
D/mali_gralloc(29330): unregister: id=23b000001f2, handle=0xb40000716eb1a600, base=0x0, importpid=29330, clone_count=1
D/mali_gralloc(29330): register: id=23b000001f3, handle=0xb40000716eb1a600, importpid=29330
D/mali_gralloc(29330): register: id=23b000001f3, handle=0xb40000716eb1a6e0, importpid=29330
D/mali_gralloc(29330): unregister: id=23b000001f3, handle=0xb40000716eb1a6e0, base=0x0, importpid=29330, clone_count=1
D/mali_gralloc(29330): register: id=23b000001f4, handle=0xb40000716eb1a6e0, importpid=29330
D/mali_gralloc(29330): register: id=23b000001f4, handle=0xb40000716eb1a7c0, importpid=29330
D/mali_gralloc(29330): unregister: id=23b000001f4, handle=0xb40000716eb1a7c0, base=0x0, importpid=29330, clone_count=1
D/mali_gralloc(29330): register: id=23b000001f5, handle=0xb40000716eb1a7c0, importpid=29330
D/mali_gralloc(29330): register: id=23b000001f5, handle=0xb40000716eb1a8a0, importpid=29330
D/mali_gralloc(29330): unregister: id=23b000001f5, handle=0xb40000716eb1a8a0, base=0x0, importpid=29330, clone_count=1
W/Choreographer(29330): Already have a pending vsync event.  There should only be one at a time.
D/FlutterJNI(29330): Sending viewport metrics to the engine.
I/TextToSpeech(29330): Connected to TTS engine
I/TextToSpeech(29330): Setting up the connection to TTS engine...
W/mple.jarvis_app(29330): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-RYyD.frro' with 3 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-RPNR.frro' with 3 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-gJHf.frro' with 3 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(29330): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (29330): [Jarvis WebSocket] WebSocket verbunden
I/Choreographer(29330): Skipped 126 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(29330): register: id=23b000001f6, handle=0xb40000704ca2d5c0, importpid=29330
I/mple.jarvis_app(29330): NativeAlloc concurrent mark compact GC freed 917KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 2830KB/5661KB, paused 199us,6.530ms total 37.101ms
