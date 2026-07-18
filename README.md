import 'package:flutter/foundation.dart';

class JarvisWakewordService {

  Future<void> initialize({
    required VoidCallback onWakeword,
  }) async {

    debugPrint(
      '[JARVIS WAKEWORD] Service initialisiert',
    );

    // Porcupine wird
    // im nächsten Schritt angeschlossen.
  }

  Future<void> dispose() async {
  }
}
