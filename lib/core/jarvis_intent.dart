enum IntentType {
  lightOn,
  lightOff,
  dailyInfo,
  unknown,
}

class JarvisIntent {
  final IntentType type;
  final String? entity;
  final String rawText;

  JarvisIntent({
    required this.type,
    required this.rawText,
    this.entity,
  });
}