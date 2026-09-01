import 'dart:convert';
//import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import '../core/constants.dart';

import '../core/ha_response.dart';
import '../core/jarvis_intent.dart';
import 'home_assistant_service.dart';

class RealHomeAssistantService implements HomeAssistantService {
  final String baseUrl;
  final String token;

  RealHomeAssistantService({
    required this.baseUrl,
    required this.token,
  });

  Map<String, String> get _headers {
    final credentials = base64Encode(
      utf8.encode('${NodeRedConfig.username}:${NodeRedConfig.password}'),
    );

    return {
      'Content-Type': 'application/json',
      'Authorization': 'Basic $credentials',
    };
  }

  @override
  Future<bool> ping() async {
    try {
      final res = await http.post(
        Uri.parse('$baseUrl/jarvis-router'),
        headers: _headers,
        body: jsonEncode({
          'rawText': 'ping',
          'intentType': 'ping',
          'entity': null,
        })
      );

      return res.statusCode >= 200 && res.statusCode < 300;
    } catch (_) {
      return false;
    }
  }

  @override
  Future<HaResponse> sendIntent(JarvisIntent intent) async {
    try {
      final res = await http.post(
        Uri.parse('$baseUrl/jarvis-router'),
        headers: _headers,
        body: jsonEncode({
          'rawText': intent.rawText,
          'intentType': intent.type.name,
          'entity': intent.entity,
        }),
      );

      if (res.statusCode >= 200 && res.statusCode < 300) {
        if (res.body.isEmpty) {
          return HaResponse(
            success: true,
            intent: intent.type.name,
            entity: intent.entity ?? '',
            state: 'executed',
            message: 'Intent wurde erfolgreich an Home Assistant gesendet',
          );
        }
        final data = jsonDecode(res.body);
        return HaResponse.fromJson(data);
      }

      return HaResponse(
        success: false,
        intent: intent.type.name,
        entity: intent.entity ?? '',
        state: 'error',
        message: 'HTTP ${res.statusCode}: ${res.body}',
      );
    } catch (e) {
      return HaResponse(
        success: false,
        intent: 'exception',
        entity: intent.entity ?? '',
        state: 'error',
        message: e.toString(),
      );
    }
  }
}