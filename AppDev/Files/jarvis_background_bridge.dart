import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

class JarvisBackgroundBridge {
  static const MethodChannel _channel = MethodChannel('jarvis/background');
  static void initialize({required Function(String event) onEvent,Function()? onWakeword}) {
    _channel.setMethodCallHandler((call) async {
      debugPrint('[JARVIS BRIDGE] ${call.method}');
      if(call.method=='backgroundEvent'){
        final args=call.arguments;
        if(args is String) onEvent(args);
        return;
      }
      if(call.method=='wakewordDetected'){
        onWakeword?.call();
      }
    });
  }
}
