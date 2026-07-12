PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             60,3s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,5s
I/FlutterActivityAndFragmentDelegate( 9499): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 9499): Beginning load of flutter...
D/FlutterJNI( 9499): flutter (null) was loaded normally!
I/flutter ( 9499): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 9499): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              208ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:62857/mAErV0ISGY4=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:62857/mAErV0ISGY4=/devtools/?uri=ws://127.0.0.1:62857/mAErV0ISGY4=/ws
I/flutter ( 9499): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech( 9499): Connected to TTS engine
I/mple.jarvis_app( 9499): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer( 9499): Width is zero. 0,0
I/mple.jarvis_app( 9499): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x53fb673e58dce4b
I/UnisocBufferQueueHelper( 9499): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb40000719b940540, size:88
I/mple.jarvis_app( 9499): createUnisocBufferQueueHelperFactory success, get instance 0xb40000719b940540
I/mple.jarvis_app( 9499): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400007050f5dc80, size:296, enable:0
I/mple.jarvis_app( 9499): createUnisocFrameRecordFactory success, get instance 0xb400007050f5dc80
D/FlutterJNI( 9499): Sending viewport metrics to the engine.
W/libc    ( 9499): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 9499): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 9499): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9499): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 9499): register: id=23b000002aa, handle=0xb40000710c0e55c0, importpid=9499
W/libc    ( 9499): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 9499): initIonKernelMemtrack open devices:/dev/systemheap success, fd:207
D/mali_gralloc( 9499): register: id=23b000002aa, handle=0xb40000710c0e5940, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002aa, handle=0xb40000710c0e5940, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002ab, handle=0xb40000710c0e5940, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002ab, handle=0xb40000710c0e5a20, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002ab, handle=0xb40000710c0e5a20, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002ac, handle=0xb40000710c0e5a20, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002ac, handle=0xb40000710c0e5b00, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002ac, handle=0xb40000710c0e5b00, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002ad, handle=0xb40000710c0e5b00, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002ad, handle=0xb40000710c0e5be0, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002ad, handle=0xb40000710c0e5be0, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002ae, handle=0xb40000710c0e5be0, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002ae, handle=0xb40000710c0e5cc0, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002ae, handle=0xb40000710c0e5cc0, base=0x0, importpid=9499, clone_count=1
W/DisplayEventDispatcher( 9499): Vsync time out! vsyncScheduleDelay=358ms
W/Choreographer( 9499): Already have a pending vsync event.  There should only be one at a time.
W/Choreographer( 9499): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_SERVICE( 9499): Background Service gestartet
I/TextToSpeech( 9499): Setting up the connection to TTS engine...
D/JARVIS_SERVICE( 9499): Background Service läuft
I/Choreographer( 9499): Skipped 55 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 9499): register: id=23b000002af, handle=0xb40000710beb0620, importpid=9499
D/ProfileInstaller( 9499): Installing profile for com.example.jarvis_app
D/FlutterJNI( 9499): Sending viewport metrics to the engine.
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter ( 9499): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/mali_gralloc( 9499): unregister: id=23b000002ab, handle=0xb40000710c0e5940, base=0x0, importpid=9499, clone_count=0
I/flutter ( 9499): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter ( 9499): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc( 9499): unregister: id=23b000002af, handle=0xb40000710beb0620, base=0x0, importpid=9499, clone_count=0
D/mali_gralloc( 9499): unregister: id=23b000002ac, handle=0xb40000710c0e5a20, base=0x0, importpid=9499, clone_count=0
D/mali_gralloc( 9499): unregister: id=23b000002ad, handle=0xb40000710c0e5b00, base=0x0, importpid=9499, clone_count=0
D/mali_gralloc( 9499): unregister: id=23b000002aa, handle=0xb40000710c0e55c0, base=0x0, importpid=9499, clone_count=0
D/mali_gralloc( 9499): unregister: id=23b000002ae, handle=0xb40000710c0e5be0, base=0x0, importpid=9499, clone_count=0
I/ActivityThread( 9499): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 15247508
I/ActivityThread( 9499): assets removed: [/data/resource-cache/com.android.systemui-neutral-aKi5.frro, /data/resource-cache/com.android.systemui-accent-7aqv.frro, /data/resource-cache/com.android.systemui-dynamic-qEkc.frro]
I/ActivityThread( 9499): assets added: [/data/resource-cache/com.android.systemui-neutral-Jk7k.frro, /data/resource-cache/com.android.systemui-accent-EIpw.frro, /data/resource-cache/com.android.systemui-dynamic-OKgN.frro]
I/flutter ( 9499): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech( 9499): Disconnected from TTS engine
W/WindowOnBackDispatcher( 9499): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@df68cfc
I/FlutterActivityAndFragmentDelegate( 9499): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter ( 9499): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech( 9499): Sucessfully bound to com.google.android.tts
D/FlutterRenderer( 9499): Width is zero. 0,0
W/CheckTime( 9499): App running slow: Executing activity onCreate took 897ms
I/flutter ( 9499): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech( 9499): Connected to TTS engine
D/FlutterRenderer( 9499): Width is zero. 0,0
D/FlutterJNI( 9499): Sending viewport metrics to the engine.
E/mali_gralloc( 9499): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9499): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9499): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 9499): register: id=23b000002bf, handle=0xb40000710c0e55c0, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002bf, handle=0xb40000710c0e5940, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002bf, handle=0xb40000710c0e5940, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002c0, handle=0xb40000710c0e5940, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002c0, handle=0xb40000710c0e5a20, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002c0, handle=0xb40000710c0e5a20, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002c1, handle=0xb40000710c0e5a20, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002c1, handle=0xb40000710c0e5b00, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002c1, handle=0xb40000710c0e5b00, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002c2, handle=0xb40000710c0e5b00, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002c2, handle=0xb40000710c0e5be0, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002c2, handle=0xb40000710c0e5be0, base=0x0, importpid=9499, clone_count=1
D/mali_gralloc( 9499): register: id=23b000002c3, handle=0xb40000710c0e5be0, importpid=9499
D/mali_gralloc( 9499): register: id=23b000002c3, handle=0xb40000710c0e5cc0, importpid=9499
D/mali_gralloc( 9499): unregister: id=23b000002c3, handle=0xb40000710c0e5cc0, base=0x0, importpid=9499, clone_count=1
I/TextToSpeech( 9499): Setting up the connection to TTS engine...
W/Choreographer( 9499): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_SERVICE( 9499): Background Service läuft
D/mali_gralloc( 9499): register: id=23b000002c4, handle=0xb40000705144e940, importpid=9499
W/mple.jarvis_app( 9499): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-aKi5.frro' with 3 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-7aqv.frro' with 3 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-qEkc.frro' with 3 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 9499): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/FlutterJNI( 9499): Sending viewport metrics to the engine.PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             22,5s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,7s
I/FlutterActivityAndFragmentDelegate( 4223): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 4223): Beginning load of flutter...
D/FlutterJNI( 4223): flutter (null) was loaded normally!
I/flutter ( 4223): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 4223): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              196ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:62471/UCIhuHPjwvQ=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:62471/UCIhuHPjwvQ=/devtools/?uri=ws://127.0.0.1:62471/UCIhuHPjwvQ=/ws
I/flutter ( 4223): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech( 4223): Connected to TTS engine
D/FlutterRenderer( 4223): Width is zero. 0,0
I/mple.jarvis_app( 4223): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xdf0b1fe1b9d558fd
I/UnisocBufferQueueHelper( 4223): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb40000719b941620, size:88
I/mple.jarvis_app( 4223): createUnisocBufferQueueHelperFactory success, get instance 0xb40000719b941620
I/mple.jarvis_app( 4223): Unisoc-Graphics: UnisocFrameRecord create, this:0xb40000710e642c80, size:296, enable:0
I/mple.jarvis_app( 4223): createUnisocFrameRecordFactory success, get instance 0xb40000710e642c80
D/FlutterJNI( 4223): Sending viewport metrics to the engine.
I/mple.jarvis_app( 4223): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
W/libc    ( 4223): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 4223): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 4223): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4223): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 4223): register: id=23b00000264, handle=0xb40000716270d860, importpid=4223
W/libc    ( 4223): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 4223): initIonKernelMemtrack open devices:/dev/systemheap success, fd:207
I/TextToSpeech( 4223): Setting up the connection to TTS engine...
D/mali_gralloc( 4223): register: id=23b00000264, handle=0xb40000716270dbe0, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000264, handle=0xb40000716270dbe0, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b00000265, handle=0xb40000716270dbe0, importpid=4223
D/mali_gralloc( 4223): register: id=23b00000265, handle=0xb40000716270dcc0, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000265, handle=0xb40000716270dcc0, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b00000266, handle=0xb40000716270dcc0, importpid=4223
D/mali_gralloc( 4223): register: id=23b00000266, handle=0xb40000716270dda0, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000266, handle=0xb40000716270dda0, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b00000267, handle=0xb40000716270dda0, importpid=4223
D/mali_gralloc( 4223): register: id=23b00000267, handle=0xb40000716270de80, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000267, handle=0xb40000716270de80, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b00000268, handle=0xb40000716270de80, importpid=4223
D/mali_gralloc( 4223): register: id=23b00000268, handle=0xb40000716270df60, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000268, handle=0xb40000716270df60, base=0x0, importpid=4223, clone_count=1
W/Choreographer( 4223): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_SERVICE( 4223): Background Service gestartet
D/JARVIS_SERVICE( 4223): Background Service läuft
I/Choreographer( 4223): Skipped 44 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 4223): register: id=23b00000269, handle=0xb40000710e6d9080, importpid=4223
I/HWUI    ( 4223): Davey! duration=765ms; Flags=1, FrameTimelineVsyncId=482866, IntendedVsync=10258661885001, Vsync=10259395218349, InputEventId=0, HandleInputStart=10259410323507, AnimationStart=10259410327122, PerformTraversalsStart=10259410328699, DrawStart=10259414765007, FrameDeadline=10258678551668, FrameInterval=10259409874699, FrameStartTime=16666667, SyncQueued=10259416836737, SyncStart=10259417111045, IssueDrawCommandsStart=10259418115084, SwapBuffers=10259426067084, FrameCompleted=10259427659161, DequeueBufferDuration=2555885, QueueBufferDuration=1338115, GpuCompleted=10259427030007, SwapBuffersCompleted=10259427659161, DisplayPresentTime=365176205361, CommandSubmissionCompleted=10259426067084, 
D/ProfileInstaller( 4223): Installing profile for com.example.jarvis_app
D/FlutterJNI( 4223): Sending viewport metrics to the engine.
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter ( 4223): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity]( 4223): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc( 4223): unregister: id=23b00000267, handle=0xb40000716270dda0, base=0x0, importpid=4223, clone_count=0
I/flutter ( 4223): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter ( 4223): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc( 4223): unregister: id=23b00000269, handle=0xb40000710e6d9080, base=0x0, importpid=4223, clone_count=0
D/mali_gralloc( 4223): unregister: id=23b00000268, handle=0xb40000716270de80, base=0x0, importpid=4223, clone_count=0
D/mali_gralloc( 4223): unregister: id=23b00000264, handle=0xb40000716270d860, base=0x0, importpid=4223, clone_count=0
D/mali_gralloc( 4223): unregister: id=23b00000266, handle=0xb40000716270dcc0, base=0x0, importpid=4223, clone_count=0
D/mali_gralloc( 4223): unregister: id=23b00000265, handle=0xb40000716270dbe0, base=0x0, importpid=4223, clone_count=0
I/ActivityThread( 4223): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 10288323
I/ActivityThread( 4223): assets removed: [/data/resource-cache/com.android.systemui-neutral-bC8H.frro, /data/resource-cache/com.android.systemui-accent-8dMl.frro, /data/resource-cache/com.android.systemui-dynamic-q9Sh.frro]
I/ActivityThread( 4223): assets added: [/data/resource-cache/com.android.systemui-neutral-G6wi.frro, /data/resource-cache/com.android.systemui-accent-o0Ls.frro, /data/resource-cache/com.android.systemui-dynamic-u6oH.frro]
I/flutter ( 4223): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech( 4223): Disconnected from TTS engine
W/WindowOnBackDispatcher( 4223): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@df68cfc
I/FlutterActivityAndFragmentDelegate( 4223): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter ( 4223): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech( 4223): Sucessfully bound to com.google.android.tts
D/FlutterRenderer( 4223): Width is zero. 0,0
I/flutter ( 4223): [Jarvis WebSocket] WebSocket verbunden
I/TextToSpeech( 4223): Connected to TTS engine
D/FlutterRenderer( 4223): Width is zero. 0,0
D/FlutterJNI( 4223): Sending viewport metrics to the engine.
E/mali_gralloc( 4223): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4223): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4223): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 4223): register: id=23b00000278, handle=0xb40000716eba9f60, importpid=4223
D/mali_gralloc( 4223): register: id=23b00000278, handle=0xb40000716ebaa040, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000278, handle=0xb40000716ebaa040, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b00000279, handle=0xb40000716ebaa040, importpid=4223
D/mali_gralloc( 4223): register: id=23b00000279, handle=0xb40000716ebaa120, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b00000279, handle=0xb40000716ebaa120, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b0000027a, handle=0xb40000716ebaa120, importpid=4223
D/mali_gralloc( 4223): register: id=23b0000027a, handle=0xb40000716ebaa200, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b0000027a, handle=0xb40000716ebaa200, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b0000027b, handle=0xb40000716ebaa200, importpid=4223
D/mali_gralloc( 4223): register: id=23b0000027b, handle=0xb40000716ebaa2e0, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b0000027b, handle=0xb40000716ebaa2e0, base=0x0, importpid=4223, clone_count=1
D/mali_gralloc( 4223): register: id=23b0000027c, handle=0xb40000716ebaa2e0, importpid=4223
D/mali_gralloc( 4223): register: id=23b0000027c, handle=0xb40000716ebaa3c0, importpid=4223
D/mali_gralloc( 4223): unregister: id=23b0000027c, handle=0xb40000716ebaa3c0, base=0x0, importpid=4223, clone_count=1
W/Choreographer( 4223): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 4223): Setting up the connection to TTS engine...
D/JARVIS_SERVICE( 4223): Background Service läuft
D/mali_gralloc( 4223): register: id=23b0000027d, handle=0xb40000704d002a20, importpid=4223
W/mple.jarvis_app( 4223): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-bC8H.frro' with 3 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-8dMl.frro' with 3 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-q9Sh.frro' with 3 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 4223): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/mple.jarvis_app( 4223): Background concurrent mark compact GC freed 3408KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 2918KB/5837KB, paused 740us,6.248ms total 39.209ms
D/FlutterJNI( 4223): Sending viewport metrics to the engine.
