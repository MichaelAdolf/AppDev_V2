import '../core/ha_response.dart';
import '../core/jarvis_intent.dart';
import 'home_assistant_service.dart';

class MockHomeAssistantService implements HomeAssistantService {
  @override
  Future<bool> ping() async {
    await Future.delayed(const Duration(milliseconds: 300));
    return true;
  }

  @override
  Future<HaResponse> sendIntent(JarvisIntent intent) async {
    await Future.delayed(const Duration(seconds: 1));

    switch (intent.type) {
      case IntentType.lightOn:
        final entityId = _mapRoomToLightEntity(intent.entity);
        
        return HaResponse(
          success: true,
          intent: 'light.turn_on',
          entity: entityId,
          state: 'on',
          message: '$entityId wurde eingeschaltet (MOCK)',
        );
      
      case IntentType.lightOff:
        final entityId = _mapRoomToLightEntity(intent.entity);
        
        return HaResponse(
          success: true,
          intent: 'light.turn_off',
          entity: entityId,
          state: 'off',
          message: '$entityId wurde ausgeschaltet (MOCK)',
        );

      case IntentType.dailyInfo:
        return HaResponse(
          success: true,
          intent: 'daily_info',
          entity: '',
          state: 'info',
          message: 'Hier sind die Tagesinfos (MOCK)',
        );
      
      case IntentType.unknown:        
        return HaResponse(
          success: false,
          intent: 'unknown',
          entity: '',
          state: 'ignored',
          message: 'Mock: Command nicht erkannt: "${intent.rawText}"',
        );
    }
  }

  String _mapRoomToLightEntity(String? room) {
    switch (room) {
      case 'living_room':
        return 'light.living_room';
      case 'bedroom':
        return 'light.bedroom';
      default:
        return 'light.unknown_room';
    }
  }
}