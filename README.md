void _handleRequestError({
  required int interactionId,
  required Object error,
}) {
  if (!_isInteractionCurrent(interactionId)) {
    return;
  }

  _finishInteraction(interactionId);

  // Hier deinen bisherigen Catch-Fehlerpfad verwenden.
  //
  // Beispiel:
  // lastResponse = HaResponse(
  //   success: false,
  //   message: 'Die Anfrage konnte nicht verarbeitet werden.',
  // );

  _setState(JarvisState.error);
}
