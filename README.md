PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             19,4s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,6s
I/FlutterActivityAndFragmentDelegate(32334): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(32334): Beginning load of flutter...
D/FlutterJNI(32334): flutter (null) was loaded normally!
I/flutter (32334): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(32334): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              158ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:50122/i4xxeoTNgXs=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:50122/i4xxeoTNgXs=/devtools/?uri=ws://127.0.0.1:50122/i4xxeoTNgXs=/ws
D/FlutterRenderer(32334): Width is zero. 0,0
I/mple.jarvis_app(32334): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(32334): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x31bcec91148d3289
I/UnisocBufferQueueHelper(32334): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006e0b15f780, size:88
I/mple.jarvis_app(32334): createUnisocBufferQueueHelperFactory success, get instance 0xb400006e0b15f780
I/mple.jarvis_app(32334): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f25c3bd80, size:296, enable:0
I/mple.jarvis_app(32334): createUnisocFrameRecordFactory success, get instance 0xb400006f25c3bd80
D/FlutterJNI(32334): Sending viewport metrics to the engine.
W/libc    (32334): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(32334): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(32334): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(32334): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(32334): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(32334): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(32334): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(32334): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(32334): register: id=23b00000b2a, handle=0xb400006f25c05160, importpid=32334
W/libc    (32334): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(32334): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc(32334): register: id=23b00000b2a, handle=0xb400006f25c054e0, importpid=32334
D/mali_gralloc(32334): unregister: id=23b00000b2a, handle=0xb400006f25c054e0, base=0x0, importpid=32334, clone_count=1
D/mali_gralloc(32334): register: id=23b00000b2b, handle=0xb400006f25c054e0, importpid=32334
D/mali_gralloc(32334): register: id=23b00000b2b, handle=0xb400006f25c055c0, importpid=32334
D/mali_gralloc(32334): unregister: id=23b00000b2b, handle=0xb400006f25c055c0, base=0x0, importpid=32334, clone_count=1
D/mali_gralloc(32334): register: id=23b00000b2c, handle=0xb400006f25c055c0, importpid=32334
D/mali_gralloc(32334): register: id=23b00000b2c, handle=0xb400006f25c056a0, importpid=32334
D/mali_gralloc(32334): unregister: id=23b00000b2c, handle=0xb400006f25c056a0, base=0x0, importpid=32334, clone_count=1
D/mali_gralloc(32334): register: id=23b00000b2d, handle=0xb400006f25c056a0, importpid=32334
D/mali_gralloc(32334): register: id=23b00000b2d, handle=0xb400006f25c05780, importpid=32334
D/mali_gralloc(32334): unregister: id=23b00000b2d, handle=0xb400006f25c05780, base=0x0, importpid=32334, clone_count=1
D/mali_gralloc(32334): register: id=23b00000b2e, handle=0xb400006f25c05780, importpid=32334
D/mali_gralloc(32334): register: id=23b00000b2e, handle=0xb400006f25c05860, importpid=32334
D/mali_gralloc(32334): unregister: id=23b00000b2e, handle=0xb400006f25c05860, base=0x0, importpid=32334, clone_count=1
W/Choreographer(32334): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(32334): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(32334): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(32334): Connected to TTS engine
I/TextToSpeech(32334): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(32334): Listening gestartet
D/JARVIS_SERVICE(32334): Foreground Service läuft
D/JARVIS_WS(32334): WebSocket verbunden
I/Choreographer(32334): Skipped 73 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(32334): register: id=23b00000b2f, handle=0xb400006e03d51040, importpid=32334
I/HWUI    (32334): Davey! duration=1254ms; Flags=1, FrameTimelineVsyncId=5939013, IntendedVsync=29820033895668, Vsync=29821250562359, InputEventId=0, HandleInputStart=29821260143246, AnimationStart=29821260149131, PerformTraversalsStart=29821260151631, DrawStart=29821266103400, FrameDeadline=29820050562335, FrameInterval=29821258584284, FrameStartTime=16666667, SyncQueued=29821269877938, SyncStart=29821270020323, IssueDrawCommandsStart=29821271044746, SwapBuffers=29821286775592, FrameCompleted=29821288762977, DequeueBufferDuration=3248461, QueueBufferDuration=1747384, GpuCompleted=29821287608938, SwapBuffersCompleted=29821288762977, DisplayPresentTime=7083992225261320037, CommandSubmissionCompleted=29821286775592, 
D/ProfileInstaller(32334): Installing profile for com.example.jarvis_app
D/JARVIS_TTS(32334): Android TTS bereit
D/FlutterJNI(32334): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD(32334): Bereit für Wakeword
D/JARVIS_WAKEWORD(32334): Sprache erkannt
D/JARVIS_WAKEWORD(32334): Sprachende
D/JARVIS_WAKEWORD(32334): Fehler: 7
D/JARVIS_WAKEWORD(32334): Listening gestartet
D/JARVIS_WAKEWORD(32334): Bereit für Wakeword
D/JARVIS_WAKEWORD(32334): Sprache erkannt
D/JARVIS_WAKEWORD(32334): Sprachende
D/JARVIS_WAKEWORD(32334): Fehler: 7
D/JARVIS_WAKEWORD(32334): Listening gestartet
D/JARVIS_WAKEWORD(32334): Bereit für Wakeword
D/JARVIS_WAKEWORD(32334): Sprache erkannt
D/JARVIS_WAKEWORD(32334): Sprachende
D/JARVIS_WAKEWORD(32334): Erkannt: okay jarvis
D/JARVIS_WAKEWORD(32334): Wakeword erkannt
W/libc    (32334): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(32334): type=1400 audit(0.0:21069): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(32334): WakeLock aktiviert
D/JARVIS_WAKEWORD(32334): sendWakewordToFlutter
I/flutter (32334): [JARVIS BRIDGE] wakewordDetected
I/flutter (32334): [JARVIS BRIDGE] null
I/flutter (32334): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (32334): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
W/mple.jarvis_app(32334): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(32334): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(32334): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(32334): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter (32334): [JARVIS] Wakeword Trigger empfangen
I/flutter (32334): [JARVIS] Controller State: JarvisState.idle
I/flutter (32334): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(32334): Wakeword STOP
D/mali_gralloc(32334): register: id=23b00000b38, handle=0xb400006f20d573c0, importpid=32334
I/flutter (32334): [JARVIS] Wakeword gestoppt
I/flutter (32334): [VOICE] listen() wird gestartet
I/flutter (32334): [VOICE] verfügbar: true
I/flutter (32334): [VOICE] SpeechToText aktiv
I/flutter (32334): [JARVIS] startListening verlassen
I/flutter (32334): [VOICE] Ergebnis:  | final=false
I/flutter (32334): [VOICE] Ergebnis:  | final=false
I/flutter (32334): [VOICE] Ergebnis:  | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl mir | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl mir was | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl mir was | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl mir was zum | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl mir was zum Licht | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähl mir was zum Licht | final=true
D/TTS     (32334): Utterance ID has started: 093df279-25dd-48aa-befe-836fea58e3c7
D/TTS     (32334): Utterance ID has completed: 093df279-25dd-48aa-befe-836fea58e3c7
D/JARVIS_WAKEWORD(32334): Mikrofon gehört Flutter
D/JARVIS_WAKEWORD(32334): Wakeword STOP
I/flutter (32334): [JARVIS] Wakeword gestoppt
I/flutter (32334): [VOICE] listen() wird gestartet
I/flutter (32334): [VOICE] verfügbar: true
I/flutter (32334): [VOICE] SpeechToText aktiv
I/flutter (32334): [JARVIS] startListening verlassen
I/flutter (32334): [VOICE] Ergebnis:  | final=false
I/flutter (32334): [VOICE] Ergebnis:  | final=false
I/flutter (32334): [VOICE] Ergebnis:  | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir was | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir was zum | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir was zum Licht | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir was zum Licht | final=false
I/flutter (32334): [VOICE] Ergebnis: erzähle mir was zum Licht | final=true
D/TTS     (32334): Utterance ID has started: d8834e7d-59c2-48a0-ae6c-ff807f356b80
D/TTS     (32334): Utterance ID has completed: d8834e7d-59c2-48a0-ae6c-ff807f356b80
D/JARVIS_WAKEWORD(32334): Mikrofon gehört Flutter
