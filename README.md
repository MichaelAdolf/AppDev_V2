int _beginInteraction() {
  _interactionSequence += 1;
  _activeInteractionId = _interactionSequence;

  debugPrint(
    'JarvisController: '
    'Interaktion $_activeInteractionId gestartet',
  );

  return _interactionSequence;
}

bool _isInteractionCurrent(int interactionId) {
  return !_isDisposed &&
      _activeInteractionId == interactionId;
}

void _finishInteraction(int interactionId) {
  if (_activeInteractionId != interactionId) {
    return;
  }

  debugPrint(
    'JarvisController: '
    'Interaktion $interactionId abgeschlossen',
  );

  _activeInteractionId = null;
}

void _invalidateActiveInteraction() {
  final previousInteractionId = _activeInteractionId;

  _interactionSequence += 1;
  _activeInteractionId = null;

  if (previousInteractionId != null) {
    debugPrint(
      'JarvisController: '
      'Interaktion $previousInteractionId ungültig gemacht',
    );
  }
}
