# jarvis_app

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Learn Flutter](https://docs.flutter.dev/get-started/learn-flutter)
- [Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Flutter learning resources](https://docs.flutter.dev/reference/learning-resources)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

```
jarvis_app
├─ .metadata
├─ analysis_options.yaml
├─ android
│  ├─ .gradle
│  │  ├─ 9.1.0
│  │  │  ├─ checksums
│  │  │  │  ├─ checksums.lock
│  │  │  │  ├─ md5-checksums.bin
│  │  │  │  └─ sha1-checksums.bin
│  │  │  ├─ executionHistory
│  │  │  │  ├─ executionHistory.bin
│  │  │  │  └─ executionHistory.lock
│  │  │  ├─ expanded
│  │  │  ├─ fileChanges
│  │  │  │  └─ last-build.bin
│  │  │  ├─ fileHashes
│  │  │  │  ├─ fileHashes.bin
│  │  │  │  ├─ fileHashes.lock
│  │  │  │  └─ resourceHashesCache.bin
│  │  │  ├─ gc.properties
│  │  │  └─ vcsMetadata
│  │  ├─ buildOutputCleanup
│  │  │  ├─ buildOutputCleanup.lock
│  │  │  ├─ cache.properties
│  │  │  └─ outputFiles.bin
│  │  ├─ file-system.probe
│  │  ├─ nb-cache
│  │  │  ├─ android-1936318943
│  │  │  │  └─ project-info.ser
│  │  │  ├─ app-95194650
│  │  │  │  └─ project-info.ser
│  │  │  ├─ subprojects.ser
│  │  │  └─ trust
│  │  │     └─ 150E256445646A9450001591087AD2CC8895FBBFE21F0B58201CAD66018FE577
│  │  ├─ noVersion
│  │  │  └─ buildLogic.lock
│  │  └─ vcs-1
│  │     └─ gc.properties
│  ├─ .kotlin
│  │  ├─ errors
│  │  └─ sessions
│  ├─ app
│  │  ├─ build.gradle.kts
│  │  └─ src
│  │     ├─ debug
│  │     │  └─ AndroidManifest.xml
│  │     ├─ main
│  │     │  ├─ AndroidManifest.xml
│  │     │  ├─ java
│  │     │  │  └─ io
│  │     │  │     └─ flutter
│  │     │  │        └─ plugins
│  │     │  │           └─ GeneratedPluginRegistrant.java
│  │     │  ├─ kotlin
│  │     │  │  └─ com
│  │     │  │     └─ example
│  │     │  │        └─ jarvis_app
│  │     │  │           ├─ JarvisBackgroundService.kt
│  │     │  │           ├─ JarvisForegroundService.kt
│  │     │  │           └─ MainActivity.kt
│  │     │  └─ res
│  │     │     ├─ drawable
│  │     │     │  └─ launch_background.xml
│  │     │     ├─ drawable-v21
│  │     │     │  └─ launch_background.xml
│  │     │     ├─ mipmap-hdpi
│  │     │     │  └─ ic_launcher.png
│  │     │     ├─ mipmap-mdpi
│  │     │     │  └─ ic_launcher.png
│  │     │     ├─ mipmap-xhdpi
│  │     │     │  └─ ic_launcher.png
│  │     │     ├─ mipmap-xxhdpi
│  │     │     │  └─ ic_launcher.png
│  │     │     ├─ mipmap-xxxhdpi
│  │     │     │  └─ ic_launcher.png
│  │     │     ├─ values
│  │     │     │  └─ styles.xml
│  │     │     └─ values-night
│  │     │        └─ styles.xml
│  │     └─ profile
│  │        └─ AndroidManifest.xml
│  ├─ build.gradle.kts
│  ├─ gradle
│  │  └─ wrapper
│  │     ├─ gradle-wrapper.jar
│  │     └─ gradle-wrapper.properties
│  ├─ gradle.properties
│  ├─ gradlew
│  ├─ gradlew.bat
│  ├─ local.properties
│  └─ settings.gradle.kts
├─ ios
│  ├─ Flutter
│  │  ├─ AppFrameworkInfo.plist
│  │  ├─ Debug.xcconfig
│  │  ├─ ephemeral
│  │  │  ├─ flutter_lldbinit
│  │  │  ├─ flutter_lldb_helper.py
│  │  │  ├─ flutter_native_integration.env
│  │  │  └─ Packages
│  │  │     ├─ .packages
│  │  │     └─ FlutterGeneratedPluginSwiftPackage
│  │  │        ├─ Package.swift
│  │  │        └─ Sources
│  │  │           └─ FlutterGeneratedPluginSwiftPackage
│  │  │              └─ FlutterGeneratedPluginSwiftPackage.swift
│  │  ├─ flutter_export_environment.sh
│  │  ├─ Generated.xcconfig
│  │  └─ Release.xcconfig
│  ├─ Runner
│  │  ├─ AppDelegate.swift
│  │  ├─ Assets.xcassets
│  │  │  ├─ AppIcon.appiconset
│  │  │  │  ├─ Contents.json
│  │  │  │  ├─ Icon-App-1024x1024@1x.png
│  │  │  │  ├─ Icon-App-20x20@1x.png
│  │  │  │  ├─ Icon-App-20x20@2x.png
│  │  │  │  ├─ Icon-App-20x20@3x.png
│  │  │  │  ├─ Icon-App-29x29@1x.png
│  │  │  │  ├─ Icon-App-29x29@2x.png
│  │  │  │  ├─ Icon-App-29x29@3x.png
│  │  │  │  ├─ Icon-App-40x40@1x.png
│  │  │  │  ├─ Icon-App-40x40@2x.png
│  │  │  │  ├─ Icon-App-40x40@3x.png
│  │  │  │  ├─ Icon-App-60x60@2x.png
│  │  │  │  ├─ Icon-App-60x60@3x.png
│  │  │  │  ├─ Icon-App-76x76@1x.png
│  │  │  │  ├─ Icon-App-76x76@2x.png
│  │  │  │  └─ Icon-App-83.5x83.5@2x.png
│  │  │  └─ LaunchImage.imageset
│  │  │     ├─ Contents.json
│  │  │     ├─ LaunchImage.png
│  │  │     ├─ LaunchImage@2x.png
│  │  │     ├─ LaunchImage@3x.png
│  │  │     └─ README.md
│  │  ├─ Base.lproj
│  │  │  ├─ LaunchScreen.storyboard
│  │  │  └─ Main.storyboard
│  │  ├─ GeneratedPluginRegistrant.h
│  │  ├─ GeneratedPluginRegistrant.m
│  │  ├─ Info.plist
│  │  ├─ Runner-Bridging-Header.h
│  │  └─ SceneDelegate.swift
│  ├─ Runner.xcodeproj
│  │  ├─ project.pbxproj
│  │  ├─ project.xcworkspace
│  │  │  ├─ contents.xcworkspacedata
│  │  │  └─ xcshareddata
│  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │     └─ WorkspaceSettings.xcsettings
│  │  └─ xcshareddata
│  │     └─ xcschemes
│  │        └─ Runner.xcscheme
│  ├─ Runner.xcworkspace
│  │  ├─ contents.xcworkspacedata
│  │  └─ xcshareddata
│  │     ├─ IDEWorkspaceChecks.plist
│  │     └─ WorkspaceSettings.xcsettings
│  └─ RunnerTests
│     └─ RunnerTests.swift
├─ lib
│  ├─ core
│  │  ├─ constants.dart
│  │  ├─ conversation_entry.dart
│  │  ├─ ha_response.dart
│  │  ├─ jarvis_event.dart
│  │  ├─ jarvis_intent.dart
│  │  ├─ jarvis_intent_parser.dart
│  │  ├─ jarvis_state.dart
│  │  ├─ speech_output_mode.dart
│  │  └─ theme.dart
│  ├─ features
│  │  └─ jarvis
│  │     ├─ logic
│  │     │  └─ jarvis_controller.dart
│  │     ├─ ui
│  │     │  └─ home_screen.dart
│  │     └─ widgets
│  │        ├─ ambient_connections.dart
│  │        ├─ ambient_particles.dart
│  │        ├─ background_grid.dart
│  │        ├─ conversation_timeline.dart
│  │        ├─ hud_overlay.dart
│  │        ├─ hud_panel.dart
│  │        ├─ jarvis_circle.dart
│  │        └─ speech_waveform.dart
│  ├─ main.dart
│  ├─ pubspec.lock
│  ├─ services
│  │  ├─ audio_service.dart
│  │  ├─ conversation_service.dart
│  │  ├─ device_wake_service.dart
│  │  ├─ home_assistant_service.dart
│  │  ├─ jarvis_background_bridge.dart
│  │  ├─ jarvis_external_trigger_service.dart
│  │  ├─ jarvis_wakeword_bus.dart
│  │  ├─ jarvis_wakeword_control.dart
│  │  ├─ jarvis_wakeword_service.dart
│  │  ├─ mock_home_assistant_service.dart
│  │  ├─ real_home_assistant_service.dart
│  │  ├─ speech_output_service.dart
│  │  ├─ thinking_feedback_service.dart
│  │  └─ voice_service.dart
│  └─ shared
│     └─ widgets
├─ linux
│  ├─ CMakeLists.txt
│  ├─ flutter
│  │  ├─ CMakeLists.txt
│  │  ├─ ephemeral
│  │  │  └─ .plugin_symlinks
│  │  │     ├─ jni
│  │  │     │  ├─ analysis_options.yaml
│  │  │     │  ├─ android
│  │  │     │  │  ├─ .cxx
│  │  │     │  │  │  ├─ Debug
│  │  │     │  │  │  │  └─ 5h5h3o3w
│  │  │     │  │  │  │     ├─ arm64-v8a
│  │  │     │  │  │  │     │  ├─ .cmake
│  │  │     │  │  │  │     │  │  └─ api
│  │  │     │  │  │  │     │  │     └─ v1
│  │  │     │  │  │  │     │  │        ├─ query
│  │  │     │  │  │  │     │  │        │  └─ client-agp
│  │  │     │  │  │  │     │  │        │     ├─ cache-v2
│  │  │     │  │  │  │     │  │        │     ├─ cmakeFiles-v1
│  │  │     │  │  │  │     │  │        │     └─ codemodel-v2
│  │  │     │  │  │  │     │  │        └─ reply
│  │  │     │  │  │  │     │  │           ├─ cache-v2-f05c7c1fb0cdff075fd2.json
│  │  │     │  │  │  │     │  │           ├─ cmakeFiles-v1-55aafbfe3a72401545d9.json
│  │  │     │  │  │  │     │  │           ├─ codemodel-v2-16547c5b470ca935e2b8.json
│  │  │     │  │  │  │     │  │           ├─ directory-.-Debug-d0094a50bb2071803777.json
│  │  │     │  │  │  │     │  │           ├─ index-2026-07-18T09-22-57-0122.json
│  │  │     │  │  │  │     │  │           └─ target-jni-Debug-ddc91ce5d5a83b3481e8.json
│  │  │     │  │  │  │     │  ├─ .ninja_deps
│  │  │     │  │  │  │     │  ├─ .ninja_log
│  │  │     │  │  │  │     │  ├─ additional_project_files.txt
│  │  │     │  │  │  │     │  ├─ android_gradle_build.json
│  │  │     │  │  │  │     │  ├─ android_gradle_build_mini.json
│  │  │     │  │  │  │     │  ├─ build.ninja
│  │  │     │  │  │  │     │  ├─ build_file_index.txt
│  │  │     │  │  │  │     │  ├─ CMakeCache.txt
│  │  │     │  │  │  │     │  ├─ CMakeFiles
│  │  │     │  │  │  │     │  │  ├─ 3.22.1-g37088a8-dirty
│  │  │     │  │  │  │     │  │  │  ├─ CMakeCCompiler.cmake
│  │  │     │  │  │  │     │  │  │  ├─ CMakeDetermineCompilerABI_C.bin
│  │  │     │  │  │  │     │  │  │  ├─ CMakeSystem.cmake
│  │  │     │  │  │  │     │  │  │  └─ CompilerIdC
│  │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.c
│  │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.o
│  │  │     │  │  │  │     │  │  │     └─ tmp
│  │  │     │  │  │  │     │  │  ├─ cmake.check_cache
│  │  │     │  │  │  │     │  │  ├─ CMakeTmp
│  │  │     │  │  │  │     │  │  ├─ jni.dir
│  │  │     │  │  │  │     │  │  │  ├─ dartjni.c.o
│  │  │     │  │  │  │     │  │  │  ├─ include
│  │  │     │  │  │  │     │  │  │  │  └─ dart_api_dl.c.o
│  │  │     │  │  │  │     │  │  │  └─ third_party
│  │  │     │  │  │  │     │  │  │     └─ global_jni_env.c.o
│  │  │     │  │  │  │     │  │  ├─ rules.ninja
│  │  │     │  │  │  │     │  │  └─ TargetDirectories.txt
│  │  │     │  │  │  │     │  ├─ cmake_install.cmake
│  │  │     │  │  │  │     │  ├─ compile_commands.json
│  │  │     │  │  │  │     │  ├─ compile_commands.json.bin
│  │  │     │  │  │  │     │  ├─ configure_fingerprint.bin
│  │  │     │  │  │  │     │  ├─ metadata_generation_command.txt
│  │  │     │  │  │  │     │  ├─ prefab_config.json
│  │  │     │  │  │  │     │  └─ symbol_folder_index.txt
│  │  │     │  │  │  │     ├─ armeabi-v7a
│  │  │     │  │  │  │     │  ├─ .cmake
│  │  │     │  │  │  │     │  │  └─ api
│  │  │     │  │  │  │     │  │     └─ v1
│  │  │     │  │  │  │     │  │        ├─ query
│  │  │     │  │  │  │     │  │        │  └─ client-agp
│  │  │     │  │  │  │     │  │        │     ├─ cache-v2
│  │  │     │  │  │  │     │  │        │     ├─ cmakeFiles-v1
│  │  │     │  │  │  │     │  │        │     └─ codemodel-v2
│  │  │     │  │  │  │     │  │        └─ reply
│  │  │     │  │  │  │     │  │           ├─ cache-v2-a459056d10074e395e6f.json
│  │  │     │  │  │  │     │  │           ├─ cmakeFiles-v1-10732f32faa124b640eb.json
│  │  │     │  │  │  │     │  │           ├─ codemodel-v2-5f4152ddd7832a335f0b.json
│  │  │     │  │  │  │     │  │           ├─ directory-.-Debug-d0094a50bb2071803777.json
│  │  │     │  │  │  │     │  │           ├─ index-2026-07-18T09-22-59-0725.json
│  │  │     │  │  │  │     │  │           └─ target-jni-Debug-372e5383e0cf9081c74c.json
│  │  │     │  │  │  │     │  ├─ .ninja_deps
│  │  │     │  │  │  │     │  ├─ .ninja_log
│  │  │     │  │  │  │     │  ├─ additional_project_files.txt
│  │  │     │  │  │  │     │  ├─ android_gradle_build.json
│  │  │     │  │  │  │     │  ├─ android_gradle_build_mini.json
│  │  │     │  │  │  │     │  ├─ build.ninja
│  │  │     │  │  │  │     │  ├─ build_file_index.txt
│  │  │     │  │  │  │     │  ├─ CMakeCache.txt
│  │  │     │  │  │  │     │  ├─ CMakeFiles
│  │  │     │  │  │  │     │  │  ├─ 3.22.1-g37088a8-dirty
│  │  │     │  │  │  │     │  │  │  ├─ CMakeCCompiler.cmake
│  │  │     │  │  │  │     │  │  │  ├─ CMakeDetermineCompilerABI_C.bin
│  │  │     │  │  │  │     │  │  │  ├─ CMakeSystem.cmake
│  │  │     │  │  │  │     │  │  │  └─ CompilerIdC
│  │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.c
│  │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.o
│  │  │     │  │  │  │     │  │  │     └─ tmp
│  │  │     │  │  │  │     │  │  ├─ cmake.check_cache
│  │  │     │  │  │  │     │  │  ├─ CMakeTmp
│  │  │     │  │  │  │     │  │  ├─ jni.dir
│  │  │     │  │  │  │     │  │  │  ├─ dartjni.c.o
│  │  │     │  │  │  │     │  │  │  ├─ include
│  │  │     │  │  │  │     │  │  │  │  └─ dart_api_dl.c.o
│  │  │     │  │  │  │     │  │  │  └─ third_party
│  │  │     │  │  │  │     │  │  │     └─ global_jni_env.c.o
│  │  │     │  │  │  │     │  │  ├─ rules.ninja
│  │  │     │  │  │  │     │  │  └─ TargetDirectories.txt
│  │  │     │  │  │  │     │  ├─ cmake_install.cmake
│  │  │     │  │  │  │     │  ├─ compile_commands.json
│  │  │     │  │  │  │     │  ├─ compile_commands.json.bin
│  │  │     │  │  │  │     │  ├─ configure_fingerprint.bin
│  │  │     │  │  │  │     │  ├─ metadata_generation_command.txt
│  │  │     │  │  │  │     │  ├─ prefab_config.json
│  │  │     │  │  │  │     │  └─ symbol_folder_index.txt
│  │  │     │  │  │  │     ├─ hash_key.txt
│  │  │     │  │  │  │     ├─ x86
│  │  │     │  │  │  │     │  ├─ .cmake
│  │  │     │  │  │  │     │  │  └─ api
│  │  │     │  │  │  │     │  │     └─ v1
│  │  │     │  │  │  │     │  │        ├─ query
│  │  │     │  │  │  │     │  │        │  └─ client-agp
│  │  │     │  │  │  │     │  │        │     ├─ cache-v2
│  │  │     │  │  │  │     │  │        │     ├─ cmakeFiles-v1
│  │  │     │  │  │  │     │  │        │     └─ codemodel-v2
│  │  │     │  │  │  │     │  │        └─ reply
│  │  │     │  │  │  │     │  │           ├─ cache-v2-415322deaeb6dba77bb8.json
│  │  │     │  │  │  │     │  │           ├─ cmakeFiles-v1-bcd3d11348c1b573392d.json
│  │  │     │  │  │  │     │  │           ├─ codemodel-v2-90291965cbd0c9882e73.json
│  │  │     │  │  │  │     │  │           ├─ directory-.-Debug-d0094a50bb2071803777.json
│  │  │     │  │  │  │     │  │           ├─ index-2026-07-18T09-23-02-0341.json
│  │  │     │  │  │  │     │  │           └─ target-jni-Debug-04336afdec6a8716c903.json
│  │  │     │  │  │  │     │  ├─ .ninja_deps
│  │  │     │  │  │  │     │  ├─ .ninja_log
│  │  │     │  │  │  │     │  ├─ additional_project_files.txt
│  │  │     │  │  │  │     │  ├─ android_gradle_build.json
│  │  │     │  │  │  │     │  ├─ android_gradle_build_mini.json
│  │  │     │  │  │  │     │  ├─ build.ninja
│  │  │     │  │  │  │     │  ├─ build_file_index.txt
│  │  │     │  │  │  │     │  ├─ CMakeCache.txt
│  │  │     │  │  │  │     │  ├─ CMakeFiles
│  │  │     │  │  │  │     │  │  ├─ 3.22.1-g37088a8-dirty
│  │  │     │  │  │  │     │  │  │  ├─ CMakeCCompiler.cmake
│  │  │     │  │  │  │     │  │  │  ├─ CMakeDetermineCompilerABI_C.bin
│  │  │     │  │  │  │     │  │  │  ├─ CMakeSystem.cmake
│  │  │     │  │  │  │     │  │  │  └─ CompilerIdC
│  │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.c
│  │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.o
│  │  │     │  │  │  │     │  │  │     └─ tmp
│  │  │     │  │  │  │     │  │  ├─ cmake.check_cache
│  │  │     │  │  │  │     │  │  ├─ CMakeTmp
│  │  │     │  │  │  │     │  │  ├─ jni.dir
│  │  │     │  │  │  │     │  │  │  ├─ dartjni.c.o
│  │  │     │  │  │  │     │  │  │  ├─ include
│  │  │     │  │  │  │     │  │  │  │  └─ dart_api_dl.c.o
│  │  │     │  │  │  │     │  │  │  └─ third_party
│  │  │     │  │  │  │     │  │  │     └─ global_jni_env.c.o
│  │  │     │  │  │  │     │  │  ├─ rules.ninja
│  │  │     │  │  │  │     │  │  └─ TargetDirectories.txt
│  │  │     │  │  │  │     │  ├─ cmake_install.cmake
│  │  │     │  │  │  │     │  ├─ compile_commands.json
│  │  │     │  │  │  │     │  ├─ compile_commands.json.bin
│  │  │     │  │  │  │     │  ├─ configure_fingerprint.bin
│  │  │     │  │  │  │     │  ├─ metadata_generation_command.txt
│  │  │     │  │  │  │     │  ├─ prefab_config.json
│  │  │     │  │  │  │     │  └─ symbol_folder_index.txt
│  │  │     │  │  │  │     └─ x86_64
│  │  │     │  │  │  │        ├─ .cmake
│  │  │     │  │  │  │        │  └─ api
│  │  │     │  │  │  │        │     └─ v1
│  │  │     │  │  │  │        │        ├─ query
│  │  │     │  │  │  │        │        │  └─ client-agp
│  │  │     │  │  │  │        │        │     ├─ cache-v2
│  │  │     │  │  │  │        │        │     ├─ cmakeFiles-v1
│  │  │     │  │  │  │        │        │     └─ codemodel-v2
│  │  │     │  │  │  │        │        └─ reply
│  │  │     │  │  │  │        │           ├─ cache-v2-060598f8a2545faaa1c8.json
│  │  │     │  │  │  │        │           ├─ cmakeFiles-v1-ad7f91c0dd7c473dd9a7.json
│  │  │     │  │  │  │        │           ├─ codemodel-v2-0c05986467f230caea39.json
│  │  │     │  │  │  │        │           ├─ directory-.-Debug-d0094a50bb2071803777.json
│  │  │     │  │  │  │        │           ├─ index-2026-07-18T09-23-05-0151.json
│  │  │     │  │  │  │        │           └─ target-jni-Debug-33d293cdc5f5868a4768.json
│  │  │     │  │  │  │        ├─ .ninja_deps
│  │  │     │  │  │  │        ├─ .ninja_log
│  │  │     │  │  │  │        ├─ additional_project_files.txt
│  │  │     │  │  │  │        ├─ android_gradle_build.json
│  │  │     │  │  │  │        ├─ android_gradle_build_mini.json
│  │  │     │  │  │  │        ├─ build.ninja
│  │  │     │  │  │  │        ├─ build_file_index.txt
│  │  │     │  │  │  │        ├─ CMakeCache.txt
│  │  │     │  │  │  │        ├─ CMakeFiles
│  │  │     │  │  │  │        │  ├─ 3.22.1-g37088a8-dirty
│  │  │     │  │  │  │        │  │  ├─ CMakeCCompiler.cmake
│  │  │     │  │  │  │        │  │  ├─ CMakeDetermineCompilerABI_C.bin
│  │  │     │  │  │  │        │  │  ├─ CMakeSystem.cmake
│  │  │     │  │  │  │        │  │  └─ CompilerIdC
│  │  │     │  │  │  │        │  │     ├─ CMakeCCompilerId.c
│  │  │     │  │  │  │        │  │     ├─ CMakeCCompilerId.o
│  │  │     │  │  │  │        │  │     └─ tmp
│  │  │     │  │  │  │        │  ├─ cmake.check_cache
│  │  │     │  │  │  │        │  ├─ CMakeTmp
│  │  │     │  │  │  │        │  ├─ jni.dir
│  │  │     │  │  │  │        │  │  ├─ dartjni.c.o
│  │  │     │  │  │  │        │  │  ├─ include
│  │  │     │  │  │  │        │  │  │  └─ dart_api_dl.c.o
│  │  │     │  │  │  │        │  │  └─ third_party
│  │  │     │  │  │  │        │  │     └─ global_jni_env.c.o
│  │  │     │  │  │  │        │  ├─ rules.ninja
│  │  │     │  │  │  │        │  └─ TargetDirectories.txt
│  │  │     │  │  │  │        ├─ cmake_install.cmake
│  │  │     │  │  │  │        ├─ compile_commands.json
│  │  │     │  │  │  │        ├─ compile_commands.json.bin
│  │  │     │  │  │  │        ├─ configure_fingerprint.bin
│  │  │     │  │  │  │        ├─ metadata_generation_command.txt
│  │  │     │  │  │  │        ├─ prefab_config.json
│  │  │     │  │  │  │        └─ symbol_folder_index.txt
│  │  │     │  │  │  └─ tools
│  │  │     │  │  │     └─ profile
│  │  │     │  │  │        ├─ arm64-v8a
│  │  │     │  │  │        │  └─ compile_commands.json
│  │  │     │  │  │        ├─ armeabi-v7a
│  │  │     │  │  │        │  └─ compile_commands.json
│  │  │     │  │  │        ├─ x86
│  │  │     │  │  │        │  └─ compile_commands.json
│  │  │     │  │  │        └─ x86_64
│  │  │     │  │  │           └─ compile_commands.json
│  │  │     │  │  ├─ build.gradle
│  │  │     │  │  ├─ consumer-rules.pro
│  │  │     │  │  ├─ README.md
│  │  │     │  │  ├─ settings.gradle
│  │  │     │  │  └─ src
│  │  │     │  │     └─ main
│  │  │     │  │        ├─ AndroidManifest.xml
│  │  │     │  │        └─ java
│  │  │     │  │           └─ com
│  │  │     │  │              └─ github
│  │  │     │  │                 └─ dart_lang
│  │  │     │  │                    └─ jni
│  │  │     │  │                       └─ JniPlugin.java
│  │  │     │  ├─ bin
│  │  │     │  │  └─ setup.dart
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ dart_test.yaml
│  │  │     │  ├─ example
│  │  │     │  │  ├─ analysis_options.yaml
│  │  │     │  │  ├─ android
│  │  │     │  │  │  ├─ app
│  │  │     │  │  │  │  ├─ build.gradle
│  │  │     │  │  │  │  └─ src
│  │  │     │  │  │  │     ├─ debug
│  │  │     │  │  │  │     │  └─ AndroidManifest.xml
│  │  │     │  │  │  │     ├─ main
│  │  │     │  │  │  │     │  ├─ AndroidManifest.xml
│  │  │     │  │  │  │     │  ├─ java
│  │  │     │  │  │  │     │  │  ├─ com
│  │  │     │  │  │  │     │  │  │  └─ github
│  │  │     │  │  │  │     │  │  │     └─ dart_lang
│  │  │     │  │  │  │     │  │  │        └─ jni_example
│  │  │     │  │  │  │     │  │  │           └─ Toaster.java
│  │  │     │  │  │  │     │  │  └─ io
│  │  │     │  │  │  │     │  │     └─ flutter
│  │  │     │  │  │  │     │  │        └─ plugins
│  │  │     │  │  │  │     │  ├─ kotlin
│  │  │     │  │  │  │     │  │  └─ dev
│  │  │     │  │  │  │     │  │     └─ dart
│  │  │     │  │  │  │     │  │        └─ jni_example
│  │  │     │  │  │  │     │  │           └─ MainActivity.kt
│  │  │     │  │  │  │     │  └─ res
│  │  │     │  │  │  │     │     ├─ drawable
│  │  │     │  │  │  │     │     │  └─ launch_background.xml
│  │  │     │  │  │  │     │     ├─ drawable-v21
│  │  │     │  │  │  │     │     │  └─ launch_background.xml
│  │  │     │  │  │  │     │     ├─ mipmap-hdpi
│  │  │     │  │  │  │     │     │  └─ ic_launcher.png
│  │  │     │  │  │  │     │     ├─ mipmap-mdpi
│  │  │     │  │  │  │     │     │  └─ ic_launcher.png
│  │  │     │  │  │  │     │     ├─ mipmap-xhdpi
│  │  │     │  │  │  │     │     │  └─ ic_launcher.png
│  │  │     │  │  │  │     │     ├─ mipmap-xxhdpi
│  │  │     │  │  │  │     │     │  └─ ic_launcher.png
│  │  │     │  │  │  │     │     ├─ mipmap-xxxhdpi
│  │  │     │  │  │  │     │     │  └─ ic_launcher.png
│  │  │     │  │  │  │     │     ├─ values
│  │  │     │  │  │  │     │     │  └─ styles.xml
│  │  │     │  │  │  │     │     └─ values-night
│  │  │     │  │  │  │     │        └─ styles.xml
│  │  │     │  │  │  │     └─ profile
│  │  │     │  │  │  │        └─ AndroidManifest.xml
│  │  │     │  │  │  ├─ build.gradle
│  │  │     │  │  │  ├─ gradle
│  │  │     │  │  │  │  └─ wrapper
│  │  │     │  │  │  │     └─ gradle-wrapper.properties
│  │  │     │  │  │  ├─ gradle.properties
│  │  │     │  │  │  └─ settings.gradle
│  │  │     │  │  ├─ integration_test
│  │  │     │  │  │  └─ on_device_jni_test.dart
│  │  │     │  │  ├─ lib
│  │  │     │  │  │  └─ main.dart
│  │  │     │  │  ├─ linux
│  │  │     │  │  │  ├─ CMakeLists.txt
│  │  │     │  │  │  ├─ flutter
│  │  │     │  │  │  │  └─ CMakeLists.txt
│  │  │     │  │  │  ├─ main.cc
│  │  │     │  │  │  ├─ my_application.cc
│  │  │     │  │  │  └─ my_application.h
│  │  │     │  │  ├─ macos
│  │  │     │  │  │  ├─ Flutter
│  │  │     │  │  │  │  ├─ Flutter-Debug.xcconfig
│  │  │     │  │  │  │  └─ Flutter-Release.xcconfig
│  │  │     │  │  │  ├─ Podfile
│  │  │     │  │  │  ├─ Runner
│  │  │     │  │  │  │  ├─ AppDelegate.swift
│  │  │     │  │  │  │  ├─ Assets.xcassets
│  │  │     │  │  │  │  │  └─ AppIcon.appiconset
│  │  │     │  │  │  │  │     ├─ app_icon_1024.png
│  │  │     │  │  │  │  │     ├─ app_icon_128.png
│  │  │     │  │  │  │  │     ├─ app_icon_16.png
│  │  │     │  │  │  │  │     ├─ app_icon_256.png
│  │  │     │  │  │  │  │     ├─ app_icon_32.png
│  │  │     │  │  │  │  │     ├─ app_icon_512.png
│  │  │     │  │  │  │  │     ├─ app_icon_64.png
│  │  │     │  │  │  │  │     └─ Contents.json
│  │  │     │  │  │  │  ├─ Base.lproj
│  │  │     │  │  │  │  │  └─ MainMenu.xib
│  │  │     │  │  │  │  ├─ Configs
│  │  │     │  │  │  │  │  ├─ AppInfo.xcconfig
│  │  │     │  │  │  │  │  ├─ Debug.xcconfig
│  │  │     │  │  │  │  │  ├─ Release.xcconfig
│  │  │     │  │  │  │  │  └─ Warnings.xcconfig
│  │  │     │  │  │  │  ├─ DebugProfile.entitlements
│  │  │     │  │  │  │  ├─ Info.plist
│  │  │     │  │  │  │  ├─ MainFlutterWindow.swift
│  │  │     │  │  │  │  └─ Release.entitlements
│  │  │     │  │  │  ├─ Runner.xcodeproj
│  │  │     │  │  │  │  ├─ project.pbxproj
│  │  │     │  │  │  │  ├─ project.xcworkspace
│  │  │     │  │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │  │     └─ IDEWorkspaceChecks.plist
│  │  │     │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │     └─ xcschemes
│  │  │     │  │  │  │        └─ Runner.xcscheme
│  │  │     │  │  │  └─ Runner.xcworkspace
│  │  │     │  │  │     ├─ contents.xcworkspacedata
│  │  │     │  │  │     └─ xcshareddata
│  │  │     │  │  │        └─ IDEWorkspaceChecks.plist
│  │  │     │  │  ├─ pubspec.yaml
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ windows
│  │  │     │  │     ├─ CMakeLists.txt
│  │  │     │  │     ├─ flutter
│  │  │     │  │     │  └─ CMakeLists.txt
│  │  │     │  │     └─ runner
│  │  │     │  │        ├─ CMakeLists.txt
│  │  │     │  │        ├─ flutter_window.cpp
│  │  │     │  │        ├─ flutter_window.h
│  │  │     │  │        ├─ main.cpp
│  │  │     │  │        ├─ resource.h
│  │  │     │  │        ├─ resources
│  │  │     │  │        │  └─ app_icon.ico
│  │  │     │  │        ├─ runner.exe.manifest
│  │  │     │  │        ├─ Runner.rc
│  │  │     │  │        ├─ utils.cpp
│  │  │     │  │        ├─ utils.h
│  │  │     │  │        ├─ win32_window.cpp
│  │  │     │  │        └─ win32_window.h
│  │  │     │  ├─ ffigen.yaml
│  │  │     │  ├─ ffigen_exts.yaml
│  │  │     │  ├─ java
│  │  │     │  │  ├─ build.gradle.kts
│  │  │     │  │  ├─ gradle
│  │  │     │  │  │  ├─ libs.versions.toml
│  │  │     │  │  │  └─ wrapper
│  │  │     │  │  │     ├─ gradle-wrapper.jar
│  │  │     │  │  │     └─ gradle-wrapper.properties
│  │  │     │  │  ├─ gradlew
│  │  │     │  │  ├─ gradlew.bat
│  │  │     │  │  ├─ README.md
│  │  │     │  │  ├─ settings.gradle.kts
│  │  │     │  │  ├─ src
│  │  │     │  │  │  └─ main
│  │  │     │  │  │     └─ java
│  │  │     │  │  │        └─ com
│  │  │     │  │  │           └─ github
│  │  │     │  │  │              └─ dart_lang
│  │  │     │  │  │                 └─ jni
│  │  │     │  │  │                    ├─ JniUtils.java
│  │  │     │  │  │                    ├─ PortCleaner.java
│  │  │     │  │  │                    ├─ PortContinuation.java
│  │  │     │  │  │                    └─ PortProxyBuilder.java
│  │  │     │  │  └─ ~
│  │  │     │  │     └─ dev
│  │  │     │  │        ├─ native
│  │  │     │  │        │  └─ native
│  │  │     │  │        │     └─ pkgs
│  │  │     │  │        │        └─ jnigen
│  │  │     │  │        │           └─ example
│  │  │     │  │        │              └─ pdfbox_plugin
│  │  │     │  │        │                 └─ dart_example
│  │  │     │  │        └─ native2
│  │  │     │  │           └─ pkgs
│  │  │     │  │              └─ jnigen
│  │  │     │  │                 └─ example
│  │  │     │  │                    └─ pdfbox_plugin
│  │  │     │  │                       └─ dart_example
│  │  │     │  ├─ lib
│  │  │     │  │  ├─ jni.dart
│  │  │     │  │  ├─ jni_symbols.yaml
│  │  │     │  │  ├─ src
│  │  │     │  │  │  ├─ accessors.dart
│  │  │     │  │  │  ├─ build_util
│  │  │     │  │  │  │  └─ build_util.dart
│  │  │     │  │  │  ├─ core_bindings.dart
│  │  │     │  │  │  ├─ errors.dart
│  │  │     │  │  │  ├─ jarray.dart
│  │  │     │  │  │  ├─ jclass.dart
│  │  │     │  │  │  ├─ jimplementer.dart
│  │  │     │  │  │  ├─ jni.dart
│  │  │     │  │  │  ├─ jobject.dart
│  │  │     │  │  │  ├─ jprimitives.dart
│  │  │     │  │  │  ├─ jreference.dart
│  │  │     │  │  │  ├─ jvalues.dart
│  │  │     │  │  │  ├─ kotlin.dart
│  │  │     │  │  │  ├─ lang
│  │  │     │  │  │  │  ├─ jboolean.dart
│  │  │     │  │  │  │  ├─ jbyte.dart
│  │  │     │  │  │  │  ├─ jcharacter.dart
│  │  │     │  │  │  │  ├─ jdouble.dart
│  │  │     │  │  │  │  ├─ jfloat.dart
│  │  │     │  │  │  │  ├─ jinteger.dart
│  │  │     │  │  │  │  ├─ jlong.dart
│  │  │     │  │  │  │  ├─ jnumber.dart
│  │  │     │  │  │  │  ├─ jshort.dart
│  │  │     │  │  │  │  ├─ jstring.dart
│  │  │     │  │  │  │  └─ lang.dart
│  │  │     │  │  │  ├─ method_invocation.dart
│  │  │     │  │  │  ├─ nio
│  │  │     │  │  │  │  ├─ jbuffer.dart
│  │  │     │  │  │  │  ├─ jbyte_buffer.dart
│  │  │     │  │  │  │  └─ nio.dart
│  │  │     │  │  │  ├─ primitive_jarrays.dart
│  │  │     │  │  │  ├─ third_party
│  │  │     │  │  │  │  ├─ generated_bindings.dart
│  │  │     │  │  │  │  ├─ global_env_extensions.dart
│  │  │     │  │  │  │  └─ jni_bindings_generated.dart
│  │  │     │  │  │  ├─ types.dart
│  │  │     │  │  │  ├─ util
│  │  │     │  │  │  │  ├─ jiterator.dart
│  │  │     │  │  │  │  ├─ jlist.dart
│  │  │     │  │  │  │  ├─ jmap.dart
│  │  │     │  │  │  │  ├─ jset.dart
│  │  │     │  │  │  │  └─ util.dart
│  │  │     │  │  │  └─ version_check.dart
│  │  │     │  │  └─ _internal.dart
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ linux
│  │  │     │  │  └─ CMakeLists.txt
│  │  │     │  ├─ pubspec.yaml
│  │  │     │  ├─ README.md
│  │  │     │  ├─ src
│  │  │     │  │  ├─ CMakeLists.txt
│  │  │     │  │  ├─ dartjni.c
│  │  │     │  │  ├─ dartjni.h
│  │  │     │  │  ├─ include
│  │  │     │  │  │  ├─ analyze_snapshot_api.h
│  │  │     │  │  │  ├─ bin
│  │  │     │  │  │  │  ├─ dart_io_api.h
│  │  │     │  │  │  │  └─ native_assets_api.h
│  │  │     │  │  │  ├─ BUILD.gn
│  │  │     │  │  │  ├─ dart_api.h
│  │  │     │  │  │  ├─ dart_api_dl.c
│  │  │     │  │  │  ├─ dart_api_dl.h
│  │  │     │  │  │  ├─ dart_embedder_api.h
│  │  │     │  │  │  ├─ dart_native_api.h
│  │  │     │  │  │  ├─ dart_tools_api.h
│  │  │     │  │  │  ├─ dart_version.h
│  │  │     │  │  │  └─ internal
│  │  │     │  │  │     └─ dart_api_dl_impl.h
│  │  │     │  │  ├─ jni_constants.h
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ third_party
│  │  │     │  │     ├─ global_jni_env.c
│  │  │     │  │     └─ global_jni_env.h
│  │  │     │  ├─ test
│  │  │     │  │  ├─ boxed_test.dart
│  │  │     │  │  ├─ debug_release_test.dart
│  │  │     │  │  ├─ exception_test.dart
│  │  │     │  │  ├─ global_env_test.dart
│  │  │     │  │  ├─ isolate_test.dart
│  │  │     │  │  ├─ jarray_test.dart
│  │  │     │  │  ├─ jbyte_buffer_test.dart
│  │  │     │  │  ├─ jlist_test.dart
│  │  │     │  │  ├─ jmap_test.dart
│  │  │     │  │  ├─ jobject_test.dart
│  │  │     │  │  ├─ jset_test.dart
│  │  │     │  │  ├─ jstring_test.dart
│  │  │     │  │  ├─ load_test.dart
│  │  │     │  │  ├─ test_util
│  │  │     │  │  │  └─ test_util.dart
│  │  │     │  │  ├─ version_check
│  │  │     │  │  │  ├─ fail_major.dart
│  │  │     │  │  │  ├─ fail_minor.dart
│  │  │     │  │  │  └─ pass.dart
│  │  │     │  │  └─ version_check_test.dart
│  │  │     │  ├─ third_party
│  │  │     │  │  └─ jni.h
│  │  │     │  ├─ tool
│  │  │     │  │  ├─ generate_ffi_bindings.dart
│  │  │     │  │  ├─ generate_ide_files.dart
│  │  │     │  │  ├─ generate_jni_bindings.dart
│  │  │     │  │  ├─ generate_primitive_arrays.dart
│  │  │     │  │  └─ wrapper_generators
│  │  │     │  │     ├─ ffigen_util.dart
│  │  │     │  │     ├─ generate_c_extensions.dart
│  │  │     │  │     ├─ generate_dart_extensions.dart
│  │  │     │  │     ├─ generate_helper_functions.dart
│  │  │     │  │     └─ logging.dart
│  │  │     │  └─ windows
│  │  │     │     └─ CMakeLists.txt
│  │  │     ├─ package_info_plus
│  │  │     │  ├─ android
│  │  │     │  │  ├─ .gradle
│  │  │     │  │  │  ├─ 9.3.0
│  │  │     │  │  │  │  ├─ checksums
│  │  │     │  │  │  │  │  └─ checksums.lock
│  │  │     │  │  │  │  ├─ expanded
│  │  │     │  │  │  │  ├─ fileChanges
│  │  │     │  │  │  │  │  └─ last-build.bin
│  │  │     │  │  │  │  ├─ fileHashes
│  │  │     │  │  │  │  │  ├─ fileHashes.bin
│  │  │     │  │  │  │  │  └─ fileHashes.lock
│  │  │     │  │  │  │  ├─ gc.properties
│  │  │     │  │  │  │  └─ vcsMetadata
│  │  │     │  │  │  ├─ buildOutputCleanup
│  │  │     │  │  │  │  ├─ buildOutputCleanup.lock
│  │  │     │  │  │  │  └─ cache.properties
│  │  │     │  │  │  ├─ nb-cache
│  │  │     │  │  │  │  └─ trust
│  │  │     │  │  │  │     ├─ 1091BD2091310B8B25A9BB02CA8EECB26410AB1EAB7B592369DAC1440802511E
│  │  │     │  │  │  │     └─ 5F331A9272FAC7AF948AEF82359CA442D42F889C4AC427E416A0DD4E37DF2D11
│  │  │     │  │  │  └─ vcs-1
│  │  │     │  │  │     └─ gc.properties
│  │  │     │  │  ├─ build.gradle.kts
│  │  │     │  │  ├─ gradle.properties
│  │  │     │  │  ├─ settings.gradle.kts
│  │  │     │  │  └─ src
│  │  │     │  │     └─ main
│  │  │     │  │        ├─ AndroidManifest.xml
│  │  │     │  │        └─ kotlin
│  │  │     │  │           └─ dev
│  │  │     │  │              └─ fluttercommunity
│  │  │     │  │                 └─ plus
│  │  │     │  │                    └─ packageinfo
│  │  │     │  │                       └─ PackageInfoPlugin.kt
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ example
│  │  │     │  │  ├─ analysis_options.yaml
│  │  │     │  │  ├─ android
│  │  │     │  │  │  ├─ app
│  │  │     │  │  │  │  ├─ build.gradle.kts
│  │  │     │  │  │  │  └─ src
│  │  │     │  │  │  │     ├─ androidTest
│  │  │     │  │  │  │     │  └─ java
│  │  │     │  │  │  │     │     └─ io
│  │  │     │  │  │  │     │        └─ flutter
│  │  │     │  │  │  │     │           └─ plugins
│  │  │     │  │  │  │     │              └─ packageinfoexample
│  │  │     │  │  │  │     │                 ├─ EmbedderV1ActivityTest.java
│  │  │     │  │  │  │     │                 └─ MainActivityTest.java
│  │  │     │  │  │  │     └─ main
│  │  │     │  │  │  │        ├─ AndroidManifest.xml
│  │  │     │  │  │  │        ├─ java
│  │  │     │  │  │  │        │  └─ io
│  │  │     │  │  │  │        │     └─ flutter
│  │  │     │  │  │  │        │        └─ plugins
│  │  │     │  │  │  │        └─ res
│  │  │     │  │  │  │           ├─ mipmap-hdpi
│  │  │     │  │  │  │           │  └─ ic_launcher.png
│  │  │     │  │  │  │           ├─ mipmap-mdpi
│  │  │     │  │  │  │           │  └─ ic_launcher.png
│  │  │     │  │  │  │           ├─ mipmap-xhdpi
│  │  │     │  │  │  │           │  └─ ic_launcher.png
│  │  │     │  │  │  │           ├─ mipmap-xxhdpi
│  │  │     │  │  │  │           │  └─ ic_launcher.png
│  │  │     │  │  │  │           └─ mipmap-xxxhdpi
│  │  │     │  │  │  │              └─ ic_launcher.png
│  │  │     │  │  │  ├─ build.gradle.kts
│  │  │     │  │  │  ├─ gradle
│  │  │     │  │  │  │  └─ wrapper
│  │  │     │  │  │  │     └─ gradle-wrapper.properties
│  │  │     │  │  │  ├─ gradle.properties
│  │  │     │  │  │  └─ settings.gradle.kts
│  │  │     │  │  ├─ build.yaml
│  │  │     │  │  ├─ integration_test
│  │  │     │  │  │  ├─ driver.dart
│  │  │     │  │  │  ├─ package_info_plus_test.dart
│  │  │     │  │  │  ├─ package_info_plus_web_test.dart
│  │  │     │  │  │  └─ package_info_plus_web_test.mocks.dart
│  │  │     │  │  ├─ ios
│  │  │     │  │  │  ├─ Flutter
│  │  │     │  │  │  │  ├─ AppFrameworkInfo.plist
│  │  │     │  │  │  │  ├─ Debug.xcconfig
│  │  │     │  │  │  │  └─ Release.xcconfig
│  │  │     │  │  │  ├─ Runner
│  │  │     │  │  │  │  ├─ AppDelegate.swift
│  │  │     │  │  │  │  ├─ Assets.xcassets
│  │  │     │  │  │  │  │  ├─ AppIcon.appiconset
│  │  │     │  │  │  │  │  │  ├─ Contents.json
│  │  │     │  │  │  │  │  │  ├─ Icon-App-1024x1024@1x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@1x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@2x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@3x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@1x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@2x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@3x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@1x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@2x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@3x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-60x60@2x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-60x60@3x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-76x76@1x.png
│  │  │     │  │  │  │  │  │  ├─ Icon-App-76x76@2x.png
│  │  │     │  │  │  │  │  │  └─ Icon-App-83.5x83.5@2x.png
│  │  │     │  │  │  │  │  └─ LaunchImage.imageset
│  │  │     │  │  │  │  │     ├─ Contents.json
│  │  │     │  │  │  │  │     ├─ LaunchImage.png
│  │  │     │  │  │  │  │     ├─ LaunchImage@2x.png
│  │  │     │  │  │  │  │     ├─ LaunchImage@3x.png
│  │  │     │  │  │  │  │     └─ README.md
│  │  │     │  │  │  │  ├─ Base.lproj
│  │  │     │  │  │  │  │  ├─ LaunchScreen.storyboard
│  │  │     │  │  │  │  │  └─ Main.storyboard
│  │  │     │  │  │  │  ├─ Info.plist
│  │  │     │  │  │  │  └─ Runner-Bridging-Header.h
│  │  │     │  │  │  ├─ Runner.xcodeproj
│  │  │     │  │  │  │  ├─ project.pbxproj
│  │  │     │  │  │  │  ├─ project.xcworkspace
│  │  │     │  │  │  │  │  ├─ contents.xcworkspacedata
│  │  │     │  │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │     │  │  │  │  │     ├─ swiftpm
│  │  │     │  │  │  │  │     │  └─ configuration
│  │  │     │  │  │  │  │     └─ WorkspaceSettings.xcsettings
│  │  │     │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │     └─ xcschemes
│  │  │     │  │  │  │        └─ Runner.xcscheme
│  │  │     │  │  │  ├─ Runner.xcworkspace
│  │  │     │  │  │  │  ├─ contents.xcworkspacedata
│  │  │     │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │     │  │  │  │     ├─ swiftpm
│  │  │     │  │  │  │     │  └─ configuration
│  │  │     │  │  │  │     └─ WorkspaceSettings.xcsettings
│  │  │     │  │  │  └─ RunnerTests
│  │  │     │  │  │     └─ RunnerTests.swift
│  │  │     │  │  ├─ lib
│  │  │     │  │  │  └─ main.dart
│  │  │     │  │  ├─ linux
│  │  │     │  │  │  ├─ CMakeLists.txt
│  │  │     │  │  │  ├─ flutter
│  │  │     │  │  │  │  └─ CMakeLists.txt
│  │  │     │  │  │  ├─ main.cc
│  │  │     │  │  │  ├─ my_application.cc
│  │  │     │  │  │  └─ my_application.h
│  │  │     │  │  ├─ macos
│  │  │     │  │  │  ├─ Flutter
│  │  │     │  │  │  │  ├─ Flutter-Debug.xcconfig
│  │  │     │  │  │  │  └─ Flutter-Release.xcconfig
│  │  │     │  │  │  ├─ Runner
│  │  │     │  │  │  │  ├─ AppDelegate.swift
│  │  │     │  │  │  │  ├─ Assets.xcassets
│  │  │     │  │  │  │  │  └─ AppIcon.appiconset
│  │  │     │  │  │  │  │     ├─ app_icon_1024.png
│  │  │     │  │  │  │  │     ├─ app_icon_128.png
│  │  │     │  │  │  │  │     ├─ app_icon_16.png
│  │  │     │  │  │  │  │     ├─ app_icon_256.png
│  │  │     │  │  │  │  │     ├─ app_icon_32.png
│  │  │     │  │  │  │  │     ├─ app_icon_512.png
│  │  │     │  │  │  │  │     ├─ app_icon_64.png
│  │  │     │  │  │  │  │     └─ Contents.json
│  │  │     │  │  │  │  ├─ Base.lproj
│  │  │     │  │  │  │  │  └─ MainMenu.xib
│  │  │     │  │  │  │  ├─ Configs
│  │  │     │  │  │  │  │  ├─ AppInfo.xcconfig
│  │  │     │  │  │  │  │  ├─ Debug.xcconfig
│  │  │     │  │  │  │  │  ├─ Release.xcconfig
│  │  │     │  │  │  │  │  └─ Warnings.xcconfig
│  │  │     │  │  │  │  ├─ DebugProfile.entitlements
│  │  │     │  │  │  │  ├─ Info.plist
│  │  │     │  │  │  │  ├─ MainFlutterWindow.swift
│  │  │     │  │  │  │  └─ Release.entitlements
│  │  │     │  │  │  ├─ Runner.xcodeproj
│  │  │     │  │  │  │  ├─ project.pbxproj
│  │  │     │  │  │  │  ├─ project.xcworkspace
│  │  │     │  │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │     │  │  │  │  │     └─ swiftpm
│  │  │     │  │  │  │  │        └─ configuration
│  │  │     │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │     └─ xcschemes
│  │  │     │  │  │  │        └─ Runner.xcscheme
│  │  │     │  │  │  ├─ Runner.xcworkspace
│  │  │     │  │  │  │  ├─ contents.xcworkspacedata
│  │  │     │  │  │  │  └─ xcshareddata
│  │  │     │  │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │     │  │  │  │     └─ swiftpm
│  │  │     │  │  │  │        └─ configuration
│  │  │     │  │  │  └─ RunnerTests
│  │  │     │  │  │     └─ RunnerTests.swift
│  │  │     │  │  ├─ pubspec.yaml
│  │  │     │  │  ├─ README.md
│  │  │     │  │  ├─ test
│  │  │     │  │  ├─ web
│  │  │     │  │  │  ├─ favicon.png
│  │  │     │  │  │  ├─ icons
│  │  │     │  │  │  │  ├─ Icon-192.png
│  │  │     │  │  │  │  ├─ Icon-512.png
│  │  │     │  │  │  │  ├─ Icon-maskable-192.png
│  │  │     │  │  │  │  └─ Icon-maskable-512.png
│  │  │     │  │  │  ├─ index.html
│  │  │     │  │  │  └─ manifest.json
│  │  │     │  │  └─ windows
│  │  │     │  │     ├─ CMakeLists.txt
│  │  │     │  │     ├─ flutter
│  │  │     │  │     │  └─ CMakeLists.txt
│  │  │     │  │     └─ runner
│  │  │     │  │        ├─ CMakeLists.txt
│  │  │     │  │        ├─ flutter_window.cpp
│  │  │     │  │        ├─ flutter_window.h
│  │  │     │  │        ├─ main.cpp
│  │  │     │  │        ├─ resource.h
│  │  │     │  │        ├─ resources
│  │  │     │  │        │  └─ app_icon.ico
│  │  │     │  │        ├─ runner.exe.manifest
│  │  │     │  │        ├─ Runner.rc
│  │  │     │  │        ├─ utils.cpp
│  │  │     │  │        ├─ utils.h
│  │  │     │  │        ├─ win32_window.cpp
│  │  │     │  │        └─ win32_window.h
│  │  │     │  ├─ ios
│  │  │     │  │  ├─ package_info_plus
│  │  │     │  │  │  ├─ Package.swift
│  │  │     │  │  │  └─ Sources
│  │  │     │  │  │     └─ package_info_plus
│  │  │     │  │  │        ├─ FPPPackageInfoPlusPlugin.m
│  │  │     │  │  │        ├─ include
│  │  │     │  │  │        │  └─ package_info_plus
│  │  │     │  │  │        │     └─ FPPPackageInfoPlusPlugin.h
│  │  │     │  │  │        └─ PrivacyInfo.xcprivacy
│  │  │     │  │  └─ package_info_plus.podspec
│  │  │     │  ├─ lib
│  │  │     │  │  ├─ package_info_plus.dart
│  │  │     │  │  └─ src
│  │  │     │  │     ├─ file_attribute.dart
│  │  │     │  │     ├─ file_version_info.dart
│  │  │     │  │     ├─ package_info_plus_linux.dart
│  │  │     │  │     ├─ package_info_plus_macos.dart
│  │  │     │  │     ├─ package_info_plus_web.dart
│  │  │     │  │     └─ package_info_plus_windows.dart
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ macos
│  │  │     │  │  ├─ package_info_plus
│  │  │     │  │  │  ├─ Package.swift
│  │  │     │  │  │  └─ Sources
│  │  │     │  │  │     └─ package_info_plus
│  │  │     │  │  │        ├─ FPPPackageInfoPlusPlugin.m
│  │  │     │  │  │        ├─ include
│  │  │     │  │  │        │  └─ package_info_plus
│  │  │     │  │  │        │     └─ FPPPackageInfoPlusPlugin.h
│  │  │     │  │  │        └─ PrivacyInfo.xcprivacy
│  │  │     │  │  └─ package_info_plus.podspec
│  │  │     │  ├─ pubspec.yaml
│  │  │     │  ├─ README.md
│  │  │     │  └─ test
│  │  │     │     ├─ package_info_plus_linux_test.dart
│  │  │     │     ├─ package_info_plus_windows_test.dart
│  │  │     │     └─ package_info_test.dart
│  │  │     ├─ path_provider_linux
│  │  │     │  ├─ AUTHORS
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ example
│  │  │     │  │  ├─ integration_test
│  │  │     │  │  │  └─ path_provider_test.dart
│  │  │     │  │  ├─ lib
│  │  │     │  │  │  └─ main.dart
│  │  │     │  │  ├─ linux
│  │  │     │  │  │  ├─ CMakeLists.txt
│  │  │     │  │  │  ├─ flutter
│  │  │     │  │  │  │  └─ CMakeLists.txt
│  │  │     │  │  │  ├─ main.cc
│  │  │     │  │  │  ├─ my_application.cc
│  │  │     │  │  │  └─ my_application.h
│  │  │     │  │  ├─ pubspec.yaml
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ test_driver
│  │  │     │  │     └─ integration_test.dart
│  │  │     │  ├─ lib
│  │  │     │  │  ├─ path_provider_linux.dart
│  │  │     │  │  └─ src
│  │  │     │  │     ├─ get_application_id.dart
│  │  │     │  │     ├─ get_application_id_real.dart
│  │  │     │  │     ├─ get_application_id_stub.dart
│  │  │     │  │     └─ path_provider_linux.dart
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ pubspec.yaml
│  │  │     │  ├─ README.md
│  │  │     │  └─ test
│  │  │     │     ├─ get_application_id_test.dart
│  │  │     │     └─ path_provider_linux_test.dart
│  │  │     └─ wakelock_plus
│  │  │        ├─ analysis_options.yaml
│  │  │        ├─ android
│  │  │        │  ├─ .gradle
│  │  │        │  │  ├─ 9.3.0
│  │  │        │  │  │  ├─ checksums
│  │  │        │  │  │  │  └─ checksums.lock
│  │  │        │  │  │  ├─ expanded
│  │  │        │  │  │  ├─ fileChanges
│  │  │        │  │  │  │  └─ last-build.bin
│  │  │        │  │  │  ├─ fileHashes
│  │  │        │  │  │  │  ├─ fileHashes.bin
│  │  │        │  │  │  │  └─ fileHashes.lock
│  │  │        │  │  │  ├─ gc.properties
│  │  │        │  │  │  └─ vcsMetadata
│  │  │        │  │  ├─ buildOutputCleanup
│  │  │        │  │  │  ├─ buildOutputCleanup.lock
│  │  │        │  │  │  └─ cache.properties
│  │  │        │  │  ├─ nb-cache
│  │  │        │  │  │  └─ trust
│  │  │        │  │  │     ├─ 506B6481844514C42B5113DF3ECE21943EE1DCE0192C040A9B87FF6210987242
│  │  │        │  │  │     └─ 927C1BF9B394344BB3951AD39AB52F331483697A8C445F7D033058ABBEC42540
│  │  │        │  │  └─ vcs-1
│  │  │        │  │     └─ gc.properties
│  │  │        │  ├─ build.gradle
│  │  │        │  ├─ settings.gradle
│  │  │        │  └─ src
│  │  │        │     └─ main
│  │  │        │        ├─ AndroidManifest.xml
│  │  │        │        └─ kotlin
│  │  │        │           └─ dev
│  │  │        │              └─ fluttercommunity
│  │  │        │                 └─ plus
│  │  │        │                    └─ wakelock
│  │  │        │                       ├─ Wakelock.kt
│  │  │        │                       ├─ WakelockPlusMessages.g.kt
│  │  │        │                       └─ WakelockPlusPlugin.kt
│  │  │        ├─ CHANGELOG.md
│  │  │        ├─ example
│  │  │        │  ├─ analysis_options.yaml
│  │  │        │  ├─ android
│  │  │        │  │  ├─ app
│  │  │        │  │  │  ├─ build.gradle
│  │  │        │  │  │  └─ src
│  │  │        │  │  │     ├─ debug
│  │  │        │  │  │     │  └─ AndroidManifest.xml
│  │  │        │  │  │     ├─ main
│  │  │        │  │  │     │  ├─ AndroidManifest.xml
│  │  │        │  │  │     │  ├─ java
│  │  │        │  │  │     │  │  └─ io
│  │  │        │  │  │     │  │     └─ flutter
│  │  │        │  │  │     │  │        └─ plugins
│  │  │        │  │  │     │  ├─ kotlin
│  │  │        │  │  │     │  │  └─ dev
│  │  │        │  │  │     │  │     └─ fluttercommunity
│  │  │        │  │  │     │  │        └─ plus
│  │  │        │  │  │     │  │           └─ wakelock_example
│  │  │        │  │  │     │  │              └─ MainActivity.kt
│  │  │        │  │  │     │  └─ res
│  │  │        │  │  │     │     ├─ drawable
│  │  │        │  │  │     │     │  └─ launch_background.xml
│  │  │        │  │  │     │     ├─ drawable-v21
│  │  │        │  │  │     │     │  └─ launch_background.xml
│  │  │        │  │  │     │     ├─ mipmap-hdpi
│  │  │        │  │  │     │     │  └─ ic_launcher.png
│  │  │        │  │  │     │     ├─ mipmap-mdpi
│  │  │        │  │  │     │     │  └─ ic_launcher.png
│  │  │        │  │  │     │     ├─ mipmap-xhdpi
│  │  │        │  │  │     │     │  └─ ic_launcher.png
│  │  │        │  │  │     │     ├─ mipmap-xxhdpi
│  │  │        │  │  │     │     │  └─ ic_launcher.png
│  │  │        │  │  │     │     ├─ mipmap-xxxhdpi
│  │  │        │  │  │     │     │  └─ ic_launcher.png
│  │  │        │  │  │     │     ├─ values
│  │  │        │  │  │     │     │  └─ styles.xml
│  │  │        │  │  │     │     └─ values-night
│  │  │        │  │  │     │        └─ styles.xml
│  │  │        │  │  │     └─ profile
│  │  │        │  │  │        └─ AndroidManifest.xml
│  │  │        │  │  ├─ build.gradle
│  │  │        │  │  ├─ gradle
│  │  │        │  │  │  └─ wrapper
│  │  │        │  │  │     └─ gradle-wrapper.properties
│  │  │        │  │  ├─ gradle.properties
│  │  │        │  │  └─ settings.gradle
│  │  │        │  ├─ integration_test
│  │  │        │  │  └─ wakelock_plus_test.dart
│  │  │        │  ├─ ios
│  │  │        │  │  ├─ Flutter
│  │  │        │  │  │  ├─ AppFrameworkInfo.plist
│  │  │        │  │  │  ├─ Debug.xcconfig
│  │  │        │  │  │  └─ Release.xcconfig
│  │  │        │  │  ├─ Podfile
│  │  │        │  │  ├─ Podfile.lock
│  │  │        │  │  ├─ Runner
│  │  │        │  │  │  ├─ AppDelegate.h
│  │  │        │  │  │  ├─ AppDelegate.m
│  │  │        │  │  │  ├─ Assets.xcassets
│  │  │        │  │  │  │  ├─ AppIcon.appiconset
│  │  │        │  │  │  │  │  ├─ Contents.json
│  │  │        │  │  │  │  │  ├─ Icon-App-1024x1024@1x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-20x20@1x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-20x20@2x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-20x20@3x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-29x29@1x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-29x29@2x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-29x29@3x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-40x40@1x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-40x40@2x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-40x40@3x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-60x60@2x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-60x60@3x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-76x76@1x.png
│  │  │        │  │  │  │  │  ├─ Icon-App-76x76@2x.png
│  │  │        │  │  │  │  │  └─ Icon-App-83.5x83.5@2x.png
│  │  │        │  │  │  │  └─ LaunchImage.imageset
│  │  │        │  │  │  │     ├─ Contents.json
│  │  │        │  │  │  │     ├─ LaunchImage.png
│  │  │        │  │  │  │     ├─ LaunchImage@2x.png
│  │  │        │  │  │  │     ├─ LaunchImage@3x.png
│  │  │        │  │  │  │     └─ README.md
│  │  │        │  │  │  ├─ Base.lproj
│  │  │        │  │  │  │  ├─ LaunchScreen.storyboard
│  │  │        │  │  │  │  └─ Main.storyboard
│  │  │        │  │  │  ├─ Info.plist
│  │  │        │  │  │  └─ main.m
│  │  │        │  │  ├─ Runner.xcodeproj
│  │  │        │  │  │  ├─ project.pbxproj
│  │  │        │  │  │  ├─ project.xcworkspace
│  │  │        │  │  │  │  ├─ contents.xcworkspacedata
│  │  │        │  │  │  │  └─ xcshareddata
│  │  │        │  │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │        │  │  │  │     ├─ swiftpm
│  │  │        │  │  │  │     │  └─ configuration
│  │  │        │  │  │  │     └─ WorkspaceSettings.xcsettings
│  │  │        │  │  │  └─ xcshareddata
│  │  │        │  │  │     └─ xcschemes
│  │  │        │  │  │        └─ Runner.xcscheme
│  │  │        │  │  ├─ Runner.xcworkspace
│  │  │        │  │  │  ├─ contents.xcworkspacedata
│  │  │        │  │  │  └─ xcshareddata
│  │  │        │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │        │  │  │     ├─ swiftpm
│  │  │        │  │  │     │  └─ configuration
│  │  │        │  │  │     └─ WorkspaceSettings.xcsettings
│  │  │        │  │  └─ RunnerTests
│  │  │        │  │     └─ RunnerTests.m
│  │  │        │  ├─ lib
│  │  │        │  │  └─ main.dart
│  │  │        │  ├─ linux
│  │  │        │  │  ├─ CMakeLists.txt
│  │  │        │  │  ├─ flutter
│  │  │        │  │  │  ├─ CMakeLists.txt
│  │  │        │  │  │  ├─ generated_plugins.cmake
│  │  │        │  │  │  ├─ generated_plugin_registrant.cc
│  │  │        │  │  │  └─ generated_plugin_registrant.h
│  │  │        │  │  ├─ main.cc
│  │  │        │  │  ├─ my_application.cc
│  │  │        │  │  └─ my_application.h
│  │  │        │  ├─ macos
│  │  │        │  │  ├─ Flutter
│  │  │        │  │  │  ├─ Flutter-Debug.xcconfig
│  │  │        │  │  │  ├─ Flutter-Release.xcconfig
│  │  │        │  │  │  └─ GeneratedPluginRegistrant.swift
│  │  │        │  │  ├─ Podfile
│  │  │        │  │  ├─ Podfile.lock
│  │  │        │  │  ├─ Runner
│  │  │        │  │  │  ├─ AppDelegate.swift
│  │  │        │  │  │  ├─ Assets.xcassets
│  │  │        │  │  │  │  └─ AppIcon.appiconset
│  │  │        │  │  │  │     ├─ app_icon_1024.png
│  │  │        │  │  │  │     ├─ app_icon_128.png
│  │  │        │  │  │  │     ├─ app_icon_16.png
│  │  │        │  │  │  │     ├─ app_icon_256.png
│  │  │        │  │  │  │     ├─ app_icon_32.png
│  │  │        │  │  │  │     ├─ app_icon_512.png
│  │  │        │  │  │  │     ├─ app_icon_64.png
│  │  │        │  │  │  │     └─ Contents.json
│  │  │        │  │  │  ├─ Base.lproj
│  │  │        │  │  │  │  └─ MainMenu.xib
│  │  │        │  │  │  ├─ Configs
│  │  │        │  │  │  │  ├─ AppInfo.xcconfig
│  │  │        │  │  │  │  ├─ Debug.xcconfig
│  │  │        │  │  │  │  ├─ Release.xcconfig
│  │  │        │  │  │  │  └─ Warnings.xcconfig
│  │  │        │  │  │  ├─ DebugProfile.entitlements
│  │  │        │  │  │  ├─ Info.plist
│  │  │        │  │  │  ├─ MainFlutterWindow.swift
│  │  │        │  │  │  └─ Release.entitlements
│  │  │        │  │  ├─ Runner.xcodeproj
│  │  │        │  │  │  ├─ project.pbxproj
│  │  │        │  │  │  ├─ project.xcworkspace
│  │  │        │  │  │  │  └─ xcshareddata
│  │  │        │  │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │        │  │  │  │     └─ swiftpm
│  │  │        │  │  │  │        └─ configuration
│  │  │        │  │  │  └─ xcshareddata
│  │  │        │  │  │     └─ xcschemes
│  │  │        │  │  │        └─ Runner.xcscheme
│  │  │        │  │  ├─ Runner.xcworkspace
│  │  │        │  │  │  ├─ contents.xcworkspacedata
│  │  │        │  │  │  └─ xcshareddata
│  │  │        │  │  │     ├─ IDEWorkspaceChecks.plist
│  │  │        │  │  │     └─ swiftpm
│  │  │        │  │  │        └─ configuration
│  │  │        │  │  └─ RunnerTests
│  │  │        │  │     └─ RunnerTests.swift
│  │  │        │  ├─ pubspec.yaml
│  │  │        │  ├─ README.md
│  │  │        │  ├─ test_driver
│  │  │        │  │  └─ integration_test.dart
│  │  │        │  ├─ web
│  │  │        │  │  ├─ favicon.png
│  │  │        │  │  ├─ icons
│  │  │        │  │  │  ├─ Icon-192.png
│  │  │        │  │  │  ├─ Icon-512.png
│  │  │        │  │  │  ├─ Icon-maskable-192.png
│  │  │        │  │  │  └─ Icon-maskable-512.png
│  │  │        │  │  ├─ index.html
│  │  │        │  │  └─ manifest.json
│  │  │        │  └─ windows
│  │  │        │     ├─ CMakeLists.txt
│  │  │        │     ├─ flutter
│  │  │        │     │  ├─ CMakeLists.txt
│  │  │        │     │  ├─ generated_plugins.cmake
│  │  │        │     │  ├─ generated_plugin_registrant.cc
│  │  │        │     │  └─ generated_plugin_registrant.h
│  │  │        │     └─ runner
│  │  │        │        ├─ CMakeLists.txt
│  │  │        │        ├─ flutter_window.cpp
│  │  │        │        ├─ flutter_window.h
│  │  │        │        ├─ main.cpp
│  │  │        │        ├─ resource.h
│  │  │        │        ├─ resources
│  │  │        │        │  └─ app_icon.ico
│  │  │        │        ├─ runner.exe.manifest
│  │  │        │        ├─ Runner.rc
│  │  │        │        ├─ utils.cpp
│  │  │        │        ├─ utils.h
│  │  │        │        ├─ win32_window.cpp
│  │  │        │        └─ win32_window.h
│  │  │        ├─ ios
│  │  │        │  ├─ wakelock_plus
│  │  │        │  │  ├─ Package.swift
│  │  │        │  │  └─ Sources
│  │  │        │  │     └─ wakelock_plus
│  │  │        │  │        ├─ include
│  │  │        │  │        │  └─ wakelock_plus
│  │  │        │  │        │     ├─ messages.g.h
│  │  │        │  │        │     ├─ UIApplication+idleTimerLock.h
│  │  │        │  │        │     └─ WakelockPlusPlugin.h
│  │  │        │  │        ├─ messages.g.m
│  │  │        │  │        ├─ Resources
│  │  │        │  │        │  └─ PrivacyInfo.xcprivacy
│  │  │        │  │        ├─ UIApplication+idleTimerLock.m
│  │  │        │  │        └─ WakelockPlusPlugin.m
│  │  │        │  └─ wakelock_plus.podspec
│  │  │        ├─ lib
│  │  │        │  ├─ assets
│  │  │        │  │  └─ no_sleep.js
│  │  │        │  ├─ src
│  │  │        │  │  ├─ wakelock_plus_io_plugin.dart
│  │  │        │  │  ├─ wakelock_plus_linux_plugin.dart
│  │  │        │  │  ├─ wakelock_plus_macos_plugin.dart
│  │  │        │  │  ├─ wakelock_plus_web_plugin.dart
│  │  │        │  │  ├─ wakelock_plus_windows_plugin.dart
│  │  │        │  │  └─ web_impl
│  │  │        │  │     ├─ import_js_library.dart
│  │  │        │  │     └─ js_wakelock.dart
│  │  │        │  └─ wakelock_plus.dart
│  │  │        ├─ LICENSE
│  │  │        ├─ macos
│  │  │        │  ├─ wakelock_plus
│  │  │        │  │  ├─ Package.swift
│  │  │        │  │  └─ Sources
│  │  │        │  │     └─ wakelock_plus
│  │  │        │  │        ├─ Resources
│  │  │        │  │        │  └─ PrivacyInfo.xcprivacy
│  │  │        │  │        └─ WakelockPlusMacosPlugin.swift
│  │  │        │  └─ wakelock_plus.podspec
│  │  │        ├─ pigeons
│  │  │        │  └─ messages.dart
│  │  │        ├─ pubspec.yaml
│  │  │        ├─ README.md
│  │  │        └─ test
│  │  │           ├─ wakelock_plus_linux_plugin_test.dart
│  │  │           ├─ wakelock_plus_test.dart
│  │  │           └─ wakelock_plus_web_plugin_test.dart
│  │  ├─ generated_plugins.cmake
│  │  ├─ generated_plugin_registrant.cc
│  │  └─ generated_plugin_registrant.h
│  └─ runner
│     ├─ CMakeLists.txt
│     ├─ main.cc
│     ├─ my_application.cc
│     └─ my_application.h
├─ macos
│  ├─ Flutter
│  │  ├─ ephemeral
│  │  │  ├─ Flutter-Generated.xcconfig
│  │  │  ├─ flutter_export_environment.sh
│  │  │  ├─ flutter_native_integration.env
│  │  │  └─ Packages
│  │  │     ├─ .packages
│  │  │     └─ FlutterGeneratedPluginSwiftPackage
│  │  │        ├─ Package.swift
│  │  │        └─ Sources
│  │  │           └─ FlutterGeneratedPluginSwiftPackage
│  │  │              └─ FlutterGeneratedPluginSwiftPackage.swift
│  │  ├─ Flutter-Debug.xcconfig
│  │  ├─ Flutter-Release.xcconfig
│  │  └─ GeneratedPluginRegistrant.swift
│  ├─ Runner
│  │  ├─ AppDelegate.swift
│  │  ├─ Assets.xcassets
│  │  │  └─ AppIcon.appiconset
│  │  │     ├─ app_icon_1024.png
│  │  │     ├─ app_icon_128.png
│  │  │     ├─ app_icon_16.png
│  │  │     ├─ app_icon_256.png
│  │  │     ├─ app_icon_32.png
│  │  │     ├─ app_icon_512.png
│  │  │     ├─ app_icon_64.png
│  │  │     └─ Contents.json
│  │  ├─ Base.lproj
│  │  │  └─ MainMenu.xib
│  │  ├─ Configs
│  │  │  ├─ AppInfo.xcconfig
│  │  │  ├─ Debug.xcconfig
│  │  │  ├─ Release.xcconfig
│  │  │  └─ Warnings.xcconfig
│  │  ├─ DebugProfile.entitlements
│  │  ├─ Info.plist
│  │  ├─ MainFlutterWindow.swift
│  │  └─ Release.entitlements
│  ├─ Runner.xcodeproj
│  │  ├─ project.pbxproj
│  │  ├─ project.xcworkspace
│  │  │  └─ xcshareddata
│  │  │     └─ IDEWorkspaceChecks.plist
│  │  └─ xcshareddata
│  │     └─ xcschemes
│  │        └─ Runner.xcscheme
│  ├─ Runner.xcworkspace
│  │  ├─ contents.xcworkspacedata
│  │  └─ xcshareddata
│  │     └─ IDEWorkspaceChecks.plist
│  └─ RunnerTests
│     └─ RunnerTests.swift
├─ pubspec.lock
├─ pubspec.yaml
├─ README.md
├─ test
│  └─ widget_test.dart
├─ web
│  ├─ favicon.png
│  ├─ icons
│  │  ├─ Icon-192.png
│  │  ├─ Icon-512.png
│  │  ├─ Icon-maskable-192.png
│  │  └─ Icon-maskable-512.png
│  ├─ index.html
│  └─ manifest.json
└─ windows
   ├─ CMakeLists.txt
   ├─ flutter
   │  ├─ CMakeLists.txt
   │  ├─ ephemeral
   │  │  └─ .plugin_symlinks
   │  │     ├─ flutter_tts
   │  │     │  ├─ analysis_options.yaml
   │  │     │  ├─ android
   │  │     │  │  ├─ .gradle
   │  │     │  │  │  ├─ 8.13
   │  │     │  │  │  │  ├─ checksums
   │  │     │  │  │  │  │  ├─ checksums.lock
   │  │     │  │  │  │  │  ├─ md5-checksums.bin
   │  │     │  │  │  │  │  └─ sha1-checksums.bin
   │  │     │  │  │  │  ├─ expanded
   │  │     │  │  │  │  ├─ fileChanges
   │  │     │  │  │  │  │  └─ last-build.bin
   │  │     │  │  │  │  ├─ fileHashes
   │  │     │  │  │  │  │  ├─ fileHashes.bin
   │  │     │  │  │  │  │  └─ fileHashes.lock
   │  │     │  │  │  │  ├─ gc.properties
   │  │     │  │  │  │  └─ vcsMetadata
   │  │     │  │  │  ├─ buildOutputCleanup
   │  │     │  │  │  │  ├─ buildOutputCleanup.lock
   │  │     │  │  │  │  └─ cache.properties
   │  │     │  │  │  ├─ nb-cache
   │  │     │  │  │  │  ├─ android-1356970351
   │  │     │  │  │  │  │  └─ project-info.ser
   │  │     │  │  │  │  ├─ subprojects.ser
   │  │     │  │  │  │  └─ trust
   │  │     │  │  │  │     └─ 9B6069EAAF8A97CF77EB33074CC54A1BD6146B7CDB6E7683C0FFA6049317D3A7
   │  │     │  │  │  └─ vcs-1
   │  │     │  │  │     └─ gc.properties
   │  │     │  │  ├─ build.gradle
   │  │     │  │  ├─ gradle
   │  │     │  │  │  └─ wrapper
   │  │     │  │  │     └─ gradle-wrapper.properties
   │  │     │  │  ├─ gradle.properties
   │  │     │  │  ├─ settings.gradle
   │  │     │  │  └─ src
   │  │     │  │     └─ main
   │  │     │  │        ├─ AndroidManifest.xml
   │  │     │  │        └─ kotlin
   │  │     │  │           └─ com
   │  │     │  │              └─ eyedeadevelopment
   │  │     │  │                 └─ fluttertts
   │  │     │  │                    └─ FlutterTtsPlugin.kt
   │  │     │  ├─ CHANGELOG.md
   │  │     │  ├─ CODE_OF_CONDUCT.md
   │  │     │  ├─ example
   │  │     │  │  ├─ analysis_options.yaml
   │  │     │  │  ├─ android
   │  │     │  │  │  ├─ app
   │  │     │  │  │  │  ├─ build.gradle
   │  │     │  │  │  │  └─ src
   │  │     │  │  │  │     ├─ debug
   │  │     │  │  │  │     │  └─ AndroidManifest.xml
   │  │     │  │  │  │     ├─ main
   │  │     │  │  │  │     │  ├─ AndroidManifest.xml
   │  │     │  │  │  │     │  ├─ java
   │  │     │  │  │  │     │  │  └─ io
   │  │     │  │  │  │     │  │     └─ flutter
   │  │     │  │  │  │     │  │        └─ plugins
   │  │     │  │  │  │     │  └─ res
   │  │     │  │  │  │     │     ├─ drawable
   │  │     │  │  │  │     │     │  └─ launch_background.xml
   │  │     │  │  │  │     │     ├─ mipmap-hdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-mdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-xhdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-xxhdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-xxxhdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     └─ values
   │  │     │  │  │  │     │        └─ styles.xml
   │  │     │  │  │  │     └─ profile
   │  │     │  │  │  │        └─ AndroidManifest.xml
   │  │     │  │  │  ├─ build.gradle
   │  │     │  │  │  ├─ gradle
   │  │     │  │  │  │  └─ wrapper
   │  │     │  │  │  │     └─ gradle-wrapper.properties
   │  │     │  │  │  ├─ gradle.properties
   │  │     │  │  │  ├─ settings.gradle
   │  │     │  │  │  └─ settings_aar.gradle
   │  │     │  │  ├─ ios
   │  │     │  │  │  ├─ Flutter
   │  │     │  │  │  │  ├─ AppFrameworkInfo.plist
   │  │     │  │  │  │  ├─ Debug.xcconfig
   │  │     │  │  │  │  ├─ ephemeral
   │  │     │  │  │  │  │  ├─ flutter_lldbinit
   │  │     │  │  │  │  │  └─ flutter_lldb_helper.py
   │  │     │  │  │  │  ├─ Flutter.podspec
   │  │     │  │  │  │  └─ Release.xcconfig
   │  │     │  │  │  ├─ Podfile
   │  │     │  │  │  ├─ Runner
   │  │     │  │  │  │  ├─ AppDelegate.swift
   │  │     │  │  │  │  ├─ Assets.xcassets
   │  │     │  │  │  │  │  ├─ AppIcon.appiconset
   │  │     │  │  │  │  │  │  ├─ Contents.json
   │  │     │  │  │  │  │  │  ├─ Icon-App-1024x1024@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-60x60@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-60x60@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-76x76@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-76x76@2x.png
   │  │     │  │  │  │  │  │  └─ Icon-App-83.5x83.5@2x.png
   │  │     │  │  │  │  │  └─ LaunchImage.imageset
   │  │     │  │  │  │  │     ├─ Contents.json
   │  │     │  │  │  │  │     ├─ LaunchImage.png
   │  │     │  │  │  │  │     ├─ LaunchImage@2x.png
   │  │     │  │  │  │  │     ├─ LaunchImage@3x.png
   │  │     │  │  │  │  │     └─ README.md
   │  │     │  │  │  │  ├─ Base.lproj
   │  │     │  │  │  │  │  ├─ LaunchScreen.storyboard
   │  │     │  │  │  │  │  └─ Main.storyboard
   │  │     │  │  │  │  ├─ Info.plist
   │  │     │  │  │  │  └─ Runner-Bridging-Header.h
   │  │     │  │  │  ├─ Runner.xcodeproj
   │  │     │  │  │  │  ├─ project.pbxproj
   │  │     │  │  │  │  ├─ project.xcworkspace
   │  │     │  │  │  │  │  ├─ contents.xcworkspacedata
   │  │     │  │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │  │     ├─ swiftpm
   │  │     │  │  │  │  │     │  └─ configuration
   │  │     │  │  │  │  │     └─ WorkspaceSettings.xcsettings
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     └─ xcschemes
   │  │     │  │  │  │        └─ Runner.xcscheme
   │  │     │  │  │  └─ Runner.xcworkspace
   │  │     │  │  │     ├─ contents.xcworkspacedata
   │  │     │  │  │     └─ xcshareddata
   │  │     │  │  │        ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │        ├─ swiftpm
   │  │     │  │  │        │  └─ configuration
   │  │     │  │  │        └─ WorkspaceSettings.xcsettings
   │  │     │  │  ├─ lib
   │  │     │  │  │  ├─ language_helper.dart
   │  │     │  │  │  ├─ main.dart
   │  │     │  │  │  ├─ non_web_language_helper.dart
   │  │     │  │  │  └─ web_language_helper.dart
   │  │     │  │  ├─ macos
   │  │     │  │  │  ├─ Flutter
   │  │     │  │  │  │  ├─ Flutter-Debug.xcconfig
   │  │     │  │  │  │  └─ Flutter-Release.xcconfig
   │  │     │  │  │  ├─ Podfile
   │  │     │  │  │  ├─ Runner
   │  │     │  │  │  │  ├─ AppDelegate.swift
   │  │     │  │  │  │  ├─ Assets.xcassets
   │  │     │  │  │  │  │  └─ AppIcon.appiconset
   │  │     │  │  │  │  │     ├─ app_icon_1024.png
   │  │     │  │  │  │  │     ├─ app_icon_128.png
   │  │     │  │  │  │  │     ├─ app_icon_16.png
   │  │     │  │  │  │  │     ├─ app_icon_256.png
   │  │     │  │  │  │  │     ├─ app_icon_32.png
   │  │     │  │  │  │  │     ├─ app_icon_512.png
   │  │     │  │  │  │  │     ├─ app_icon_64.png
   │  │     │  │  │  │  │     └─ Contents.json
   │  │     │  │  │  │  ├─ Base.lproj
   │  │     │  │  │  │  │  └─ MainMenu.xib
   │  │     │  │  │  │  ├─ Configs
   │  │     │  │  │  │  │  ├─ AppInfo.xcconfig
   │  │     │  │  │  │  │  ├─ Debug.xcconfig
   │  │     │  │  │  │  │  ├─ Release.xcconfig
   │  │     │  │  │  │  │  └─ Warnings.xcconfig
   │  │     │  │  │  │  ├─ DebugProfile.entitlements
   │  │     │  │  │  │  ├─ Info.plist
   │  │     │  │  │  │  ├─ MainFlutterWindow.swift
   │  │     │  │  │  │  └─ Release.entitlements
   │  │     │  │  │  ├─ Runner.xcodeproj
   │  │     │  │  │  │  ├─ project.pbxproj
   │  │     │  │  │  │  ├─ project.xcworkspace
   │  │     │  │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │  │     └─ swiftpm
   │  │     │  │  │  │  │        └─ configuration
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     └─ xcschemes
   │  │     │  │  │  │        └─ Runner.xcscheme
   │  │     │  │  │  └─ Runner.xcworkspace
   │  │     │  │  │     ├─ contents.xcworkspacedata
   │  │     │  │  │     └─ xcshareddata
   │  │     │  │  │        ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │        └─ swiftpm
   │  │     │  │  │           └─ configuration
   │  │     │  │  ├─ pubspec.yaml
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ test
   │  │     │  │  │  └─ widget_test.dart
   │  │     │  │  ├─ web
   │  │     │  │  │  ├─ favicon.png
   │  │     │  │  │  ├─ icons
   │  │     │  │  │  │  ├─ Icon-192.png
   │  │     │  │  │  │  └─ Icon-512.png
   │  │     │  │  │  ├─ index.html
   │  │     │  │  │  └─ manifest.json
   │  │     │  │  ├─ windows
   │  │     │  │  │  ├─ CMakeLists.txt
   │  │     │  │  │  ├─ flutter
   │  │     │  │  │  │  └─ CMakeLists.txt
   │  │     │  │  │  └─ runner
   │  │     │  │  │     ├─ CMakeLists.txt
   │  │     │  │  │     ├─ flutter_window.cpp
   │  │     │  │  │     ├─ flutter_window.h
   │  │     │  │  │     ├─ main.cpp
   │  │     │  │  │     ├─ resource.h
   │  │     │  │  │     ├─ resources
   │  │     │  │  │     │  └─ app_icon.ico
   │  │     │  │  │     ├─ runner.exe.manifest
   │  │     │  │  │     ├─ Runner.rc
   │  │     │  │  │     ├─ utils.cpp
   │  │     │  │  │     ├─ utils.h
   │  │     │  │  │     ├─ win32_window.cpp
   │  │     │  │  │     └─ win32_window.h
   │  │     │  │  └─ winuwp
   │  │     │  │     ├─ CMakeLists.txt
   │  │     │  │     ├─ flutter
   │  │     │  │     │  ├─ CMakeLists.txt
   │  │     │  │     │  └─ flutter_windows.h
   │  │     │  │     ├─ project_version
   │  │     │  │     └─ runner_uwp
   │  │     │  │        ├─ appxmanifest.in
   │  │     │  │        ├─ Assets
   │  │     │  │        │  ├─ LargeTile.scale-100.png
   │  │     │  │        │  ├─ LargeTile.scale-125.png
   │  │     │  │        │  ├─ LargeTile.scale-150.png
   │  │     │  │        │  ├─ LargeTile.scale-200.png
   │  │     │  │        │  ├─ LargeTile.scale-400.png
   │  │     │  │        │  ├─ LockScreenLogo.scale-200.png
   │  │     │  │        │  ├─ SmallTile.scale-100.png
   │  │     │  │        │  ├─ SmallTile.scale-125.png
   │  │     │  │        │  ├─ SmallTile.scale-150.png
   │  │     │  │        │  ├─ SmallTile.scale-200.png
   │  │     │  │        │  ├─ SmallTile.scale-400.png
   │  │     │  │        │  ├─ SplashScreen.scale-100.png
   │  │     │  │        │  ├─ SplashScreen.scale-125.png
   │  │     │  │        │  ├─ SplashScreen.scale-150.png
   │  │     │  │        │  ├─ SplashScreen.scale-200.png
   │  │     │  │        │  ├─ SplashScreen.scale-400.png
   │  │     │  │        │  ├─ Square150x150Logo.scale-100.png
   │  │     │  │        │  ├─ Square150x150Logo.scale-125.png
   │  │     │  │        │  ├─ Square150x150Logo.scale-150.png
   │  │     │  │        │  ├─ Square150x150Logo.scale-200.png
   │  │     │  │        │  ├─ Square150x150Logo.scale-400.png
   │  │     │  │        │  ├─ Square44x44Logo.altform-unplated_targetsize-16.png
   │  │     │  │        │  ├─ Square44x44Logo.altform-unplated_targetsize-256.png
   │  │     │  │        │  ├─ Square44x44Logo.altform-unplated_targetsize-32.png
   │  │     │  │        │  ├─ Square44x44Logo.altform-unplated_targetsize-48.png
   │  │     │  │        │  ├─ Square44x44Logo.scale-100.png
   │  │     │  │        │  ├─ Square44x44Logo.scale-125.png
   │  │     │  │        │  ├─ Square44x44Logo.scale-150.png
   │  │     │  │        │  ├─ Square44x44Logo.scale-200.png
   │  │     │  │        │  ├─ Square44x44Logo.scale-400.png
   │  │     │  │        │  ├─ Square44x44Logo.targetsize-16.png
   │  │     │  │        │  ├─ Square44x44Logo.targetsize-24.png
   │  │     │  │        │  ├─ Square44x44Logo.targetsize-24_altform-unplated.png
   │  │     │  │        │  ├─ Square44x44Logo.targetsize-256.png
   │  │     │  │        │  ├─ Square44x44Logo.targetsize-32.png
   │  │     │  │        │  ├─ Square44x44Logo.targetsize-48.png
   │  │     │  │        │  ├─ StoreLogo.png
   │  │     │  │        │  ├─ StoreLogo.scale-100.png
   │  │     │  │        │  ├─ StoreLogo.scale-125.png
   │  │     │  │        │  ├─ StoreLogo.scale-150.png
   │  │     │  │        │  ├─ StoreLogo.scale-200.png
   │  │     │  │        │  ├─ StoreLogo.scale-400.png
   │  │     │  │        │  ├─ Wide310x150Logo.scale-200.png
   │  │     │  │        │  ├─ WideTile.scale-100.png
   │  │     │  │        │  ├─ WideTile.scale-125.png
   │  │     │  │        │  ├─ WideTile.scale-150.png
   │  │     │  │        │  ├─ WideTile.scale-200.png
   │  │     │  │        │  └─ WideTile.scale-400.png
   │  │     │  │        ├─ CMakeLists.txt
   │  │     │  │        ├─ CMakeSettings.json
   │  │     │  │        ├─ flutter_frameworkview.cpp
   │  │     │  │        ├─ main.cpp
   │  │     │  │        ├─ resources.pri
   │  │     │  │        └─ Windows_TemporaryKey.pfx
   │  │     │  ├─ gen
   │  │     │  ├─ ios
   │  │     │  │  ├─ Assets
   │  │     │  │  ├─ Classes
   │  │     │  │  │  ├─ AudioCategory.swift
   │  │     │  │  │  ├─ AudioCategoryOptions.swift
   │  │     │  │  │  ├─ AudioModes.swift
   │  │     │  │  │  ├─ FlutterTtsPlugin.h
   │  │     │  │  │  ├─ FlutterTtsPlugin.m
   │  │     │  │  │  └─ SwiftFlutterTtsPlugin.swift
   │  │     │  │  └─ flutter_tts.podspec
   │  │     │  ├─ lib
   │  │     │  │  ├─ flutter_tts.dart
   │  │     │  │  ├─ flutter_tts_web.dart
   │  │     │  │  └─ interop_types.dart
   │  │     │  ├─ LICENSE
   │  │     │  ├─ macos
   │  │     │  │  ├─ Classes
   │  │     │  │  │  └─ FlutterTtsPlugin.swift
   │  │     │  │  └─ flutter_tts.podspec
   │  │     │  ├─ pubspec.yaml
   │  │     │  ├─ README.md
   │  │     │  ├─ test
   │  │     │  └─ windows
   │  │     │     ├─ CMakeLists.txt
   │  │     │     ├─ flutter_tts_plugin.cpp
   │  │     │     └─ include
   │  │     │        └─ flutter_tts
   │  │     │           └─ flutter_tts_plugin.h
   │  │     ├─ jni
   │  │     │  ├─ analysis_options.yaml
   │  │     │  ├─ android
   │  │     │  │  ├─ .cxx
   │  │     │  │  │  ├─ Debug
   │  │     │  │  │  │  └─ 5h5h3o3w
   │  │     │  │  │  │     ├─ arm64-v8a
   │  │     │  │  │  │     │  ├─ .cmake
   │  │     │  │  │  │     │  │  └─ api
   │  │     │  │  │  │     │  │     └─ v1
   │  │     │  │  │  │     │  │        ├─ query
   │  │     │  │  │  │     │  │        │  └─ client-agp
   │  │     │  │  │  │     │  │        │     ├─ cache-v2
   │  │     │  │  │  │     │  │        │     ├─ cmakeFiles-v1
   │  │     │  │  │  │     │  │        │     └─ codemodel-v2
   │  │     │  │  │  │     │  │        └─ reply
   │  │     │  │  │  │     │  │           ├─ cache-v2-f05c7c1fb0cdff075fd2.json
   │  │     │  │  │  │     │  │           ├─ cmakeFiles-v1-55aafbfe3a72401545d9.json
   │  │     │  │  │  │     │  │           ├─ codemodel-v2-16547c5b470ca935e2b8.json
   │  │     │  │  │  │     │  │           ├─ directory-.-Debug-d0094a50bb2071803777.json
   │  │     │  │  │  │     │  │           ├─ index-2026-07-18T09-22-57-0122.json
   │  │     │  │  │  │     │  │           └─ target-jni-Debug-ddc91ce5d5a83b3481e8.json
   │  │     │  │  │  │     │  ├─ .ninja_deps
   │  │     │  │  │  │     │  ├─ .ninja_log
   │  │     │  │  │  │     │  ├─ additional_project_files.txt
   │  │     │  │  │  │     │  ├─ android_gradle_build.json
   │  │     │  │  │  │     │  ├─ android_gradle_build_mini.json
   │  │     │  │  │  │     │  ├─ build.ninja
   │  │     │  │  │  │     │  ├─ build_file_index.txt
   │  │     │  │  │  │     │  ├─ CMakeCache.txt
   │  │     │  │  │  │     │  ├─ CMakeFiles
   │  │     │  │  │  │     │  │  ├─ 3.22.1-g37088a8-dirty
   │  │     │  │  │  │     │  │  │  ├─ CMakeCCompiler.cmake
   │  │     │  │  │  │     │  │  │  ├─ CMakeDetermineCompilerABI_C.bin
   │  │     │  │  │  │     │  │  │  ├─ CMakeSystem.cmake
   │  │     │  │  │  │     │  │  │  └─ CompilerIdC
   │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.c
   │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.o
   │  │     │  │  │  │     │  │  │     └─ tmp
   │  │     │  │  │  │     │  │  ├─ cmake.check_cache
   │  │     │  │  │  │     │  │  ├─ CMakeTmp
   │  │     │  │  │  │     │  │  ├─ jni.dir
   │  │     │  │  │  │     │  │  │  ├─ dartjni.c.o
   │  │     │  │  │  │     │  │  │  ├─ include
   │  │     │  │  │  │     │  │  │  │  └─ dart_api_dl.c.o
   │  │     │  │  │  │     │  │  │  └─ third_party
   │  │     │  │  │  │     │  │  │     └─ global_jni_env.c.o
   │  │     │  │  │  │     │  │  ├─ rules.ninja
   │  │     │  │  │  │     │  │  └─ TargetDirectories.txt
   │  │     │  │  │  │     │  ├─ cmake_install.cmake
   │  │     │  │  │  │     │  ├─ compile_commands.json
   │  │     │  │  │  │     │  ├─ compile_commands.json.bin
   │  │     │  │  │  │     │  ├─ configure_fingerprint.bin
   │  │     │  │  │  │     │  ├─ metadata_generation_command.txt
   │  │     │  │  │  │     │  ├─ prefab_config.json
   │  │     │  │  │  │     │  └─ symbol_folder_index.txt
   │  │     │  │  │  │     ├─ armeabi-v7a
   │  │     │  │  │  │     │  ├─ .cmake
   │  │     │  │  │  │     │  │  └─ api
   │  │     │  │  │  │     │  │     └─ v1
   │  │     │  │  │  │     │  │        ├─ query
   │  │     │  │  │  │     │  │        │  └─ client-agp
   │  │     │  │  │  │     │  │        │     ├─ cache-v2
   │  │     │  │  │  │     │  │        │     ├─ cmakeFiles-v1
   │  │     │  │  │  │     │  │        │     └─ codemodel-v2
   │  │     │  │  │  │     │  │        └─ reply
   │  │     │  │  │  │     │  │           ├─ cache-v2-a459056d10074e395e6f.json
   │  │     │  │  │  │     │  │           ├─ cmakeFiles-v1-10732f32faa124b640eb.json
   │  │     │  │  │  │     │  │           ├─ codemodel-v2-5f4152ddd7832a335f0b.json
   │  │     │  │  │  │     │  │           ├─ directory-.-Debug-d0094a50bb2071803777.json
   │  │     │  │  │  │     │  │           ├─ index-2026-07-18T09-22-59-0725.json
   │  │     │  │  │  │     │  │           └─ target-jni-Debug-372e5383e0cf9081c74c.json
   │  │     │  │  │  │     │  ├─ .ninja_deps
   │  │     │  │  │  │     │  ├─ .ninja_log
   │  │     │  │  │  │     │  ├─ additional_project_files.txt
   │  │     │  │  │  │     │  ├─ android_gradle_build.json
   │  │     │  │  │  │     │  ├─ android_gradle_build_mini.json
   │  │     │  │  │  │     │  ├─ build.ninja
   │  │     │  │  │  │     │  ├─ build_file_index.txt
   │  │     │  │  │  │     │  ├─ CMakeCache.txt
   │  │     │  │  │  │     │  ├─ CMakeFiles
   │  │     │  │  │  │     │  │  ├─ 3.22.1-g37088a8-dirty
   │  │     │  │  │  │     │  │  │  ├─ CMakeCCompiler.cmake
   │  │     │  │  │  │     │  │  │  ├─ CMakeDetermineCompilerABI_C.bin
   │  │     │  │  │  │     │  │  │  ├─ CMakeSystem.cmake
   │  │     │  │  │  │     │  │  │  └─ CompilerIdC
   │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.c
   │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.o
   │  │     │  │  │  │     │  │  │     └─ tmp
   │  │     │  │  │  │     │  │  ├─ cmake.check_cache
   │  │     │  │  │  │     │  │  ├─ CMakeTmp
   │  │     │  │  │  │     │  │  ├─ jni.dir
   │  │     │  │  │  │     │  │  │  ├─ dartjni.c.o
   │  │     │  │  │  │     │  │  │  ├─ include
   │  │     │  │  │  │     │  │  │  │  └─ dart_api_dl.c.o
   │  │     │  │  │  │     │  │  │  └─ third_party
   │  │     │  │  │  │     │  │  │     └─ global_jni_env.c.o
   │  │     │  │  │  │     │  │  ├─ rules.ninja
   │  │     │  │  │  │     │  │  └─ TargetDirectories.txt
   │  │     │  │  │  │     │  ├─ cmake_install.cmake
   │  │     │  │  │  │     │  ├─ compile_commands.json
   │  │     │  │  │  │     │  ├─ compile_commands.json.bin
   │  │     │  │  │  │     │  ├─ configure_fingerprint.bin
   │  │     │  │  │  │     │  ├─ metadata_generation_command.txt
   │  │     │  │  │  │     │  ├─ prefab_config.json
   │  │     │  │  │  │     │  └─ symbol_folder_index.txt
   │  │     │  │  │  │     ├─ hash_key.txt
   │  │     │  │  │  │     ├─ x86
   │  │     │  │  │  │     │  ├─ .cmake
   │  │     │  │  │  │     │  │  └─ api
   │  │     │  │  │  │     │  │     └─ v1
   │  │     │  │  │  │     │  │        ├─ query
   │  │     │  │  │  │     │  │        │  └─ client-agp
   │  │     │  │  │  │     │  │        │     ├─ cache-v2
   │  │     │  │  │  │     │  │        │     ├─ cmakeFiles-v1
   │  │     │  │  │  │     │  │        │     └─ codemodel-v2
   │  │     │  │  │  │     │  │        └─ reply
   │  │     │  │  │  │     │  │           ├─ cache-v2-415322deaeb6dba77bb8.json
   │  │     │  │  │  │     │  │           ├─ cmakeFiles-v1-bcd3d11348c1b573392d.json
   │  │     │  │  │  │     │  │           ├─ codemodel-v2-90291965cbd0c9882e73.json
   │  │     │  │  │  │     │  │           ├─ directory-.-Debug-d0094a50bb2071803777.json
   │  │     │  │  │  │     │  │           ├─ index-2026-07-18T09-23-02-0341.json
   │  │     │  │  │  │     │  │           └─ target-jni-Debug-04336afdec6a8716c903.json
   │  │     │  │  │  │     │  ├─ .ninja_deps
   │  │     │  │  │  │     │  ├─ .ninja_log
   │  │     │  │  │  │     │  ├─ additional_project_files.txt
   │  │     │  │  │  │     │  ├─ android_gradle_build.json
   │  │     │  │  │  │     │  ├─ android_gradle_build_mini.json
   │  │     │  │  │  │     │  ├─ build.ninja
   │  │     │  │  │  │     │  ├─ build_file_index.txt
   │  │     │  │  │  │     │  ├─ CMakeCache.txt
   │  │     │  │  │  │     │  ├─ CMakeFiles
   │  │     │  │  │  │     │  │  ├─ 3.22.1-g37088a8-dirty
   │  │     │  │  │  │     │  │  │  ├─ CMakeCCompiler.cmake
   │  │     │  │  │  │     │  │  │  ├─ CMakeDetermineCompilerABI_C.bin
   │  │     │  │  │  │     │  │  │  ├─ CMakeSystem.cmake
   │  │     │  │  │  │     │  │  │  └─ CompilerIdC
   │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.c
   │  │     │  │  │  │     │  │  │     ├─ CMakeCCompilerId.o
   │  │     │  │  │  │     │  │  │     └─ tmp
   │  │     │  │  │  │     │  │  ├─ cmake.check_cache
   │  │     │  │  │  │     │  │  ├─ CMakeTmp
   │  │     │  │  │  │     │  │  ├─ jni.dir
   │  │     │  │  │  │     │  │  │  ├─ dartjni.c.o
   │  │     │  │  │  │     │  │  │  ├─ include
   │  │     │  │  │  │     │  │  │  │  └─ dart_api_dl.c.o
   │  │     │  │  │  │     │  │  │  └─ third_party
   │  │     │  │  │  │     │  │  │     └─ global_jni_env.c.o
   │  │     │  │  │  │     │  │  ├─ rules.ninja
   │  │     │  │  │  │     │  │  └─ TargetDirectories.txt
   │  │     │  │  │  │     │  ├─ cmake_install.cmake
   │  │     │  │  │  │     │  ├─ compile_commands.json
   │  │     │  │  │  │     │  ├─ compile_commands.json.bin
   │  │     │  │  │  │     │  ├─ configure_fingerprint.bin
   │  │     │  │  │  │     │  ├─ metadata_generation_command.txt
   │  │     │  │  │  │     │  ├─ prefab_config.json
   │  │     │  │  │  │     │  └─ symbol_folder_index.txt
   │  │     │  │  │  │     └─ x86_64
   │  │     │  │  │  │        ├─ .cmake
   │  │     │  │  │  │        │  └─ api
   │  │     │  │  │  │        │     └─ v1
   │  │     │  │  │  │        │        ├─ query
   │  │     │  │  │  │        │        │  └─ client-agp
   │  │     │  │  │  │        │        │     ├─ cache-v2
   │  │     │  │  │  │        │        │     ├─ cmakeFiles-v1
   │  │     │  │  │  │        │        │     └─ codemodel-v2
   │  │     │  │  │  │        │        └─ reply
   │  │     │  │  │  │        │           ├─ cache-v2-060598f8a2545faaa1c8.json
   │  │     │  │  │  │        │           ├─ cmakeFiles-v1-ad7f91c0dd7c473dd9a7.json
   │  │     │  │  │  │        │           ├─ codemodel-v2-0c05986467f230caea39.json
   │  │     │  │  │  │        │           ├─ directory-.-Debug-d0094a50bb2071803777.json
   │  │     │  │  │  │        │           ├─ index-2026-07-18T09-23-05-0151.json
   │  │     │  │  │  │        │           └─ target-jni-Debug-33d293cdc5f5868a4768.json
   │  │     │  │  │  │        ├─ .ninja_deps
   │  │     │  │  │  │        ├─ .ninja_log
   │  │     │  │  │  │        ├─ additional_project_files.txt
   │  │     │  │  │  │        ├─ android_gradle_build.json
   │  │     │  │  │  │        ├─ android_gradle_build_mini.json
   │  │     │  │  │  │        ├─ build.ninja
   │  │     │  │  │  │        ├─ build_file_index.txt
   │  │     │  │  │  │        ├─ CMakeCache.txt
   │  │     │  │  │  │        ├─ CMakeFiles
   │  │     │  │  │  │        │  ├─ 3.22.1-g37088a8-dirty
   │  │     │  │  │  │        │  │  ├─ CMakeCCompiler.cmake
   │  │     │  │  │  │        │  │  ├─ CMakeDetermineCompilerABI_C.bin
   │  │     │  │  │  │        │  │  ├─ CMakeSystem.cmake
   │  │     │  │  │  │        │  │  └─ CompilerIdC
   │  │     │  │  │  │        │  │     ├─ CMakeCCompilerId.c
   │  │     │  │  │  │        │  │     ├─ CMakeCCompilerId.o
   │  │     │  │  │  │        │  │     └─ tmp
   │  │     │  │  │  │        │  ├─ cmake.check_cache
   │  │     │  │  │  │        │  ├─ CMakeTmp
   │  │     │  │  │  │        │  ├─ jni.dir
   │  │     │  │  │  │        │  │  ├─ dartjni.c.o
   │  │     │  │  │  │        │  │  ├─ include
   │  │     │  │  │  │        │  │  │  └─ dart_api_dl.c.o
   │  │     │  │  │  │        │  │  └─ third_party
   │  │     │  │  │  │        │  │     └─ global_jni_env.c.o
   │  │     │  │  │  │        │  ├─ rules.ninja
   │  │     │  │  │  │        │  └─ TargetDirectories.txt
   │  │     │  │  │  │        ├─ cmake_install.cmake
   │  │     │  │  │  │        ├─ compile_commands.json
   │  │     │  │  │  │        ├─ compile_commands.json.bin
   │  │     │  │  │  │        ├─ configure_fingerprint.bin
   │  │     │  │  │  │        ├─ metadata_generation_command.txt
   │  │     │  │  │  │        ├─ prefab_config.json
   │  │     │  │  │  │        └─ symbol_folder_index.txt
   │  │     │  │  │  └─ tools
   │  │     │  │  │     └─ profile
   │  │     │  │  │        ├─ arm64-v8a
   │  │     │  │  │        │  └─ compile_commands.json
   │  │     │  │  │        ├─ armeabi-v7a
   │  │     │  │  │        │  └─ compile_commands.json
   │  │     │  │  │        ├─ x86
   │  │     │  │  │        │  └─ compile_commands.json
   │  │     │  │  │        └─ x86_64
   │  │     │  │  │           └─ compile_commands.json
   │  │     │  │  ├─ build.gradle
   │  │     │  │  ├─ consumer-rules.pro
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ settings.gradle
   │  │     │  │  └─ src
   │  │     │  │     └─ main
   │  │     │  │        ├─ AndroidManifest.xml
   │  │     │  │        └─ java
   │  │     │  │           └─ com
   │  │     │  │              └─ github
   │  │     │  │                 └─ dart_lang
   │  │     │  │                    └─ jni
   │  │     │  │                       └─ JniPlugin.java
   │  │     │  ├─ bin
   │  │     │  │  └─ setup.dart
   │  │     │  ├─ CHANGELOG.md
   │  │     │  ├─ dart_test.yaml
   │  │     │  ├─ example
   │  │     │  │  ├─ analysis_options.yaml
   │  │     │  │  ├─ android
   │  │     │  │  │  ├─ app
   │  │     │  │  │  │  ├─ build.gradle
   │  │     │  │  │  │  └─ src
   │  │     │  │  │  │     ├─ debug
   │  │     │  │  │  │     │  └─ AndroidManifest.xml
   │  │     │  │  │  │     ├─ main
   │  │     │  │  │  │     │  ├─ AndroidManifest.xml
   │  │     │  │  │  │     │  ├─ java
   │  │     │  │  │  │     │  │  ├─ com
   │  │     │  │  │  │     │  │  │  └─ github
   │  │     │  │  │  │     │  │  │     └─ dart_lang
   │  │     │  │  │  │     │  │  │        └─ jni_example
   │  │     │  │  │  │     │  │  │           └─ Toaster.java
   │  │     │  │  │  │     │  │  └─ io
   │  │     │  │  │  │     │  │     └─ flutter
   │  │     │  │  │  │     │  │        └─ plugins
   │  │     │  │  │  │     │  ├─ kotlin
   │  │     │  │  │  │     │  │  └─ dev
   │  │     │  │  │  │     │  │     └─ dart
   │  │     │  │  │  │     │  │        └─ jni_example
   │  │     │  │  │  │     │  │           └─ MainActivity.kt
   │  │     │  │  │  │     │  └─ res
   │  │     │  │  │  │     │     ├─ drawable
   │  │     │  │  │  │     │     │  └─ launch_background.xml
   │  │     │  │  │  │     │     ├─ drawable-v21
   │  │     │  │  │  │     │     │  └─ launch_background.xml
   │  │     │  │  │  │     │     ├─ mipmap-hdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-mdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-xhdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-xxhdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ mipmap-xxxhdpi
   │  │     │  │  │  │     │     │  └─ ic_launcher.png
   │  │     │  │  │  │     │     ├─ values
   │  │     │  │  │  │     │     │  └─ styles.xml
   │  │     │  │  │  │     │     └─ values-night
   │  │     │  │  │  │     │        └─ styles.xml
   │  │     │  │  │  │     └─ profile
   │  │     │  │  │  │        └─ AndroidManifest.xml
   │  │     │  │  │  ├─ build.gradle
   │  │     │  │  │  ├─ gradle
   │  │     │  │  │  │  └─ wrapper
   │  │     │  │  │  │     └─ gradle-wrapper.properties
   │  │     │  │  │  ├─ gradle.properties
   │  │     │  │  │  └─ settings.gradle
   │  │     │  │  ├─ integration_test
   │  │     │  │  │  └─ on_device_jni_test.dart
   │  │     │  │  ├─ lib
   │  │     │  │  │  └─ main.dart
   │  │     │  │  ├─ linux
   │  │     │  │  │  ├─ CMakeLists.txt
   │  │     │  │  │  ├─ flutter
   │  │     │  │  │  │  └─ CMakeLists.txt
   │  │     │  │  │  ├─ main.cc
   │  │     │  │  │  ├─ my_application.cc
   │  │     │  │  │  └─ my_application.h
   │  │     │  │  ├─ macos
   │  │     │  │  │  ├─ Flutter
   │  │     │  │  │  │  ├─ Flutter-Debug.xcconfig
   │  │     │  │  │  │  └─ Flutter-Release.xcconfig
   │  │     │  │  │  ├─ Podfile
   │  │     │  │  │  ├─ Runner
   │  │     │  │  │  │  ├─ AppDelegate.swift
   │  │     │  │  │  │  ├─ Assets.xcassets
   │  │     │  │  │  │  │  └─ AppIcon.appiconset
   │  │     │  │  │  │  │     ├─ app_icon_1024.png
   │  │     │  │  │  │  │     ├─ app_icon_128.png
   │  │     │  │  │  │  │     ├─ app_icon_16.png
   │  │     │  │  │  │  │     ├─ app_icon_256.png
   │  │     │  │  │  │  │     ├─ app_icon_32.png
   │  │     │  │  │  │  │     ├─ app_icon_512.png
   │  │     │  │  │  │  │     ├─ app_icon_64.png
   │  │     │  │  │  │  │     └─ Contents.json
   │  │     │  │  │  │  ├─ Base.lproj
   │  │     │  │  │  │  │  └─ MainMenu.xib
   │  │     │  │  │  │  ├─ Configs
   │  │     │  │  │  │  │  ├─ AppInfo.xcconfig
   │  │     │  │  │  │  │  ├─ Debug.xcconfig
   │  │     │  │  │  │  │  ├─ Release.xcconfig
   │  │     │  │  │  │  │  └─ Warnings.xcconfig
   │  │     │  │  │  │  ├─ DebugProfile.entitlements
   │  │     │  │  │  │  ├─ Info.plist
   │  │     │  │  │  │  ├─ MainFlutterWindow.swift
   │  │     │  │  │  │  └─ Release.entitlements
   │  │     │  │  │  ├─ Runner.xcodeproj
   │  │     │  │  │  │  ├─ project.pbxproj
   │  │     │  │  │  │  ├─ project.xcworkspace
   │  │     │  │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │  │     └─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     └─ xcschemes
   │  │     │  │  │  │        └─ Runner.xcscheme
   │  │     │  │  │  └─ Runner.xcworkspace
   │  │     │  │  │     ├─ contents.xcworkspacedata
   │  │     │  │  │     └─ xcshareddata
   │  │     │  │  │        └─ IDEWorkspaceChecks.plist
   │  │     │  │  ├─ pubspec.yaml
   │  │     │  │  ├─ README.md
   │  │     │  │  └─ windows
   │  │     │  │     ├─ CMakeLists.txt
   │  │     │  │     ├─ flutter
   │  │     │  │     │  └─ CMakeLists.txt
   │  │     │  │     └─ runner
   │  │     │  │        ├─ CMakeLists.txt
   │  │     │  │        ├─ flutter_window.cpp
   │  │     │  │        ├─ flutter_window.h
   │  │     │  │        ├─ main.cpp
   │  │     │  │        ├─ resource.h
   │  │     │  │        ├─ resources
   │  │     │  │        │  └─ app_icon.ico
   │  │     │  │        ├─ runner.exe.manifest
   │  │     │  │        ├─ Runner.rc
   │  │     │  │        ├─ utils.cpp
   │  │     │  │        ├─ utils.h
   │  │     │  │        ├─ win32_window.cpp
   │  │     │  │        └─ win32_window.h
   │  │     │  ├─ ffigen.yaml
   │  │     │  ├─ ffigen_exts.yaml
   │  │     │  ├─ java
   │  │     │  │  ├─ build.gradle.kts
   │  │     │  │  ├─ gradle
   │  │     │  │  │  ├─ libs.versions.toml
   │  │     │  │  │  └─ wrapper
   │  │     │  │  │     ├─ gradle-wrapper.jar
   │  │     │  │  │     └─ gradle-wrapper.properties
   │  │     │  │  ├─ gradlew
   │  │     │  │  ├─ gradlew.bat
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ settings.gradle.kts
   │  │     │  │  ├─ src
   │  │     │  │  │  └─ main
   │  │     │  │  │     └─ java
   │  │     │  │  │        └─ com
   │  │     │  │  │           └─ github
   │  │     │  │  │              └─ dart_lang
   │  │     │  │  │                 └─ jni
   │  │     │  │  │                    ├─ JniUtils.java
   │  │     │  │  │                    ├─ PortCleaner.java
   │  │     │  │  │                    ├─ PortContinuation.java
   │  │     │  │  │                    └─ PortProxyBuilder.java
   │  │     │  │  └─ ~
   │  │     │  │     └─ dev
   │  │     │  │        ├─ native
   │  │     │  │        │  └─ native
   │  │     │  │        │     └─ pkgs
   │  │     │  │        │        └─ jnigen
   │  │     │  │        │           └─ example
   │  │     │  │        │              └─ pdfbox_plugin
   │  │     │  │        │                 └─ dart_example
   │  │     │  │        └─ native2
   │  │     │  │           └─ pkgs
   │  │     │  │              └─ jnigen
   │  │     │  │                 └─ example
   │  │     │  │                    └─ pdfbox_plugin
   │  │     │  │                       └─ dart_example
   │  │     │  ├─ lib
   │  │     │  │  ├─ jni.dart
   │  │     │  │  ├─ jni_symbols.yaml
   │  │     │  │  ├─ src
   │  │     │  │  │  ├─ accessors.dart
   │  │     │  │  │  ├─ build_util
   │  │     │  │  │  │  └─ build_util.dart
   │  │     │  │  │  ├─ core_bindings.dart
   │  │     │  │  │  ├─ errors.dart
   │  │     │  │  │  ├─ jarray.dart
   │  │     │  │  │  ├─ jclass.dart
   │  │     │  │  │  ├─ jimplementer.dart
   │  │     │  │  │  ├─ jni.dart
   │  │     │  │  │  ├─ jobject.dart
   │  │     │  │  │  ├─ jprimitives.dart
   │  │     │  │  │  ├─ jreference.dart
   │  │     │  │  │  ├─ jvalues.dart
   │  │     │  │  │  ├─ kotlin.dart
   │  │     │  │  │  ├─ lang
   │  │     │  │  │  │  ├─ jboolean.dart
   │  │     │  │  │  │  ├─ jbyte.dart
   │  │     │  │  │  │  ├─ jcharacter.dart
   │  │     │  │  │  │  ├─ jdouble.dart
   │  │     │  │  │  │  ├─ jfloat.dart
   │  │     │  │  │  │  ├─ jinteger.dart
   │  │     │  │  │  │  ├─ jlong.dart
   │  │     │  │  │  │  ├─ jnumber.dart
   │  │     │  │  │  │  ├─ jshort.dart
   │  │     │  │  │  │  ├─ jstring.dart
   │  │     │  │  │  │  └─ lang.dart
   │  │     │  │  │  ├─ method_invocation.dart
   │  │     │  │  │  ├─ nio
   │  │     │  │  │  │  ├─ jbuffer.dart
   │  │     │  │  │  │  ├─ jbyte_buffer.dart
   │  │     │  │  │  │  └─ nio.dart
   │  │     │  │  │  ├─ primitive_jarrays.dart
   │  │     │  │  │  ├─ third_party
   │  │     │  │  │  │  ├─ generated_bindings.dart
   │  │     │  │  │  │  ├─ global_env_extensions.dart
   │  │     │  │  │  │  └─ jni_bindings_generated.dart
   │  │     │  │  │  ├─ types.dart
   │  │     │  │  │  ├─ util
   │  │     │  │  │  │  ├─ jiterator.dart
   │  │     │  │  │  │  ├─ jlist.dart
   │  │     │  │  │  │  ├─ jmap.dart
   │  │     │  │  │  │  ├─ jset.dart
   │  │     │  │  │  │  └─ util.dart
   │  │     │  │  │  └─ version_check.dart
   │  │     │  │  └─ _internal.dart
   │  │     │  ├─ LICENSE
   │  │     │  ├─ linux
   │  │     │  │  └─ CMakeLists.txt
   │  │     │  ├─ pubspec.yaml
   │  │     │  ├─ README.md
   │  │     │  ├─ src
   │  │     │  │  ├─ CMakeLists.txt
   │  │     │  │  ├─ dartjni.c
   │  │     │  │  ├─ dartjni.h
   │  │     │  │  ├─ include
   │  │     │  │  │  ├─ analyze_snapshot_api.h
   │  │     │  │  │  ├─ bin
   │  │     │  │  │  │  ├─ dart_io_api.h
   │  │     │  │  │  │  └─ native_assets_api.h
   │  │     │  │  │  ├─ BUILD.gn
   │  │     │  │  │  ├─ dart_api.h
   │  │     │  │  │  ├─ dart_api_dl.c
   │  │     │  │  │  ├─ dart_api_dl.h
   │  │     │  │  │  ├─ dart_embedder_api.h
   │  │     │  │  │  ├─ dart_native_api.h
   │  │     │  │  │  ├─ dart_tools_api.h
   │  │     │  │  │  ├─ dart_version.h
   │  │     │  │  │  └─ internal
   │  │     │  │  │     └─ dart_api_dl_impl.h
   │  │     │  │  ├─ jni_constants.h
   │  │     │  │  ├─ README.md
   │  │     │  │  └─ third_party
   │  │     │  │     ├─ global_jni_env.c
   │  │     │  │     └─ global_jni_env.h
   │  │     │  ├─ test
   │  │     │  │  ├─ boxed_test.dart
   │  │     │  │  ├─ debug_release_test.dart
   │  │     │  │  ├─ exception_test.dart
   │  │     │  │  ├─ global_env_test.dart
   │  │     │  │  ├─ isolate_test.dart
   │  │     │  │  ├─ jarray_test.dart
   │  │     │  │  ├─ jbyte_buffer_test.dart
   │  │     │  │  ├─ jlist_test.dart
   │  │     │  │  ├─ jmap_test.dart
   │  │     │  │  ├─ jobject_test.dart
   │  │     │  │  ├─ jset_test.dart
   │  │     │  │  ├─ jstring_test.dart
   │  │     │  │  ├─ load_test.dart
   │  │     │  │  ├─ test_util
   │  │     │  │  │  └─ test_util.dart
   │  │     │  │  ├─ version_check
   │  │     │  │  │  ├─ fail_major.dart
   │  │     │  │  │  ├─ fail_minor.dart
   │  │     │  │  │  └─ pass.dart
   │  │     │  │  └─ version_check_test.dart
   │  │     │  ├─ third_party
   │  │     │  │  └─ jni.h
   │  │     │  ├─ tool
   │  │     │  │  ├─ generate_ffi_bindings.dart
   │  │     │  │  ├─ generate_ide_files.dart
   │  │     │  │  ├─ generate_jni_bindings.dart
   │  │     │  │  ├─ generate_primitive_arrays.dart
   │  │     │  │  └─ wrapper_generators
   │  │     │  │     ├─ ffigen_util.dart
   │  │     │  │     ├─ generate_c_extensions.dart
   │  │     │  │     ├─ generate_dart_extensions.dart
   │  │     │  │     ├─ generate_helper_functions.dart
   │  │     │  │     └─ logging.dart
   │  │     │  └─ windows
   │  │     │     └─ CMakeLists.txt
   │  │     ├─ package_info_plus
   │  │     │  ├─ android
   │  │     │  │  ├─ .gradle
   │  │     │  │  │  ├─ 9.3.0
   │  │     │  │  │  │  ├─ checksums
   │  │     │  │  │  │  │  └─ checksums.lock
   │  │     │  │  │  │  ├─ expanded
   │  │     │  │  │  │  ├─ fileChanges
   │  │     │  │  │  │  │  └─ last-build.bin
   │  │     │  │  │  │  ├─ fileHashes
   │  │     │  │  │  │  │  ├─ fileHashes.bin
   │  │     │  │  │  │  │  └─ fileHashes.lock
   │  │     │  │  │  │  ├─ gc.properties
   │  │     │  │  │  │  └─ vcsMetadata
   │  │     │  │  │  ├─ buildOutputCleanup
   │  │     │  │  │  │  ├─ buildOutputCleanup.lock
   │  │     │  │  │  │  └─ cache.properties
   │  │     │  │  │  ├─ nb-cache
   │  │     │  │  │  │  └─ trust
   │  │     │  │  │  │     ├─ 1091BD2091310B8B25A9BB02CA8EECB26410AB1EAB7B592369DAC1440802511E
   │  │     │  │  │  │     └─ 5F331A9272FAC7AF948AEF82359CA442D42F889C4AC427E416A0DD4E37DF2D11
   │  │     │  │  │  └─ vcs-1
   │  │     │  │  │     └─ gc.properties
   │  │     │  │  ├─ build.gradle.kts
   │  │     │  │  ├─ gradle.properties
   │  │     │  │  ├─ settings.gradle.kts
   │  │     │  │  └─ src
   │  │     │  │     └─ main
   │  │     │  │        ├─ AndroidManifest.xml
   │  │     │  │        └─ kotlin
   │  │     │  │           └─ dev
   │  │     │  │              └─ fluttercommunity
   │  │     │  │                 └─ plus
   │  │     │  │                    └─ packageinfo
   │  │     │  │                       └─ PackageInfoPlugin.kt
   │  │     │  ├─ CHANGELOG.md
   │  │     │  ├─ example
   │  │     │  │  ├─ analysis_options.yaml
   │  │     │  │  ├─ android
   │  │     │  │  │  ├─ app
   │  │     │  │  │  │  ├─ build.gradle.kts
   │  │     │  │  │  │  └─ src
   │  │     │  │  │  │     ├─ androidTest
   │  │     │  │  │  │     │  └─ java
   │  │     │  │  │  │     │     └─ io
   │  │     │  │  │  │     │        └─ flutter
   │  │     │  │  │  │     │           └─ plugins
   │  │     │  │  │  │     │              └─ packageinfoexample
   │  │     │  │  │  │     │                 ├─ EmbedderV1ActivityTest.java
   │  │     │  │  │  │     │                 └─ MainActivityTest.java
   │  │     │  │  │  │     └─ main
   │  │     │  │  │  │        ├─ AndroidManifest.xml
   │  │     │  │  │  │        ├─ java
   │  │     │  │  │  │        │  └─ io
   │  │     │  │  │  │        │     └─ flutter
   │  │     │  │  │  │        │        └─ plugins
   │  │     │  │  │  │        └─ res
   │  │     │  │  │  │           ├─ mipmap-hdpi
   │  │     │  │  │  │           │  └─ ic_launcher.png
   │  │     │  │  │  │           ├─ mipmap-mdpi
   │  │     │  │  │  │           │  └─ ic_launcher.png
   │  │     │  │  │  │           ├─ mipmap-xhdpi
   │  │     │  │  │  │           │  └─ ic_launcher.png
   │  │     │  │  │  │           ├─ mipmap-xxhdpi
   │  │     │  │  │  │           │  └─ ic_launcher.png
   │  │     │  │  │  │           └─ mipmap-xxxhdpi
   │  │     │  │  │  │              └─ ic_launcher.png
   │  │     │  │  │  ├─ build.gradle.kts
   │  │     │  │  │  ├─ gradle
   │  │     │  │  │  │  └─ wrapper
   │  │     │  │  │  │     └─ gradle-wrapper.properties
   │  │     │  │  │  ├─ gradle.properties
   │  │     │  │  │  └─ settings.gradle.kts
   │  │     │  │  ├─ build.yaml
   │  │     │  │  ├─ integration_test
   │  │     │  │  │  ├─ driver.dart
   │  │     │  │  │  ├─ package_info_plus_test.dart
   │  │     │  │  │  ├─ package_info_plus_web_test.dart
   │  │     │  │  │  └─ package_info_plus_web_test.mocks.dart
   │  │     │  │  ├─ ios
   │  │     │  │  │  ├─ Flutter
   │  │     │  │  │  │  ├─ AppFrameworkInfo.plist
   │  │     │  │  │  │  ├─ Debug.xcconfig
   │  │     │  │  │  │  └─ Release.xcconfig
   │  │     │  │  │  ├─ Runner
   │  │     │  │  │  │  ├─ AppDelegate.swift
   │  │     │  │  │  │  ├─ Assets.xcassets
   │  │     │  │  │  │  │  ├─ AppIcon.appiconset
   │  │     │  │  │  │  │  │  ├─ Contents.json
   │  │     │  │  │  │  │  │  ├─ Icon-App-1024x1024@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-20x20@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-29x29@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-40x40@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-60x60@2x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-60x60@3x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-76x76@1x.png
   │  │     │  │  │  │  │  │  ├─ Icon-App-76x76@2x.png
   │  │     │  │  │  │  │  │  └─ Icon-App-83.5x83.5@2x.png
   │  │     │  │  │  │  │  └─ LaunchImage.imageset
   │  │     │  │  │  │  │     ├─ Contents.json
   │  │     │  │  │  │  │     ├─ LaunchImage.png
   │  │     │  │  │  │  │     ├─ LaunchImage@2x.png
   │  │     │  │  │  │  │     ├─ LaunchImage@3x.png
   │  │     │  │  │  │  │     └─ README.md
   │  │     │  │  │  │  ├─ Base.lproj
   │  │     │  │  │  │  │  ├─ LaunchScreen.storyboard
   │  │     │  │  │  │  │  └─ Main.storyboard
   │  │     │  │  │  │  ├─ Info.plist
   │  │     │  │  │  │  └─ Runner-Bridging-Header.h
   │  │     │  │  │  ├─ Runner.xcodeproj
   │  │     │  │  │  │  ├─ project.pbxproj
   │  │     │  │  │  │  ├─ project.xcworkspace
   │  │     │  │  │  │  │  ├─ contents.xcworkspacedata
   │  │     │  │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │  │     ├─ swiftpm
   │  │     │  │  │  │  │     │  └─ configuration
   │  │     │  │  │  │  │     └─ WorkspaceSettings.xcsettings
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     └─ xcschemes
   │  │     │  │  │  │        └─ Runner.xcscheme
   │  │     │  │  │  ├─ Runner.xcworkspace
   │  │     │  │  │  │  ├─ contents.xcworkspacedata
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │     ├─ swiftpm
   │  │     │  │  │  │     │  └─ configuration
   │  │     │  │  │  │     └─ WorkspaceSettings.xcsettings
   │  │     │  │  │  └─ RunnerTests
   │  │     │  │  │     └─ RunnerTests.swift
   │  │     │  │  ├─ lib
   │  │     │  │  │  └─ main.dart
   │  │     │  │  ├─ linux
   │  │     │  │  │  ├─ CMakeLists.txt
   │  │     │  │  │  ├─ flutter
   │  │     │  │  │  │  └─ CMakeLists.txt
   │  │     │  │  │  ├─ main.cc
   │  │     │  │  │  ├─ my_application.cc
   │  │     │  │  │  └─ my_application.h
   │  │     │  │  ├─ macos
   │  │     │  │  │  ├─ Flutter
   │  │     │  │  │  │  ├─ Flutter-Debug.xcconfig
   │  │     │  │  │  │  └─ Flutter-Release.xcconfig
   │  │     │  │  │  ├─ Runner
   │  │     │  │  │  │  ├─ AppDelegate.swift
   │  │     │  │  │  │  ├─ Assets.xcassets
   │  │     │  │  │  │  │  └─ AppIcon.appiconset
   │  │     │  │  │  │  │     ├─ app_icon_1024.png
   │  │     │  │  │  │  │     ├─ app_icon_128.png
   │  │     │  │  │  │  │     ├─ app_icon_16.png
   │  │     │  │  │  │  │     ├─ app_icon_256.png
   │  │     │  │  │  │  │     ├─ app_icon_32.png
   │  │     │  │  │  │  │     ├─ app_icon_512.png
   │  │     │  │  │  │  │     ├─ app_icon_64.png
   │  │     │  │  │  │  │     └─ Contents.json
   │  │     │  │  │  │  ├─ Base.lproj
   │  │     │  │  │  │  │  └─ MainMenu.xib
   │  │     │  │  │  │  ├─ Configs
   │  │     │  │  │  │  │  ├─ AppInfo.xcconfig
   │  │     │  │  │  │  │  ├─ Debug.xcconfig
   │  │     │  │  │  │  │  ├─ Release.xcconfig
   │  │     │  │  │  │  │  └─ Warnings.xcconfig
   │  │     │  │  │  │  ├─ DebugProfile.entitlements
   │  │     │  │  │  │  ├─ Info.plist
   │  │     │  │  │  │  ├─ MainFlutterWindow.swift
   │  │     │  │  │  │  └─ Release.entitlements
   │  │     │  │  │  ├─ Runner.xcodeproj
   │  │     │  │  │  │  ├─ project.pbxproj
   │  │     │  │  │  │  ├─ project.xcworkspace
   │  │     │  │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │  │     └─ swiftpm
   │  │     │  │  │  │  │        └─ configuration
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     └─ xcschemes
   │  │     │  │  │  │        └─ Runner.xcscheme
   │  │     │  │  │  ├─ Runner.xcworkspace
   │  │     │  │  │  │  ├─ contents.xcworkspacedata
   │  │     │  │  │  │  └─ xcshareddata
   │  │     │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │     │  │  │  │     └─ swiftpm
   │  │     │  │  │  │        └─ configuration
   │  │     │  │  │  └─ RunnerTests
   │  │     │  │  │     └─ RunnerTests.swift
   │  │     │  │  ├─ pubspec.yaml
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ test
   │  │     │  │  ├─ web
   │  │     │  │  │  ├─ favicon.png
   │  │     │  │  │  ├─ icons
   │  │     │  │  │  │  ├─ Icon-192.png
   │  │     │  │  │  │  ├─ Icon-512.png
   │  │     │  │  │  │  ├─ Icon-maskable-192.png
   │  │     │  │  │  │  └─ Icon-maskable-512.png
   │  │     │  │  │  ├─ index.html
   │  │     │  │  │  └─ manifest.json
   │  │     │  │  └─ windows
   │  │     │  │     ├─ CMakeLists.txt
   │  │     │  │     ├─ flutter
   │  │     │  │     │  └─ CMakeLists.txt
   │  │     │  │     └─ runner
   │  │     │  │        ├─ CMakeLists.txt
   │  │     │  │        ├─ flutter_window.cpp
   │  │     │  │        ├─ flutter_window.h
   │  │     │  │        ├─ main.cpp
   │  │     │  │        ├─ resource.h
   │  │     │  │        ├─ resources
   │  │     │  │        │  └─ app_icon.ico
   │  │     │  │        ├─ runner.exe.manifest
   │  │     │  │        ├─ Runner.rc
   │  │     │  │        ├─ utils.cpp
   │  │     │  │        ├─ utils.h
   │  │     │  │        ├─ win32_window.cpp
   │  │     │  │        └─ win32_window.h
   │  │     │  ├─ ios
   │  │     │  │  ├─ package_info_plus
   │  │     │  │  │  ├─ Package.swift
   │  │     │  │  │  └─ Sources
   │  │     │  │  │     └─ package_info_plus
   │  │     │  │  │        ├─ FPPPackageInfoPlusPlugin.m
   │  │     │  │  │        ├─ include
   │  │     │  │  │        │  └─ package_info_plus
   │  │     │  │  │        │     └─ FPPPackageInfoPlusPlugin.h
   │  │     │  │  │        └─ PrivacyInfo.xcprivacy
   │  │     │  │  └─ package_info_plus.podspec
   │  │     │  ├─ lib
   │  │     │  │  ├─ package_info_plus.dart
   │  │     │  │  └─ src
   │  │     │  │     ├─ file_attribute.dart
   │  │     │  │     ├─ file_version_info.dart
   │  │     │  │     ├─ package_info_plus_linux.dart
   │  │     │  │     ├─ package_info_plus_macos.dart
   │  │     │  │     ├─ package_info_plus_web.dart
   │  │     │  │     └─ package_info_plus_windows.dart
   │  │     │  ├─ LICENSE
   │  │     │  ├─ macos
   │  │     │  │  ├─ package_info_plus
   │  │     │  │  │  ├─ Package.swift
   │  │     │  │  │  └─ Sources
   │  │     │  │  │     └─ package_info_plus
   │  │     │  │  │        ├─ FPPPackageInfoPlusPlugin.m
   │  │     │  │  │        ├─ include
   │  │     │  │  │        │  └─ package_info_plus
   │  │     │  │  │        │     └─ FPPPackageInfoPlusPlugin.h
   │  │     │  │  │        └─ PrivacyInfo.xcprivacy
   │  │     │  │  └─ package_info_plus.podspec
   │  │     │  ├─ pubspec.yaml
   │  │     │  ├─ README.md
   │  │     │  └─ test
   │  │     │     ├─ package_info_plus_linux_test.dart
   │  │     │     ├─ package_info_plus_windows_test.dart
   │  │     │     └─ package_info_test.dart
   │  │     ├─ path_provider_windows
   │  │     │  ├─ AUTHORS
   │  │     │  ├─ CHANGELOG.md
   │  │     │  ├─ example
   │  │     │  │  ├─ integration_test
   │  │     │  │  │  └─ path_provider_test.dart
   │  │     │  │  ├─ lib
   │  │     │  │  │  └─ main.dart
   │  │     │  │  ├─ pubspec.yaml
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ test_driver
   │  │     │  │  │  └─ integration_test.dart
   │  │     │  │  └─ windows
   │  │     │  │     ├─ CMakeLists.txt
   │  │     │  │     ├─ flutter
   │  │     │  │     │  ├─ CMakeLists.txt
   │  │     │  │     │  └─ generated_plugins.cmake
   │  │     │  │     └─ runner
   │  │     │  │        ├─ CMakeLists.txt
   │  │     │  │        ├─ flutter_window.cpp
   │  │     │  │        ├─ flutter_window.h
   │  │     │  │        ├─ main.cpp
   │  │     │  │        ├─ resource.h
   │  │     │  │        ├─ resources
   │  │     │  │        │  └─ app_icon.ico
   │  │     │  │        ├─ runner.exe.manifest
   │  │     │  │        ├─ Runner.rc
   │  │     │  │        ├─ run_loop.cpp
   │  │     │  │        ├─ run_loop.h
   │  │     │  │        ├─ utils.cpp
   │  │     │  │        ├─ utils.h
   │  │     │  │        ├─ win32_window.cpp
   │  │     │  │        └─ win32_window.h
   │  │     │  ├─ lib
   │  │     │  │  ├─ path_provider_windows.dart
   │  │     │  │  └─ src
   │  │     │  │     ├─ folders.dart
   │  │     │  │     ├─ folders_stub.dart
   │  │     │  │     ├─ guid.dart
   │  │     │  │     ├─ path_provider_windows_real.dart
   │  │     │  │     ├─ path_provider_windows_stub.dart
   │  │     │  │     └─ win32_wrappers.dart
   │  │     │  ├─ LICENSE
   │  │     │  ├─ pubspec.yaml
   │  │     │  ├─ README.md
   │  │     │  └─ test
   │  │     │     ├─ guid_test.dart
   │  │     │     └─ path_provider_windows_test.dart
   │  │     ├─ screen_brightness_windows
   │  │     │  ├─ analysis_options.yaml
   │  │     │  ├─ CHANGELOG.md
   │  │     │  ├─ example
   │  │     │  │  ├─ analysis_options.yaml
   │  │     │  │  ├─ lib
   │  │     │  │  │  └─ main.dart
   │  │     │  │  ├─ pubspec.yaml
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ test
   │  │     │  │  │  └─ widget_test.dart
   │  │     │  │  └─ windows
   │  │     │  │     ├─ CMakeLists.txt
   │  │     │  │     ├─ flutter
   │  │     │  │     │  ├─ CMakeLists.txt
   │  │     │  │     │  ├─ generated_plugins.cmake
   │  │     │  │     │  ├─ generated_plugin_registrant.cc
   │  │     │  │     │  └─ generated_plugin_registrant.h
   │  │     │  │     └─ runner
   │  │     │  │        ├─ CMakeLists.txt
   │  │     │  │        ├─ flutter_window.cpp
   │  │     │  │        ├─ flutter_window.h
   │  │     │  │        ├─ main.cpp
   │  │     │  │        ├─ resource.h
   │  │     │  │        ├─ resources
   │  │     │  │        │  └─ app_icon.ico
   │  │     │  │        ├─ runner.exe.manifest
   │  │     │  │        ├─ Runner.rc
   │  │     │  │        ├─ utils.cpp
   │  │     │  │        ├─ utils.h
   │  │     │  │        ├─ win32_window.cpp
   │  │     │  │        └─ win32_window.h
   │  │     │  ├─ LICENSE
   │  │     │  ├─ pubspec.yaml
   │  │     │  ├─ README.md
   │  │     │  └─ windows
   │  │     │     ├─ CMakeLists.txt
   │  │     │     ├─ include
   │  │     │     │  └─ screen_brightness_windows
   │  │     │     │     ├─ base_stream_handler.h
   │  │     │     │     ├─ screen_brightness_changed_stream_handler.h
   │  │     │     │     ├─ screen_brightness_windows_plugin.h
   │  │     │     │     └─ screen_brightness_windows_plugin_c_api.h
   │  │     │     ├─ screen_brightness_windows_plugin_c_api.cpp
   │  │     │     └─ src
   │  │     │        ├─ screen_brightness_changed_stream_handler.cpp
   │  │     │        └─ screen_brightness_windows_plugin.cpp
   │  │     ├─ speech_to_text_windows
   │  │     │  ├─ CHANGELOG.md
   │  │     │  ├─ example
   │  │     │  │  ├─ analysis_options.yaml
   │  │     │  │  ├─ lib
   │  │     │  │  │  └─ main.dart
   │  │     │  │  ├─ pubspec.yaml
   │  │     │  │  ├─ README.md
   │  │     │  │  ├─ test
   │  │     │  │  │  └─ widget_test.dart
   │  │     │  │  └─ windows
   │  │     │  │     ├─ CMakeLists.txt
   │  │     │  │     ├─ flutter
   │  │     │  │     │  ├─ CMakeLists.txt
   │  │     │  │     │  ├─ generated_plugins.cmake
   │  │     │  │     │  ├─ generated_plugin_registrant.cc
   │  │     │  │     │  └─ generated_plugin_registrant.h
   │  │     │  │     └─ runner
   │  │     │  │        ├─ CMakeLists.txt
   │  │     │  │        ├─ flutter_window.cpp
   │  │     │  │        ├─ flutter_window.h
   │  │     │  │        ├─ main.cpp
   │  │     │  │        ├─ resource.h
   │  │     │  │        ├─ resources
   │  │     │  │        │  └─ app_icon.ico
   │  │     │  │        ├─ runner.exe.manifest
   │  │     │  │        ├─ Runner.rc
   │  │     │  │        ├─ utils.cpp
   │  │     │  │        ├─ utils.h
   │  │     │  │        ├─ win32_window.cpp
   │  │     │  │        └─ win32_window.h
   │  │     │  ├─ lib
   │  │     │  │  ├─ speech_to_text_windows.dart
   │  │     │  │  └─ speech_to_text_windows_method_channel.dart
   │  │     │  ├─ LICENSE
   │  │     │  ├─ pubspec.yaml
   │  │     │  ├─ README.md
   │  │     │  └─ windows
   │  │     │     ├─ CMakeLists.txt
   │  │     │     ├─ include
   │  │     │     │  └─ speech_to_text_windows
   │  │     │     │     └─ speech_to_text_windows.h
   │  │     │     ├─ speech_to_text_windows.cpp
   │  │     │     ├─ speech_to_text_windows_plugin.cpp
   │  │     │     └─ speech_to_text_windows_plugin.h
   │  │     └─ wakelock_plus
   │  │        ├─ analysis_options.yaml
   │  │        ├─ android
   │  │        │  ├─ .gradle
   │  │        │  │  ├─ 9.3.0
   │  │        │  │  │  ├─ checksums
   │  │        │  │  │  │  └─ checksums.lock
   │  │        │  │  │  ├─ expanded
   │  │        │  │  │  ├─ fileChanges
   │  │        │  │  │  │  └─ last-build.bin
   │  │        │  │  │  ├─ fileHashes
   │  │        │  │  │  │  ├─ fileHashes.bin
   │  │        │  │  │  │  └─ fileHashes.lock
   │  │        │  │  │  ├─ gc.properties
   │  │        │  │  │  └─ vcsMetadata
   │  │        │  │  ├─ buildOutputCleanup
   │  │        │  │  │  ├─ buildOutputCleanup.lock
   │  │        │  │  │  └─ cache.properties
   │  │        │  │  ├─ nb-cache
   │  │        │  │  │  └─ trust
   │  │        │  │  │     ├─ 506B6481844514C42B5113DF3ECE21943EE1DCE0192C040A9B87FF6210987242
   │  │        │  │  │     └─ 927C1BF9B394344BB3951AD39AB52F331483697A8C445F7D033058ABBEC42540
   │  │        │  │  └─ vcs-1
   │  │        │  │     └─ gc.properties
   │  │        │  ├─ build.gradle
   │  │        │  ├─ settings.gradle
   │  │        │  └─ src
   │  │        │     └─ main
   │  │        │        ├─ AndroidManifest.xml
   │  │        │        └─ kotlin
   │  │        │           └─ dev
   │  │        │              └─ fluttercommunity
   │  │        │                 └─ plus
   │  │        │                    └─ wakelock
   │  │        │                       ├─ Wakelock.kt
   │  │        │                       ├─ WakelockPlusMessages.g.kt
   │  │        │                       └─ WakelockPlusPlugin.kt
   │  │        ├─ CHANGELOG.md
   │  │        ├─ example
   │  │        │  ├─ analysis_options.yaml
   │  │        │  ├─ android
   │  │        │  │  ├─ app
   │  │        │  │  │  ├─ build.gradle
   │  │        │  │  │  └─ src
   │  │        │  │  │     ├─ debug
   │  │        │  │  │     │  └─ AndroidManifest.xml
   │  │        │  │  │     ├─ main
   │  │        │  │  │     │  ├─ AndroidManifest.xml
   │  │        │  │  │     │  ├─ java
   │  │        │  │  │     │  │  └─ io
   │  │        │  │  │     │  │     └─ flutter
   │  │        │  │  │     │  │        └─ plugins
   │  │        │  │  │     │  ├─ kotlin
   │  │        │  │  │     │  │  └─ dev
   │  │        │  │  │     │  │     └─ fluttercommunity
   │  │        │  │  │     │  │        └─ plus
   │  │        │  │  │     │  │           └─ wakelock_example
   │  │        │  │  │     │  │              └─ MainActivity.kt
   │  │        │  │  │     │  └─ res
   │  │        │  │  │     │     ├─ drawable
   │  │        │  │  │     │     │  └─ launch_background.xml
   │  │        │  │  │     │     ├─ drawable-v21
   │  │        │  │  │     │     │  └─ launch_background.xml
   │  │        │  │  │     │     ├─ mipmap-hdpi
   │  │        │  │  │     │     │  └─ ic_launcher.png
   │  │        │  │  │     │     ├─ mipmap-mdpi
   │  │        │  │  │     │     │  └─ ic_launcher.png
   │  │        │  │  │     │     ├─ mipmap-xhdpi
   │  │        │  │  │     │     │  └─ ic_launcher.png
   │  │        │  │  │     │     ├─ mipmap-xxhdpi
   │  │        │  │  │     │     │  └─ ic_launcher.png
   │  │        │  │  │     │     ├─ mipmap-xxxhdpi
   │  │        │  │  │     │     │  └─ ic_launcher.png
   │  │        │  │  │     │     ├─ values
   │  │        │  │  │     │     │  └─ styles.xml
   │  │        │  │  │     │     └─ values-night
   │  │        │  │  │     │        └─ styles.xml
   │  │        │  │  │     └─ profile
   │  │        │  │  │        └─ AndroidManifest.xml
   │  │        │  │  ├─ build.gradle
   │  │        │  │  ├─ gradle
   │  │        │  │  │  └─ wrapper
   │  │        │  │  │     └─ gradle-wrapper.properties
   │  │        │  │  ├─ gradle.properties
   │  │        │  │  └─ settings.gradle
   │  │        │  ├─ integration_test
   │  │        │  │  └─ wakelock_plus_test.dart
   │  │        │  ├─ ios
   │  │        │  │  ├─ Flutter
   │  │        │  │  │  ├─ AppFrameworkInfo.plist
   │  │        │  │  │  ├─ Debug.xcconfig
   │  │        │  │  │  └─ Release.xcconfig
   │  │        │  │  ├─ Podfile
   │  │        │  │  ├─ Podfile.lock
   │  │        │  │  ├─ Runner
   │  │        │  │  │  ├─ AppDelegate.h
   │  │        │  │  │  ├─ AppDelegate.m
   │  │        │  │  │  ├─ Assets.xcassets
   │  │        │  │  │  │  ├─ AppIcon.appiconset
   │  │        │  │  │  │  │  ├─ Contents.json
   │  │        │  │  │  │  │  ├─ Icon-App-1024x1024@1x.png
   │  │        │  │  │  │  │  ├─ Icon-App-20x20@1x.png
   │  │        │  │  │  │  │  ├─ Icon-App-20x20@2x.png
   │  │        │  │  │  │  │  ├─ Icon-App-20x20@3x.png
   │  │        │  │  │  │  │  ├─ Icon-App-29x29@1x.png
   │  │        │  │  │  │  │  ├─ Icon-App-29x29@2x.png
   │  │        │  │  │  │  │  ├─ Icon-App-29x29@3x.png
   │  │        │  │  │  │  │  ├─ Icon-App-40x40@1x.png
   │  │        │  │  │  │  │  ├─ Icon-App-40x40@2x.png
   │  │        │  │  │  │  │  ├─ Icon-App-40x40@3x.png
   │  │        │  │  │  │  │  ├─ Icon-App-60x60@2x.png
   │  │        │  │  │  │  │  ├─ Icon-App-60x60@3x.png
   │  │        │  │  │  │  │  ├─ Icon-App-76x76@1x.png
   │  │        │  │  │  │  │  ├─ Icon-App-76x76@2x.png
   │  │        │  │  │  │  │  └─ Icon-App-83.5x83.5@2x.png
   │  │        │  │  │  │  └─ LaunchImage.imageset
   │  │        │  │  │  │     ├─ Contents.json
   │  │        │  │  │  │     ├─ LaunchImage.png
   │  │        │  │  │  │     ├─ LaunchImage@2x.png
   │  │        │  │  │  │     ├─ LaunchImage@3x.png
   │  │        │  │  │  │     └─ README.md
   │  │        │  │  │  ├─ Base.lproj
   │  │        │  │  │  │  ├─ LaunchScreen.storyboard
   │  │        │  │  │  │  └─ Main.storyboard
   │  │        │  │  │  ├─ Info.plist
   │  │        │  │  │  └─ main.m
   │  │        │  │  ├─ Runner.xcodeproj
   │  │        │  │  │  ├─ project.pbxproj
   │  │        │  │  │  ├─ project.xcworkspace
   │  │        │  │  │  │  ├─ contents.xcworkspacedata
   │  │        │  │  │  │  └─ xcshareddata
   │  │        │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │        │  │  │  │     ├─ swiftpm
   │  │        │  │  │  │     │  └─ configuration
   │  │        │  │  │  │     └─ WorkspaceSettings.xcsettings
   │  │        │  │  │  └─ xcshareddata
   │  │        │  │  │     └─ xcschemes
   │  │        │  │  │        └─ Runner.xcscheme
   │  │        │  │  ├─ Runner.xcworkspace
   │  │        │  │  │  ├─ contents.xcworkspacedata
   │  │        │  │  │  └─ xcshareddata
   │  │        │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │        │  │  │     ├─ swiftpm
   │  │        │  │  │     │  └─ configuration
   │  │        │  │  │     └─ WorkspaceSettings.xcsettings
   │  │        │  │  └─ RunnerTests
   │  │        │  │     └─ RunnerTests.m
   │  │        │  ├─ lib
   │  │        │  │  └─ main.dart
   │  │        │  ├─ linux
   │  │        │  │  ├─ CMakeLists.txt
   │  │        │  │  ├─ flutter
   │  │        │  │  │  ├─ CMakeLists.txt
   │  │        │  │  │  ├─ generated_plugins.cmake
   │  │        │  │  │  ├─ generated_plugin_registrant.cc
   │  │        │  │  │  └─ generated_plugin_registrant.h
   │  │        │  │  ├─ main.cc
   │  │        │  │  ├─ my_application.cc
   │  │        │  │  └─ my_application.h
   │  │        │  ├─ macos
   │  │        │  │  ├─ Flutter
   │  │        │  │  │  ├─ Flutter-Debug.xcconfig
   │  │        │  │  │  ├─ Flutter-Release.xcconfig
   │  │        │  │  │  └─ GeneratedPluginRegistrant.swift
   │  │        │  │  ├─ Podfile
   │  │        │  │  ├─ Podfile.lock
   │  │        │  │  ├─ Runner
   │  │        │  │  │  ├─ AppDelegate.swift
   │  │        │  │  │  ├─ Assets.xcassets
   │  │        │  │  │  │  └─ AppIcon.appiconset
   │  │        │  │  │  │     ├─ app_icon_1024.png
   │  │        │  │  │  │     ├─ app_icon_128.png
   │  │        │  │  │  │     ├─ app_icon_16.png
   │  │        │  │  │  │     ├─ app_icon_256.png
   │  │        │  │  │  │     ├─ app_icon_32.png
   │  │        │  │  │  │     ├─ app_icon_512.png
   │  │        │  │  │  │     ├─ app_icon_64.png
   │  │        │  │  │  │     └─ Contents.json
   │  │        │  │  │  ├─ Base.lproj
   │  │        │  │  │  │  └─ MainMenu.xib
   │  │        │  │  │  ├─ Configs
   │  │        │  │  │  │  ├─ AppInfo.xcconfig
   │  │        │  │  │  │  ├─ Debug.xcconfig
   │  │        │  │  │  │  ├─ Release.xcconfig
   │  │        │  │  │  │  └─ Warnings.xcconfig
   │  │        │  │  │  ├─ DebugProfile.entitlements
   │  │        │  │  │  ├─ Info.plist
   │  │        │  │  │  ├─ MainFlutterWindow.swift
   │  │        │  │  │  └─ Release.entitlements
   │  │        │  │  ├─ Runner.xcodeproj
   │  │        │  │  │  ├─ project.pbxproj
   │  │        │  │  │  ├─ project.xcworkspace
   │  │        │  │  │  │  └─ xcshareddata
   │  │        │  │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │        │  │  │  │     └─ swiftpm
   │  │        │  │  │  │        └─ configuration
   │  │        │  │  │  └─ xcshareddata
   │  │        │  │  │     └─ xcschemes
   │  │        │  │  │        └─ Runner.xcscheme
   │  │        │  │  ├─ Runner.xcworkspace
   │  │        │  │  │  ├─ contents.xcworkspacedata
   │  │        │  │  │  └─ xcshareddata
   │  │        │  │  │     ├─ IDEWorkspaceChecks.plist
   │  │        │  │  │     └─ swiftpm
   │  │        │  │  │        └─ configuration
   │  │        │  │  └─ RunnerTests
   │  │        │  │     └─ RunnerTests.swift
   │  │        │  ├─ pubspec.yaml
   │  │        │  ├─ README.md
   │  │        │  ├─ test_driver
   │  │        │  │  └─ integration_test.dart
   │  │        │  ├─ web
   │  │        │  │  ├─ favicon.png
   │  │        │  │  ├─ icons
   │  │        │  │  │  ├─ Icon-192.png
   │  │        │  │  │  ├─ Icon-512.png
   │  │        │  │  │  ├─ Icon-maskable-192.png
   │  │        │  │  │  └─ Icon-maskable-512.png
   │  │        │  │  ├─ index.html
   │  │        │  │  └─ manifest.json
   │  │        │  └─ windows
   │  │        │     ├─ CMakeLists.txt
   │  │        │     ├─ flutter
   │  │        │     │  ├─ CMakeLists.txt
   │  │        │     │  ├─ generated_plugins.cmake
   │  │        │     │  ├─ generated_plugin_registrant.cc
   │  │        │     │  └─ generated_plugin_registrant.h
   │  │        │     └─ runner
   │  │        │        ├─ CMakeLists.txt
   │  │        │        ├─ flutter_window.cpp
   │  │        │        ├─ flutter_window.h
   │  │        │        ├─ main.cpp
   │  │        │        ├─ resource.h
   │  │        │        ├─ resources
   │  │        │        │  └─ app_icon.ico
   │  │        │        ├─ runner.exe.manifest
   │  │        │        ├─ Runner.rc
   │  │        │        ├─ utils.cpp
   │  │        │        ├─ utils.h
   │  │        │        ├─ win32_window.cpp
   │  │        │        └─ win32_window.h
   │  │        ├─ ios
   │  │        │  ├─ wakelock_plus
   │  │        │  │  ├─ Package.swift
   │  │        │  │  └─ Sources
   │  │        │  │     └─ wakelock_plus
   │  │        │  │        ├─ include
   │  │        │  │        │  └─ wakelock_plus
   │  │        │  │        │     ├─ messages.g.h
   │  │        │  │        │     ├─ UIApplication+idleTimerLock.h
   │  │        │  │        │     └─ WakelockPlusPlugin.h
   │  │        │  │        ├─ messages.g.m
   │  │        │  │        ├─ Resources
   │  │        │  │        │  └─ PrivacyInfo.xcprivacy
   │  │        │  │        ├─ UIApplication+idleTimerLock.m
   │  │        │  │        └─ WakelockPlusPlugin.m
   │  │        │  └─ wakelock_plus.podspec
   │  │        ├─ lib
   │  │        │  ├─ assets
   │  │        │  │  └─ no_sleep.js
   │  │        │  ├─ src
   │  │        │  │  ├─ wakelock_plus_io_plugin.dart
   │  │        │  │  ├─ wakelock_plus_linux_plugin.dart
   │  │        │  │  ├─ wakelock_plus_macos_plugin.dart
   │  │        │  │  ├─ wakelock_plus_web_plugin.dart
   │  │        │  │  ├─ wakelock_plus_windows_plugin.dart
   │  │        │  │  └─ web_impl
   │  │        │  │     ├─ import_js_library.dart
   │  │        │  │     └─ js_wakelock.dart
   │  │        │  └─ wakelock_plus.dart
   │  │        ├─ LICENSE
   │  │        ├─ macos
   │  │        │  ├─ wakelock_plus
   │  │        │  │  ├─ Package.swift
   │  │        │  │  └─ Sources
   │  │        │  │     └─ wakelock_plus
   │  │        │  │        ├─ Resources
   │  │        │  │        │  └─ PrivacyInfo.xcprivacy
   │  │        │  │        └─ WakelockPlusMacosPlugin.swift
   │  │        │  └─ wakelock_plus.podspec
   │  │        ├─ pigeons
   │  │        │  └─ messages.dart
   │  │        ├─ pubspec.yaml
   │  │        ├─ README.md
   │  │        └─ test
   │  │           ├─ wakelock_plus_linux_plugin_test.dart
   │  │           ├─ wakelock_plus_test.dart
   │  │           └─ wakelock_plus_web_plugin_test.dart
   │  ├─ generated_plugins.cmake
   │  ├─ generated_plugin_registrant.cc
   │  └─ generated_plugin_registrant.h
   └─ runner
      ├─ CMakeLists.txt
      ├─ flutter_window.cpp
      ├─ flutter_window.h
      ├─ main.cpp
      ├─ resource.h
      ├─ resources
      │  └─ app_icon.ico
      ├─ runner.exe.manifest
      ├─ Runner.rc
      ├─ utils.cpp
      ├─ utils.h
      ├─ win32_window.cpp
      └─ win32_window.h

```