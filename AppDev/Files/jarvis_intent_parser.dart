import 'jarvis_intent.dart';

class JarvisIntentParser {
  JarvisIntent parse(String input) {
    final text = input.toLowerCase();

    if (text.contains('licht') && text.contains('an')) {
      return JarvisIntent(
        type: IntentType.lightOn,
        entity: _extractRoom(text),
        rawText: input,
      );
    }

    if (text.contains('licht') && text.contains('aus')) {
      return JarvisIntent(
        type: IntentType.lightOff,
        entity: _extractRoom(text),
        rawText: input,
      );
    }

    if (text.contains('tagesinfo')) {
      return JarvisIntent(
        type: IntentType.dailyInfo,
        rawText: input,
      );
    }

    return JarvisIntent(
      type: IntentType.unknown,
      rawText: input,
    );
  }

  String? _extractRoom(String text) {
    if (text.contains('wohnzimmer')) return 'living_room';
    if (text.contains('schlafzimmer')) return 'bedroom';
    return null;
  }
}