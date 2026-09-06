void _handleRequestTimeout(int interactionId) {
  if (!_isInteractionCurrent(interactionId)) {
    return;
  }

  _finishInteraction(interactionId);

  lastUserText = lastUserText;

  // Verwende hier deinen bereits vorhandenen Mechanismus
  // für eine lokale Fehlerantwort.
  //
  // Falls HaResponse einen passenden Konstruktor besitzt:
  //
  // lastResponse = HaResponse(
  //   success: false,
  //   message: 'Die Verarbeitung hat zu lange gedauert.',
  // );
  //
  // Passe den Konstruktor an dein tatsächliches Modell an.

  _setState(JarvisState.error);
}
