PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             77,2s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           8,3s
I/FlutterActivityAndFragmentDelegate( 4420): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 4420): Beginning load of flutter...
D/FlutterJNI( 4420): flutter (null) was loaded normally!
I/flutter ( 4420): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 4420): Width is zero. 0,0
Syncing files to device 25028RN03Y...                              154ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:53589/WbzkUcygMxM=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:53589/WbzkUcygMxM=/devtools/?uri=ws://127.0.0.1:53589/WbzkUcygMxM=/ws
I/mple.jarvis_app( 4420): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
D/FlutterRenderer( 4420): Width is zero. 0,0
I/mple.jarvis_app( 4420): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x66f77473e1cbf015
I/UnisocBufferQueueHelper( 4420): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb4000076ff4933e0, size:88
I/mple.jarvis_app( 4420): createUnisocBufferQueueHelperFactory success, get instance 0xb4000076ff4933e0
I/mple.jarvis_app( 4420): Unisoc-Graphics: UnisocFrameRecord create, this:0xb4000076ff5aa500, size:296, enable:0
I/mple.jarvis_app( 4420): createUnisocFrameRecordFactory success, get instance 0xb4000076ff5aa500
D/FlutterJNI( 4420): Sending viewport metrics to the engine.
W/libc    ( 4420): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 4420): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 4420): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 4420): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4420): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4420): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 4420): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 4420): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 4420): register: id=234000001ea, handle=0xb4000076ff28a940, importpid=4420
W/libc    ( 4420): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 4420): initIonKernelMemtrack open devices:/dev/systemheap success, fd:210
D/mali_gralloc( 4420): register: id=234000001ea, handle=0xb4000076ff28acc0, importpid=4420
D/mali_gralloc( 4420): unregister: id=234000001ea, handle=0xb4000076ff28acc0, base=0x0, importpid=4420, clone_count=1
D/mali_gralloc( 4420): register: id=234000001eb, handle=0xb4000076ff28acc0, importpid=4420
D/mali_gralloc( 4420): register: id=234000001eb, handle=0xb4000076ff28ada0, importpid=4420
D/mali_gralloc( 4420): unregister: id=234000001eb, handle=0xb4000076ff28ada0, base=0x0, importpid=4420, clone_count=1
D/mali_gralloc( 4420): register: id=234000001ec, handle=0xb4000076ff28ada0, importpid=4420
D/mali_gralloc( 4420): register: id=234000001ec, handle=0xb4000076ff28ae80, importpid=4420
D/mali_gralloc( 4420): unregister: id=234000001ec, handle=0xb4000076ff28ae80, base=0x0, importpid=4420, clone_count=1
D/mali_gralloc( 4420): register: id=234000001ed, handle=0xb4000076ff28ae80, importpid=4420
D/mali_gralloc( 4420): register: id=234000001ed, handle=0xb4000076ff28af60, importpid=4420
D/mali_gralloc( 4420): unregister: id=234000001ed, handle=0xb4000076ff28af60, base=0x0, importpid=4420, clone_count=1
D/mali_gralloc( 4420): register: id=234000001ee, handle=0xb4000076ff28af60, importpid=4420
D/mali_gralloc( 4420): register: id=234000001ee, handle=0xb4000076ff28b040, importpid=4420
D/mali_gralloc( 4420): unregister: id=234000001ee, handle=0xb4000076ff28b040, base=0x0, importpid=4420, clone_count=1
W/Choreographer( 4420): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 4420): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 4420): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 4420): Connected to TTS engine
I/TextToSpeech( 4420): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 4420): Listening gestartet
D/JARVIS_SERVICE( 4420): Foreground Service läuft
D/JARVIS_WS( 4420): WebSocket verbunden
I/Choreographer( 4420): Skipped 76 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 4420): register: id=234000001ef, handle=0xb4000075dbdb2740, importpid=4420
I/HWUI    ( 4420): Davey! duration=1303ms; Flags=1, FrameTimelineVsyncId=2430850, IntendedVsync=13138357340586, Vsync=13139624277914, InputEventId=0, HandleInputStart=13139637152716, AnimationStart=13139637155524, PerformTraversalsStart=13139637156793, DrawStart=13139641284908, FrameDeadline=13138374007253, FrameInterval=13139636314562, FrameStartTime=16670228, SyncQueued=13139645692562, SyncStart=13139645866716, IssueDrawCommandsStart=13139646872831, SwapBuffers=13139660160447, FrameCompleted=13139661332293, DequeueBufferDuration=4177730, QueueBufferDuration=982115, GpuCompleted=13139661192177, SwapBuffersCompleted=13139661332293, DisplayPresentTime=15688, CommandSubmissionCompleted=13139660160447, 
D/ProfileInstaller( 4420): Installing profile for com.example.jarvis_app
D/JARVIS_TTS( 4420): Android TTS bereit
D/FlutterJNI( 4420): Sending viewport metrics to the engine.
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
D/JARVIS_WAKEWORD( 4420): Wakeword STOP
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [JARVIS] Wakeword gestoppt
I/flutter ( 4420): [VOICE] listen() wird gestartet
I/flutter ( 4420): [VOICE] verfügbar: true
I/flutter ( 4420): [VOICE] SpeechToText aktiv
I/flutter ( 4420): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/mple.jarvis_app( 4420): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 4420): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 4420): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 4420): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir die | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir die | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir die | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir die tagesinformation | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir die tagesinformation | final=false
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir die tagesinformation | final=true
D/JARVIS_WS( 4420): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:28. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT( 4420): Node-RED Event wird verarbeitet
W/libc    ( 4420): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...( 4420): type=1400 audit(0.0:1009): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 4420): WakeLock aktiviert
D/JARVIS_TTS( 4420): Sprache: Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:28. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT( 4420): Activity wird geöffnet
D/JARVIS_BRIDGE( 4420): openAndDeliverEvent
D/JARVIS_BRIDGE( 4420): Bridge Activity in Vordergrund
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 4420): [Jarvis] App resumed -> voice neu initialisieren
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE( 4420): Intent Event empfangen
D/JARVIS_BRIDGE( 4420): Gepuffertes Event wird gesendet
I/flutter ( 4420): [JARVIS BRIDGE] backgroundEvent
I/flutter ( 4420): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:28. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 4420): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:28. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 4420): [Jarvis] App resumed -> voice neu initialisieren
D/mali_gralloc( 4420): register: id=234000001f4, handle=0xb4000076ff2883a0, importpid=4420
D/JARVIS_WAKEWORD( 4420): Listening gestartet
D/FlutterJNI( 4420): Sending viewport metrics to the engine.
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
D/JARVIS_WAKEWORD( 4420): Sprachende
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
D/JARVIS_WAKEWORD( 4420): Erkannt: guten abend heute ist donnerstag der 23 juli 2026
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Fehler: 7
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Fehler: 7
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
D/JARVIS_WAKEWORD( 4420): Sprachende
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Fehler: 7
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
D/JARVIS_WAKEWORD( 4420): Sprachende
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Erkannt: jarvis
D/JARVIS_WAKEWORD( 4420): Wakeword erkannt
W/libc    ( 4420): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 4420): type=1400 audit(0.0:1011): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 4420): WakeLock aktiviert
D/JARVIS_WAKEWORD( 4420): sendWakewordToFlutter
I/flutter ( 4420): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 4420): [JARVIS BRIDGE] null
I/flutter ( 4420): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 4420): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 4420): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 4420): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 4420): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 4420): Wakeword STOP
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [JARVIS] Wakeword gestoppt
I/flutter ( 4420): [VOICE] listen() wird gestartet
I/flutter ( 4420): [VOICE] verfügbar: true
I/flutter ( 4420): [VOICE] SpeechToText aktiv
I/flutter ( 4420): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir Informationen | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir Informationen zum | final=false
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir Informationen zum Licht | final=false
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [VOICE] Ergebnis: gebe mir Informationen zum Licht | final=true
D/TTS     ( 4420): Utterance ID has started: afdc9f2a-3247-4dda-8bcb-3173c29e7d00
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [JARVIS] Audio Mode: AudioOutputMode.remote
D/TTS     ( 4420): Utterance ID has completed: afdc9f2a-3247-4dda-8bcb-3173c29e7d00
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
D/JARVIS_WAKEWORD( 4420): Sprachende
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Erkannt: okay jarvis
W/mple.jarvis_app( 4420): type=1400 audit(0.0:1013): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKEWORD( 4420): Wakeword erkannt
W/libc    ( 4420): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE( 4420): WakeLock aktiviert
D/JARVIS_WAKEWORD( 4420): sendWakewordToFlutter
I/flutter ( 4420): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 4420): [JARVIS BRIDGE] null
I/flutter ( 4420): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 4420): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 4420): [JARVIS] Wakeword Trigger empfangen
I/flutter ( 4420): [JARVIS] Controller State: JarvisState.idle
I/flutter ( 4420): [JARVIS] Controller Busy: false
D/JARVIS_WAKEWORD( 4420): Wakeword STOP
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [JARVIS] Wakeword gestoppt
I/flutter ( 4420): [VOICE] listen() wird gestartet
I/flutter ( 4420): [VOICE] verfügbar: true
I/flutter ( 4420): [VOICE] SpeechToText aktiv
I/flutter ( 4420): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis: die Tages | final=false
I/mple.jarvis_app( 4420): Background concurrent mark compact GC freed 2821KB AllocSpace bytes, 0(0B) LOS objects, 49% free, 2978KB/5957KB, paused 519us,6.697ms total 51.306ms
I/flutter ( 4420): [VOICE] Ergebnis: die Tages | final=true
D/JARVIS_WAKEWORD( 4420): Wakeword STOP
I/flutter ( 4420): [JARVIS] Wakeword gestoppt
I/flutter ( 4420): [VOICE] listen() wird gestartet
I/flutter ( 4420): [VOICE] verfügbar: true
I/flutter ( 4420): [VOICE] SpeechToText aktiv
I/flutter ( 4420): [JARVIS] startListening verlassen
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis:  | final=false
I/flutter ( 4420): [VOICE] Ergebnis: die | final=false
I/flutter ( 4420): [VOICE] Ergebnis: die | final=false
I/flutter ( 4420): [VOICE] Ergebnis: die | final=false
I/flutter ( 4420): [VOICE] Ergebnis: die tagesinformation | final=false
I/flutter ( 4420): [VOICE] Ergebnis: die tagesinformation | final=false
I/flutter ( 4420): [JARVIS] Listening Timeout
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
I/flutter ( 4420): [VOICE] Ergebnis: die tagesinformation | final=true
D/JARVIS_WS( 4420): Nachricht empfangen: {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:29. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
D/JARVIS_EVENT( 4420): Node-RED Event wird verarbeitet
W/libc    ( 4420): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/178.47:1880/...( 4420): type=1400 audit(0.0:1014): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 4420): WakeLock aktiviert
D/JARVIS_TTS( 4420): Sprache: Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:29. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.
D/JARVIS_EVENT( 4420): Activity wird geöffnet
D/JARVIS_BRIDGE( 4420): openAndDeliverEvent
D/JARVIS_BRIDGE( 4420): Bridge Activity in Vordergrund
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.inactive
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 4420): [Jarvis] App resumed -> voice neu initialisieren
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.inactive
D/JARVIS_BRIDGE( 4420): Intent Event empfangen
D/JARVIS_BRIDGE( 4420): Gepuffertes Event wird gesendet
I/flutter ( 4420): [JARVIS BRIDGE] backgroundEvent
I/flutter ( 4420): [JARVIS BRIDGE] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:29. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 4420): [JARVIS BACKGROUND RAW] {"success":true,"intent":"dailyInfo","entity":"jarvis.daily_info","state":"executed","message":"Guten Abend. Heute ist Donnerstag, der dreiundzwanzigster Juli 2026. Die aktuelle Uhrzeit ist 21:29. Draußen sind es aktuell 19 Grad bei leicht bewölktem Himmel. Du hast aktuell keine anstehenden Termine.","audioUrl":"http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3","ttsProfile":"jarvis"}
I/flutter ( 4420): [Jarvis] Lifecycle: AppLifecycleState.resumed
I/flutter ( 4420): [Jarvis] App resumed -> voice neu initialisieren
D/FlutterJNI( 4420): Sending viewport metrics to the engine.
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Sprachende
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Erkannt: guten abend heute ist donnerstag der 23 juli 2026 die aktuelle uhrzeit ist 21:29 uhr draußen sind es aktuell 19 grad bei leicht bewölktem himmel du hast aktuell keine anstehenden termine
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Fehler: 7
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Sprache erkannt
D/JARVIS_WAKEWORD( 4420): Fehler: 7
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Listening gestartet
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk( 4420): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD( 4420): Bereit für Wakeword
