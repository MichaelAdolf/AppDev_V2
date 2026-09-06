import 'dart:async';
import 'dart:math';

import 'package:flutter/foundation.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:just_audio/just_audio.dart';

import '../../../core/speech_output_mode.dart';

class ThinkingFeedbackService {
  ThinkingFeedbackService({
    this.localText = 'Ich prüfe das, Sir.',
    List<String>? remoteAudioUrls,
  }) : remoteAudioUrls = remoteAudioUrls ?? _defaultRemoteAudioUrls;

  static const List<String> _defaultRemoteAudioUrls = <String>[
    'http://192.168.178.47:8123/local/jarvis/phrases/processing_01.mp3',
    'http://192.168.178.47:8123/local/jarvis/phrases/processing_02.mp3',
    'http://192.168.178.47:8123/local/jarvis/phrases/processing_03.mp3',
    'http://192.168.178.47:8123/local/jarvis/phrases/processing_04.mp3',
  ];

  final String localText;
  final List<String> remoteAudioUrls;
  final FlutterTts _tts = FlutterTts();
  final AudioPlayer _player = AudioPlayer();
  final Random _random = Random();

  Future<void>? _activePlayback;
  int? _activeInteractionId;
  bool _initialized = false;
  bool _disposed = false;
  int _generation = 0;

  bool get isPlaying => _activePlayback != null;
  int? get activeInteractionId => _activeInteractionId;

  Future<void> initialize() async {
    if (_initialized || _disposed) return;
    await _tts.setLanguage('de-DE');
    await _tts.setSpeechRate(0.45);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);
    await _tts.awaitSpeakCompletion(true);
    _initialized = true;
  }

  /// Spielt die Thinking-Phrase genau einmal und vollständig ab.
  /// Mehrere Aufrufer derselben Interaktion warten auf dasselbe Future.
  Future<void> play({
    required int interactionId,
    required SpeechOutputMode mode,
  }) {
    if (_disposed) return Future<void>.value();

    final current = _activePlayback;
    if (current != null && _activeInteractionId == interactionId) {
      return current;
    }

    if (current != null) {
      return current.then(
        (_) => play(interactionId: interactionId, mode: mode),
      );
    }

    _activeInteractionId = interactionId;
    final generation = _generation;
    final playback = _playInternal(mode, generation);
    _activePlayback = playback;

    return playback.whenComplete(() {
      if (_activePlayback == playback) {
        _activePlayback = null;
        _activeInteractionId = null;
      }
    });
  }

  Future<void> _playInternal(
    SpeechOutputMode mode,
    int generation,
  ) async {
    await initialize();
    if (_disposed || generation != _generation) return;

    switch (mode) {
      case SpeechOutputMode.appTts:
        await _speakLocal(generation);
        break;
      case SpeechOutputMode.nodeRedAudio:
        try {
          await _playRemote(generation);
        } catch (error, stackTrace) {
          debugPrint(
            '[THINKING] Remote-Phrase fehlgeschlagen, Fallback auf App-TTS: '
            '$error',
          );
          debugPrintStack(stackTrace: stackTrace);
          if (!_disposed && generation == _generation) {
            await _speakLocal(generation);
          }
        }
        break;
    }
  }

  Future<void> _speakLocal(int generation) async {
    if (_disposed || generation != _generation) return;
    final text = localText.trim();
    if (text.isEmpty) return;
    debugPrint('[THINKING] App-TTS startet: $text');
    await _tts.speak(text);
    debugPrint('[THINKING] App-TTS beendet');
  }

  Future<void> _playRemote(int generation) async {
    if (_disposed || generation != _generation) return;
    if (remoteAudioUrls.isEmpty) {
      throw StateError('Keine Remote-Thinking-Phrasen konfiguriert.');
    }

    final url = remoteAudioUrls[_random.nextInt(remoteAudioUrls.length)];
    debugPrint('[THINKING] Remote-Phrase startet: $url');
    await _player.setUrl(url);
    if (_disposed || generation != _generation) return;
    await _player.play();
    debugPrint('[THINKING] Remote-Phrase beendet');
  }

  /// Technischer Notabbruch. Nicht für reguläre State-Wechsel verwenden.
  Future<void> forceStop() async {
    _generation += 1;
    try {
      await _tts.stop();
    } catch (error) {
      debugPrint('[THINKING] TTS konnte nicht gestoppt werden: $error');
    }
    try {
      await _player.stop();
    } catch (error) {
      debugPrint('[THINKING] Player konnte nicht gestoppt werden: $error');
    }
    _activePlayback = null;
    _activeInteractionId = null;
  }

  Future<void> dispose() async {
    if (_disposed) return;
    _disposed = true;
    await forceStop();
    await _player.dispose();
  }
}
