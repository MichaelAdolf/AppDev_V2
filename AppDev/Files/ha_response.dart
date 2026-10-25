class HaResponse {
  final bool success;
  final String intent;
  final String entity;
  final String state;
  final String message;
  final String? audioUrl;

  const HaResponse({
    required this.success,
    required this.intent,
    required this.entity,
    required this.state,
    required this.message,
    this.audioUrl,
  });

  factory HaResponse.fromJson(Map<String, dynamic> json) {
    return HaResponse(
      success: json['success'] ?? false,
      intent: json['intent'] ?? 'unknown',
      entity: json['entity'] ?? '',
      state: json['state'] ?? '',
      message: json['message'] ?? '',
      audioUrl: json['audioUrl'],
    );
  }
}