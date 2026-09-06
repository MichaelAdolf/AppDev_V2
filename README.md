import 'package:flutter/foundation.dart';

import '../core/ha_response.dart';
import '../core/speech_output_mode.dart';
import 'audio_service.dart';

class SpeechOutputService {
  SpeechOutputService({
    SpeechOutputMode initialMode = SpeechOutputMode.appTts,
  }) : _mode = initialMode;

  SpeechOutputMode _mode;
  int _requestId = 0;

  SpeechOutputMode get mode => _mode;

  void setMode(SpeechOutputMode mode) {
    if (_mode == mode) return;
    _mode = mode;
    debugPrint('[SPEECH OUTPUT] Modus geändert: ${_mode.name}');
  }

  Future<bool> output(HaResponse response) async {
    final requestId = ++_requestId;
    await AudioService.stop();
    if (!_isCurrentRequest(requestId)) return false;

    try {
      if (_mode == SpeechOutputMode.nodeRedAudio) {
        await _playNodeRedAudio(response, requestId);
      } else {
        await _speakWithAppTts(response, requestId);
      }
      return _isCurrentRequest(requestId);
    } catch (error, stackTrace) {
      if (_isCurrentRequest(requestId)) {
        debugPrint('[SPEECH OUTPUT] Ausgabe fehlgeschlagen: $error');
        debugPrintStack(stackTrace: stackTrace);
      }
      return false;
    }
  }

  Future<void> _speakWithAppTts(HaResponse response, int requestId) async {
    if (!_isCurrentRequest(requestId)) return;
    final message = response.message.trim();
    if (message.isEmpty) return;
    await AudioService.speakText(message);
  }

  Future<void> _playNodeRedAudio(HaResponse response, int requestId) async {
    if (!_isCurrentRequest(requestId)) return;
    final audioUrl = response.audioUrl?.trim();
    if (audioUrl == null || audioUrl.isEmpty) {
      await _speakWithAppTts(response, requestId);
      return;
    }
    try {
      await AudioService.playRemoteUrl(audioUrl);
    } catch (error) {
      if (!_isCurrentRequest(requestId)) return;
      debugPrint('[SPEECH OUTPUT] Remote-Audio fehlgeschlagen: $error');
      await _speakWithAppTts(response, requestId);
    }
  }

  Future<void> stop() async {
    _requestId += 1;
    await AudioService.stop();
  }

  bool _isCurrentRequest(int requestId) => requestId == _requestId;
}
