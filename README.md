PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              5,0s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,3s
I/FlutterActivityAndFragmentDelegate(26017): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(26017): Beginning load of flutter...
D/FlutterJNI(26017): flutter (null) was loaded normally!
I/flutter (26017): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(26017): Width is zero. 0,0
Syncing files to device 25028RN03Y...                               97ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:50307/rsmwGEIhp8o=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:50307/rsmwGEIhp8o=/devtools/?uri=ws://127.0.0.1:50307/rsmwGEIhp8o=/ws
D/FlutterRenderer(26017): Width is zero. 0,0
I/mple.jarvis_app(26017): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(26017): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xc99ee4d0dda8d02d
I/UnisocBufferQueueHelper(26017): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006fb220d540, size:88
I/mple.jarvis_app(26017): createUnisocBufferQueueHelperFactory success, get instance 0xb400006fb220d540
I/mple.jarvis_app(26017): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006fb204bd80, size:296, enable:0
I/mple.jarvis_app(26017): createUnisocFrameRecordFactory success, get instance 0xb400006fb204bd80
D/FlutterJNI(26017): Sending viewport metrics to the engine.
W/libc    (26017): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(26017): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(26017): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(26017): register: id=23e0000061b, handle=0xb400006fa4fb3780, importpid=26017
W/libc    (26017): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(26017): initIonKernelMemtrack open devices:/dev/systemheap success, fd:206
D/mali_gralloc(26017): register: id=23e0000061b, handle=0xb400006fa4fb3b00, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000061b, handle=0xb400006fa4fb3b00, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e0000061c, handle=0xb400006fa4fb3b00, importpid=26017
D/mali_gralloc(26017): register: id=23e0000061c, handle=0xb400006fa4fb3be0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000061c, handle=0xb400006fa4fb3be0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e0000061d, handle=0xb400006fa4fb3be0, importpid=26017
D/mali_gralloc(26017): register: id=23e0000061d, handle=0xb400006fa4fb3cc0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000061d, handle=0xb400006fa4fb3cc0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e0000061e, handle=0xb400006fa4fb3cc0, importpid=26017
D/mali_gralloc(26017): register: id=23e0000061e, handle=0xb400006fa4fb3da0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000061e, handle=0xb400006fa4fb3da0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e0000061f, handle=0xb400006fa4fb3da0, importpid=26017
D/mali_gralloc(26017): register: id=23e0000061f, handle=0xb400006fa4fb3e80, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000061f, handle=0xb400006fa4fb3e80, base=0x0, importpid=26017, clone_count=1
W/Choreographer(26017): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_WS(26017): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
D/JARVIS_SERVICE(26017): Foreground Service läuft
I/Choreographer(26017): Skipped 61 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(26017): register: id=23e00000620, handle=0xb400006e8d055200, importpid=26017
I/HWUI    (26017): Davey! duration=1049ms; Flags=1, FrameTimelineVsyncId=687770, IntendedVsync=3022150752001, Vsync=3023167418688, InputEventId=0, HandleInputStart=3023182790183, AnimationStart=3023182793490, PerformTraversalsStart=3023182794952, DrawStart=3023185958106, FrameDeadline=3022167418668, FrameInterval=3023182360452, FrameStartTime=16666667, SyncQueued=3023187162606, SyncStart=3023187247683, IssueDrawCommandsStart=3023188262183, SwapBuffers=3023198140183, FrameCompleted=3023200488183, DequeueBufferDuration=2676923, QueueBufferDuration=1064308, GpuCompleted=3023198770490, SwapBuffersCompleted=3023200488183, DisplayPresentTime=-4294967289, CommandSubmissionCompleted=3023198140183, 
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/FlutterJNI(26017): Sending viewport metrics to the engine.
D/ProfileInstaller(26017): Installing profile for com.example.jarvis_app
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.resumed
D/JARVIS_WS(26017): WebSocket verbunden
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](26017): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(26017): unregister: id=23e0000061b, handle=0xb400006fa4fb3780, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e0000061f, handle=0xb400006fa4fb3da0, base=0x0, importpid=26017, clone_count=0
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(26017): unregister: id=23e00000620, handle=0xb400006e8d055200, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e0000061c, handle=0xb400006fa4fb3b00, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e0000061e, handle=0xb400006fa4fb3cc0, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e0000061d, handle=0xb400006fa4fb3be0, base=0x0, importpid=26017, clone_count=0
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(26017): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(26017): register: id=23e0000062d, handle=0xb400006fa4fb1c60, importpid=26017
D/mali_gralloc(26017): register: id=23e0000062d, handle=0xb400006fa4fb1d40, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000062d, handle=0xb400006fa4fb1d40, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e0000062e, handle=0xb400006fa4fb1d40, importpid=26017
D/mali_gralloc(26017): register: id=23e0000062e, handle=0xb400006fa4fb1e20, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000062e, handle=0xb400006fa4fb1e20, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e0000062f, handle=0xb400006fa4fb1e20, importpid=26017
D/mali_gralloc(26017): register: id=23e0000062f, handle=0xb400006fa4fb1f00, importpid=26017
D/mali_gralloc(26017): unregister: id=23e0000062f, handle=0xb400006fa4fb1f00, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000630, handle=0xb400006fa4fb1f00, importpid=26017
D/mali_gralloc(26017): register: id=23e00000630, handle=0xb400006fa4fb1fe0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000630, handle=0xb400006fa4fb1fe0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000631, handle=0xb400006fa4fb2fa0, importpid=26017
D/mali_gralloc(26017): register: id=23e00000631, handle=0xb400006fa4fb3080, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000631, handle=0xb400006fa4fb3080, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000632, handle=0xb400006fa4fb12c0, importpid=26017
D/mali_gralloc(26017): register: id=23e00000633, handle=0xb400006fa4fb3b00, importpid=26017
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](26017): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(26017): unregister: id=23e0000062e, handle=0xb400006fa4fb1d40, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e0000062f, handle=0xb400006fa4fb1e20, base=0x0, importpid=26017, clone_count=0
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(26017): unregister: id=23e00000630, handle=0xb400006fa4fb1f00, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e0000062d, handle=0xb400006fa4fb1c60, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e00000631, handle=0xb400006fa4fb2fa0, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e00000633, handle=0xb400006fa4fb3b00, base=0x0, importpid=26017, clone_count=0
D/mali_gralloc(26017): unregister: id=23e00000632, handle=0xb400006fa4fb12c0, base=0x0, importpid=26017, clone_count=0
D/JARVIS_WS(26017): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:12. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(26017): Node-RED Event wird verarbeitet
W/libc    (26017): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(26017): type=1400 audit(0.0:737): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c242,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(26017): WakeLock aktiviert
D/JARVIS_EVENT(26017): Activity wird geöffnet
D/JARVIS_BRIDGE(26017): openAndDeliverEvent
D/JARVIS_BRIDGE(26017): Bridge Activity in Vordergrund
I/ActivityThread(26017): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 3091581
I/ActivityThread(26017): assets removed: [/data/resource-cache/com.android.systemui-neutral-JIZZ.frro, /data/resource-cache/com.android.systemui-accent-a358.frro, /data/resource-cache/com.android.systemui-dynamic-JbFp.frro]
I/ActivityThread(26017): assets added: [/data/resource-cache/com.android.systemui-neutral-ycaE.frro, /data/resource-cache/com.android.systemui-accent-Nk8z.frro, /data/resource-cache/com.android.systemui-dynamic-jGF0.frro]
D/JARVIS_WS(26017): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:13. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(26017): Node-RED Event wird verarbeitet
W/libc    (26017): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(26017): type=1400 audit(0.0:743): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c242,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(26017): WakeLock aktiviert
D/JARVIS_EVENT(26017): Activity wird geöffnet
D/JARVIS_BRIDGE(26017): openAndDeliverEvent
D/JARVIS_BRIDGE(26017): Bridge Activity in Vordergrund
I/flutter (26017): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(26017): Disconnected from TTS engine
W/WindowOnBackDispatcher(26017): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@b5cf91b
I/FlutterActivityAndFragmentDelegate(26017): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter (26017): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(26017): Sucessfully bound to com.google.android.tts
I/TextToSpeech(26017): Connected to TTS engine
D/JARVIS_BRIDGE(26017): MethodChannel erstellt
D/JARVIS_BRIDGE(26017): Gepuffertes Event wird gesendet
I/TextToSpeech(26017): Setting up the connection to TTS engine...
D/FlutterRenderer(26017): Width is zero. 0,0
D/JARVIS_BRIDGE(26017): Intent Event empfangen
D/JARVIS_BRIDGE(26017): Gepuffertes Event wird gesendet
D/JARVIS_BRIDGE(26017): Intent Event empfangen
D/JARVIS_BRIDGE(26017): Gepuffertes Event wird gesendet
I/flutter (26017): [JARVIS BRIDGE] backgroundEvent
I/flutter (26017): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:13. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (26017): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 20:13. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/FlutterRenderer(26017): Width is zero. 0,0
D/FlutterJNI(26017): Sending viewport metrics to the engine.
E/mali_gralloc(26017): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(26017): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(26017): register: id=23e00000650, handle=0xb400006f5062d200, importpid=26017
D/mali_gralloc(26017): register: id=23e00000650, handle=0xb400006f5062d2e0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000650, handle=0xb400006f5062d2e0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000651, handle=0xb400006f5062d2e0, importpid=26017
D/mali_gralloc(26017): register: id=23e00000651, handle=0xb400006f5062d3c0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000651, handle=0xb400006f5062d3c0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000652, handle=0xb400006f5062d3c0, importpid=26017
D/mali_gralloc(26017): register: id=23e00000652, handle=0xb400006f5062d4a0, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000652, handle=0xb400006f5062d4a0, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000653, handle=0xb400006f5062d4a0, importpid=26017
D/mali_gralloc(26017): register: id=23e00000653, handle=0xb400006f5062d580, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000653, handle=0xb400006f5062d580, base=0x0, importpid=26017, clone_count=1
D/mali_gralloc(26017): register: id=23e00000654, handle=0xb400006f5062d580, importpid=26017
D/mali_gralloc(26017): register: id=23e00000654, handle=0xb400006f5062d660, importpid=26017
D/mali_gralloc(26017): unregister: id=23e00000654, handle=0xb400006f5062d660, base=0x0, importpid=26017, clone_count=1
W/Choreographer(26017): Already have a pending vsync event.  There should only be one at a time.
W/mple.jarvis_app(26017): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-JIZZ.frro' with 3 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-a358.frro' with 3 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-JbFp.frro' with 3 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(26017): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_SERVICE(26017): Foreground Service läuft
D/mali_gralloc(26017): register: id=23e00000655, handle=0xb400006fa4fb1720, importpid=26017
D/mali_gralloc(26017): register: id=23e00000656, handle=0xb400006f5062dac0, importpid=26017
D/FlutterJNI(26017): Sending viewport metrics to the engine.
D/TTS     (26017): Utterance ID has started: ff4d5624-cd11-4e76-ac3a-816f7d43ba14
D/TTS     (26017): Utterance ID has completed: ff4d5624-cd11-4e76-ac3a-816f7d43ba14
