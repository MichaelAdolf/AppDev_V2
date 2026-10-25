import 'package:flutter/foundation.dart';
import 'package:speech_to_text/speech_to_text.dart';

class VoiceService {
  final SpeechToText _speech = SpeechToText();
  bool _initialized = false;
  bool _isStarting = false;
  String _lastPartial = '';
  DateTime _lastPartialAt = DateTime.fromMillisecondsSinceEpoch(0);

  bool get isListening => _speech.isListening;

  Future<bool> initialize() async {
    if (_initialized) return true;
    try {
      final available = await _speech.initialize(
        debugLogging: false,
        onStatus: (status) {
          if (status != 'listening') debugPrint('[VOICE] Status: $status');
        },
        onError: (error) => debugPrint(
          '[VOICE] Fehler: ${error.errorMsg}, permanent=${error.permanent}',
        ),
      );
      _initialized = available;
      debugPrint('[VOICE] Initialisierung: available=$available');
      return available;
    } catch (error) {
      _initialized = false;
      debugPrint('[VOICE] Initialisierung fehlgeschlagen: $error');
      return false;
    }
  }

  Future<bool> startListening({
    required void Function(String text) onFinalResult,
    void Function(String text)? onPartialResult,
  }) async {
    if (_isStarting) return false;
    _isStarting = true;
    try {
      if (!await initialize()) return false;
      if (_speech.isListening) await _speech.cancel();
      _lastPartial = '';
      _lastPartialAt = DateTime.fromMillisecondsSinceEpoch(0);
      await _speech.listen(
        localeId: 'de_DE',
        partialResults: true,
        cancelOnError: true,
        listenMode: ListenMode.dictation,
        listenFor: const Duration(seconds: 10),
        pauseFor: const Duration(seconds: 3),
        onResult: (result) {
          final text = result.recognizedWords.trim();
          if (text.isEmpty) return;
          if (result.finalResult) {
            onFinalResult(text);
            return;
          }
          final now = DateTime.now();
          if (text == _lastPartial ||
              now.difference(_lastPartialAt) < const Duration(milliseconds: 80)) {
            return;
          }
          _lastPartial = text;
          _lastPartialAt = now;
          onPartialResult?.call(text);
        },
      );
      return _speech.isListening;
    } catch (error, stackTrace) {
      debugPrint('[VOICE] Listening konnte nicht gestartet werden: $error');
      debugPrintStack(stackTrace: stackTrace);
      return false;
    } finally {
      _isStarting = false;
    }
  }

  Future<void> stopListening() async {
    try {
      if (_speech.isListening) await _speech.stop();
    } catch (error) {
      debugPrint('[VOICE] Stop fehlgeschlagen: $error');
    }
  }

  Future<void> cancelListening() async {
    try {
      if (_speech.isListening) await _speech.cancel();
    } catch (error) {
      debugPrint('[VOICE] Cancel fehlgeschlagen: $error');
    }
  }
}
