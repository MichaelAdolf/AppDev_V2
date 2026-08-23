void _handleControllerChanged() {
  if (!mounted) {
    return;
  }

  final response = controller.lastResponse;

  final shouldStartSpeech =
      controller.state == JarvisState.speaking &&
      !_isSpeaking &&
      response != null &&
      response.message.trim().isNotEmpty;

  if (shouldStartSpeech) {
    unawaited(
      _playCurrentResponse(response),
    );
  }

  setState(() {});
}
