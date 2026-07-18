PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter clean  
Deleting build...                                                  517ms
Deleting .dart_tool...                                              14ms
Deleting ephemeral...                                                4ms
Deleting Generated.xcconfig...                                       0ms
Deleting flutter_export_environment.sh...                            0ms
Deleting ephemeral...                                                1ms
Deleting ephemeral...                                                2ms
Deleting ephemeral...                                                2ms
Deleting .flutter-plugins-dependencies...                            0ms
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter pub get
Resolving dependencies... 
Downloading packages... 
  matcher 0.12.19 (0.12.20 available)
  meta 1.18.0 (1.19.0 available)
  package_info_plus 10.2.0 (10.2.1 available)
  test_api 0.7.11 (0.7.13 available)
  vector_math 2.2.0 (2.4.0 available)
  xml 6.6.1 (7.0.1 available)
Got dependencies!
6 packages have newer versions incompatible with dependency constraints.
Try `flutter pub outdated` for more information.
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run    
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
e: file:///D:/Users/Michael/Dokumente/16_AppDev/jarvis_app/android/app/src/main/kotlin/com/example/jarvis_app/JarvisForegroundService.kt:395:23 Unresolved reference 'isRecognitionAvailable'.
e: file:///D:/Users/Michael/Dokumente/16_AppDev/jarvis_app/android/app/src/main/kotlin/com/example/jarvis_app/JarvisForegroundService.kt:422:22 Unresolved reference 'createSpeechRecognizer'.
e: file:///D:/Users/Michael/Dokumente/16_AppDev/jarvis_app/android/app/src/main/kotlin/com/example/jarvis_app/JarvisForegroundService.kt:476:38 Unresolved reference 'RESULTS_RECOGNITION'.
e: file:///D:/Users/Michael/Dokumente/16_AppDev/jarvis_app/android/app/src/main/kotlin/com/example/jarvis_app/JarvisForegroundService.kt:502:38 Unresolved reference 'RESULTS_RECOGNITION'.

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:compileDebugKotlin'.
> A failure occurred while executing org.jetbrains.kotlin.compilerRunner.GradleCompilerRunnerWithWorkers$GradleKotlinCompilerWorkAction
   > Compilation error. See log for more details

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to generate a Build Scan (Powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 36s
Running Gradle task 'assembleDebug'...                             37,0s
Error: Gradle task assembleDebug failed with exit code 1
