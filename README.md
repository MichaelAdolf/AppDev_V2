PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              6,5s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           4,7s
I/FlutterActivityAndFragmentDelegate(16402): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(16402): Beginning load of flutter...
D/FlutterJNI(16402): flutter (null) was loaded normally!
I/flutter (16402): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(16402): Width is zero. 0,0
Syncing files to device 25028RN03Y...                               93ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:50506/NjNuxo0qJag=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:50506/NjNuxo0qJag=/devtools/?uri=ws://127.0.0.1:50506/NjNuxo0qJag=/ws
D/FlutterRenderer(16402): Width is zero. 0,0
I/mple.jarvis_app(16402): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(16402): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xd861b8df59fb61c9
I/UnisocBufferQueueHelper(16402): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006f508e9600, size:88
I/mple.jarvis_app(16402): createUnisocBufferQueueHelperFactory success, get instance 0xb400006f508e9600
I/mple.jarvis_app(16402): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006fb203ed80, size:296, enable:0
I/mple.jarvis_app(16402): createUnisocFrameRecordFactory success, get instance 0xb400006fb203ed80
D/FlutterJNI(16402): Sending viewport metrics to the engine.
W/libc    (16402): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(16402): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(16402): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(16402): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(16402): register: id=23e00000119, handle=0xb400006fb1ffd780, importpid=16402
W/libc    (16402): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(16402): initIonKernelMemtrack open devices:/dev/systemheap success, fd:206
D/mali_gralloc(16402): register: id=23e00000119, handle=0xb400006fb1ffdb00, importpid=16402
D/mali_gralloc(16402): unregister: id=23e00000119, handle=0xb400006fb1ffdb00, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000011a, handle=0xb400006fb1ffdb00, importpid=16402
D/mali_gralloc(16402): register: id=23e0000011a, handle=0xb400006fb1ffdbe0, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000011a, handle=0xb400006fb1ffdbe0, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000011b, handle=0xb400006fb1ffdbe0, importpid=16402
D/mali_gralloc(16402): register: id=23e0000011b, handle=0xb400006fb1ffdcc0, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000011b, handle=0xb400006fb1ffdcc0, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000011c, handle=0xb400006fb1ffdcc0, importpid=16402
D/mali_gralloc(16402): register: id=23e0000011c, handle=0xb400006fb1ffdda0, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000011c, handle=0xb400006fb1ffdda0, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000011d, handle=0xb400006fb1ffdda0, importpid=16402
D/mali_gralloc(16402): register: id=23e0000011d, handle=0xb400006fb1ffde80, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000011d, handle=0xb400006fb1ffde80, base=0x0, importpid=16402, clone_count=1
W/Choreographer(16402): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_WS(16402): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
D/JARVIS_SERVICE(16402): Foreground Service läuft
D/JARVIS_WS(16402): WebSocket verbunden
I/Choreographer(16402): Skipped 55 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(16402): register: id=23e0000011e, handle=0xb400006e90481200, importpid=16402
I/HWUI    (16402): Davey! duration=945ms; Flags=1, FrameTimelineVsyncId=296088, IntendedVsync=1432093024001, Vsync=1433009690686, InputEventId=0, HandleInputStart=1433024585666, AnimationStart=1433024588166, PerformTraversalsStart=1433024589628, DrawStart=1433028191782, FrameDeadline=1432109690668, FrameInterval=1433024165512, FrameStartTime=16666667, SyncQueued=1433030266051, SyncStart=1433030382012, IssueDrawCommandsStart=1433031297628, SwapBuffers=1433037031859, FrameCompleted=1433038198436, DequeueBufferDuration=1769577, QueueBufferDuration=801423, GpuCompleted=1433038198436, SwapBuffersCompleted=1433038019051, DisplayPresentTime=0, CommandSubmissionCompleted=1433037031859, 
D/FlutterJNI(16402): Sending viewport metrics to the engine.
D/ProfileInstaller(16402): Installing profile for com.example.jarvis_app
W/mple.jarvis_app(16402): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(16402): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(16402): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(16402): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](16402): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(16402): unregister: id=23e0000011c, handle=0xb400006fb1ffdcc0, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000011d, handle=0xb400006fb1ffdda0, base=0x0, importpid=16402, clone_count=0
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(16402): unregister: id=23e0000011e, handle=0xb400006e90481200, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e00000119, handle=0xb400006fb1ffd780, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000011b, handle=0xb400006fb1ffdbe0, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000011a, handle=0xb400006fb1ffdb00, base=0x0, importpid=16402, clone_count=0
D/JARVIS_WS(16402): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:45. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(16402): Node-RED Event wird verarbeitet
W/libc    (16402): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(16402): type=1400 audit(0.0:578): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c241,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(16402): WakeLock aktiviert
D/JARVIS_EVENT(16402): Activity wird geöffnet
D/JARVIS_BRIDGE(16402): openAndDeliverEvent
D/JARVIS_BRIDGE(16402): Bridge Activity in Vordergrund
D/JARVIS_BRIDGE(16402): Intent Event empfangen
D/JARVIS_BRIDGE(16402): Gepuffertes Event wird gesendet
I/flutter (16402): [JARVIS BRIDGE] backgroundEvent
I/flutter (16402): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:45. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (16402): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:45. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(16402): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(16402): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(16402): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(16402): register: id=23e00000129, handle=0xb400006fb1ffb3a0, importpid=16402
D/mali_gralloc(16402): register: id=23e00000129, handle=0xb400006fb1ffb480, importpid=16402
D/mali_gralloc(16402): unregister: id=23e00000129, handle=0xb400006fb1ffb480, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000012a, handle=0xb400006fb1ffb480, importpid=16402
D/mali_gralloc(16402): register: id=23e0000012a, handle=0xb400006fb1ffb560, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000012a, handle=0xb400006fb1ffb560, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000012b, handle=0xb400006fb1ffb560, importpid=16402
D/mali_gralloc(16402): register: id=23e0000012b, handle=0xb400006fb1ffb640, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000012b, handle=0xb400006fb1ffb640, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000012c, handle=0xb400006fb1ffb640, importpid=16402
D/mali_gralloc(16402): register: id=23e0000012c, handle=0xb400006fb1ffb720, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000012c, handle=0xb400006fb1ffb720, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000012d, handle=0xb400006fb1ffb720, importpid=16402
D/mali_gralloc(16402): register: id=23e0000012d, handle=0xb400006fb1ffb800, importpid=16402
D/mali_gralloc(16402): unregister: id=23e0000012d, handle=0xb400006fb1ffb800, base=0x0, importpid=16402, clone_count=1
D/mali_gralloc(16402): register: id=23e0000012e, handle=0xb400006fb1ffb100, importpid=16402
D/FlutterJNI(16402): Sending viewport metrics to the engine.
D/mali_gralloc(16402): register: id=23e0000012f, handle=0xb400006e90481200, importpid=16402
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.resumed
D/TTS     (16402): Utterance ID has started: 33c870ac-803a-413c-af88-365fb357f1ee
D/TTS     (16402): Utterance ID has completed: 33c870ac-803a-413c-af88-365fb357f1ee
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](16402): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(16402): unregister: id=23e00000129, handle=0xb400006fb1ffb3a0, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000012a, handle=0xb400006fb1ffb480, base=0x0, importpid=16402, clone_count=0
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(16402): unregister: id=23e0000012b, handle=0xb400006fb1ffb560, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000012f, handle=0xb400006e90481200, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000012e, handle=0xb400006fb1ffb100, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000012d, handle=0xb400006fb1ffb720, base=0x0, importpid=16402, clone_count=0
D/mali_gralloc(16402): unregister: id=23e0000012c, handle=0xb400006fb1ffb640, base=0x0, importpid=16402, clone_count=0
I/ActivityThread(16402): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 1490870
I/ActivityThread(16402): assets removed: [/data/resource-cache/com.android.systemui-neutral-QQXt.frro, /data/resource-cache/com.android.systemui-accent-rEfx.frro, /data/resource-cache/com.android.systemui-dynamic-Jtid.frro]
I/ActivityThread(16402): assets added: [/data/resource-cache/com.android.systemui-neutral-JIZZ.frro, /data/resource-cache/com.android.systemui-accent-a358.frro, /data/resource-cache/com.android.systemui-dynamic-JbFp.frro]
D/JARVIS_WS(16402): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:46. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(16402): Node-RED Event wird verarbeitet
W/libc    (16402): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(16402): type=1400 audit(0.0:585): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c241,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(16402): WakeLock aktiviert
D/JARVIS_EVENT(16402): Activity wird geöffnet
D/JARVIS_BRIDGE(16402): openAndDeliverEvent
D/JARVIS_BRIDGE(16402): Bridge Activity in Vordergrund
I/flutter (16402): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(16402): Disconnected from TTS engine
W/WindowOnBackDispatcher(16402): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@5e7ab8
Lost connection to device.
