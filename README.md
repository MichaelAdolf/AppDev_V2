void interrupt({
  bool clearLastResponse = true,
}) {
  _invalidateActiveInteraction();

  if (clearLastResponse) {
    lastResponse = null;
  }

  partialText = '';
  finalText = '';

  _setState(JarvisState.idle);

  debugPrint(
    'JarvisController: '
    'Aktuelle Verarbeitung wurde unterbrochen',
  );
}
