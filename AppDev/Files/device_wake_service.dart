import 'package:wakelock_plus/wakelock_plus.dart';
import 'package:screen_brightness/screen_brightness.dart';

class DeviceWakeService {
  static Future<void> wakeDevice() async {
    try {
      await WakelockPlus.enable();
      await ScreenBrightness().setScreenBrightness(
        1.0,
      );
    } catch (_) {}
  }
}