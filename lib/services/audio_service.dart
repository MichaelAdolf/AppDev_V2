import 'package:flutter_tts/flutter_tts.dart';
import 'package:flutter/foundation.dart';
class AudioService {
  static final FlutterTts _tts = FlutterTts();
  
  static bool _initialized = false;
  static bool _isSpeaking = false;

  static Future<void> init() async {
    if (_initialized) return;

    await _tts.setLanguage('de-DE');
    await _tts.setSpeechRate(0.45);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);

      _initialized = true;
  }

  static Future<void> speak(String text, {VoidCallback? onComplete}) async {
    await init();

    if (text.isEmpty) return;
    
    await _tts.stop();

    _tts.setCompletionHandler(() {

      _isSpeaking = false;

      if (onComplete != null){
        onComplete();
      }
    });
    
    _tts.setErrorHandler((msg) {
      if (onComplete != null) {
        onComplete();
      }
    });
    _isSpeaking = false;
    await _tts.speak(text);
  }

  static Future<void> stop() async {
    await _tts.stop();
  }
  
  static bool get isSpeaking => _isSpeaking;
}