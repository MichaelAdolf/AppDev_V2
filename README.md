import '../core/ha_response.dart';
import '../core/jarvis_intent.dart';
import 'home_assistant_service.dart';

class ConversationService {
  final HomeAssistantService _ha;

  ConversationService({
    required HomeAssistantService ha,
  }) : _ha = ha;

  Future<HaResponse> execute(JarvisIntent intent) async {
    return _ha.sendIntent(intent);
  }
}
