PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             31,7s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,9s
I/FlutterActivityAndFragmentDelegate(14053): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(14053): Beginning load of flutter...
D/FlutterJNI(14053): flutter (null) was loaded normally!
I/flutter (14053): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(14053): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              126ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:54607/30M6_jb9yFo=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:54607/30M6_jb9yFo=/devtools/?uri=ws://127.0.0.1:54607/30M6_jb9yFo=/ws
I/mple.jarvis_app(14053): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer(14053): Width is zero. 0,0
I/mple.jarvis_app(14053): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x8d88d2ad130c8c45
I/UnisocBufferQueueHelper(14053): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb4000076ff3705c0, size:88
I/mple.jarvis_app(14053): createUnisocBufferQueueHelperFactory success, get instance 0xb4000076ff3705c0
I/mple.jarvis_app(14053): Unisoc-Graphics: UnisocFrameRecord create, this:0xb4000076ff59c3c0, size:296, enable:0
I/mple.jarvis_app(14053): createUnisocFrameRecordFactory success, get instance 0xb4000076ff59c3c0
D/FlutterJNI(14053): Sending viewport metrics to the engine.
W/libc    (14053): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(14053): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(14053): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(14053): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(14053): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(14053): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(14053): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(14053): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(14053): register: id=234000005c2, handle=0xb4000076ff24e780, importpid=14053
W/libc    (14053): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(14053): initIonKernelMemtrack open devices:/dev/systemheap success, fd:211
D/mali_gralloc(14053): register: id=234000005c2, handle=0xb4000076ff24eb00, importpid=14053
D/mali_gralloc(14053): unregister: id=234000005c2, handle=0xb4000076ff24eb00, base=0x0, importpid=14053, clone_count=1
D/mali_gralloc(14053): register: id=234000005c3, handle=0xb4000076ff24eb00, importpid=14053
D/mali_gralloc(14053): register: id=234000005c3, handle=0xb4000076ff24ebe0, importpid=14053
D/mali_gralloc(14053): unregister: id=234000005c3, handle=0xb4000076ff24ebe0, base=0x0, importpid=14053, clone_count=1
D/mali_gralloc(14053): register: id=234000005c4, handle=0xb4000076ff24ebe0, importpid=14053
D/mali_gralloc(14053): register: id=234000005c4, handle=0xb4000076ff24ecc0, importpid=14053
D/mali_gralloc(14053): unregister: id=234000005c4, handle=0xb4000076ff24ecc0, base=0x0, importpid=14053, clone_count=1
D/mali_gralloc(14053): register: id=234000005c5, handle=0xb4000076ff24ecc0, importpid=14053
D/mali_gralloc(14053): register: id=234000005c5, handle=0xb4000076ff24eda0, importpid=14053
D/mali_gralloc(14053): unregister: id=234000005c5, handle=0xb4000076ff24eda0, base=0x0, importpid=14053, clone_count=1
D/mali_gralloc(14053): register: id=234000005c6, handle=0xb4000076ff24eda0, importpid=14053
D/mali_gralloc(14053): register: id=234000005c6, handle=0xb4000076ff24ee80, importpid=14053
D/mali_gralloc(14053): unregister: id=234000005c6, handle=0xb4000076ff24ee80, base=0x0, importpid=14053, clone_count=1
W/Choreographer(14053): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech(14053): Sucessfully bound to com.google.android.tts
D/JARVIS_WS(14053): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech(14053): Connected to TTS engine
I/TextToSpeech(14053): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/JARVIS_SERVICE(14053): Foreground Service läuft
I/Choreographer(14053): Skipped 67 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc(14053): register: id=234000005c7, handle=0xb4000075d7d20780, importpid=14053
I/HWUI    (14053): Davey! duration=1164ms; Flags=1, FrameTimelineVsyncId=3231793, IntendedVsync=16901718050001, Vsync=16902834716690, InputEventId=0, HandleInputStart=16902837995640, AnimationStart=16902838000909, PerformTraversalsStart=16902838003678, DrawStart=16902844641255, FrameDeadline=16901734716668, FrameInterval=16902837100447, FrameStartTime=16666667, SyncQueued=16902848312794, SyncStart=16902848661255, IssueDrawCommandsStart=16902849459217, SwapBuffers=16902881271024, FrameCompleted=16902882485255, DequeueBufferDuration=1459423, QueueBufferDuration=679346, GpuCompleted=16902882485255, SwapBuffersCompleted=16902882124640, DisplayPresentTime=72904454231491824, CommandSubmissionCompleted=16902881271024, 
D/JARVIS_TTS(14053): Android TTS bereit
D/FlutterJNI(14053): Sending viewport metrics to the engine.
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/ProfileInstaller(14053): Installing profile for com.example.jarvis_app
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WS(14053): WebSocket verbunden
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/mple.jarvis_app(14053): Background concurrent mark compact GC freed 10MB AllocSpace bytes, 3(60KB) LOS objects, 49% free, 2970KB/5941KB, paused 879us,6.933ms total 66.225ms
W/mple.jarvis_app(14053): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app(14053): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app(14053): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app(14053): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD(14053): Erkannt: okay schatz
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: okay jarvis
D/JARVIS_WAKEWORD(14053): Wakeword erkannt
W/libc    (14053): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(14053): type=1400 audit(0.0:18168): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14053): WakeLock aktiviert
D/JARVIS_WAKEWORD(14053): sendWakewordToFlutter
I/flutter (14053): [JARVIS BRIDGE] wakewordDetected
I/flutter (14053): [JARVIS BRIDGE] null
I/flutter (14053): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14053): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (14053): [JARVIS] Wakeword Trigger empfangen
I/flutter (14053): [JARVIS] Controller State: JarvisState.idle
I/flutter (14053): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(14053): Wakeword STOP
D/mali_gralloc(14053): register: id=234000005cc, handle=0xb4000076f9022f20, importpid=14053
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [JARVIS] Wakeword gestoppt
I/flutter (14053): [VOICE] listen() wird gestartet
I/flutter (14053): [VOICE] verfügbar: true
I/flutter (14053): [VOICE] SpeechToText aktiv
I/flutter (14053): [JARVIS] startListening verlassen
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [VOICE] Ergebnis:  | final=false
I/flutter (14053): [VOICE] Ergebnis:  | final=false
I/flutter (14053): [VOICE] Ergebnis: sage | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir tagesinformation | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir tagesinformation | final=false
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [VOICE] Ergebnis: sage mir tagesinformation | final=true
D/JARVIS_WS(14053): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:31. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT(14053): Node-RED Event wird verarbeitet
W/libc    (14053): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(14053): type=1400 audit(0.0:18169): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14053): WakeLock aktiviert
D/JARVIS_EVENT(14053): Activity wird geöffnet
D/JARVIS_BRIDGE(14053): openAndDeliverEvent
D/JARVIS_BRIDGE(14053): Bridge Activity in Vordergrund
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (14053): [Jarvis] App resumed -> voice neu initialisieren
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE(14053): Intent Event empfangen
D/JARVIS_BRIDGE(14053): Gepuffertes Event wird gesendet
I/flutter (14053): [JARVIS BRIDGE] backgroundEvent
I/flutter (14053): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:31. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter (14053): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:31. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (14053): [Jarvis] App resumed -> voice neu initialisieren
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/FlutterJNI(14053): Sending viewport metrics to the engine.
I/flutter (14053): [JARVIS] MODE=AudioOutputMode.local
I/flutter (14053): [JARVIS] RESPONSE=Instance of 'HaResponse'
I/flutter (14053): [JARVIS] AUDIOURL=http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/TTS     (14053): Utterance ID has started: 6db651e2-1827-46f7-a4f4-9a393aaa614a
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Sprache erkannt
I/flutter (14053): [JARVIS] Audio Mode: AudioOutputMode.remote
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: guten abend heute ist donnerstag der 23 juli 2026
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Fehler: 7
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
I/mple.jarvis_app(14053): Background concurrent mark compact GC freed 3015KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 3022KB/6045KB, paused 669us,5.465ms total 34.213ms
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Fehler: 7
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/TTS     (14053): Utterance ID has completed: 6db651e2-1827-46f7-a4f4-9a393aaa614a
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Fehler: 7
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: okay jarvis
D/JARVIS_WAKEWORD(14053): Wakeword erkannt
W/mple.jarvis_app(14053): type=1400 audit(0.0:18171): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
W/libc    (14053): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE(14053): WakeLock aktiviert
D/JARVIS_WAKEWORD(14053): sendWakewordToFlutter
I/flutter (14053): [JARVIS BRIDGE] wakewordDetected
I/flutter (14053): [JARVIS BRIDGE] null
I/flutter (14053): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14053): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (14053): [JARVIS] Wakeword Trigger empfangen
I/flutter (14053): [JARVIS] Controller State: JarvisState.idle
I/flutter (14053): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(14053): Wakeword STOP
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [JARVIS] Wakeword gestoppt
I/flutter (14053): [VOICE] listen() wird gestartet
I/flutter (14053): [VOICE] verfügbar: true
I/flutter (14053): [VOICE] SpeechToText aktiv
I/flutter (14053): [JARVIS] startListening verlassen
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [VOICE] Ergebnis:  | final=false
I/flutter (14053): [VOICE] Ergebnis:  | final=false
I/flutter (14053): [VOICE] Ergebnis: sage | final=false
I/flutter (14053): [VOICE] Ergebnis: sage | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir | final=false
I/flutter (14053): [VOICE] Ergebnis: sage mir tagesinformationen | final=false
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [VOICE] Ergebnis: sage mir tagesinformationen | final=true
D/JARVIS_WS(14053): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:32. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT(14053): Node-RED Event wird verarbeitet
W/libc    (14053): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...(14053): type=1400 audit(0.0:18173): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14053): WakeLock aktiviert
D/JARVIS_EVENT(14053): Activity wird geöffnet
D/JARVIS_BRIDGE(14053): openAndDeliverEvent
D/JARVIS_BRIDGE(14053): Bridge Activity in Vordergrund
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (14053): [Jarvis] App resumed -> voice neu initialisieren
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE(14053): Intent Event empfangen
D/JARVIS_BRIDGE(14053): Gepuffertes Event wird gesendet
I/flutter (14053): [JARVIS BRIDGE] backgroundEvent
I/flutter (14053): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:32. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter (14053): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:32. Draußen sind es aktuell 17 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter (14053): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter (14053): [Jarvis] App resumed -> voice neu initialisieren
D/JARVIS_WAKEWORD(14053): Listening gestartet
I/flutter (14053): [JARVIS] MODE=AudioOutputMode.remote
I/flutter (14053): [JARVIS] RESPONSE=Instance of 'HaResponse'
I/flutter (14053): [JARVIS] AUDIOURL=http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
I/flutter (14053): [JARVIS] REMOTE Audio: http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
I/flutter (14053): [JARVIS] Remotebranch enter
D/FlutterJNI(14053): Sending viewport metrics to the engine.
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
I/ExoPlayerImpl(14053): Init 1c265c9 [AndroidXMedia3/1.4.1] [serenity, 25028RN03Y, Xiaomi, 35]
I/mple.jarvis_app(14053): hiddenapi: Accessing hidden method Landroid/media/AudioTrack;->getLatency()I (runtime_flags=0, domain=platform, api=unsupported) from Landroidx/media3/exoplayer/audio/AudioTrackPositionTracker; (domain=app) using reflection: allowed
W/AudioCapabilities(14053): Unsupported mime audio/ima-adpcm
W/AudioCapabilities(14053): Unsupported mime audio/mpeg-L1
W/AudioCapabilities(14053): Unsupported mime audio/mpeg-L2
W/VideoCapabilities(14053): Unsupported mime video/jpeg
W/VideoCapabilities(14053): Unsupported mime video/jpeg
I/DMCodecAdapterFactory(14053): Creating an asynchronous MediaCodec adapter for track type audio
W/libc    (14053): Access denied finding property "persist.unipnp.video_mediacodec_fps_upload.enabled"
W/ExoPlayer:Playb(14053): type=1400 audit(0.0:18174): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/CCodec  (14053): allocate(c2.unisoc.mp3.decoder)
I/Codec2-HalSelection(14053): selection: hidl
I/Codec2Client(14053): Available Codec2 services: "default" "software"
I/Codec2-HalSelection(14053): selection: hidl
I/CCodec  (14053): setting up 'default' as default (vendor) store
I/Codec2-HalSelection(14053): selection: hidl
I/CCodec  (14053): Created component [c2.unisoc.mp3.decoder]
D/CCodecConfig(14053): read media type: audio/mpeg
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: algo.buffers.max-count.values
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: output.subscribed-indices.values
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: input.buffers.allocator-ids.values
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: output.buffers.allocator-ids.values
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: algo.buffers.allocator-ids.values
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: output.buffers.pool-ids.values
D/ReflectedParamUpdater(14053): extent() != 1 for single value type: algo.buffers.pool-ids.values
I/CCodecConfig(14053): query failed after returning 9 values (BAD_INDEX)
D/CCodecConfig(14053): c2 config diff is Dict {
D/CCodecConfig(14053):   c2::i32 algo.priority.value = -1
D/CCodecConfig(14053):   c2::float algo.rate.value = -1
D/CCodecConfig(14053):   c2::u32 coded.bitrate.value = 64000
D/CCodecConfig(14053):   c2::u32 input.buffers.max-size.value = 8192
D/CCodecConfig(14053):   c2::u32 input.delay.value = 0
D/CCodecConfig(14053):   string input.media-type.value = "audio/mpeg"
D/CCodecConfig(14053):   string output.media-type.value = "audio/raw"
D/CCodecConfig(14053):   c2::u32 raw.channel-count.value = 2
D/CCodecConfig(14053):   c2::u32 raw.sample-rate.value = 44100
D/CCodecConfig(14053): }
I/MediaCodec(14053): MediaCodec will operate in async mode
D/CCodec  (14053): [c2.unisoc.mp3.decoder] buffers are bound to CCodec for this session
D/CCodecConfig(14053): no c2 equivalents for log-session-id
D/CCodecConfig(14053): no c2 equivalents for importance
D/CCodecConfig(14053): no c2 equivalents for flags
D/CCodecConfig(14053): config failed => CORRUPTED
D/CCodecConfig(14053): c2 config diff is   c2::i32 algo.priority.value = 0
D/CCodecConfig(14053):   c2::u32 raw.channel-count.value = 1
D/CCodecConfig(14053):   c2::u32 raw.sample-rate.value = 22050
W/Codec2Client(14053): query -- param skipped: index = 1107298332.
D/CCodec  (14053): client requested max input size 4096, which is smaller than what component recommended (8192); overriding with component recommendation.
W/CCodec  (14053): This behavior is subject to change. It is recommended that app developers double check whether the requested max input size is in reasonable range.
D/CCodec  (14053): encoding statistics level = 0
D/CCodec  (14053): setup formats input: AMessage(what = 0x00000000) = {
D/CCodec  (14053):   int32_t bitrate = 64000
D/CCodec  (14053):   int32_t channel-count = 1
D/CCodec  (14053):   int32_t max-input-size = 8192
D/CCodec  (14053):   string mime = "audio/mpeg"
D/CCodec  (14053):   int32_t priority = 0
D/CCodec  (14053):   int32_t sample-rate = 22050
D/CCodec  (14053): }
D/CCodec  (14053): setup formats output: AMessage(what = 0x00000000) = {
D/CCodec  (14053):   int32_t channel-count = 1
D/CCodec  (14053):   string mime = "audio/raw"
D/CCodec  (14053):   int32_t priority = 0
D/CCodec  (14053):   int32_t sample-rate = 22050
D/CCodec  (14053):   int32_t android._config-pcm-encoding = 2
D/CCodec  (14053): }
I/CCodecConfig(14053): query failed after returning 9 values (BAD_INDEX)
D/MediaCodec(14053): keep callback message for reclaim
W/AString (14053): ctor got NULL, using empty string instead
W/Codec2Client(14053): query -- param skipped: index = 1342179345.
W/Codec2Client(14053): query -- param skipped: index = 2415921170.
W/Codec2Client(14053): query -- param skipped: index = 2684356609.
D/C2Store (14053): Using DMABUF Heaps
I/Codec2-HalSelection(14053): selection: hidl
D/CCodecBufferChannel(14053): [c2.unisoc.mp3.decoder#268] Created input block pool with allocatorID 16 => poolID 17 - OK (0)
I/CCodecBufferChannel(14053): [c2.unisoc.mp3.decoder#268] Created output block pool with allocatorID 16 => poolID 17 - OK
D/CCodecBufferChannel(14053): [c2.unisoc.mp3.decoder#268] Configured output block pool ids 17 => OK
I/DMABUFHEAPS(14053): Using DMA-BUF heap named: system
I/AudioTrack(14053): set(): streamType -1, sampleRate 22050, format 0x1, channelMask 0x1, frameCount 7120, flags 0, notificationFrames 0, sessionId 7881, transferType 3, uid 10247, pid 14053, packageName com.example.jarvis_app
D/AudioTrack(14053): set() fadeEnabled:1, isWhiteApp: 0
D/AudioTrack(14053): set(): Building AudioTrack with attributes: usage=1 content=2 flags=0xa00 tags=[]
D/AudioTrack(14053): set(), create sync notify, streamType 3
D/AudioNotifyPnp(14053): createAudioNotify()
D/mple.jarvis_app(14053): createAudioNotifyPnpFactory(), create unisoc AudioNotifyPnpInterface 0xb4000075d5ae1be0
D/AudioNotifyPnp(14053): checkWriterThreadName(), notify start to pnp, mWriterTid 14427, name ExoPlayer:Playb
I/AudioTrack(14053): start(1653): prior state:STATE_STOPPED
D/AudioNotifyPnp(14053): setStateAndNotify(), state STATE_ACTIVE, pid 14053, tid 14427
D/AudioNotifyPnp(14053): checkWriterThreadName(), notify start to pnp, mWriterTid 14427, name ExoPlayer:Playb
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Sprache erkannt
I/AudioTrack(14053): stop(1653): prior state:STATE_ACTIVE
D/AudioTrack(14053): stop(1653): called with 50112 frames delivered
D/AudioNotifyPnp(14053): setStateAndNotify(), state STATE_STOPPED, pid 14053, tid 14427
D/AudioNotifyPnp(14053): setStateAndNotify(), notify stop to pnp
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Sprachende
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: hallo wie kann ich beruflich sein
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/BufferPoolAccessor2.0(14053): bufferpool2 0xb4000075d40ca628 : 5(40960 size) total buffers - 0(0 size) used buffers - 84/89 (recycle/alloc) - 5/174 (fetch/transfer)
D/BufferPoolAccessor2.0(14053): evictor expired: 1, evicted: 1
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
D/AudioManager(14053): dispatching onAudioFocusChange(1) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: sage mir tagesinformationen
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
D/AudioManager(14053): dispatching onAudioFocusChange(1) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: hey jarvis
D/JARVIS_WAKEWORD(14053): Wakeword erkannt
W/libc    (14053): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app(14053): type=1400 audit(0.0:18175): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE(14053): WakeLock aktiviert
D/JARVIS_WAKEWORD(14053): sendWakewordToFlutter
I/flutter (14053): [JARVIS BRIDGE] wakewordDetected
I/flutter (14053): [JARVIS BRIDGE] null
I/flutter (14053): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter (14053): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter (14053): [JARVIS] Wakeword Trigger empfangen
I/flutter (14053): [JARVIS] Controller State: JarvisState.idle
I/flutter (14053): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD(14053): Wakeword STOP
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (14053): [JARVIS] Wakeword gestoppt
I/flutter (14053): [VOICE] listen() wird gestartet
I/flutter (14053): [VOICE] verfügbar: true
I/flutter (14053): [VOICE] SpeechToText aktiv
I/flutter (14053): [JARVIS] startListening verlassen
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Sprache erkannt
D/JARVIS_WAKEWORD(14053): Sprachende
D/AudioManager(14053): dispatching onAudioFocusChange(1) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: sage mir tagesinformationen
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/JARVIS_WAKEWORD(14053): Wakeword STOP
D/AudioManager(14053): dispatching onAudioFocusChange(1) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
D/JARVIS_WAKEWORD(14053): Listening gestartet
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
I/flutter (14053): [JARVIS] Wakeword gestoppt
I/flutter (14053): [VOICE] listen() wird gestartet
I/flutter (14053): [VOICE] verfügbar: true
I/flutter (14053): [VOICE] SpeechToText aktiv
I/flutter (14053): [JARVIS] startListening verlassen
D/JARVIS_WAKEWORD(14053): Sprache erkannt
I/flutter (14053): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD(14053): Sprachende
D/AudioManager(14053): dispatching onAudioFocusChange(1) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Erkannt: sage mir tagesinformationen
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
D/AudioManager(14053): dispatching onAudioFocusChange(1) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Fehler: 7
D/JARVIS_WAKEWORD(14053): Listening gestartet
D/AudioManager(14053): dispatching onAudioFocusChange(-2) to android.media.AudioManager@f2f830com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@4327ca9
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(14053): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(14053): Bereit für Wakeword
