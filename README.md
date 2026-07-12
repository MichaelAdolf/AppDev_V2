PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run 
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_foreground_task, flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
lib/services/jarvis_runtime_service.dart:28:48: Error: Cannot invoke a non-'const' factory where a const expression is expected.
Try using a constructor or factory that is 'const'.
        eventAction: ForegroundTaskEventAction.repeat(5000),
                                               ^^^^^^
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

BUILD FAILED in 11s
Running Gradle task 'assembleDebug'...                             11,5s
Error: Gradle task assembleDebug failed with exit code 1
