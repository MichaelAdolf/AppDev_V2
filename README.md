void _processCurrentResponse({
  required int interactionId,
  required HaResponse response,
}) {
  if (!_isInteractionCurrent(interactionId)) {
    return;
  }

  lastResponse = response;

  // Hier deinen bestehenden History-Eintrag beibehalten.
  //
  // Beispiel:
  // _conversationHistory.add(
  //   ConversationEntry.assistant(response.message),
  // );

  if (response.success) {
    _setState(JarvisState.speaking);
    return;
  }

  _finishInteraction(interactionId);
  _setState(JarvisState.error);
}
``
