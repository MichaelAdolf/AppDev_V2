PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             21,3s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           7,1s
I/FlutterActivityAndFragmentDelegate(10095): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(10095): Beginning load of flutter...
D/FlutterJNI(10095): flutter (null) was loaded normally!
I/flutter (10095): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(10095): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              153ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:57785/b9j-yaQKexY=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:57785/b9j-yaQKexY=/devtools/?uri=ws://127.0.0.1:57785/b9j-yaQKexY=/ws
D/FlutterRenderer(10095): Width is zero. 0,0
I/mple.jarvis_app(10095): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(10095): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x997fe683ff8e3213
I/UnisocBufferQueueHelper(10095): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb4000076ff4de540, size:88
I/mple.jarvis_app(10095): createUnisocBufferQueueHelperFactory success, get instance 0xb4000076ff4de540
I/mple.jarvis_app(10095): Unisoc-Graphics: UnisocFrameRecord create, this:0xb40000769a4573c0, size:296, enable:0
I/mple.jarvis_app(10095): createUnisocFrameRecordFactory success, get instance 0xb40000769a4573c0
D/FlutterJNI(10095): Sending viewport metrics to the engine.
W/libc    (10095): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(10095): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(10095): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(10095): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(10095): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(10095): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(10095): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(10095): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(10095): register: id=234000003da, handle=0xb4000076ff438940, importpid=10095
W/libc    (10095): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(10095): initIonKernelMemtrack open devices:/dev/systemheap success, fd:210
D/mali_gralloc(10095): register: id=234000003da, handle=0xb4000076ff438cc0, importpid=10095
D/mali_gralloc(10095): unregister: id=234000003da, handle=0xb4000076ff438cc0, base=0x0, importpid=10095, clone_count=1
D/mali_gralloc(10095): register: id=234000003db, handle=0xb4000076ff438cc0, importpid=10095
D/mali_gralloc(10095): register: id=234000003db, handle=0xb4000076ff438da0, importpid=10095
D/mali_gralloc(10095): unregister: id=234000003db, handle=0xb4000076ff438da0, base=0x0, importpid=10095, clone_count=1
D/mali_gralloc(10095): register: id=234000003dc, handle=0xb4000076ff438da0, importpid=10095
D/mali_gralloc(10095): register: id=234000003dc, handle=0xb4000076ff438e80, importpid=10095
D/mali_gralloc(10095): unregister: id=234000003dc, handle=0xb4000076ff438e80, base=0x0, importpid=10095, clone_count=1
D/mali_gralloc(10095): register: id=234000003dd, handle=0xb4000076ff438e80, importpid=10095
D/mali_gralloc(10095): register: id=234000003dd, handle=0xb4000076ff438f60, importpid=10095
D/mali_gralloc(10095): unregister: id=234000003dd, handle=0xb4000076ff438f60, base=0x0, importpid=10095, clone_count=1
D/mali_gralloc(10095): register: id=234000003de, handle=0xb4000076ff438f60, importpid=10095
D/mali_gralloc(10095): register: id=234000003de, handle=0xb4000076ff439040, importpid=10095
D/mali_gralloc(10095): unregister: id=234000003de, handle=0xb4000076ff439040, base=0x0, importpid=10095, clone_count=1
W/Choreographer(10095): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(10095): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(10095): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(10095): Connected to TTS engine
I/TextToSpeech(10095): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(10095): Listening gestartet
D/JARVIS_SERVICE(10095): Foreground Service läuft
I/Choreographer(10095): Skipped 60 frames!  The application may be doing too much work on its main thread.
D/JARVIS_WS(10095): WebSocket verbunden
D/mali_gralloc(10095): register: id=234000003df, handle=0xb4000075d4cc3400, importpid=10095
I/HWUI    (10095): Davey! duration=1025ms; Flags=1, FrameTimelineVsyncId=2842908, IntendedVsync=16030006541001, Vsync=16031006541021, InputEventId=0, HandleInputStart=16031009420263, AnimationStart=16031009424879, PerformTraversalsStart=16031009427417, DrawStart=16031014716956, FrameDeadline=16030023207668, FrameInterval=16031008814686, FrameStartTime=16666667, SyncQueued=16031018197686, SyncStart=16031018290686, IssueDrawCommandsStart=16031019231456, SwapBuffers=16031030719186, FrameCompleted=16031031859956, DequeueBufferDuration=1587692, QueueBufferDuration=890038, GpuCompleted=16031031859956, SwapBuffersCompleted=16031031797956, DisplayPresentTime=8030591510791615077, CommandSubmissionCompleted=16031030719186, 
D/JARVIS_TTS(10095): Android TTS bereit
D/FlutterJNI(10095): Sending viewport metrics to the engine.
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
D/ProfileInstaller(10095): Installing profile for com.example.jarvis_app
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/mple.jarvis_app(10095): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(10095): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(10095): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(10095): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD(10095): Fehler: 7
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
I/flutter (10095): [JARVIS] Audio Mode: AudioOutputMode.remote
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Erkannt: hey jarvis
D/JARVIS_WAKEWORD(10095): Wakeword erkannt
W/libc    (10095): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(10095): type=1400 audit(0.0:18114): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(10095): WakeLock aktiviert
D/JARVIS_WAKEWORD(10095): sendWakewordToFlutter
I/flutter (10095): [JARVIS BRIDGE] wakewordDetected
I/flutter (10095): [JARVIS BRIDGE] null
I/flutter (10095): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (10095): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (10095): [JARVIS] Wakeword Trigger empfangen
I/flutter (10095): [JARVIS] Controller State: JarvisState.idle
I/flutter (10095): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(10095): Wakeword STOP
D/mali_gralloc(10095): register: id=23400000410, handle=0xb4000076f91269a0, importpid=10095
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [JARVIS] Wakeword gestoppt
I/flutter (10095): [VOICE] listen() wird gestartet
I/flutter (10095): [VOICE] verfügbar: true
I/flutter (10095): [VOICE] SpeechToText aktiv
I/flutter (10095): [JARVIS] startListening verlassen
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [VOICE] Ergebnis:  | final=false
I/flutter (10095): [VOICE] Ergebnis:  | final=false
I/flutter (10095): [VOICE] Ergebnis:  | final=false
I/flutter (10095): [VOICE] Ergebnis: gib | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir die | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir die | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir die | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir die | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir die tagesinformation | final=false
I/flutter (10095): [VOICE] Ergebnis: gib mir die tagesinformation | final=false
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [VOICE] Ergebnis: gib mir die tagesinformation | final=true
D/JARVIS_WS(10095): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:18. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT(10095): Node-RED Event wird verarbeitet
W/libc    (10095): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(10095): type=1400 audit(0.0:18115): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(10095): WakeLock aktiviert
D/JARVIS_TTS(10095): Sprache: Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:18. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT(10095): Activity wird geöffnet
D/JARVIS_BRIDGE(10095): openAndDeliverEvent
D/JARVIS_BRIDGE(10095): Bridge Activity in Vordergrund
I/flutter (10095): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter (10095): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (10095): [Jarvis] App resumed -> voice neu initialisieren
I/flutter (10095): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE(10095): Intent Event empfangen
D/JARVIS_BRIDGE(10095): Gepuffertes Event wird gesendet
I/flutter (10095): [JARVIS BRIDGE] backgroundEvent
I/flutter (10095): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:18. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter (10095): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:18. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter (10095): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (10095): [Jarvis] App resumed -> voice neu initialisieren
D/JARVIS_WAKEWORD(10095): Listening gestartet
D/FlutterJNI(10095): Sending viewport metrics to the engine.
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Erkannt: guten abend heute ist donnerstag der 23 juli 2026 die aktuelle uhrzeit ist 22:18 uhr
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
I/flutter (10095): [JARVIS] Audio Mode: AudioOutputMode.local
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Fehler: 7
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Erkannt: hey jarvis
D/JARVIS_WAKEWORD(10095): Wakeword erkannt
W/libc    (10095): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(10095): type=1400 audit(0.0:18118): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(10095): WakeLock aktiviert
D/JARVIS_WAKEWORD(10095): sendWakewordToFlutter
I/flutter (10095): [JARVIS BRIDGE] wakewordDetected
I/flutter (10095): [JARVIS BRIDGE] null
I/flutter (10095): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (10095): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (10095): [JARVIS] Wakeword Trigger empfangen
I/flutter (10095): [JARVIS] Controller State: JarvisState.idle
I/flutter (10095): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(10095): Wakeword STOP
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [JARVIS] Wakeword gestoppt
I/flutter (10095): [VOICE] listen() wird gestartet
I/flutter (10095): [VOICE] verfügbar: true
I/flutter (10095): [VOICE] SpeechToText aktiv
I/flutter (10095): [JARVIS] startListening verlassen
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [JARVIS] Audio Mode: AudioOutputMode.remote
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Erkannt: hey jarvis
D/JARVIS_WAKEWORD(10095): Wakeword erkannt
W/libc    (10095): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(10095): type=1400 audit(0.0:18119): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(10095): WakeLock aktiviert
D/JARVIS_WAKEWORD(10095): sendWakewordToFlutter
I/flutter (10095): [JARVIS BRIDGE] wakewordDetected
I/flutter (10095): [JARVIS BRIDGE] null
I/flutter (10095): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (10095): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (10095): [JARVIS] Wakeword Trigger empfangen
I/flutter (10095): [JARVIS] Controller State: JarvisState.idle
I/flutter (10095): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(10095): Wakeword STOP
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [JARVIS] Wakeword gestoppt
I/flutter (10095): [VOICE] listen() wird gestartet
I/flutter (10095): [VOICE] verfügbar: true
I/flutter (10095): [VOICE] SpeechToText aktiv
I/flutter (10095): [JARVIS] startListening verlassen
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (10095): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(10095): Listening gestartet
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Bereit für Wakeword
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Sprache erkannt
D/JARVIS_WAKEWORD(10095): Sprachende
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(10095): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(10095): Erkannt: hey jarvis
D/JARVIS_WAKEWORD(10095): Wakeword erkannt
