import 'package:flutter/foundation.dart';
import 'package:porcupine_flutter/porcupine_manager.dart';

class JarvisWakewordService {

  PorcupineManager? _manager;

  Future<void> initialize({
    required VoidCallback onWakeword,
  }) async {

    _manager =
        await PorcupineManager.fromKeywordPaths(

      'DEIN_PORCUPINE_ACCESS_KEY',

      keywordPaths: [
        // später eigene Jarvis-Datei
      ],

      onKeywordDetected: (index) {

        debugPrint(
          '[JARVIS WAKEWORD] erkannt',
        );

        onWakeword();
      },
    );

    await _manager?.start();
  }

  Future<void> dispose() async {
    await _manager?.stop();
    await _manager?.delete();
  }
}