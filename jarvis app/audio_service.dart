import 'package:flutter/foundation.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:just_audio/just_audio.dart';

class AudioService {
  static final FlutterTts _tts = FlutterTts();
  static final AudioPlayer _player = AudioPlayer();

  static bool _initialized = false;
  static bool _isSpeaking = false;

  static bool get isSpeaking => _isSpeaking;

  static Future<void> init() async {
    if (_initialized) {
      return;
    }

    await _tts.setLanguage('de-DE');
    await _tts.setSpeechRate(0.45);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);

    // Dadurch wartet _tts.speak(), bis die Ausgabe beendet ist.
    await _tts.awaitSpeakCompletion(true);

    _initialized = true;

    debugPrint('[AUDIO] AudioService initialisiert');
  }

  static Future<void> speakText(String text) async {
    final normalizedText = text.trim();

    if (normalizedText.isEmpty) {
      return;
    }

    await init();
    await stop();

    _isSpeaking = true;

    try {
      debugPrint('[AUDIO] App-TTS startet: $normalizedText');

      await _tts.speak(normalizedText);

      debugPrint('[AUDIO] App-TTS beendet');
    } catch (error) {
      debugPrint('[AUDIO] App-TTS Fehler: $error');
      rethrow;
    } finally {
      _isSpeaking = false;
    }
  }

  static Future<void> playRemoteUrl(String url) async {
    final normalizedUrl = url.trim();

    if (normalizedUrl.isEmpty) {
      throw ArgumentError('Die Audio-URL darf nicht leer sein.');
    }

    await init();
    await stop();

    _isSpeaking = true;

    try {
      debugPrint('[AUDIO] Node-RED-Audio startet: $normalizedUrl');

      await _player.setUrl(normalizedUrl);
      await _player.play();

      debugPrint('[AUDIO] Node-RED-Audio beendet');
    } catch (error) {
      debugPrint('[AUDIO] Node-RED-Audio Fehler: $error');
      rethrow;
    } finally {
      _isSpeaking = false;
    }
  }

  static Future<void> stop() async {
    try {
      await _tts.stop();
    } catch (error) {
      debugPrint('[AUDIO] App-TTS konnte nicht gestoppt werden: $error');
    }

    try {
      await _player.stop();
    } catch (error) {
      debugPrint('[AUDIO] Remote-Audio konnte nicht gestoppt werden: $error');
    }

    _isSpeaking = false;
  }

  static Future<void> dispose() async {
    await stop();
    await _player.dispose();
  }
}