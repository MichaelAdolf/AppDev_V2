PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                             19,7s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,0s
I/FlutterActivityAndFragmentDelegate( 9842): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI( 9842): Beginning load of flutter...
D/FlutterJNI( 9842): flutter (null) was loaded normally!
I/flutter ( 9842): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer( 9842): Width is zero. 0,0
D/FlutterRenderer( 9842): Width is zero. 0,0
I/mple.jarvis_app( 9842): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app( 9842): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x51f99f84cd4f40c9
I/UnisocBufferQueueHelper( 9842): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006f49d40540, size:88
I/mple.jarvis_app( 9842): createUnisocBufferQueueHelperFactory success, get instance 0xb400006f49d40540
I/mple.jarvis_app( 9842): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006e0854eb40, size:296, enable:0
I/mple.jarvis_app( 9842): createUnisocFrameRecordFactory success, get instance 0xb400006e0854eb40
D/FlutterJNI( 9842): Sending viewport metrics to the engine.
W/libc    ( 9842): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc( 9842): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc( 9842): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9842): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9842): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9842): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc( 9842): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc( 9842): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc( 9842): register: id=23b00000377, handle=0xb400006f1ec05240, importpid=9842
W/libc    ( 9842): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc( 9842): initIonKernelMemtrack open devices:/dev/systemheap success, fd:208
D/mali_gralloc( 9842): register: id=23b00000377, handle=0xb400006f1ec055c0, importpid=9842
D/mali_gralloc( 9842): unregister: id=23b00000377, handle=0xb400006f1ec055c0, base=0x0, importpid=9842, clone_count=1
D/mali_gralloc( 9842): register: id=23b00000378, handle=0xb400006f1ec055c0, importpid=9842
D/mali_gralloc( 9842): register: id=23b00000378, handle=0xb400006f1ec056a0, importpid=9842
D/mali_gralloc( 9842): unregister: id=23b00000378, handle=0xb400006f1ec056a0, base=0x0, importpid=9842, clone_count=1
D/mali_gralloc( 9842): register: id=23b00000379, handle=0xb400006f1ec056a0, importpid=9842
D/mali_gralloc( 9842): register: id=23b00000379, handle=0xb400006f1ec05780, importpid=9842
D/mali_gralloc( 9842): unregister: id=23b00000379, handle=0xb400006f1ec05780, base=0x0, importpid=9842, clone_count=1
D/mali_gralloc( 9842): register: id=23b0000037a, handle=0xb400006f1ec05780, importpid=9842
D/mali_gralloc( 9842): register: id=23b0000037a, handle=0xb400006f1ec05860, importpid=9842
D/mali_gralloc( 9842): unregister: id=23b0000037a, handle=0xb400006f1ec05860, base=0x0, importpid=9842, clone_count=1
D/mali_gralloc( 9842): register: id=23b0000037b, handle=0xb400006f1ec05860, importpid=9842
D/mali_gralloc( 9842): register: id=23b0000037b, handle=0xb400006f1ec05940, importpid=9842
D/mali_gralloc( 9842): unregister: id=23b0000037b, handle=0xb400006f1ec05940, base=0x0, importpid=9842, clone_count=1
W/DisplayEventDispatcher( 9842): Vsync time out! vsyncScheduleDelay=320ms
W/Choreographer( 9842): Already have a pending vsync event.  There should only be one at a time.
Syncing files to device 25028RN03Y...                            1.911ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:59048/75R6_vNpzdA=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:59048/75R6_vNpzdA=/devtools/?uri=ws://127.0.0.1:59048/75R6_vNpzdA=/ws
W/Choreographer( 9842): Already have a pending vsync event.  There should only be one at a time.
I/TextToSpeech( 9842): Sucessfully bound to com.google.android.tts
D/JARVIS_WS( 9842): Verbinde mit ws://192.168.178.47:1880/endpoint/ws/jarvis-router
I/TextToSpeech( 9842): Connected to TTS engine
I/TextToSpeech( 9842): Setting up the connection to TTS engine...
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_SERVICE( 9842): Foreground Service läuft
D/JARVIS_WS( 9842): WebSocket verbunden
I/Choreographer( 9842): Skipped 84 frames!  The application may be doing too much work on its main thread.
D/mali_gralloc( 9842): register: id=23b0000037c, handle=0xb400006e039fbf60, importpid=9842
I/HWUI    ( 9842): Davey! duration=1436ms; Flags=1, FrameTimelineVsyncId=773159, IntendedVsync=9674682723668, Vsync=9676082723696, InputEventId=0, HandleInputStart=9676086450155, AnimationStart=9676086455001, PerformTraversalsStart=9676086457616, DrawStart=9676092159770, FrameDeadline=9674699390335, FrameInterval=9676085635463, FrameStartTime=16666667, SyncQueued=9676098113078, SyncStart=9676098368770, IssueDrawCommandsStart=9676100327809, SwapBuffers=9676114703193, FrameCompleted=9676119169155, DequeueBufferDuration=3459538, QueueBufferDuration=1472500, GpuCompleted=9676115886616, SwapBuffersCompleted=9676119169155, DisplayPresentTime=340, CommandSubmissionCompleted=9676114703193, 
D/ProfileInstaller( 9842): Installing profile for com.example.jarvis_app
D/JARVIS_TTS( 9842): Android TTS bereit
D/FlutterJNI( 9842): Sending viewport metrics to the engine.
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
W/mple.jarvis_app( 9842): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/base.apk' with 1 weak references
W/mple.jarvis_app( 9842): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.arm64_v8a.apk' with 1 weak references
W/mple.jarvis_app( 9842): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.de.apk' with 1 weak references
W/mple.jarvis_app( 9842): ApkAssets: Deleting an ApkAssets object '<empty> and /data/app/~~qu_oYd0WvY2oF27paYQ9Ag==/com.google.android.tts-asJUmntKfTsMMdL6ZSNNVQ==/split_config.xhdpi.apk' with 1 weak references
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: jarvis chavez chave
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3040): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/mali_gralloc( 9842): register: id=23b00000385, handle=0xb400006f20d57580, importpid=9842
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: erzähle mir was zum wetter erzähl mir was zum wetter
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: zeige mir etwas zum licht sage mir etwas zum licht zeige mir etwas vom licht
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: jarvis chavez javis
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3042): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: was ist mit dem licht
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Partial Wakeword erkannt: hallo jarvis
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3043): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: hallo jarvis hallo service hallo servis
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3044): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Partial Wakeword erkannt: okay jarvis
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3047): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD( 9842): Sprachende
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3048): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKEWORD( 9842): Erkannt: okay jarvis ok jarvis okay jarvis ja
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: okay ciao sag mir was zum licht okay ciao sag mal was zum licht okay ciao was sag mir was zum licht
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Sprache erkannt
D/JARVIS_WAKEWORD( 9842): Sprachende
D/JARVIS_WAKEWORD( 9842): Erkannt: okay tschüss okay service okay jarvis
D/JARVIS_WAKEWORD( 9842): Wakeword erkannt
W/libc    ( 9842): Access denied finding property "persist.unipnp.wakelock_upload.enabled"
W/mple.jarvis_app( 9842): type=1400 audit(0.0:3049): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c244,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/JARVIS_WAKE( 9842): WakeLock aktiviert
D/JARVIS_WAKEWORD( 9842): sendWakewordToFlutter
I/flutter ( 9842): [JARVIS BRIDGE] wakewordDetected
I/flutter ( 9842): [JARVIS BRIDGE] null
I/flutter ( 9842): [JARVIS BRIDGE] Wakeword Event empfangen
I/flutter ( 9842): [JARVIS WAKEWORD] Flutter hat Wakeword erkannt
I/flutter ( 9842): [JARVIS] Wakeword Trigger empfangen
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
D/JARVIS_WAKEWORD( 9842): Fehler: 7
D/JARVIS_WAKEWORD( 9842): Listening gestartet
D/JARVIS_WAKEWORD( 9842): Bereit für Wakeword
