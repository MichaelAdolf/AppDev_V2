import 'package:speech_to_text/speech_to_text.dart';
import 'package:flutter/foundation.dart';

class VoiceService {
  final SpeechToText _speech = SpeechToText();

  Future<bool> initialize() async {
    return await _speech.initialize();
  }

  Future startListening({ 
    required Function(String text) onFinalResult, 
    Function(String text)? onPartialResult, 
  }) async {

    debugPrint( '[VOICE] listen() wird gestartet', );

    final available = await _speech.initialize();

    debugPrint( '[VOICE] verfügbar: $available', );

    if (!available) {

    debugPrint(
      '[VOICE] SpeechToText nicht verfügbar',
    );

    return false;

    }

    await _speech.listen( 
      localeId: 'de_DE', 
      partialResults: true, 
      listenMode: ListenMode.confirmation, 
      listenFor: const Duration( seconds: 10,),
      pauseFor: const Duration( seconds: 3),
      onResult: (result) {

      final text =
          result.recognizedWords.trim();

      debugPrint(
        '[VOICE] Ergebnis: $text | final=${result.finalResult}',
      );

      if (text.isEmpty) {
        return;
      }

      if (result.finalResult) {

        onFinalResult(text);

      } else {

        onPartialResult?.call(text);
      }
    },

    );

    debugPrint( '[VOICE] SpeechToText aktiv', );

    return true; }
  
  Future<void> stopListening() async {
    await _speech.stop();
  }
}