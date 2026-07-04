import 'package:speech_to_text/speech_to_text.dart';

class VoiceService {
  final SpeechToText _speech = SpeechToText();

  Future<bool> initialize() async {
    return await _speech.initialize();
  }

  Future<void> startListening({
    required Function(String text) onFinalResult,
    Function(String text)? onPartialResult,
  }) async {
    await _speech.listen(
      localeId: 'de_DE',
      partialResults: true,
      listenMode: ListenMode.confirmation,
      onResult: (result) {
        final text = result.recognizedWords.trim();
        if (text.isEmpty) return;

        if (result.finalResult) {
          onFinalResult(text);
        } else {
          if (onPartialResult != null) {
            onPartialResult(text);
          }
        }
      },
    );
  }
  
  Future<void> stopListening() async {
    await _speech.stop();
  }
}