JarvisBackgroundBridge.initialize(
  onEvent: (event) async {
    print(
      '[JARVIS BACKGROUND RAW] $event',
    );

    try {
      final decoded =
          jsonDecode(event) as Map<String, dynamic>;

      final response =
          HaResponse.fromJson(decoded);

      await DeviceWakeService.wakeDevice();

      await controller.handleExternalResponse(
        response,
        source: 'android-service',
      );
    } catch (e) {
      print(
        '[JARVIS BACKGROUND ERROR] $e',
      );
    }
  },
  onWakeword: () async {
    print(
      '[JARVIS WAKEWORD] Flutter hat Wakeword erkannt',
    );

    await DeviceWakeService.wakeDevice();

    // Nächster Schritt:
    // Hier koppeln wir später direkt controller.startListening()
    // oder deine bestehende Mikrofon-Startlogik an.
  },
);
