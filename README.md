import 'dart:async';

import 'package:flutter/foundation.dart';

typedef ThinkingFeedbackCallback = Future<void> Function();

class ThinkingFeedbackService {
  Timer? _delayTimer;
  int? _scheduledInteractionId;
  int? _playingInteractionId;
  bool _isDisposed = false;

  bool get isScheduled => _delayTimer?.isActive ?? false;
  bool get isPlaying => _playingInteractionId != null;
  int? get scheduledInteractionId => _scheduledInteractionId;
  int? get playingInteractionId => _playingInteractionId;

  void schedule({
    required int interactionId,
    required Duration delay,
    required ThinkingFeedbackCallback onPlay,
  }) {
    if (_isDisposed) return;

    cancel();
    _scheduledInteractionId = interactionId;

    _delayTimer = Timer(delay, () async {
      if (_isDisposed || _scheduledInteractionId != interactionId) return;

      _delayTimer = null;
      _scheduledInteractionId = null;
      _playingInteractionId = interactionId;

      try {
        await onPlay();
      } catch (error, stackTrace) {
        debugPrint(
          'ThinkingFeedbackService: Feedback konnte nicht gestartet werden: '
          '$error',
        );
        debugPrintStack(stackTrace: stackTrace);
      } finally {
        if (_playingInteractionId == interactionId) {
          _playingInteractionId = null;
        }
      }
    });
  }

  void cancel() {
    _delayTimer?.cancel();
    _delayTimer = null;
    _scheduledInteractionId = null;
    _playingInteractionId = null;
  }

  void cancelForInteraction(int interactionId) {
    if (_scheduledInteractionId == interactionId ||
        _playingInteractionId == interactionId) {
      cancel();
    }
  }

  void dispose() {
    if (_isDisposed) return;
    _isDisposed = true;
    cancel();
  }
}
