import 'package:flutter/services.dart';

class JarvisBackgroundBridge {
  static const MethodChannel _channel =
      MethodChannel(
    'jarvis/background',
  );

  static void initialize({
    required Function(String event) onEvent,
    Function()? onWakeword,
  }) {
    _channel.setMethodCallHandler(
      (call) async {
        print(
          '[JARVIS BRIDGE] ${call.method}',
        );

        print(
          '[JARVIS BRIDGE] ${call.arguments}',
        );

        if (call.method == 'backgroundEvent') {
          final event =
              call.arguments as String;

          onEvent(event);
          return;
        }

        if (call.method == 'wakewordDetected') {
          print(
            '[JARVIS BRIDGE] Wakeword Event empfangen',
          );

          onWakeword?.call();
          return;
        }
      },
    );
  }
}
