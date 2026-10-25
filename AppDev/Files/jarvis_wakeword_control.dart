import 'package:flutter/services.dart';

class JarvisWakewordControl {
  static const MethodChannel _channel = MethodChannel('jarvis/background');

  static Future<bool> stop() async {
    final released = await _channel.invokeMethod<bool>('stopWakeword');
    return released ?? true;
  }

  static Future<void> start() async {
    await _channel.invokeMethod<void>('startWakeword');
  }
}
