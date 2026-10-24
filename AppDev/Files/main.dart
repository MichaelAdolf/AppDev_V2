import 'package:flutter/material.dart';

import 'features/jarvis/ui/home_screen.dart';
import 'features/jarvis/logic/jarvis_controller.dart';

import 'services/home_assistant_service.dart';
import 'services/real_home_assistant_service.dart';
import 'services/jarvis_background_bridge.dart';
import 'services/device_wake_service.dart';
import 'services/jarvis_wakeword_bus.dart';
//import 'services/mock_home_assistant_service.dart';
import 'core/constants.dart';
import 'core/theme.dart';
import 'core/ha_response.dart';
import 'dart:convert';


Future<void> main() async {
  // final HomeAssistantService haService =
  //    MockHomeAssistantService();
  WidgetsFlutterBinding.ensureInitialized();

  final HomeAssistantService haService =
      RealHomeAssistantService(
        baseUrl: NodeRedConfig.baseUrl,
        token: '',
      );

  // Später:
  //
  // final HomeAssistantService haService =
  //     RealHomeAssistantService(
  //       baseUrl: 'http://192.168.178.50:8123',
  //       token: 'TOKEN',
  //     );

  final controller = JarvisController(
    homeAssistantService: haService,
  );

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

      }, onWakeword: () async { 
        print( '[JARVIS WAKEWORD] Flutter hat Wakeword erkannt', 
        );

      await DeviceWakeService.wakeDevice();

      JarvisWakewordBus.fire();
    }, 
  );

  runApp(
    JarvisApp(
      controller: controller,
    ),
  );
}

class JarvisApp extends StatelessWidget {
  final JarvisController controller;

  const JarvisApp({
    super.key,
    required this.controller,
  });

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: JarvisTheme.darkTheme,
      home: HomeScreen(
        controller: controller,
      ),
    );
  }
}