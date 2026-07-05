import 'dart:async';
import 'dart:convert';

import 'package:web_socket_channel/web_socket_channel.dart';

import '../core/ha_response.dart';

class JarvisExternalTriggerService {
  final String websocketUrl;
  final void Function(HaResponse response) onResponse;
  final void Function(String message)? onStatusChanged;

  WebSocketChannel? _channel;
  StreamSubscription? _subscription;
  Timer? _reconnectTimer;

  bool _manuallyClosed = false;
  bool _isConnected = false;

  JarvisExternalTriggerService({
    required this.websocketUrl,
    required this.onResponse,
    this.onStatusChanged,
  });

  bool get isConnected => _isConnected;

  void connect() {
    _manuallyClosed = false;
    _openConnection();
  }

  void _openConnection() {
    try {
      _channel = WebSocketChannel.connect(
        Uri.parse(websocketUrl),
      );

      _isConnected = true;
      onStatusChanged?.call('WebSocket verbunden');

      _subscription = _channel!.stream.listen(
        _handleMessage,
        onError: (error) {
          _isConnected = false;
          onStatusChanged?.call(
            'WebSocket Fehler: $error',
          );
          _scheduleReconnect();
        },
        onDone: () {
          _isConnected = false;
          onStatusChanged?.call(
            'WebSocket getrennt',
          );
          _scheduleReconnect();
        },
        cancelOnError: true,
      );
    } catch (e) {
      _isConnected = false;
      onStatusChanged?.call(
        'WebSocket konnte nicht verbunden werden: $e',
      );
      _scheduleReconnect();
    }
  }

  void _handleMessage(dynamic data) {
    try {
      final Map<String, dynamic> json;

      if (data is String) {
        json = jsonDecode(data) as Map<String, dynamic>;
      } else if (data is Map<String, dynamic>) {
        json = data;
      } else {
        onStatusChanged?.call(
          'Unbekanntes WebSocket Payload-Format',
        );
        return;
      }

      final response = HaResponse.fromJson(json);
      onResponse(response);
    } catch (e) {
      onStatusChanged?.call(
        'WebSocket Nachricht konnte nicht verarbeitet werden: $e',
      );
    }
  }

  void _scheduleReconnect() {
    if (_manuallyClosed) return;

    _reconnectTimer?.cancel();
    _reconnectTimer = Timer(
      const Duration(seconds: 3),
      () {
        if (!_manuallyClosed) {
          _openConnection();
        }
      },
    );
  }

  Future<void> dispose() async {
    _manuallyClosed = true;

    _reconnectTimer?.cancel();
    _reconnectTimer = null;

    await _subscription?.cancel();
    _subscription = null;

    await _channel?.sink.close();
    _channel = null;

    _isConnected = false;
  }
}
