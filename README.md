void completeSpeaking() {
  final interactionId = _activeInteractionId;

  if (interactionId != null) {
    _finishInteraction(interactionId);
  }

  if (_isDisposed) {
    return;
  }

  _setState(JarvisState.idle);
}
