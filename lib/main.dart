import 'package:flutter/material.dart';

import 'features/jarvis/ui/home_screen.dart';
import 'features/jarvis/logic/jarvis_controller.dart';

import 'services/home_assistant_service.dart';
import 'services/real_home_assistant_service.dart';
//import 'services/mock_home_assistant_service.dart';
import 'core/constants.dart';

import 'core/theme.dart';

void main() {
  // final HomeAssistantService haService =
  //    MockHomeAssistantService();

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