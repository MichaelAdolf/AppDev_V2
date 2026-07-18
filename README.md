PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter clean
Failed to remove build. A program may still be using a file in the directory or the directory itself.
To find and stop such a program, see:
https://superuser.com/questions/1333118/cant-delete-empty-folder-because-it-is-used
Deleting build...                                                1.110ms
Deleting .dart_tool...                                              81ms
Deleting ephemeral...                                               16ms
Deleting Generated.xcconfig...                                      66ms
Deleting flutter_export_environment.sh...                          113ms
Deleting ephemeral...                                               50ms
Deleting ephemeral...                                               42ms
Deleting ephemeral...                                               18ms
Deleting .flutter-plugins-dependencies...                           18ms
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

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':flutter_voice_processor:checkDebugAarMetadata'.
> A failure occurred while executing com.android.build.gradle.internal.tasks.CheckAarMetadataWorkAction
   > 20 issues were found when checking AAR metadata:

       1.  Dependency 'androidx.fragment:fragment:1.7.1' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       2.  Dependency 'androidx.window:window:1.2.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       3.  Dependency 'androidx.window:window-java:1.2.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       4.  Dependency 'androidx.activity:activity:1.8.1' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       5.  Dependency 'androidx.lifecycle:lifecycle-livedata-core-ktx:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       6.  Dependency 'androidx.lifecycle:lifecycle-livedata:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       7.  Dependency 'androidx.lifecycle:lifecycle-viewmodel:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       8.  Dependency 'androidx.lifecycle:lifecycle-livedata-core:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

       9.  Dependency 'androidx.lifecycle:lifecycle-viewmodel-savedstate:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      10.  Dependency 'androidx.core:core-ktx:1.13.1' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      11.  Dependency 'androidx.core:core:1.13.1' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      12.  Dependency 'androidx.lifecycle:lifecycle-runtime:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      13.  Dependency 'androidx.lifecycle:lifecycle-process:2.7.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      14.  Dependency 'androidx.savedstate:savedstate:1.2.1' requires libraries and applications that
           depend on it to compile against version 33 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 33, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      15.  Dependency 'androidx.annotation:annotation-experimental:1.4.0' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      16.  Dependency 'androidx.profileinstaller:profileinstaller:1.3.1' requires libraries and applications that
           depend on it to compile against version 33 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 33, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      17.  Dependency 'androidx.tracing:tracing:1.2.0' requires libraries and applications that
           depend on it to compile against version 33 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 33, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      18.  Dependency 'androidx.exifinterface:exifinterface:1.4.1' requires libraries and applications that
           depend on it to compile against version 34 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 34, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      19.  Dependency 'androidx.arch.core:core-runtime:2.2.0' requires libraries and applications that
           depend on it to compile against version 33 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 33, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

      20.  Dependency 'androidx.window.extensions.core:core:1.0.0' requires libraries and applications that
           depend on it to compile against version 33 or later of the
           Android APIs.

           :flutter_voice_processor is currently compiled against android-31.

           Recommended action: Update this project to use a newer compileSdk
           of at least 33, for example 36.

           Note that updating a library or application's compileSdk (which
           allows newer APIs to be used) can be done separately from updating
           targetSdk (which opts the app in to new runtime behavior) and
           minSdk (which determines which devices the app can be installed
           on).

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to generate a Build Scan (Powered by Develocity).
> Get more help at https://help.gradle.org.

BUILD FAILED in 1m
Running Gradle task 'assembleDebug'...                             61,4s
Error: Gradle task assembleDebug failed with exit code 1
