import '../core/jarvis_intent.dart';
import '../core/ha_response.dart';
import 'home_assistant_service.dart';
import 'audio_service.dart';

class ConversationService {
  final HomeAssistantService _ha;

  ConversationService({required HomeAssistantService ha})
      : _ha = ha;

  Future<HaResponse> execute(JarvisIntent intent) async {
    return await _ha.sendIntent(intent);
  }

  Future<void> interrupt() async {
    await AudioService.stop();
  }
}