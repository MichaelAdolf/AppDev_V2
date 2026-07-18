PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter clean  
Deleting build...                                                  812ms
Deleting .dart_tool...                                              23ms
Deleting ephemeral...                                                4ms
Deleting Generated.xcconfig...                                       0ms
Deleting flutter_export_environment.sh...                            0ms
Deleting ephemeral...                                                1ms
Deleting ephemeral...                                                4ms
Deleting ephemeral...                                                4ms
Deleting .flutter-plugins-dependencies...                            1ms
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter pub get
Resolving dependencies... 
Downloading packages... 
  matcher 0.12.19 (0.12.20 available)
  meta 1.18.0 (1.19.0 available)
  package_info_plus 10.2.0 (10.2.1 available)
  test_api 0.7.11 (0.7.13 available)
  vector_math 2.2.0 (2.4.0 available)
  xml 6.6.1 (7.0.1 available)
Got dependencies!
6 packages have newer versions incompatible with dependency constraints.
Try `flutter pub outdated` for more information.
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             46,6s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,1s
I/FlutterActivityAndFragmentDelegate(25074): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(25074): Beginning load of flutter...
D/FlutterJNI(25074): flutter (null) was loaded normally!
I/flutter (25074): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(25074): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              205ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:61867/PmdwKk6O5nc=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:61867/PmdwKk6O5nc=/devtools/?uri=ws://127.0.0.1:61867/PmdwKk6O5nc=/ws
D/FlutterRenderer(25074): Width is zero. 0,0
D/FlutterJNI(25074): Sending viewport metrics to the engine.
W/Choreographer(25074): Already have a pending vsync event.  There should only be one at a time.
I/mple.jarvis_app(25074): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/TextToSpeech(25074): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(25074): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(25074): Connected to TTS engine
I/TextToSpeech(25074): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(25074): RECORD_AUDIO Permission fehlt
D/JARVIS_WS(25074): WebSocket verbunden
D/JARVIS_SERVICE(25074): Foreground Service läuft
I/Choreographer(25074): Skipped 77 frames!  The application may be doing too much work on its main thread.
I/flutter (25074): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](25074): visibilityChanged oldVisibility=true newVisibility=false
I/flutter (25074): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (25074): [Jarvis] Lifecycle: AppLifecycleState.paused
W/System  (25074): ClassLoader referenced unknown path: 
D/nativeloader(25074): Configuring clns-8 for other apk . target_sdk_version=36, uses_libraries=, library_path=/data/app/~~JRw0Ojb78-V0WqvlfmQJKA==/com.example.jarvis_app-DlVtcrU2L3iu-BBKnOO20A==/lib/arm64:/data/app/~~JRw0Ojb78-V0WqvlfmQJKA==/com.example.jarvis_app-DlVtcrU2L3iu-BBKnOO20A==/base.apk!/lib/arm64-v8a, permitted_path=/data:/mnt/expand:/data/user/0/com.example.jarvis_app
I/ActivityThread(25074): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 14489937
I/ActivityThread(25074): assets removed: [/data/resource-cache/com.android.systemui-neutral-wl4D.frro, /data/resource-cache/com.android.systemui-accent-vKDV.frro, /data/resource-cache/com.android.systemui-dynamic-AwYr.frro]
I/ActivityThread(25074): assets added: [/data/resource-cache/com.android.systemui-neutral-tJbg.frro, /data/resource-cache/com.android.systemui-accent-vA1g.frro, /data/resource-cache/com.android.systemui-dynamic-b6sq.frro]
D/JARVIS_TTS(25074): Android TTS bereit
D/FlutterJNI(25074): Sending viewport metrics to the engine.
D/ProfileInstaller(25074): Installing profile for com.example.jarvis_app
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (25074): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(25074): Disconnected from TTS engine
W/WindowOnBackDispatcher(25074): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@a705379
I/FlutterActivityAndFragmentDelegate(25074): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter (25074): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(25074): Sucessfully bound to com.google.android.tts
I/TextToSpeech(25074): Connected to TTS engine
D/JARVIS_BRIDGE(25074): MethodChannel erstellt
I/TextToSpeech(25074): Setting up the connection to TTS engine...
D/FlutterRenderer(25074): Width is zero. 0,0
W/CheckTime(25074): App running slow: Executing activity onCreate took 977ms
D/FlutterRenderer(25074): Width is zero. 0,0
I/mple.jarvis_app(25074): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x59605a4c8e745577
I/UnisocBufferQueueHelper(25074): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006ec5d76080, size:88
I/mple.jarvis_app(25074): createUnisocBufferQueueHelperFactory success, get instance 0xb400006ec5d76080
I/mple.jarvis_app(25074): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006e0bbd93c0, size:296, enable:0
I/mple.jarvis_app(25074): createUnisocFrameRecordFactory success, get instance 0xb400006e0bbd93c0
D/FlutterJNI(25074): Sending viewport metrics to the engine.
W/libc    (25074): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(25074): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(25074): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(25074): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(25074): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(25074): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(25074): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(25074): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(25074): register: id=23b000006df, handle=0xb400006ec5a71900, importpid=25074
W/libc    (25074): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(25074): initIonKernelMemtrack open devices:/dev/systemheap success, fd:210
D/mali_gralloc(25074): register: id=23b000006df, handle=0xb400006ec5a71c80, importpid=25074
D/mali_gralloc(25074): unregister: id=23b000006df, handle=0xb400006ec5a71c80, base=0x0, importpid=25074, clone_count=1
D/mali_gralloc(25074): register: id=23b000006e0, handle=0xb400006ec5a71c80, importpid=25074
D/mali_gralloc(25074): register: id=23b000006e0, handle=0xb400006ec5a71d60, importpid=25074
D/mali_gralloc(25074): unregister: id=23b000006e0, handle=0xb400006ec5a71d60, base=0x0, importpid=25074, clone_count=1
D/mali_gralloc(25074): register: id=23b000006e1, handle=0xb400006ec5a71d60, importpid=25074
D/mali_gralloc(25074): register: id=23b000006e1, handle=0xb400006ec5a71e40, importpid=25074
D/mali_gralloc(25074): unregister: id=23b000006e1, handle=0xb400006ec5a71e40, base=0x0, importpid=25074, clone_count=1
D/mali_gralloc(25074): register: id=23b000006e2, handle=0xb400006ec5a71e40, importpid=25074
D/mali_gralloc(25074): register: id=23b000006e2, handle=0xb400006ec5a71f20, importpid=25074
D/mali_gralloc(25074): unregister: id=23b000006e2, handle=0xb400006ec5a71f20, base=0x0, importpid=25074, clone_count=1
D/mali_gralloc(25074): register: id=23b000006e3, handle=0xb400006ec5a71f20, importpid=25074
D/mali_gralloc(25074): register: id=23b000006e3, handle=0xb400006e0badc000, importpid=25074
D/mali_gralloc(25074): unregister: id=23b000006e3, handle=0xb400006e0badc000, base=0x0, importpid=25074, clone_count=1
W/Choreographer(25074): Already have a pending vsync event.  There should only be one at a time.
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-wl4D.frro' with 3 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-vKDV.frro' with 3 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-AwYr.frro' with 3 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(25074): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_SERVICE(25074): Foreground Service läuft
I/Choreographer(25074): Skipped 55 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(25074): register: id=23b000006e4, handle=0xb400006e1405fc60, importpid=25074
I/mple.jarvis_app(25074): Background concurrent mark compact GC freed 3432KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 2907KB/5815KB, paused 781us,14.058ms total 61.103ms
I/HWUI    (25074): Davey! duration=991ms; Flags=1, FrameTimelineVsyncId=1148066, IntendedVsync=14533675532644, Vsync=14534592199329, InputEventId=0, HandleInputStart=14534598778641, AnimationStart=14534598785411, PerformTraversalsStart=14534599422449, DrawStart=14534605299795, FrameDeadline=14533692199311, FrameInterval=14534598082141, FrameStartTime=16666667, SyncQueued=14534608154295, SyncStart=14534608238526, IssueDrawCommandsStart=14534609191372, SwapBuffers=14534655626334, FrameCompleted=14534667412064, DequeueBufferDuration=1717923, QueueBufferDuration=728731, GpuCompleted=14534667412064, SwapBuffersCompleted=14534656518988, DisplayPresentTime=352187425297, CommandSubmissionCompleted=14534655626334, 
D/FlutterJNI(25074): Sending viewport metrics to the engine.
I/flutter (25074): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (25074): [JARVIS] _startVoiceInput START
D/JARVIS_WAKEWORD(25074): Wakeword STOP
I/flutter (25074): [JARVIS] Wakeword gestoppt
I/flutter (25074): [JARVIS] _startVoiceInput START
D/JARVIS_WAKEWORD(25074): Wakeword STOP
I/flutter (25074): [JARVIS] Wakeword gestoppt
D/TTS     (25074): Utterance ID has started: 7626068c-5498-4f7f-9fc2-e8689af9aeaa
D/TTS     (25074): Utterance ID has completed: 7626068c-5498-4f7f-9fc2-e8689af9aeaa
D/JARVIS_WAKEWORD(25074): Listening gestartet
D/JARVIS_WAKEWORD(25074): Bereit für Wakeword
D/JARVIS_WAKEWORD(25074): Sprache erkannt
D/JARVIS_WAKEWORD(25074): Sprachende
D/JARVIS_WAKEWORD(25074): Erkannt: jarvis chavez
D/JARVIS_WAKEWORD(25074): Wakeword erkannt
W/libc    (25074): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(25074): type=1400 audit(0.0:3443): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(25074): WakeLock aktiviert
D/JARVIS_WAKEWORD(25074): sendWakewordToFlutter
I/flutter (25074): [JARVIS BRIDGE] wakewordDetected
I/flutter (25074): [JARVIS BRIDGE] null
I/flutter (25074): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (25074): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (25074): [JARVIS] Wakeword Trigger empfangen
I/flutter (25074): [JARVIS] _startVoiceInput START
D/JARVIS_WAKEWORD(25074): Wakeword STOP
I/flutter (25074): [JARVIS] Wakeword gestoppt
D/FlutterJNI(25074): Sending viewport metrics to the engine.
D/mali_gralloc(25074): register: id=23b000006f6, handle=0xb400006ec5a704e0, importpid=25074
D/JARVIS_WAKEWORD(25074): Listening gestartet
D/JARVIS_WAKEWORD(25074): Bereit für Wakeword
D/JARVIS_WAKEWORD(25074): Sprache erkannt
D/JARVIS_WAKEWORD(25074): Sprachende
D/JARVIS_WAKEWORD(25074): Erkannt: sage mir etwas zum sage mir etwas zum licht
D/JARVIS_WAKEWORD(25074): Restart blockiert
