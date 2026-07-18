PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
Running Gradle task 'assembleDebug'...                              6,8s
√ Built build\app\outputs\flutter-apk\app-debug.apk
Installing build\app\outputs\flutter-apk\app-debug.apk...           6,2s
I/FlutterActivityAndFragmentDelegate(23369): If you are attempting to set --enable-dart-profiling via Intent extras to launch a Flutter component outside of using the Flutter CLI, note that support for setting engine flags on Android via Intent will soon be dropped; see https://github.com/flutter/flutter/issues/180686 for more information on this breaking change. To migrate, set --enable-dart-profiling or any other flags specified via Intent extras on the command line instead or see https://github.com/flutter/flutter/blob/main/docs/engine/Flutter-Android-Engine-Flags.md for alternative methods.
D/FlutterJNI(23369): Beginning load of flutter...
D/FlutterJNI(23369): flutter (null) was loaded normally!
I/flutter (23369): [IMPORTANT:flutter/shell/platform/android/android_context_vk_impeller.cc(62)] Using the Impeller rendering backend (Vulkan).
D/FlutterRenderer(23369): Width is zero. 0,0
Syncing files to device 25028RN03Y...                               98ms

Flutter run key commands.
r Hot reload. 
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).

A Dart VM Service on 25028RN03Y is available at: http://127.0.0.1:62911/sCKYsSZknpI=/
The Flutter DevTools debugger and profiler on 25028RN03Y is available at:
http://127.0.0.1:62911/sCKYsSZknpI=/devtools/?uri=ws://127.0.0.1:62911/sCKYsSZknpI=/ws
D/FlutterRenderer(23369): Width is zero. 0,0
I/mple.jarvis_app(23369): Compiler allocated 5021KB to compile void android.view.ViewRootImpl.performTraversals()
I/mple.jarvis_app(23369): hook_module_init libgui_unisoc_utils.so over, map size:3, library handle:0x2310e2bd5288f9ef
I/UnisocBufferQueueHelper(23369): Unisoc-Graphics: UnisocBufferQueueHelper create, this:0xb400006f25a68780, size:88
I/mple.jarvis_app(23369): createUnisocBufferQueueHelperFactory success, get instance 0xb400006f25a68780
I/mple.jarvis_app(23369): Unisoc-Graphics: UnisocFrameRecord create, this:0xb400006f259bec40, size:296, enable:0
I/mple.jarvis_app(23369): createUnisocFrameRecordFactory success, get instance 0xb400006f259bec40
D/FlutterJNI(23369): Sending viewport metrics to the engine.
W/libc    (23369): Access denied finding property "persist.vendor.gpu.fbc"
I/mali_gralloc(23369): Unisoc: get compress property: persist.vendor.gpu.fbc (1)
E/mali_gralloc(23369): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(23369): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23369): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23369): Requested R8 format is not supported with this allocator. R8 format is only supported with the AIDL allocator
E/mali_gralloc(23369): ERROR: Unrecognized and/or unsupported format R8 and usage TEXTURE + RENDER + HWC
E/mali_gralloc(23369): ERROR: Unrecognized and/or unsupported format RGBA_10101010 and usage TEXTURE + RENDER + HWC
D/mali_gralloc(23369): register: id=23b00000693, handle=0xb400006f25983400, importpid=23369
W/libc    (23369): Access denied finding property "persist.vendor.gpu.ionmemtrack"
I/mali_gralloc(23369): initIonKernelMemtrack open devices:/dev/systemheap success, fd:209
D/mali_gralloc(23369): register: id=23b00000693, handle=0xb400006f25983780, importpid=23369
D/mali_gralloc(23369): unregister: id=23b00000693, handle=0xb400006f25983780, base=0x0, importpid=23369, clone_count=1
D/mali_gralloc(23369): register: id=23b00000694, handle=0xb400006f25983780, importpid=23369
D/mali_gralloc(23369): register: id=23b00000694, handle=0xb400006f25983860, importpid=23369
D/mali_gralloc(23369): unregister: id=23b00000694, handle=0xb400006f25983860, base=0x0, importpid=23369, clone_count=1
D/mali_gralloc(23369): register: id=23b00000695, handle=0xb400006f25983860, importpid=23369
D/mali_gralloc(23369): register: id=23b00000695, handle=0xb400006f25983940, importpid=23369
D/mali_gralloc(23369): unregister: id=23b00000695, handle=0xb400006f25983940, base=0x0, importpid=23369, clone_count=1
D/mali_gralloc(23369): register: id=23b00000696, handle=0xb400006f25983940, importpid=23369
D/mali_gralloc(23369): register: id=23b00000696, handle=0xb400006f25983a20, importpid=23369
D/mali_gralloc(23369): unregister: id=23b00000696, handle=0xb400006f25983a20, base=0x0, importpid=23369, clone_count=1
D/mali_gralloc(23369): register: id=23b00000697, handle=0xb400006f25983a20, importpid=23369
D/mali_gralloc(23369): register: id=23b00000697, handle=0xb400006f25983b00, importpid=23369
D/mali_gralloc(23369): unregister: id=23b00000697, handle=0xb400006f25983b00, base=0x0, importpid=23369, clone_count=1
W/Choreographer(23369): Already have a pending vsync event.  There should only be one at a time.
D/AndroidRuntime(23369): Shutting down VM
E/AndroidRuntime(23369): FATAL EXCEPTION: main
E/AndroidRuntime(23369): Process: com.example.jarvis_app, PID: 23369
E/AndroidRuntime(23369): java.lang.RuntimeException: Unable to create service com.example.jarvis_app.JarvisForegroundService: java.lang.SecurityException: Starting FGS with type microphone callerApp=ProcessRecord{413af1b 23369:com.example.jarvis_app/u0a246} targetSDK=36 requires permissions: all of the permissions allOf=true [android.permission.FOREGROUND_SERVICE_MICROPHONE] any of the permissions allOf=false [android.permission.CAPTURE_AUDIO_HOTWORD, android.permission.CAPTURE_AUDIO_OUTPUT, android.permission.CAPTURE_MEDIA_OUTPUT, android.permission.CAPTURE_TUNER_AUDIO_INPUT, android.permission.CAPTURE_VOICE_COMMUNICATION_OUTPUT, android.permission.RECORD_AUDIO]  and the app must be in the eligible state/exemptions to access the foreground only permission
E/AndroidRuntime(23369):        at android.app.ActivityThread.handleCreateService(ActivityThread.java:5108)
E/AndroidRuntime(23369):        at android.app.ActivityThread.-$$Nest$mhandleCreateService(Unknown Source:0)
E/AndroidRuntime(23369):        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2510)
E/AndroidRuntime(23369):        at android.os.Handler.dispatchMessage(Handler.java:107)
E/AndroidRuntime(23369):        at android.os.Looper.loopOnce(Looper.java:246)
E/AndroidRuntime(23369):        at android.os.Looper.loop(Looper.java:334)
E/AndroidRuntime(23369):        at android.app.ActivityThread.main(ActivityThread.java:8895)
E/AndroidRuntime(23369):        at java.lang.reflect.Method.invoke(Native Method)
E/AndroidRuntime(23369):        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:706)
E/AndroidRuntime(23369):        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:902)
E/AndroidRuntime(23369): Caused by: java.lang.SecurityException: Starting FGS with type microphone callerApp=ProcessRecord{413af1b 23369:com.example.jarvis_app/u0a246} targetSDK=36 requires permissions: all of the permissions allOf=true [android.permission.FOREGROUND_SERVICE_MICROPHONE] any of the permissions allOf=false [android.permission.CAPTURE_AUDIO_HOTWORD, android.permission.CAPTURE_AUDIO_OUTPUT, android.permission.CAPTURE_MEDIA_OUTPUT, android.permission.CAPTURE_TUNER_AUDIO_INPUT, android.permission.CAPTURE_VOICE_COMMUNICATION_OUTPUT, android.permission.RECORD_AUDIO]  and the app must be in the eligible state/exemptions to access the foreground only permission
E/AndroidRuntime(23369):        at android.os.Parcel.createExceptionOrNull(Parcel.java:3241)
E/AndroidRuntime(23369):        at android.os.Parcel.createException(Parcel.java:3225)
E/AndroidRuntime(23369):        at android.os.Parcel.readException(Parcel.java:3208)
E/AndroidRuntime(23369):        at android.os.Parcel.readException(Parcel.java:3150)
E/AndroidRuntime(23369):        at android.app.IActivityManager$Stub$Proxy.setServiceForeground(IActivityManager.java:7366)
E/AndroidRuntime(23369):        at android.app.Service.startForeground(Service.java:776)
E/AndroidRuntime(23369):        at com.example.jarvis_app.JarvisForegroundService.startAsForegroundService(JarvisForegroundService.kt:176)
E/AndroidRuntime(23369):        at com.example.jarvis_app.JarvisForegroundService.onCreate(JarvisForegroundService.kt:73)
E/AndroidRuntime(23369):        at android.app.ActivityThread.handleCreateService(ActivityThread.java:5095)
E/AndroidRuntime(23369):        ... 9 more
E/AndroidRuntime(23369): Caused by: android.os.RemoteException: Remote stack trace:
E/AndroidRuntime(23369):        at com.android.server.am.ActiveServices.validateForegroundServiceType(ActiveServices.java:2987)
E/AndroidRuntime(23369):        at com.android.server.am.ActiveServices.setServiceForegroundInnerLocked(ActiveServices.java:2671)
E/AndroidRuntime(23369):        at com.android.server.am.ActiveServices.setServiceForegroundLocked(ActiveServices.java:1915)
E/AndroidRuntime(23369):        at com.android.server.am.ActivityManagerService.setServiceForeground(ActivityManagerService.java:14378)
E/AndroidRuntime(23369):        at android.app.IActivityManager$Stub.onTransact(IActivityManager.java:3674)
E/AndroidRuntime(23369): 
I/MQS     (23369): Found JavaCrash event
W/mple.jarvis_app(23369): type=1400 audit(0.0:3387): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/mple.jarvis_app(23369): type=1400 audit(0.0:3388): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/mple.jarvis_app(23369): type=1400 audit(0.0:3389): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/ScoutUtils(23369): Failed to mkdir /data/miuilog/stability/hprof/
W/mple.jarvis_app(23369): type=1400 audit(0.0:3390): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/mple.jarvis_app(23369): type=1400 audit(0.0:3391): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/mple.jarvis_app(23369): type=1400 audit(0.0:3392): avc:  denied  { getattr } for  path="/data/miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/mple.jarvis_app(23369): type=1400 audit(0.0:3393): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
W/mple.jarvis_app(23369): type=1400 audit(0.0:3394): avc:  denied  { search } for  name="miuilog" dev="dm-52" ino=27814 scontext=u:r:untrusted_app:s0:c246,c256,c512,c768 tcontext=u:object_r:data_log_file:s0 tclass=dir permissive=0 app=com.example.jarvis_app
I/Process (23369): Sending signal. PID: 23369 SIG: 9
Lost connection to device.
