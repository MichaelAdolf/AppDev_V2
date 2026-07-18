PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> porcupine_flutter
porcupine_flutter : Die Benennung "porcupine_flutter" wurde nicht als Name eines Cmdlet, einer 
Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie die 
Schreibweise des Namens, oder ob der Pfad korrekt ist (sofern enthalten), und wiederholen Sie den 
Vorgang.
In Zeile:1 Zeichen:1
+ porcupine_flutter
+ ~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (porcupine_flutter:String) [], CommandNotFoundExcepti 
   on
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter pub get
Resolving dependencies... 
Downloading packages... 
  hooks 2.0.2 (2.1.0 available)
  matcher 0.12.19 (0.12.20 available)
  meta 1.18.0 (1.19.0 available)
  package_config 2.2.0 (3.0.0 available)
  package_info_plus 10.2.0 (10.2.1 available)
  porcupine_flutter 3.0.6 (4.0.0 available)
  record_use 0.6.0 (1.0.0 available)
  test_api 0.7.11 (0.7.13 available)
  vector_math 2.2.0 (2.4.0 available)
  xml 6.6.1 (7.0.1 available)
Got dependencies!
10 packages have newer versions incompatible with dependency constraints.
Try `flutter pub outdated` for more information.
PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run      
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
lib/services/jarvis_wakeword_service.dart:13:48: Error: Too few positional arguments: 3 required, 1 given.
        await PorcupineManager.fromKeywordPaths(
                                               ^
/C:/Users/Michael/AppData/Local/Pub/Cache/hosted/pub.dev/porcupine_flutter-3.0.6/lib/porcupine_manager.dart:87:35: Context: Found this candidate, but the arguments don't match.
  static Future<PorcupineManager> fromKeywordPaths(String accessKey,
                                  ^^^^^^^^^^^^^^^^
Target kernel_snapshot_program failed: Exception


FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:compileFlutterBuildDebug'.
> Process 'command 'C:\Users\Michael\flutter\bin\flutter.bat'' finished with non-zero exit value 1

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to generate a Build Scan (Powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 1m 4s
Running Gradle task 'assembleDebug'...                             64,7s
Error: Gradle task assembleDebug failed with exit code 1
