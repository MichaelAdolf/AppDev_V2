PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             45,0s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,2s
I/FlutterActivityAndFragmentDelegate( 1777): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 1777): Beginning load of flutter...
D/FlutterJNI( 1777): flutter (null) was loaded normally!
I/flutter ( 1777): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 1777): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              205ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:52976/ftJ4dN4Ghsw=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:52976/ftJ4dN4Ghsw=/devtools/?uri=ws://127.0.0.1:52976/ftJ4dN4Ghsw=/ws
I/flutter ( 1777): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech( 1777): Connected to TTS engine
I/mple.jarvis_app( 1777): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/TextToSpeech( 1777): Setting up the connection to TTS engine...
D/FlutterRenderer( 1777): Width is zero. 0,0
I/mple.jarvis_app( 1777): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xbe2b700ffdb6313
I/UnisocBufferQueueHelper( 1777): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb40000719b940540, size:88
I/mple.jarvis_app( 1777): createUnisocBufferQueueHelperFactory success, get instance 0xb40000719b940540
I/mple.jarvis_app( 1777): Unisoc-Graphics: UnisocFrameRecord create, this:0xb40000710e2b1b40, size:296, enable:0
I/mple.jarvis_app( 1777): createUnisocFrameRecordFactory success, get instance 0xb40000710e2b1b40
D/FlutterJNI( 1777): Sending viewport metrics to the engine.
W/libc    ( 1777): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 1777): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 1777): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1777): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 1777): register: id=23b00000239, handle=0xb40000716ec49160, importpid=1777
W/libc    ( 1777): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 1777): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 1777): register: id=23b00000239, handle=0xb40000716ec494e0, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b00000239, handle=0xb40000716ec494e0, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b0000023a, handle=0xb40000716ec494e0, importpid=1777
D/mali_gralloc( 1777): register: id=23b0000023a, handle=0xb40000716ec495c0, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b0000023a, handle=0xb40000716ec495c0, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b0000023b, handle=0xb40000716ec495c0, importpid=1777
D/mali_gralloc( 1777): register: id=23b0000023b, handle=0xb40000716ec496a0, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b0000023b, handle=0xb40000716ec496a0, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b0000023c, handle=0xb40000716ec496a0, importpid=1777
D/mali_gralloc( 1777): register: id=23b0000023c, handle=0xb40000716ec49780, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b0000023c, handle=0xb40000716ec49780, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b0000023d, handle=0xb40000716ec49780, importpid=1777
D/mali_gralloc( 1777): register: id=23b0000023d, handle=0xb40000716ec49860, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b0000023d, handle=0xb40000716ec49860, base=0x0, importpid=1777, clone_count=1
W/Choreographer( 1777): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_SERVICE( 1777): Background Service gestartet
D/JARVIS_SERVICE( 1777): Background Service läuft
I/Choreographer( 1777): Skipped 49 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 1777): register: id=23b0000023e, handle=0xb40000704d51b700, importpid=1777
I/HWUI    ( 1777): Davey! duration=844ms; Flags=1, FrameTimelineVsyncId=452105, IntendedVsync=9082235848103, Vsync=9083052710296, InputEventId=0, HandleInputStart=9083058344233, AnimationStart=9083058347848, PerformTraversalsStart=9083058349348, DrawStart=9083062268310, FrameDeadline=9082252514770, FrameInterval=9083057750733, FrameStartTime=16670657, SyncQueued=9083063552617, SyncStart=9083063647656, IssueDrawCommandsStart=9083065073579, SwapBuffers=9083079032463, FrameCompleted=9083080418463, DequeueBufferDuration=4126962, QueueBufferDuration=960346, GpuCompleted=9083080418463, SwapBuffersCompleted=9083080257540, DisplayPresentTime=8247607618565254764, CommandSubmissionCompleted=9083079032463, 
D/FlutterJNI( 1777): Sending viewport metrics to the engine.
D/ProfileInstaller( 1777): Installing profile for com.example.jarvis_app
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter ( 1777): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity]( 1777): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc( 1777): unregister: id=23b0000023b, handle=0xb40000716ec495c0, base=0x0, importpid=1777, clone_count=0
I/flutter ( 1777): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter ( 1777): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc( 1777): unregister: id=23b0000023e, handle=0xb40000704d51b700, base=0x0, importpid=1777, clone_count=0
D/mali_gralloc( 1777): unregister: id=23b0000023c, handle=0xb40000716ec496a0, base=0x0, importpid=1777, clone_count=0
D/mali_gralloc( 1777): unregister: id=23b0000023d, handle=0xb40000716ec49780, base=0x0, importpid=1777, clone_count=0
D/mali_gralloc( 1777): unregister: id=23b0000023a, handle=0xb40000716ec494e0, base=0x0, importpid=1777, clone_count=0
D/mali_gralloc( 1777): unregister: id=23b00000239, handle=0xb40000716ec49160, base=0x0, importpid=1777, clone_count=0
I/ActivityThread( 1777): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 9094422
I/ActivityThread( 1777): assets removed: [/data/resource-cache/com.android.systemui-neutral-PhzG.frro, /data/resource-cache/com.android.systemui-accent-0dG1.frro, /data/resource-cache/com.android.systemui-dynamic-QjHj.frro]
I/ActivityThread( 1777): assets added: [/data/resource-cache/com.android.systemui-neutral-bC8H.frro, /data/resource-cache/com.android.systemui-accent-8dMl.frro, /data/resource-cache/com.android.systemui-dynamic-q9Sh.frro]
I/flutter ( 1777): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech( 1777): Disconnected from TTS engine
W/WindowOnBackDispatcher( 1777): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@df68cfc
I/FlutterActivityAndFragmentDelegate( 1777): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter ( 1777): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech( 1777): Sucessfully bound to com.google.android.tts
D/FlutterRenderer( 1777): Width is zero. 0,0
I/flutter ( 1777): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech( 1777): Connected to TTS engine
D/FlutterRenderer( 1777): Width is zero. 0,0
D/FlutterJNI( 1777): Sending viewport metrics to the engine.
E/mali_gralloc( 1777): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1777): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 1777): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 1777): register: id=23b0000024e, handle=0xb40000716ec49780, importpid=1777
D/mali_gralloc( 1777): register: id=23b0000024e, handle=0xb40000716ec49860, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b0000024e, handle=0xb40000716ec49860, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b0000024f, handle=0xb40000716ec49860, importpid=1777
D/mali_gralloc( 1777): register: id=23b0000024f, handle=0xb40000716ec49940, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b0000024f, handle=0xb40000716ec49940, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b00000250, handle=0xb40000716ec49940, importpid=1777
D/mali_gralloc( 1777): register: id=23b00000250, handle=0xb40000716ec49a20, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b00000250, handle=0xb40000716ec49a20, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b00000251, handle=0xb40000716ec49a20, importpid=1777
D/mali_gralloc( 1777): register: id=23b00000251, handle=0xb40000716ec49b00, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b00000251, handle=0xb40000716ec49b00, base=0x0, importpid=1777, clone_count=1
D/mali_gralloc( 1777): register: id=23b00000252, handle=0xb40000716ec49b00, importpid=1777
D/mali_gralloc( 1777): register: id=23b00000252, handle=0xb40000716ec49be0, importpid=1777
D/mali_gralloc( 1777): unregister: id=23b00000252, handle=0xb40000716ec49be0, base=0x0, importpid=1777, clone_count=1
W/Choreographer( 1777): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 1777): Setting up the connection to TTS engine...
D/JARVIS_SERVICE( 1777): Background Service läuft
D/mali_gralloc( 1777): register: id=23b00000253, handle=0xb40000704d520320, importpid=1777
W/mple.jarvis_app( 1777): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-PhzG.frro' with 3 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-0dG1.frro' with 3 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-QjHj.frro' with 3 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 1777): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/FlutterJNI( 1777): Sending viewport metrics to the engine.
