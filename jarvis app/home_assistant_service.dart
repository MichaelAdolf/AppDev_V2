import '../core/ha_response.dart';
import '../core/jarvis_intent.dart';

abstract class HomeAssistantService {
  Future<bool> ping();

  Future<HaResponse> sendIntent(JarvisIntent intent);
}