import 'package:flutter/widgets.dart';
import 'package:flutter_foreground_task/flutter_foreground_task.dart';

class JarvisRuntimeService {

  static Future<void> initialize() async {

    FlutterForegroundTask.init(

      androidNotificationOptions:
          AndroidNotificationOptions(
        channelId: 'jarvis_runtime',
        channelName: 'Jarvis Runtime',
        channelDescription:
            'Jarvis Hintergrunddienst',
        channelImportance:
            NotificationChannelImportance.LOW,
        priority: NotificationPriority.LOW,
      ),

      iosNotificationOptions:
          const IOSNotificationOptions(),

      foregroundTaskOptions:
          ForegroundTaskOptions(
        autoRunOnBoot: false,
        autoRunOnMyPackageReplaced: true,
        eventAction: const ForegroundTaskEventAction.nothing,
      ),
    );
  }

  static Future<void> start() async {

    if (await FlutterForegroundTask.isRunningService) {
      return;
    }

    await FlutterForegroundTask.startService(
      notificationTitle: 'Jarvis aktiv',
      notificationText:
          'Hintergrunddienst läuft',
      callback: startCallback,
    );
  }
}

@pragma('vm:entry-point')
void startCallback() {
}