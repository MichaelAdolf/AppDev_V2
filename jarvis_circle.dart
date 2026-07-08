PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              4,4s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,3s
I/FlutterActivityAndFragmentDelegate(24426): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead orsee https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(24426): Beginning load of flutter...
D/FlutterJNI(24426): flutter (null) was loaded normally!
I/flutter (24426): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(24426): Width is zero. 0,0
Syncing files to device 25028RN03Y...                               76ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:56077/wJarz_5uRyk=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:56077/wJarz_5uRyk=/devtools/?uri=ws://127.0.0.1:56077/wJarz_5uRyk=/ws
I/flutter (24426): [Jarvis WebSocket] WebSocket verbunden
I/mple.jarvis_app(24426): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer(24426): Width is zero. 0,0
I/mple.jarvis_app(24426): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x811a0512a6ccc493
I/UnisocBufferQueueHelper(24426): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400007d1c2da780, size:88
I/mple.jarvis_app(24426): createUnisocBufferQueueHelperFactory success, get instance 0xb400007d1c2da780
I/mple.jarvis_app(24426): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400007d1c32c9c0, size:296, enable:0
I/mple.jarvis_app(24426): createUnisocFrameRecordFactory success, get instance 0xb400007d1c32c9c0
D/FlutterJNI(24426): Sending viewport metrics to the engine.
W/libc    (24426): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(24426): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(24426): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(24426): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(24426): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(24426): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(24426): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(24426): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(24426): register: id=23500000143, handle=0xb400007d1c2b47c0, importpid=24426
W/libc    (24426): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(24426): initIonKernelMemtrack open devices:/dev/systemheap success, fd:206
D/mali_gralloc(24426): register: id=23500000143, handle=0xb400007d1c2b4b40, importpid=24426
D/mali_gralloc(24426): unregister: id=23500000143, handle=0xb400007d1c2b4b40, base=0x0, importpid=24426, clone_count=1
D/mali_gralloc(24426): register: id=23500000144, handle=0xb400007d1c2b4b40, importpid=24426
D/mali_gralloc(24426): register: id=23500000144, handle=0xb400007d1c2b4c20, importpid=24426
D/mali_gralloc(24426): unregister: id=23500000144, handle=0xb400007d1c2b4c20, base=0x0, importpid=24426, clone_count=1
D/mali_gralloc(24426): register: id=23500000145, handle=0xb400007d1c2b4c20, importpid=24426
D/mali_gralloc(24426): register: id=23500000145, handle=0xb400007d1c2b4d00, importpid=24426
D/mali_gralloc(24426): unregister: id=23500000145, handle=0xb400007d1c2b4d00, base=0x0, importpid=24426, clone_count=1
D/mali_gralloc(24426): register: id=23500000146, handle=0xb400007d1c2b4d00, importpid=24426
D/mali_gralloc(24426): register: id=23500000146, handle=0xb400007d1c2b4de0, importpid=24426
D/mali_gralloc(24426): unregister: id=23500000146, handle=0xb400007d1c2b4de0, base=0x0, importpid=24426, clone_count=1
D/mali_gralloc(24426): register: id=23500000147, handle=0xb400007d1c2b4de0, importpid=24426
D/mali_gralloc(24426): register: id=23500000147, handle=0xb400007d1c2b4ec0, importpid=24426
D/mali_gralloc(24426): unregister: id=23500000147, handle=0xb400007d1c2b4ec0, base=0x0, importpid=24426, clone_count=1
W/Choreographer(24426): Already have a pending vsync event.  There should only be one at a time.
I/Choreographer(24426): Skipped 49 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(24426): register: id=23500000148, handle=0xb400007c00f96600, importpid=24426
I/HWUI    (24426): Davey! duration=842ms; Flags=1, FrameTimelineVsyncId=506461, IntendedVsync=4041135011929, Vsync=4041952278715, InputEventId=0, HandleInputStart=4041965558723, AnimationStart=4041965561108, PerformTraversalsStart=4041965562531, DrawStart=4041968432339, FrameDeadline=4041151678596, FrameInterval=4041965185185, FrameStartTime=16678914, SyncQueued=4041969455377, SyncStart=4041969544377, IssueDrawCommandsStart=4041970272800, SwapBuffers=4041975984608, FrameCompleted=4041977240415, DequeueBufferDuration=1337885, QueueBufferDuration=450347, GpuCompleted=4041977240415, SwapBuffersCompleted=4041976562723, DisplayPresentTime=5476377146882523136, CommandSubmissionCompleted=4041975984608, 
D/FlutterJNI(24426): Sending viewport metrics to the engine.
D/ProfileInstaller(24426): Installing profile for com.example.jarvis_app
W/mple.jarvis_app(24426): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~PmnXcHJIvMGWHL15ZMX_Ww==/com.google.android.tts-fhuGD7-7ZGCXm593dpS1yw==/base.apk' with 1 weak references
W/mple.jarvis_app(24426): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~PmnXcHJIvMGWHL15ZMX_Ww==/com.google.android.tts-fhuGD7-7ZGCXm593dpS1yw==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(24426): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~PmnXcHJIvMGWHL15ZMX_Ww==/com.google.android.tts-fhuGD7-7ZGCXm593dpS1yw==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(24426): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~PmnXcHJIvMGWHL15ZMX_Ww==/com.google.android.tts-fhuGD7-7ZGCXm593dpS1yw==/split_config.xhdpi.apk' with 1 weak references
