void handleEvent(JarvisEvent event, {String? input}) {
    switch (event) {
      case JarvisEvent.voiceStarted:
        if (!isBusy) {
          _setState(JarvisState.listening);
        }
        // später: Mic aktiv, UI Feedback
        break;

      case JarvisEvent.voiceStopped:
        if (state == JarvisState.listening) {
          _setState(JarvisState.thinking);
        }
        // später: Speech-to-text finalize
        break;

      case JarvisEvent.intentReceived:
        // optional Logging / Debug
        break;

      case JarvisEvent.commandReceived:
        // später: HA Input verarbeitet
        break;

      case JarvisEvent.commandExecuted:
        _setState(JarvisState.speaking);
        // später: Erfolg / Feedback
        break;

      case JarvisEvent.error:
        _responseText = input ?? 'Ein unbekannter Fehler ist aufgetreten';
        _setState(JarvisState.error);
        // später: UI Error State
        break;
    }
  }
