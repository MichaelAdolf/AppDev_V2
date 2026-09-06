void _handleThinkingState(int? interactionId) {
  if (interactionId == null) {
    return;
  }

  _thinkingFeedbackService.schedule(
    interactionId: interactionId,
    delay: const Duration(milliseconds: 350),
    onPlay: () async {
      if (_controller.state != JarvisState.thinking) {
        return;
      }

      if (_controller.activeInteractionId != interactionId) {
        return;
      }

      debugPrint(
        'HomeScreen: '
        'Thinking-Feedback wäre jetzt für '
        'Interaktion $interactionId gestartet',
      );

      // Sprint 2:
      // Hier wird später "Ich prüfe das" abgespielt.
    },
  );
}
