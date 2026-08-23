import 'package:flutter/foundation.dart';

import '../core/ha_response.dart';
import '../core/speech_output_mode.dart';
import 'audio_service.dart';

class SpeechOutputService {
  SpeechOutputMode _mode;

  int _requestId = 0;

  SpeechOutputService({
    SpeechOutputMode initialMode = SpeechOutputMode.appTts,
  }) : _mode = initialMode;

  SpeechOutputMode get mode => _mode;

  void setMode(SpeechOutputMode mode) {
    if (_mode == mode) {
      return;
    }

    _mode = mode;

    debugPrint(
      '[SPEECH OUTPUT] Modus geändert: ${_mode.name}',
    );
  }

  Future<bool> output(HaResponse response) async {
    final currentRequestId = ++_requestId;

    await AudioService.stop();

    if (!_isCurrentRequest(currentRequestId)) {
      return false;
    }

    try {
      switch (_mode) {
        case SpeechOutputMode.appTts:
          await _speakWithAppTts(
            response,
            currentRequestId,
          );
          break;

        case SpeechOutputMode.nodeRedAudio:
          await _playNodeRedAudio(
            response,
            currentRequestId,
          );
          break;
      }

      return _isCurrentRequest(currentRequestId);
    } catch (error) {
      debugPrint(
        '[SPEECH OUTPUT] Ausgabe fehlgeschlagen: $error',
      );

      return false;
    }
  }

  Future<void> _speakWithAppTts(
    HaResponse response,
    int requestId,
  ) async {
    if (!_isCurrentRequest(requestId)) {
      return;
    }

    final message = response.message.trim();

    if (message.isEmpty) {
      debugPrint(
        '[SPEECH OUTPUT] Keine Textnachricht vorhanden',
      );
      return;
    }

    debugPrint(
      '[SPEECH OUTPUT] Ausgabe über App-TTS',
    );

    await AudioService.speakText(message);
  }

  Future<void> _playNodeRedAudio(
    HaResponse response,
    int requestId,
  ) async {
    if (!_isCurrentRequest(requestId)) {
      return;
    }

    final audioUrl = response.audioUrl?.trim();

    if (audioUrl == null || audioUrl.isEmpty) {
      debugPrint(
        '[SPEECH OUTPUT] Keine audioUrl vorhanden. '
        'Fallback auf App-TTS.',
      );

      await _speakWithAppTts(
        response,
        requestId,
      );

      return;
    }

    debugPrint(
      '[SPEECH OUTPUT] Ausgabe über Node-RED-Audio',
    );

    try {
      await AudioService.playRemoteUrl(audioUrl);
    } catch (error) {
      if (!_isCurrentRequest(requestId)) {
        return;
      }

      debugPrint(
        '[SPEECH OUTPUT] Node-RED-Audio nicht abspielbar. '
        'Fallback auf App-TTS: $error',
      );

      await _speakWithAppTts(
        response,
        requestId,
      );
    }
  }

  Future<void> stop() async {
    _requestId++;
    await AudioService.stop();

    debugPrint('[SPEECH OUTPUT] Ausgabe gestoppt');
  }

  bool _isCurrentRequest(int requestId) {
    return requestId == _requestId;
  }
}
