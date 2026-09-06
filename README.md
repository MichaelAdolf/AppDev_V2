Future<void> _handleIntent(/* dein bestehender Intent-Typ */ intent) async {
  final interactionId = _beginInteraction();

  _setState(JarvisState.thinking);

  try {
    final response = await _conversation
        .execute(intent)
        .timeout(_defaultRequestTimeout);

    if (!_isInteractionCurrent(interactionId)) {
      debugPrint(
        'JarvisController: '
        'Response für veraltete Interaktion '
        '$interactionId wird verworfen',
      );
      return;
    }

    // Ab hier deinen bereits vorhandenen Erfolgsablauf beibehalten.
    //
    // Beispiel:
    //
    // lastResponse = response;
    // history.add(...);
    //
    // if (response.success) {
    //   _setState(JarvisState.speaking);
    // } else {
    //   _setState(JarvisState.error);
    // }

    _processCurrentResponse(
      interactionId: interactionId,
      response: response,
    );
  } on TimeoutException {
    if (!_isInteractionCurrent(interactionId)) {
      return;
    }

    debugPrint(
      'JarvisController: '
      'Timeout für Interaktion $interactionId',
    );

    _handleRequestTimeout(interactionId);
  } catch (error, stackTrace) {
    if (!_isInteractionCurrent(interactionId)) {
      debugPrint(
        'JarvisController: '
        'Fehler einer veralteten Interaktion '
        '$interactionId wird ignoriert: $error',
      );
      return;
    }

    debugPrint(
      'JarvisController: '
      'Fehler in Interaktion $interactionId: $error',
    );
    debugPrintStack(stackTrace: stackTrace);

    _handleRequestError(
      interactionId: interactionId,
      error: error,
    );
  }
}
