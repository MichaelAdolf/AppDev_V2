PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             22,2s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           7,9s
I/FlutterActivityAndFragmentDelegate( 7696): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 7696): Beginning load of flutter...
D/FlutterJNI( 7696): flutter (null) was loaded normally!
I/flutter ( 7696): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 7696): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              111ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:53292/SxjrdVzy_uI=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:53292/SxjrdVzy_uI=/devtools/?uri=ws://127.0.0.1:53292/SxjrdVzy_uI=/ws
D/FlutterRenderer( 7696): Width is zero. 0,0
I/mple.jarvis_app( 7696): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0xde236ffb35adb369
I/UnisocBufferQueueHelper( 7696): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb4000076ff3e6f80, size:88
I/mple.jarvis_app( 7696): createUnisocBufferQueueHelperFactory success, get instance 0xb4000076ff3e6f80
I/mple.jarvis_app( 7696): Unisoc-Graphics: UnisocFrameRecord create, this:0xb4000076ff55a180, size:296, enable:0
I/mple.jarvis_app( 7696): createUnisocFrameRecordFactory success, get instance 0xb4000076ff55a180
I/mple.jarvis_app( 7696): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterJNI( 7696): Sending viewport metrics to the engine.
W/libc    ( 7696): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 7696): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 7696): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 7696): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 7696): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 7696): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 7696): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 7696): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 7696): register: id=234000002ee, handle=0xb4000076ff2f8940, importpid=7696
W/libc    ( 7696): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 7696): initIonKernelMemtrack open devices:/dev/systemheap success, fd:210
D/mali_gralloc( 7696): register: id=234000002ee, handle=0xb4000076ff2f8cc0, importpid=7696
D/mali_gralloc( 7696): unregister: id=234000002ee, handle=0xb4000076ff2f8cc0, base=0x0, importpid=7696, clone_count=1
D/mali_gralloc( 7696): register: id=234000002ef, handle=0xb4000076ff2f8cc0, importpid=7696
D/mali_gralloc( 7696): register: id=234000002ef, handle=0xb4000076ff2f8da0, importpid=7696
D/mali_gralloc( 7696): unregister: id=234000002ef, handle=0xb4000076ff2f8da0, base=0x0, importpid=7696, clone_count=1
D/mali_gralloc( 7696): register: id=234000002f0, handle=0xb4000076ff2f8da0, importpid=7696
D/mali_gralloc( 7696): register: id=234000002f0, handle=0xb4000076ff2f8e80, importpid=7696
D/mali_gralloc( 7696): unregister: id=234000002f0, handle=0xb4000076ff2f8e80, base=0x0, importpid=7696, clone_count=1
D/mali_gralloc( 7696): register: id=234000002f1, handle=0xb4000076ff2f8e80, importpid=7696
D/mali_gralloc( 7696): register: id=234000002f1, handle=0xb4000076ff2f8f60, importpid=7696
D/mali_gralloc( 7696): unregister: id=234000002f1, handle=0xb4000076ff2f8f60, base=0x0, importpid=7696, clone_count=1
D/mali_gralloc( 7696): register: id=234000002f2, handle=0xb4000076ff2f8f60, importpid=7696
D/mali_gralloc( 7696): register: id=234000002f2, handle=0xb4000076ff2f9040, importpid=7696
D/mali_gralloc( 7696): unregister: id=234000002f2, handle=0xb4000076ff2f9040, base=0x0, importpid=7696, clone_count=1
W/DisplayEventDispatcher( 7696): Vsync time out! vsyncScheduleDelay=334ms
W/Choreographer( 7696): Already have a pending vsync event.  There should only be one at a time.
W/Choreographer( 7696): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 7696): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 7696): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 7696): Connected to TTS engine
I/TextToSpeech( 7696): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 7696): Listening gestartet
D/JARVIS_SERVICE( 7696): Foreground Service läuft
I/Choreographer( 7696): Skipped 82 frames!  The application may be doing too much work on its main thread.
D/JARVIS_WS( 7696): WebSocket verbunden
D/mali_gralloc( 7696): register: id=234000002f3, handle=0xb4000075d87814a0, importpid=7696
I/HWUI    ( 7696): Davey! duration=1405ms; Flags=1, FrameTimelineVsyncId=2627209, IntendedVsync=15512437345694, Vsync=15513804264538, InputEventId=0, HandleInputStart=15513811752825, AnimationStart=15513811758133, PerformTraversalsStart=15513811761056, DrawStart=15513818523979, FrameDeadline=15512454012361, FrameInterval=15513811161056, FrameStartTime=16669742, SyncQueued=15513822262787, SyncStart=15513822399710, IssueDrawCommandsStart=15513823426902, SwapBuffers=15513841499979, FrameCompleted=15513843425595, DequeueBufferDuration=5564385, QueueBufferDuration=1532346, GpuCompleted=15513842646864, SwapBuffersCompleted=15513843425595, DisplayPresentTime=6921482064001647838, CommandSubmissionCompleted=15513841499979, 
D/ProfileInstaller( 7696): Installing profile for com.example.jarvis_app
D/JARVIS_TTS( 7696): Android TTS bereit
D/FlutterJNI( 7696): Sending viewport metrics to the engine.
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
D/JARVIS_WAKEWORD( 7696): Sprachende
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/mple.jarvis_app( 7696): Background concurrent mark compact GC freed 10MB AllocSpace bytes, 3(60KB) LOS objects, 49% free, 2870KB/5741KB, paused 620us,6.773ms total 61.537ms
W/mple.jarvis_app( 7696): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 7696): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 7696): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 7696): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD( 7696): Erkannt: hey jarvis
D/JARVIS_WAKEWORD( 7696): Wakeword erkannt
W/libc    ( 7696): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 7696): type=1400 audit(0.0:18075): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 7696): WakeLock aktiviert
D/JARVIS_WAKEWORD( 7696): sendWakewordToFlutter
I/flutter ( 7696): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 7696): [JARVIS BRIDGE] null
I/flutter ( 7696): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 7696): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 7696): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 7696): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 7696): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 7696): Wakeword STOP
D/mali_gralloc( 7696): register: id=234000002f8, handle=0xb4000076f90229e0, importpid=7696
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [JARVIS] Wakeword gestoppt
I/flutter ( 7696): [VOICE] listen() wird gestartet
I/flutter ( 7696): [VOICE] verfügbar: true
I/flutter ( 7696): [VOICE] SpeechToText aktiv
I/flutter ( 7696): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage | final=false
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [VOICE] Ergebnis: sage | final=true
D/JARVIS_WAKEWORD( 7696): Wakeword STOP
I/flutter ( 7696): [JARVIS] Wakeword gestoppt
I/flutter ( 7696): [VOICE] listen() wird gestartet
I/flutter ( 7696): [VOICE] verfügbar: true
I/flutter ( 7696): [VOICE] SpeechToText aktiv
I/flutter ( 7696): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
I/flutter ( 7696): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD( 7696): Listening gestartet
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
I/flutter ( 7696): [VOICE] Ergebnis: Tage | final=false
I/flutter ( 7696): [VOICE] Ergebnis: tagesinformation | final=false
I/flutter ( 7696): [VOICE] Ergebnis: tagesinformation | final=true
D/JARVIS_WS( 7696): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:08. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT( 7696): Node-RED Event wird verarbeitet
W/libc    ( 7696): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...( 7696): type=1400 audit(0.0:18076): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 7696): WakeLock aktiviert
D/JARVIS_TTS( 7696): Sprache: Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:08. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT( 7696): Activity wird geöffnet
D/JARVIS_BRIDGE( 7696): openAndDeliverEvent
D/JARVIS_BRIDGE( 7696): Bridge Activity in Vordergrund
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 7696): [Jarvis] App resumed -> voice neu initialisieren
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE( 7696): Intent Event empfangen
D/JARVIS_BRIDGE( 7696): Gepuffertes Event wird gesendet
I/flutter ( 7696): [JARVIS BRIDGE] backgroundEvent
I/flutter ( 7696): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:08. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 7696): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:08. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 7696): [Jarvis] App resumed -> voice neu initialisieren
D/FlutterJNI( 7696): Sending viewport metrics to the engine.
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
D/JARVIS_WAKEWORD( 7696): Fehler: 7
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
D/JARVIS_WAKEWORD( 7696): Sprachende
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Erkannt: der 23 juli 2026
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Sprachende
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Fehler: 7
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
I/flutter ( 7696): [JARVIS] Audio Mode: AudioOutputMode.remote
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
D/JARVIS_WAKEWORD( 7696): Sprachende
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Erkannt: hey jarvis
D/JARVIS_WAKEWORD( 7696): Wakeword erkannt
W/libc    ( 7696): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 7696): type=1400 audit(0.0:18078): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 7696): WakeLock aktiviert
D/JARVIS_WAKEWORD( 7696): sendWakewordToFlutter
I/flutter ( 7696): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 7696): [JARVIS BRIDGE] null
I/flutter ( 7696): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 7696): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 7696): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 7696): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 7696): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 7696): Wakeword STOP
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [JARVIS] Wakeword gestoppt
I/flutter ( 7696): [VOICE] listen() wird gestartet
I/flutter ( 7696): [VOICE] verfügbar: true
I/flutter ( 7696): [VOICE] SpeechToText aktiv
I/flutter ( 7696): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
I/flutter ( 7696): [VOICE] Ergebnis:  | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage mir | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage mir die | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage mir die | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage mir die tagesinformation | final=false
I/flutter ( 7696): [VOICE] Ergebnis: sage mir die tagesinformation | final=false
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 7696): [VOICE] Ergebnis: sage mir die tagesinformation | final=true
D/JARVIS_WS( 7696): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:09. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT( 7696): Node-RED Event wird verarbeitet
W/libc    ( 7696): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...( 7696): type=1400 audit(0.0:18079): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 7696): WakeLock aktiviert
D/JARVIS_TTS( 7696): Sprache: Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:09. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT( 7696): Activity wird geöffnet
D/JARVIS_BRIDGE( 7696): openAndDeliverEvent
D/JARVIS_BRIDGE( 7696): Bridge Activity in Vordergrund
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 7696): [Jarvis] App resumed -> voice neu initialisieren
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE( 7696): Intent Event empfangen
D/JARVIS_BRIDGE( 7696): Gepuffertes Event wird gesendet
I/flutter ( 7696): [JARVIS BRIDGE] backgroundEvent
I/flutter ( 7696): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:09. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 7696): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 22:09. Draußen sind es aktuell 18 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 7696): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 7696): [Jarvis] App resumed -> voice neu initialisieren
D/JARVIS_WAKEWORD( 7696): Listening gestartet
D/FlutterJNI( 7696): Sending viewport metrics to the engine.
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
D/JARVIS_WAKEWORD( 7696): Sprachende
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Erkannt: heute ist donnerstag der 23 juli 2026 die aktuelle uhrzeit ist 22:09 uhr draußen sind es aktuell 18
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Sprachende
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Fehler: 7
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
D/JARVIS_WAKEWORD( 7696): Sprache erkannt
D/JARVIS_WAKEWORD( 7696): Sprachende
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Fehler: 7
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Fehler: 7
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Listening gestartet
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 7696): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 7696): Bereit für Wakeword
