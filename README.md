import 'package:flutter/foundation.dart';
import 'package:speech_to_text/speech_to_text.dart';

class VoiceService {
  final SpeechToText _speech = SpeechToText();

  bool _initialized = false;
  bool _isStarting = false;

  bool get isListening => _speech.isListening;

  Future<bool> initialize() async {
    if (_initialized) {
      return true;
    }

    try {
      final available = await _speech.initialize(
        debugLogging: true,
        onStatus: (status) {
          debugPrint(
            '[VOICE] Status: $status',
          );
        },
        onError: (error) {
          debugPrint(
            '[VOICE] Fehler: '
            '${error.errorMsg}, '
            'permanent=${error.permanent}',
          );
        },
      );

      _initialized = available;

      debugPrint(
        '[VOICE] Initialisierung: '
        'available=$available',
      );

      return available;
    } catch (error) {
      debugPrint(
        '[VOICE] Initialisierung fehlgeschlagen: $error',
      );

      _initialized = false;
      return false;
    }
  }

  Future<bool> startListening({
    required void Function(String text) onFinalResult,
    void Function(String text)? onPartialResult,
  }) async {
    if (_isStarting) {
      debugPrint(
        '[VOICE] Start bereits in Bearbeitung',
      );

      return false;
    }

    _isStarting = true;

    try {
      debugPrint(
        '[VOICE] startListening angefordert',
      );

      final available = await initialize();

      if (!available) {
        debugPrint(
          '[VOICE] SpeechToText nicht verfügbar',
        );

        return false;
      }

      if (_speech.isListening) {
        debugPrint(
          '[VOICE] Bestehendes Listening wird gestoppt',
        );

        await _speech.stop();

        await Future<void>.delayed(
          const Duration(milliseconds: 250),
        );
      }

      await _speech.listen(
        localeId: 'de_DE',
        partialResults: true,
        cancelOnError: true,
        listenMode: ListenMode.dictation,
        listenFor: const Duration(seconds: 10),
        pauseFor: const Duration(seconds: 3),
        onSoundLevelChange: (level) {
          debugPrint(
            '[VOICE] Sound-Level: '
            '${level.toStringAsFixed(2)}',
          );
        },
        onResult: (result) {
          final text =
              result.recognizedWords.trim();

          debugPrint(
            '[VOICE] Ergebnis: "$text" '
            '| final=${result.finalResult}',
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

      final listening = _speech.isListening;

      debugPrint(
        '[VOICE] listen() abgeschlossen, '
        'isListening=$listening',
      );

      return listening;
    } catch (error, stackTrace) {
      debugPrint(
        '[VOICE] Listening konnte nicht '
        'gestartet werden: $error',
      );

      debugPrint(
        '[VOICE] StackTrace: $stackTrace',
      );

      return false;
    } finally {
      _isStarting = false;
    }
  }

  Future<void> stopListening() async {
    try {
      if (_speech.isListening) {
        debugPrint(
          '[VOICE] Listening wird gestoppt',
        );

        await _speech.stop();
      }

      debugPrint(
        '[VOICE] Listening gestoppt',
      );
    } catch (error) {
      debugPrint(
        '[VOICE] Stop fehlgeschlagen: $error',
      );
    }
  }

  Future<void> cancelListening() async {
    try {
      await _speech.cancel();

      debugPrint(
        '[VOICE] Listening abgebrochen',
      );
    } catch (error) {
      debugPrint(
        '[VOICE] Cancel fehlgeschlagen: $error',
      );
    }
  }
}
