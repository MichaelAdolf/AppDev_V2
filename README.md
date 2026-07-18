import 'package:flutter/services.dart';

class JarvisWakewordControl {

  static const MethodChannel _channel =
      MethodChannel(
    'jarvis/background',
  );

  static Future<void> stop() async {

    await _channel.invokeMethod(
      'stopWakeword',
    );
  }

  static Future<void> start() async {

    await _channel.invokeMethod(
      'startWakeword',
    );
  }
}
