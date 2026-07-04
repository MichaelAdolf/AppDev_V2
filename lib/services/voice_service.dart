import 'package:speech_to_text/speech_to_text.dart';

class VoiceService {
  final SpeechToText _speech = SpeechToText();

  Future<bool> initialize() async {
    return await _speech.initialize();
  }

  Future<void> startListening(
    Function(String text) onResult, 
  ) async {
    await _speech.listen(
      localeId: 'de_DE',
      onResult: (result) {
        if (result.finalResult) {
          onResult(result.recognizedWords);
        }
      },
    );
  }
  
  Future<void> stopListening() async {
    await _speech.stop();
  }
}