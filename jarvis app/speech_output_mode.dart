enum SpeechOutputMode {
  appTts,
  nodeRedAudio,
}

extension SpeechOutputModeLabel on SpeechOutputMode {
  String get displayName {
    switch (this) {
      case SpeechOutputMode.appTts:
        return 'APP TTS';

      case SpeechOutputMode.nodeRedAudio:
        return 'NODE-RED AUDIO';
    }
  }
}