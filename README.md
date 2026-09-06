PS D:\Users\Michael\Dokumente\16_AppDev\jarvis_app> flutter analyze
Analyzing jarvis_app...                                                 

   info - 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss.
          Try replacing the use of the deprecated member with the replacement -
          lib\features\jarvis\ui\home_screen.dart:444:54 - deprecated_member_use
   info - 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss.
          Try replacing the use of the deprecated member with the replacement -
          lib\features\jarvis\ui\home_screen.dart:484:58 - deprecated_member_use
   info - 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss.
          Try replacing the use of the deprecated member with the replacement -
          lib\features\jarvis\widgets\background_grid.dart:19:35 - deprecated_member_use
warning - The declaration '_glow' isn't referenced. Try removing the declaration of '_glow' -
       lib\features\jarvis\widgets\jarvis_circle.dart:114:10 - unused_element
   info - Don't invoke 'print' in production code. Try using a logging framework - lib\main.dart:43:7 -
          avoid_print
   info - Don't invoke 'print' in production code. Try using a logging framework - lib\main.dart:61:9 -
          avoid_print
   info - Don't invoke 'print' in production code. Try using a logging framework - lib\main.dart:67:9 -
          avoid_print
  error - Target of URI doesn't exist: 'package:flutter_tts/flutter_tts.dart'. Try creating the file
         referenced by the URI, or try using a URI for a file that does exist -
         lib\services\audio_service.dart:2:8 - uri_does_not_exist
  error - Target of URI doesn't exist: 'package:just_audio/just_audio.dart'. Try creating the file
         referenced by the URI, or try using a URI for a file that does exist -
         lib\services\audio_service.dart:3:8 - uri_does_not_exist
  error - Undefined class 'FlutterTts'. Try changing the name to the name of an existing class, or
         creating a class with the name 'FlutterTts' - lib\services\audio_service.dart:6:16 -
         undefined_class
  error - The method 'FlutterTts' isn't defined for the type 'AudioService'. Try correcting the name to
         the name of an existing method, or defining a method named 'FlutterTts' -
         lib\services\audio_service.dart:6:34 - undefined_method
  error - Undefined class 'AudioPlayer'. Try changing the name to the name of an existing class, or
         creating a class with the name 'AudioPlayer' - lib\services\audio_service.dart:7:16 -
         undefined_class
  error - The method 'AudioPlayer' isn't defined for the type 'AudioService'. Try correcting the name to
         the name of an existing method, or defining a method named 'AudioPlayer' -
         lib\services\audio_service.dart:7:38 - undefined_method
  error - Target of URI doesn't exist: 'package:wakelock_plus/wakelock_plus.dart'. Try creating the file
         referenced by the URI, or try using a URI for a file that does exist -
         lib\services\device_wake_service.dart:1:8 - uri_does_not_exist
  error - Target of URI doesn't exist: 'package:screen_brightness/screen_brightness.dart'. Try creating
         the file referenced by the URI, or try using a URI for a file that does exist -
         lib\services\device_wake_service.dart:2:8 - uri_does_not_exist
  error - Undefined name 'WakelockPlus'. Try correcting the name to one that is defined, or defining the
         name - lib\services\device_wake_service.dart:7:13 - undefined_identifier
  error - The method 'ScreenBrightness' isn't defined for the type 'DeviceWakeService'. Try correcting
         the name to the name of an existing method, or defining a method named 'ScreenBrightness' -
         lib\services\device_wake_service.dart:8:13 - undefined_method
   info - Don't invoke 'print' in production code. Try using a logging framework -
          lib\services\jarvis_background_bridge.dart:15:9 - avoid_print
   info - Don't invoke 'print' in production code. Try using a logging framework -
          lib\services\jarvis_background_bridge.dart:19:5 - avoid_print
   info - Don't invoke 'print' in production code. Try using a logging framework -
          lib\services\jarvis_background_bridge.dart:32:7 - avoid_print
  error - Target of URI doesn't exist: 'package:web_socket_channel/web_socket_channel.dart'. Try creating
         the file referenced by the URI, or try using a URI for a file that does exist -
         lib\services\jarvis_external_trigger_service.dart:5:8 - uri_does_not_exist
  error - Undefined class 'WebSocketChannel'. Try changing the name to the name of an existing class, or
         creating a class with the name 'WebSocketChannel' -
         lib\services\jarvis_external_trigger_service.dart:14:3 - undefined_class
  error - Undefined name 'WebSocketChannel'. Try correcting the name to one that is defined, or defining
         the name - lib\services\jarvis_external_trigger_service.dart:36:18 - undefined_identifier
  error - Target of URI doesn't exist: 'package:flutter_tts/flutter_tts.dart'. Try creating the file
         referenced by the URI, or try using a URI for a file that does exist -
         lib\services\thinking_feedback_service.dart:5:8 - uri_does_not_exist
  error - Target of URI doesn't exist: 'package:just_audio/just_audio.dart'. Try creating the file
         referenced by the URI, or try using a URI for a file that does exist -
         lib\services\thinking_feedback_service.dart:6:8 - uri_does_not_exist
  error - Target of URI doesn't exist: '../../../core/speech_output_mode.dart'. Try creating the file
         referenced by the URI, or try using a URI for a file that does exist -
         lib\services\thinking_feedback_service.dart:8:8 - uri_does_not_exist
  error - Undefined class 'FlutterTts'. Try changing the name to the name of an existing class, or
         creating a class with the name 'FlutterTts' - lib\services\thinking_feedback_service.dart:25:9 -
         undefined_class
  error - The method 'FlutterTts' isn't defined for the type 'ThinkingFeedbackService'. Try correcting
         the name to the name of an existing method, or defining a method named 'FlutterTts' -
         lib\services\thinking_feedback_service.dart:25:27 - undefined_method
  error - Undefined class 'AudioPlayer'. Try changing the name to the name of an existing class, or
         creating a class with the name 'AudioPlayer' - lib\services\thinking_feedback_service.dart:26:9
         - undefined_class
  error - The method 'AudioPlayer' isn't defined for the type 'ThinkingFeedbackService'. Try correcting
         the name to the name of an existing method, or defining a method named 'AudioPlayer' -
         lib\services\thinking_feedback_service.dart:26:31 - undefined_method
  error - Undefined class 'SpeechOutputMode'. Try changing the name to the name of an existing class, or
         creating a class with the name 'SpeechOutputMode' -
         lib\services\thinking_feedback_service.dart:52:14 - undefined_class
  error - Undefined class 'SpeechOutputMode'. Try changing the name to the name of an existing class, or
         creating a class with the name 'SpeechOutputMode' -
         lib\services\thinking_feedback_service.dart:81:5 - undefined_class
  error - Undefined name 'SpeechOutputMode'. Try correcting the name to one that is defined, or defining
         the name - lib\services\thinking_feedback_service.dart:88:12 - undefined_identifier
  error - Undefined name 'SpeechOutputMode'. Try correcting the name to one that is defined, or defining
         the name - lib\services\thinking_feedback_service.dart:91:12 - undefined_identifier
  error - Target of URI doesn't exist: 'package:speech_to_text/speech_to_text.dart'. Try creating the
         file referenced by the URI, or try using a URI for a file that does exist -
         lib\services\voice_service.dart:2:8 - uri_does_not_exist
  error - Undefined class 'SpeechToText'. Try changing the name to the name of an existing class, or
         creating a class with the name 'SpeechToText' - lib\services\voice_service.dart:5:9 -
         undefined_class
  error - The method 'SpeechToText' isn't defined for the type 'VoiceService'. Try correcting the name to
         the name of an existing method, or defining a method named 'SpeechToText' -
         lib\services\voice_service.dart:5:32 - undefined_method
  error - Undefined name 'ListenMode'. Try correcting the name to one that is defined, or defining the
         name - lib\services\voice_service.dart:99:21 - undefined_identifier
  error - The name 'MyApp' isn't a class. Try correcting the name to match an existing class -
         test\widget_test.dart:16:35 - creation_with_non_type
