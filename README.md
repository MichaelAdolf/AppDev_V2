PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                            129,9s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           5,5s
I/FlutterActivityAndFragmentDelegate(15224): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(15224): Beginning load of flutter...
D/FlutterJNI(15224): flutter (null) was loaded normally!
I/flutter (15224): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(15224): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              258ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:55456/-rN0N3OA2Os=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:55456/-rN0N3OA2Os=/devtools/?uri=ws://127.0.0.1:55456/-rN0N3OA2Os=/ws
D/FlutterRenderer(15224): Width is zero. 0,0
I/mple.jarvis_app(15224): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(15224): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xfce02bae412bad45
I/UnisocBufferQueueHelper(15224): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb40000716268fc00, size:88
I/mple.jarvis_app(15224): createUnisocBufferQueueHelperFactory success, get instance 0xb40000716268fc00
I/mple.jarvis_app(15224): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400007051000000, size:296, enable:0
I/mple.jarvis_app(15224): createUnisocFrameRecordFactory success, get instance 0xb400007051000000
D/FlutterJNI(15224): Sending viewport metrics to the engine.
W/libc    (15224): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(15224): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(15224): register: id=23b0000030e, handle=0xb40000716eab46a0, importpid=15224
W/libc    (15224): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(15224): initIonKernelMemtrack open devices:/dev/systemheap success, fd:207
D/mali_gralloc(15224): register: id=23b0000030e, handle=0xb40000716eab4a20, importpid=15224
D/mali_gralloc(15224): unregister: id=23b0000030e, handle=0xb40000716eab4a20, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b0000030f, handle=0xb40000716eab4a20, importpid=15224
D/mali_gralloc(15224): register: id=23b0000030f, handle=0xb40000716eab4b00, importpid=15224
D/mali_gralloc(15224): unregister: id=23b0000030f, handle=0xb40000716eab4b00, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000310, handle=0xb40000716eab4b00, importpid=15224
D/mali_gralloc(15224): register: id=23b00000310, handle=0xb40000716eab4be0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000310, handle=0xb40000716eab4be0, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000311, handle=0xb40000716eab4be0, importpid=15224
D/mali_gralloc(15224): register: id=23b00000311, handle=0xb40000716eab4cc0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000311, handle=0xb40000716eab4cc0, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000312, handle=0xb40000716eab4cc0, importpid=15224
D/mali_gralloc(15224): register: id=23b00000312, handle=0xb40000716eab4da0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000312, handle=0xb40000716eab4da0, base=0x0, importpid=15224, clone_count=1
W/Choreographer(15224): Already have a pending vsync event.  There should only be one at a time.
D/JARVIS_WS(15224): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
D/JARVIS_WS(15224): WebSocket verbunden
I/TextToSpeech(15224): Connected to TTS engine
D/JARVIS_SERVICE(15224): Foreground Service läuft
I/Choreographer(15224): Skipped 77 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(15224): register: id=23b00000313, handle=0xb40000704dfa5b40, importpid=15224
I/HWUI    (15224): Davey! duration=1316ms; Flags=1, FrameTimelineVsyncId=848511, IntendedVsync=18501560519668, Vsync=18502843853027, InputEventId=0, HandleInputStart=18502849486034, AnimationStart=18502849490764, PerformTraversalsStart=18502849493880, DrawStart=18502856461149, FrameDeadline=18501577186335, FrameInterval=18502848824034, FrameStartTime=16666667, SyncQueued=18502859116534, SyncStart=18502859231072, IssueDrawCommandsStart=18502860451841, SwapBuffers=18502875109726, FrameCompleted=18502876654572, DequeueBufferDuration=3517962, QueueBufferDuration=1252731, GpuCompleted=18502876089072, SwapBuffersCompleted=18502876654572, DisplayPresentTime=44, CommandSubmissionCompleted=18502875109726, 
D/ProfileInstaller(15224): Installing profile for com.example.jarvis_app
D/FlutterJNI(15224): Sending viewport metrics to the engine.
I/TextToSpeech(15224): Setting up the connection to TTS engine...
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](15224): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(15224): unregister: id=23b00000310, handle=0xb40000716eab4b00, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000311, handle=0xb40000716eab4be0, base=0x0, importpid=15224, clone_count=0
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(15224): unregister: id=23b00000313, handle=0xb40000704dfa5b40, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000312, handle=0xb40000716eab4cc0, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b0000030f, handle=0xb40000716eab4a20, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b0000030e, handle=0xb40000716eab46a0, base=0x0, importpid=15224, clone_count=0
I/ActivityThread(15224): ApplicationInfo updating for com.example.jarvis_app, new timestamp: 18589896
I/ActivityThread(15224): assets removed: [/data/resource-cache/com.android.systemui-neutral-fkQH.frro, /data/resource-cache/com.android.systemui-accent-q9NL.frro, /data/resource-cache/com.android.systemui-dynamic-ebIT.frro]
I/ActivityThread(15224): assets added: [/data/resource-cache/com.android.systemui-neutral-IaMl.frro, /data/resource-cache/com.android.systemui-accent-j2x8.frro, /data/resource-cache/com.android.systemui-dynamic-zyKr.frro]
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.detached
I/TextToSpeech(15224): Disconnected from TTS engine
W/WindowOnBackDispatcher(15224): sendCancelIfRunning: isInProgress=false callback=android.view.ViewRootImpl$$ExternalSyntheticLambda11@4c42fc9
I/FlutterActivityAndFragmentDelegate(15224): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
I/flutter (15224): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
I/TextToSpeech(15224): Sucessfully bound to com.google.android.tts
D/JARVIS_BRIDGE(15224): MethodChannel erstellt
D/FlutterRenderer(15224): Width is zero. 0,0
I/TextToSpeech(15224): Connected to TTS engine
D/FlutterRenderer(15224): Width is zero. 0,0
D/FlutterJNI(15224): Sending viewport metrics to the engine.
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(15224): register: id=23b00000323, handle=0xb40000710e3d9a20, importpid=15224
D/mali_gralloc(15224): register: id=23b00000323, handle=0xb40000710e3d9be0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000323, handle=0xb40000710e3d9be0, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000324, handle=0xb40000710e3d9be0, importpid=15224
D/mali_gralloc(15224): register: id=23b00000324, handle=0xb40000710e3d9da0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000324, handle=0xb40000710e3d9da0, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000325, handle=0xb40000710e3d9da0, importpid=15224
D/mali_gralloc(15224): register: id=23b00000325, handle=0xb40000710e3d9e80, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000325, handle=0xb40000710e3d9e80, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000326, handle=0xb40000710e3d9e80, importpid=15224
D/mali_gralloc(15224): register: id=23b00000326, handle=0xb40000710e3d9f60, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000326, handle=0xb40000710e3d9f60, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000327, handle=0xb40000710e3d9f60, importpid=15224
D/mali_gralloc(15224): register: id=23b00000327, handle=0xb40000710e3da040, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000327, handle=0xb40000710e3da040, base=0x0, importpid=15224, clone_count=1
W/Choreographer(15224): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(15224): Setting up the connection to TTS engine...
D/JARVIS_SERVICE(15224): Foreground Service läuft
D/mali_gralloc(15224): register: id=23b00000328, handle=0xb400007051015dc0, importpid=15224
W/mple.jarvis_app(15224): Cleared Reference was only reachable from finalizer (only reported once)
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-neutral-fkQH.frro' with 3 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-accent-q9NL.frro' with 3 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '/data/resource-cache/com.android.systemui-dynamic-ebIT.frro' with 3 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(15224): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/mple.jarvis_app(15224): Background concurrent mark compact GC freed 3116KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 3199KB/6399KB, paused 432us,7.043ms total 55.280ms
D/FlutterJNI(15224): Sending viewport metrics to the engine.
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](15224): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(15224): unregister: id=23b00000325, handle=0xb40000710e3d9da0, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000326, handle=0xb40000710e3d9e80, base=0x0, importpid=15224, clone_count=0
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.paused
D/mali_gralloc(15224): unregister: id=23b00000328, handle=0xb400007051015dc0, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000327, handle=0xb40000710e3d9f60, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000324, handle=0xb40000710e3d9be0, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000323, handle=0xb40000710e3d9a20, base=0x0, importpid=15224, clone_count=0
D/JARVIS_WS(15224): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Sonntag, der zwölfter Juli 2026. Die aktuelle Uhrzeit ist 20:02. Draußen sind es aktuell 26 Grad bei klarem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(15224): Node-RED Event wird verarbeitet
W/libc    (15224): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(15224): type=1400 audit(0.0:18301): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c241,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(15224): WakeLock aktiviert
D/JARVIS_BRIDGE(15224): openAndDeliverEvent
D/JARVIS_BRIDGE(15224): Intent Event empfangen
D/JARVIS_BRIDGE(15224): Gepuffertes Event wird gesendet
I/flutter (15224): [JARVIS BRIDGE] backgroundEvent
I/flutter (15224): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Sonntag, der zwölfter Juli 2026. Die aktuelle Uhrzeit ist 20:02. Draußen sind es aktuell 26 Grad bei klarem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (15224): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Sonntag, der zwölfter Juli 2026. Die aktuelle Uhrzeit ist 20:02. Draußen sind es aktuell 26 Grad bei klarem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(15224): register: id=23b0000032e, handle=0xb40000710e3d81a0, importpid=15224
D/mali_gralloc(15224): register: id=23b0000032e, handle=0xb40000710e3d8280, importpid=15224
D/mali_gralloc(15224): unregister: id=23b0000032e, handle=0xb40000710e3d8280, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b0000032f, handle=0xb40000710e3d8280, importpid=15224
D/mali_gralloc(15224): register: id=23b0000032f, handle=0xb40000710e3d8360, importpid=15224
D/mali_gralloc(15224): unregister: id=23b0000032f, handle=0xb40000710e3d8360, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000330, handle=0xb40000710e3d8360, importpid=15224
D/mali_gralloc(15224): register: id=23b00000330, handle=0xb40000710e3d8440, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000330, handle=0xb40000710e3d8440, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000331, handle=0xb40000710e3d8440, importpid=15224
D/mali_gralloc(15224): register: id=23b00000331, handle=0xb40000710e3d8520, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000331, handle=0xb40000710e3d8520, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000332, handle=0xb40000710e3d8520, importpid=15224
D/mali_gralloc(15224): register: id=23b00000332, handle=0xb40000710e3d8600, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000332, handle=0xb40000710e3d8600, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000333, handle=0xb400007167ac0ee0, importpid=15224
I/mple.jarvis_app(15224): Background concurrent mark compact GC freed 3197KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 3171KB/6343KB, paused 428us,6.166ms total 100.321ms
I/Choreographer(15224): Skipped 41 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(15224): register: id=23b0000033a, handle=0xb40000710e3da040, importpid=15224
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/HWUI    (15224): Davey! duration=714ms; Flags=0, FrameTimelineVsyncId=943307, IntendedVsync=18755689382045, Vsync=18756372371689, InputEventId=0, HandleInputStart=18756373365968, AnimationStart=18756373368775, PerformTraversalsStart=18756373370468, DrawStart=18756374439583, FrameDeadline=18755705382045, FrameInterval=18756372680237, FrameStartTime=16658284, SyncQueued=18756374616314, SyncStart=18756375913275, IssueDrawCommandsStart=18756395300698, SwapBuffers=18756403650045, FrameCompleted=18756405302968, DequeueBufferDuration=5584692, QueueBufferDuration=269423, GpuCompleted=18756405302968, SwapBuffersCompleted=18756403999083, DisplayPresentTime=-4294967295, CommandSubmissionCompleted=18756403650045, 
D/TTS     (15224): Utterance ID has started: 8a8e7950-ee2a-4d07-835f-7e1c2377969f
D/TTS     (15224): Utterance ID has completed: 8a8e7950-ee2a-4d07-835f-7e1c2377969f
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/VRI[MainActivity](15224): visibilityChanged oldVisibility=true newVisibility=false
D/mali_gralloc(15224): unregister: id=23b00000331, handle=0xb40000710e3d8440, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000332, handle=0xb40000710e3d8520, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b0000033a, handle=0xb40000710e3da040, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000333, handle=0xb400007167ac0ee0, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b0000032e, handle=0xb40000710e3d81a0, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b00000330, handle=0xb40000710e3d8360, base=0x0, importpid=15224, clone_count=0
D/mali_gralloc(15224): unregister: id=23b0000032f, handle=0xb40000710e3d8280, base=0x0, importpid=15224, clone_count=0
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.paused
D/JARVIS_WS(15224): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Sonntag, der zwölfter Juli 2026. Die aktuelle Uhrzeit ist 20:06. Draußen sind es aktuell 26 Grad bei klarem Himmel. Du hast aktuell keine anstehenden Termine."}
D/JARVIS_EVENT(15224): Node-RED Event wird verarbeitet
W/178.47:1880/...(15224): type=1400 audit(0.0:18308): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c241,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
W/libc    (15224): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(15224): WakeLock aktiviert
D/JARVIS_BRIDGE(15224): openAndDeliverEvent
D/JARVIS_BRIDGE(15224): Intent Event empfangen
D/JARVIS_BRIDGE(15224): Gepuffertes Event wird gesendet
I/flutter (15224): [JARVIS BRIDGE] backgroundEvent
I/flutter (15224): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Sonntag, der zwölfter Juli 2026. Die aktuelle Uhrzeit ist 20:06. Draußen sind es aktuell 26 Grad bei klarem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (15224): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Sonntag, der zwölfter Juli 2026. Die aktuelle Uhrzeit ist 20:06. Draußen sind es aktuell 26 Grad bei klarem Himmel. Du hast aktuell keine anstehenden Termine."}
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.hidden
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.inactive
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(15224): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(15224): register: id=23b00000350, handle=0xb40000710e3d80c0, importpid=15224
D/mali_gralloc(15224): register: id=23b00000350, handle=0xb40000710e3d81a0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000350, handle=0xb40000710e3d81a0, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000351, handle=0xb40000710e3d8360, importpid=15224
D/mali_gralloc(15224): register: id=23b00000351, handle=0xb40000710e3d8440, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000351, handle=0xb40000710e3d8440, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000352, handle=0xb40000710e3d8440, importpid=15224
D/mali_gralloc(15224): register: id=23b00000352, handle=0xb40000710e3d8520, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000352, handle=0xb40000710e3d8520, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000353, handle=0xb40000710e3d8520, importpid=15224
D/mali_gralloc(15224): register: id=23b00000353, handle=0xb40000710e3d8600, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000353, handle=0xb40000710e3d8600, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000354, handle=0xb40000710e3d8600, importpid=15224
D/mali_gralloc(15224): register: id=23b00000354, handle=0xb40000710e3d87c0, importpid=15224
D/mali_gralloc(15224): unregister: id=23b00000354, handle=0xb40000710e3d87c0, base=0x0, importpid=15224, clone_count=1
D/mali_gralloc(15224): register: id=23b00000355, handle=0xb40000716eab21e0, importpid=15224
D/FlutterJNI(15224): Sending viewport metrics to the engine.
D/mali_gralloc(15224): register: id=23b00000356, handle=0xb40000710e3da2e0, importpid=15224
I/flutter (15224): [Jarvis] Lifecycle: AppLifecycleState.resumed
D/TTS     (15224): Utterance ID has started: f2bd791c-eb69-43fc-b886-3a863823ea41
D/TTS     (15224): Utterance ID has completed: f2bd791c-eb69-43fc-b886-3a863823ea41
