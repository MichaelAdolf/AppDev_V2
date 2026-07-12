PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             22,6s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,9s
I/FlutterActivityAndFragmentDelegate(12097): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(12097): Beginning load of flutter...
D/FlutterJNI(12097): flutter (null) was loaded normally!
I/flutter (12097): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(12097): Width is zero. 0,0
I/flutter (12097): [Jarvis WebSocket] WebSocket verbunden
Syncing files to device 25028RN03Y...                              229ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:52309/uEy8VduDmqw=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:52309/uEy8VduDmqw=/devtools/?uri=ws://127.0.0.1:52309/uEy8VduDmqw=/ws
I/TextToSpeech(12097): Connected to TTS engine
D/FlutterRenderer(12097): Width is zero. 0,0
I/mple.jarvis_app(12097): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x1b7b16f492b0a5c7
I/UnisocBufferQueueHelper(12097): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb40000716ec461a0, size:88
I/mple.jarvis_app(12097): createUnisocBufferQueueHelperFactory success, get instance 0xb40000716ec461a0
I/mple.jarvis_app(12097): Unisoc-Graphics: UnisocFrameRecord create, this:0xb40000716ec39ec0, size:296, enable:0
I/mple.jarvis_app(12097): createUnisocFrameRecordFactory success, get instance 0xb40000716ec39ec0
D/FlutterJNI(12097): Sending viewport metrics to the engine.
I/mple.jarvis_app(12097): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
W/libc    (12097): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(12097): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(12097): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12097): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(12097): register: id=23b000002d8, handle=0xb40000716ebfa4e0, importpid=12097
W/libc    (12097): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(12097): initIonKernelMemtrack open devices:/dev/systemheap success, fd:207
D/mali_gralloc(12097): register: id=23b000002d8, handle=0xb40000716ebfa860, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002d8, handle=0xb40000716ebfa860, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002d9, handle=0xb40000716ebfa860, importpid=12097
D/mali_gralloc(12097): register: id=23b000002d9, handle=0xb40000716ebfa940, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002d9, handle=0xb40000716ebfa940, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002da, handle=0xb40000716ebfa940, importpid=12097
D/mali_gralloc(12097): register: id=23b000002da, handle=0xb40000716ebfaa20, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002da, handle=0xb40000716ebfaa20, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002db, handle=0xb40000716ebfaa20, importpid=12097
D/mali_gralloc(12097): register: id=23b000002db, handle=0xb40000716ebfab00, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002db, handle=0xb40000716ebfab00, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002dc, handle=0xb40000716ebfab00, importpid=12097
D/mali_gralloc(12097): register: id=23b000002dc, handle=0xb40000716ebfabe0, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002dc, handle=0xb40000716ebfabe0, base=0x0, importpid=12097, clone_count=1
W/Choreographer(12097): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(12097): Setting up the connection to TTS engine...
D/JARVIS_BRIDGE(12097): EVENT wird ausgelöst
D/JARVIS_BRIDGE(12097): currentInstance = true
D/JARVIS_BRIDGE(12097): Sende Event an Flutter
I/flutter (12097): [JARVIS BRIDGE] backgroundEvent
I/flutter (12097): [JARVIS BRIDGE] Hallo aus Android Service
I/flutter (12097): [JARVIS BACKGROUND] Hallo aus Android Service
I/Choreographer(12097): Skipped 47 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(12097): register: id=23b000002dd, handle=0xb40000710e557dc0, importpid=12097
I/HWUI    (12097): Davey! duration=804ms; Flags=1, FrameTimelineVsyncId=732129, IntendedVsync=16386053248001, Vsync=16386836581350, InputEventId=0, HandleInputStart=16386839229509, AnimationStart=16386839233624, PerformTraversalsStart=16386839235009, DrawStart=16386843950162, FrameDeadline=16386069914668, FrameInterval=16386838270239, FrameStartTime=16666667, SyncQueued=16386846350970, SyncStart=16386846634470, IssueDrawCommandsStart=16386847835316, SwapBuffers=16386857068201, FrameCompleted=16386858172316, DequeueBufferDuration=1858231, QueueBufferDuration=841538, GpuCompleted=16386858172316, SwapBuffersCompleted=16386858117201, DisplayPresentTime=0, CommandSubmissionCompleted=16386857068201, 
D/FlutterJNI(12097): Sending viewport metrics to the engine.
D/ProfileInstaller(12097): Installing profile for com.example.jarvis_app
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (12097): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](12097): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(12097): unregister: id=23b000002dc, handle=0xb40000716ebfab00, base=0x0, importpid=12097, clone_count=0
I/flutter (12097): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (12097): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(12097): unregister: id=23b000002dd, handle=0xb40000710e557dc0, base=0x0, importpid=12097, clone_count=0
D/mali_gralloc(12097): unregister: id=23b000002d8, handle=0xb40000716ebfa4e0, base=0x0, importpid=12097, clone_count=0
D/mali_gralloc(12097): unregister: id=23b000002d9, handle=0xb40000716ebfa860, base=0x0, importpid=12097, clone_count=0
D/mali_gralloc(12097): unregister: id=23b000002db, handle=0xb40000716ebfaa20, base=0x0, importpid=12097, clone_count=0
D/mali_gralloc(12097): unregister: id=23b000002da, handle=0xb40000716ebfa940, base=0x0, importpid=12097, clone_count=0
I/ActivityThread(12097): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 16401563
I/ActivityThread(12097): assets removed: [/data/resource-cache/com.android.systemui-neutral-AhlV.frro, /data/resource-cache/com.android.systemui-accent-3Y5J.frro, /data/resource-cache/com.android.systemui-dynamic-ga02.frro]
I/ActivityThread(12097): assets added: [/data/resource-cache/com.android.systemui-neutral-HFuE.frro, /data/resource-cache/com.android.systemui-accent-fZdP.frro, /data/resource-cache/com.android.systemui-dynamic-kVEr.frro]
I/flutter (12097): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(12097): Disconnected from TTS engine
W/WindowOnBackDispatcher(12097): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@c8dc6ce
I/FlutterActivityAndFragmentDelegate(12097): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter (12097): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(12097): Sucessfully bound to com.google.android.tts
D/JARVIS_BRIDGE(12097): MethodChannel erstellt
D/FlutterRenderer(12097): Width is zero. 0,0
I/flutter (12097): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech(12097): Connected to TTS engine
D/FlutterRenderer(12097): Width is zero. 0,0
D/FlutterJNI(12097): Sending viewport metrics to the engine.
E/mali_gralloc(12097): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12097): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12097): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(12097): register: id=23b000002ed, handle=0xb40000716ebfa240, importpid=12097
D/mali_gralloc(12097): register: id=23b000002ed, handle=0xb40000716ebfa4e0, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002ed, handle=0xb40000716ebfa4e0, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002ee, handle=0xb40000716ebfa4e0, importpid=12097
D/mali_gralloc(12097): register: id=23b000002ee, handle=0xb40000716ebfa860, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002ee, handle=0xb40000716ebfa860, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002ef, handle=0xb40000716ebfa860, importpid=12097
D/mali_gralloc(12097): register: id=23b000002ef, handle=0xb40000716ebfa940, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002ef, handle=0xb40000716ebfa940, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002f0, handle=0xb40000716ebfa940, importpid=12097
D/mali_gralloc(12097): register: id=23b000002f0, handle=0xb40000716ebfaa20, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002f0, handle=0xb40000716ebfaa20, base=0x0, importpid=12097, clone_count=1
D/mali_gralloc(12097): register: id=23b000002f1, handle=0xb40000716ebfaa20, importpid=12097
D/mali_gralloc(12097): register: id=23b000002f1, handle=0xb40000716ebfab00, importpid=12097
D/mali_gralloc(12097): unregister: id=23b000002f1, handle=0xb40000716ebfab00, base=0x0, importpid=12097, clone_count=1
W/Choreographer(12097): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_BRIDGE(12097): EVENT wird ausgelöst
D/JARVIS_BRIDGE(12097): currentInstance = true
D/JARVIS_BRIDGE(12097): Sende Event an Flutter
I/flutter (12097): [JARVIS BRIDGE] backgroundEvent
I/flutter (12097): [JARVIS BRIDGE] Hallo aus Android Service
I/flutter (12097): [JARVIS BACKGROUND] Hallo aus Android Service
D/mali_gralloc(12097): register: id=23b000002f2, handle=0xb40000704be2bd80, importpid=12097
I/TextToSpeech(12097): Setting up the connection to TTS engine...
W/mple.jarvis_app(12097): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-AhlV.frro' with 3 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-3Y5J.frro' with 3 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-ga02.frro' with 3 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(12097): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/FlutterJNI(12097): Sending viewport metrics to the engine.
