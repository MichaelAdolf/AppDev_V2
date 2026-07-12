import 'package:flutter/services.dart';

class JarvisBackgroundBridge {

  static const MethodChannel _channel =
      MethodChannel(
    'jarvis/background',
  );

  static void initialize({
    required Function(String event)
        onEvent,
  }) {

    _channel.setMethodCallHandler(
      (call) async {

        if (call.method ==
            'backgroundEvent') {

          final event =
              call.arguments as String;

          onEvent(event);
        }
      },
    );
  }
}
