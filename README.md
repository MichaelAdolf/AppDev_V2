PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter run
Launching lib\main.dart on 25028RN03Y in debug mode...
WARNING: Your app uses the following plugins that apply Kotlin Gradle Plugin (KGP): flutter_tts, speech_to_text, wakelock_plus
Future versions of Flutter will fail to build if your app uses plugins that apply KGP.

Please check the changelogs of these plugins and upgrade to a version that supports Built-in Kotlin.
If no such version exists, report the issue to the plugin. If necessary, here is a guide on filing 
an issue against a plugin: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-app-developers#report-incompatible-kotlin-gradle-plugin-usage-to-plugin-authors

If you are a plugin author, please migrate your plugin to Built-in Kotlin using this guide: https://docs.flutter.dev/release/breaking-changes/migrate-to-built-in-kotlin/for-plugin-authors
lib/features/jarvis/ui/home_screen.dart:14:8: Error: Error when reading 'lib/features/jarvis/services/thinking_feedback_service.dart': Das System kann den angegebenen Pfad nicht finden
import '../services/thinking_feedback_service.dart';
       ^
lib/features/jarvis/ui/home_screen.dart:38:9: Error: Type 'ThinkingFeedbackService' not found.
  final ThinkingFeedbackService _thinkingFeedbackService =
        ^^^^^^^^^^^^^^^^^^^^^^^
lib/features/jarvis/ui/home_screen.dart:38:9: Error: 'ThinkingFeedbackService' isn't a type.
  final ThinkingFeedbackService _thinkingFeedbackService =
        ^^^^^^^^^^^^^^^^^^^^^^^
lib/features/jarvis/ui/home_screen.dart:39:7: Error: Method not found: 'ThinkingFeedbackService'.
      ThinkingFeedbackService();
      ^^^^^^^^^^^^^^^^^^^^^^^
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

BUILD FAILED in 1m 18s
Running Gradle task 'assembleDebug'...                             79,0s
Error: Gradle task assembleDebug failed with exit code 1
