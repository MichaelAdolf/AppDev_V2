PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             16,6s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           4,9s
I/FlutterActivityAndFragmentDelegate(12298): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(12298): Beginning load of flutter...
D/FlutterJNI(12298): flutter (null) was loaded normally!
I/flutter (12298): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(12298): Width is zero. 0,0
Syncing files to device 25028RN03Y...                               95ms

Flutter run key commands.
r Hot reload.
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:51694/E-HBVT0ylHU=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:51694/E-HBVT0ylHU=/devtools/?uri=ws://127.0.0.1:51694/E-HBVT0ylHU=/ws
D/FlutterRenderer(12298): Width is zero. 0,0
I/mple.jarvis_app(12298): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(12298): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x38ebed6510ec9f79
I/UnisocBufferQueueHelper(12298): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006f508f9660, size:88
I/mple.jarvis_app(12298): createUnisocBufferQueueHelperFactory success, get instance 0xb400006f508f9660
I/mple.jarvis_app(12298): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006e8f68fb40, size:296, enable:0
I/mple.jarvis_app(12298): createUnisocFrameRecordFactory success, get instance 0xb400006e8f68fb40
D/FlutterJNI(12298): Sending viewport metrics to the engine.
W/libc    (12298): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(12298): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(12298): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(12298): register: id=23e00000098, handle=0xb400006fb22674e0, importpid=12298
W/libc    (12298): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(12298): initIonKernelMemtrack open devices:/dev/systemheap success, fd:207
D/mali_gralloc(12298): register: id=23e00000098, handle=0xb400006fb2267860, importpid=12298
D/mali_gralloc(12298): unregister: id=23e00000098, handle=0xb400006fb2267860, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e00000099, handle=0xb400006fb2267860, importpid=12298
D/mali_gralloc(12298): register: id=23e00000099, handle=0xb400006fb2267940, importpid=12298
D/mali_gralloc(12298): unregister: id=23e00000099, handle=0xb400006fb2267940, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e0000009a, handle=0xb400006fb2267940, importpid=12298
D/mali_gralloc(12298): register: id=23e0000009a, handle=0xb400006fb2267a20, importpid=12298
D/mali_gralloc(12298): unregister: id=23e0000009a, handle=0xb400006fb2267a20, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e0000009b, handle=0xb400006fb2267a20, importpid=12298
D/mali_gralloc(12298): register: id=23e0000009b, handle=0xb400006fb2267b00, importpid=12298
D/mali_gralloc(12298): unregister: id=23e0000009b, handle=0xb400006fb2267b00, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e0000009c, handle=0xb400006fb2267b00, importpid=12298
D/mali_gralloc(12298): register: id=23e0000009c, handle=0xb400006fb2267be0, importpid=12298
D/mali_gralloc(12298): unregister: id=23e0000009c, handle=0xb400006fb2267be0, base=0x0, importpid=12298, clone_count=1
W/DisplayEventDispatcher(12298): Vsync time out! vsyncScheduleDelay=459ms
W/Choreographer(12298): Already have a pending vsync event.  There should only be one at a time.
W/Choreographer(12298): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_WS(12298): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
D/JARVIS_WS(12298): WebSocket verbunden
D/JARVIS_SERVICE(12298): Foreground Service läuft
I/Choreographer(12298): Skipped 70 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(12298): register: id=23e0000009d, handle=0xb400006e8b0f14c0, importpid=12298
I/HWUI    (12298): Davey! duration=1210ms; Flags=1, FrameTimelineVsyncId=11801, IntendedVsync=570074513668, Vsync=571241180358, InputEventId=0, HandleInputStart=571253553590, AnimationStart=571253556398, PerformTraversalsStart=571253558052, DrawStart=571257887590, FrameDeadline=570091180335, FrameInterval=571253117437, FrameStartTime=16666667, SyncQueued=571265684590, SyncStart=571265838360, IssueDrawCommandsStart=571267179744, SwapBuffers=571283101167, FrameCompleted=571284777052, DequeueBufferDuration=4664962, QueueBufferDuration=1251038, GpuCompleted=571284777052, SwapBuffersCompleted=571284753360, DisplayPresentTime=3348817102368632878, CommandSubmissionCompleted=571283101167, 
D/ProfileInstaller(12298): Installing profile for com.example.jarvis_app
D/FlutterJNI(12298): Sending viewport metrics to the engine.
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](12298): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(12298): unregister: id=23e0000009b, handle=0xb400006fb2267a20, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e0000009c, handle=0xb400006fb2267b00, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e00000098, handle=0xb400006fb22674e0, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e0000009a, handle=0xb400006fb2267940, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e00000099, handle=0xb400006fb2267860, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e0000009d, handle=0xb400006e8b0f14c0, base=0x0, importpid=12298, clone_count=0
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.paused
D/JARVIS_WS(12298): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:31. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(12298): Node-RED Event wird verarbeitet
W/libc    (12298): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(12298): type=1400 audit(0.0:498): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c241,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(12298): WakeLock aktiviert
D/JARVIS_EVENT(12298): Activity wird geöffnet
D/JARVIS_BRIDGE(12298): openAndDeliverEvent
D/JARVIS_BRIDGE(12298): Bridge Activity in Vordergrund
D/JARVIS_BRIDGE(12298): Intent Event empfangen
D/JARVIS_BRIDGE(12298): Gepuffertes Event wird gesendet
I/flutter (12298): [JARVIS BRIDGE] backgroundEvent
I/flutter (12298): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:31. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (12298): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:31. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(12298): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(12298): register: id=23e000000ab, handle=0xb400006fb2265020, importpid=12298
D/mali_gralloc(12298): register: id=23e000000ab, handle=0xb400006fb2265100, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000ab, handle=0xb400006fb2265100, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000ac, handle=0xb400006fb2265100, importpid=12298
D/mali_gralloc(12298): register: id=23e000000ac, handle=0xb400006fb22652c0, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000ac, handle=0xb400006fb22652c0, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000ad, handle=0xb400006fb22652c0, importpid=12298
D/mali_gralloc(12298): register: id=23e000000ad, handle=0xb400006fb22653a0, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000ad, handle=0xb400006fb22653a0, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000ae, handle=0xb400006fb22653a0, importpid=12298
D/mali_gralloc(12298): register: id=23e000000ae, handle=0xb400006fb22658e0, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000ae, handle=0xb400006fb22658e0, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000af, handle=0xb400006fb22658e0, importpid=12298
D/mali_gralloc(12298): register: id=23e000000af, handle=0xb400006fb2265b80, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000af, handle=0xb400006fb2265b80, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000b0, handle=0xb400006fb2055460, importpid=12298
D/FlutterJNI(12298): Sending viewport metrics to the engine.
D/mali_gralloc(12298): register: id=23e000000b1, handle=0xb400006e8b0f5e40, importpid=12298
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.resumed
D/TTS     (12298): Utterance ID has started: f2bde6d5-b605-47be-94db-219e1ca90f73
D/TTS     (12298): Utterance ID has completed: f2bde6d5-b605-47be-94db-219e1ca90f73
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](12298): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(12298): unregister: id=23e000000ac, handle=0xb400006fb2265100, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e000000ad, handle=0xb400006fb22652c0, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e000000b1, handle=0xb400006e8b0f5e40, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e000000b0, handle=0xb400006fb2055460, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e000000ae, handle=0xb400006fb22653a0, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e000000ab, handle=0xb400006fb2265020, base=0x0, importpid=12298, clone_count=0
D/mali_gralloc(12298): unregister: id=23e000000af, handle=0xb400006fb22658e0, base=0x0, importpid=12298, clone_count=0
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.paused
I/ActivityThread(12298): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 668105
I/ActivityThread(12298): assets removed: [/data/resource-cache/com.android.systemui-neutral-LlOT.frro, /data/resource-cache/com.android.systemui-accent-9jMj.frro, /data/resource-cache/com.android.systemui-dynamic-4JMe.frro]
I/ActivityThread(12298): assets added: [/data/resource-cache/com.android.systemui-neutral-QQXt.frro, /data/resource-cache/com.android.systemui-accent-rEfx.frro, /data/resource-cache/com.android.systemui-dynamic-Jtid.frro]
D/JARVIS_WS(12298): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:32. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(12298): Node-RED Event wird verarbeitet
W/libc    (12298): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(12298): type=1400 audit(0.0:506): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c241,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(12298): WakeLock aktiviert
D/JARVIS_EVENT(12298): Activity wird geöffnet
D/JARVIS_BRIDGE(12298): openAndDeliverEvent
D/JARVIS_BRIDGE(12298): Bridge Activity in Vordergrund
I/flutter (12298): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(12298): Disconnected from TTS engine
W/WindowOnBackDispatcher(12298): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@8df1bf6
I/flutter (12298): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(12298): Sucessfully bound to com.google.android.tts
I/TextToSpeech(12298): Connected to TTS engine
D/JARVIS_BRIDGE(12298): MethodChannel erstellt
D/JARVIS_BRIDGE(12298): Gepuffertes Event wird gesendet
I/TextToSpeech(12298): Setting up the connection to TTS engine...
D/FlutterRenderer(12298): Width is zero. 0,0
D/JARVIS_BRIDGE(12298): Intent Event empfangen
D/JARVIS_BRIDGE(12298): Gepuffertes Event wird gesendet
W/CheckTime(12298): App running slow: Executing activity onCreate took 876ms
D/JARVIS_BRIDGE(12298): Intent Event empfangen
D/JARVIS_BRIDGE(12298): Gepuffertes Event wird gesendet
I/flutter (12298): [JARVIS BRIDGE] backgroundEvent
I/flutter (12298): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:32. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (12298): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Dienstag, der vierzehnter Juli 2026. Die aktuelle Uhrzeit ist 19:32. Draußen sind es aktuell 28 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine."}
D/FlutterRenderer(12298): Width is zero. 0,0
D/FlutterJNI(12298): Sending viewport metrics to the engine.
E/mali_gralloc(12298): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(12298): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(12298): register: id=23e000000cf, handle=0xb400006fb2267da0, importpid=12298
D/mali_gralloc(12298): register: id=23e000000cf, handle=0xb400006fb2267e80, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000cf, handle=0xb400006fb2267e80, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000d0, handle=0xb400006fb2267e80, importpid=12298
D/mali_gralloc(12298): register: id=23e000000d0, handle=0xb400006fb2268040, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000d0, handle=0xb400006fb2268040, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000d1, handle=0xb400006fb2268040, importpid=12298
D/mali_gralloc(12298): register: id=23e000000d1, handle=0xb400006fb2268120, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000d1, handle=0xb400006fb2268120, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000d2, handle=0xb400006fb2268120, importpid=12298
D/mali_gralloc(12298): register: id=23e000000d2, handle=0xb400006fb2268200, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000d2, handle=0xb400006fb2268200, base=0x0, importpid=12298, clone_count=1
D/mali_gralloc(12298): register: id=23e000000d3, handle=0xb400006fb2268200, importpid=12298
D/mali_gralloc(12298): register: id=23e000000d3, handle=0xb400006fb22682e0, importpid=12298
D/mali_gralloc(12298): unregister: id=23e000000d3, handle=0xb400006fb22682e0, base=0x0, importpid=12298, clone_count=1
W/Choreographer(12298): Already have a pending vsync event.  There should only be one at a time.
W/mple.jarvis_app(12298): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-LlOT.frro' with 3 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-9jMj.frro' with 3 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-4JMe.frro' with 3 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(12298): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_SERVICE(12298): Foreground Service läuft
I/Choreographer(12298): Skipped 36 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(12298): register: id=23e000000d4, handle=0xb400006fb2265640, importpid=12298
D/FlutterJNI(12298): Sending viewport metrics to the engine.
D/mali_gralloc(12298): register: id=23e000000d5, handle=0xb400006fb2265720, importpid=12298
D/TTS     (12298): Utterance ID has started: 578d5c42-cd73-4a00-a992-6c070e6a6699
I/mple.jarvis_app(12298): Background concurrent mark compact GC freed 2888KB AllocSpace bytes, 0(0B)LOS objects, 49% free, 3011KB/6023KB, paused 505us,7.270ms total 59.639ms
D/TTS     (12298): Utterance ID has completed: 578d5c42-cd73-4a00-a992-6c070e6a6699
