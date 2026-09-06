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

  /// Plant das Thinking-Feedback für eine konkrete Interaktion.
  ///
  /// Sprint 1:
  /// [onPlay] enthält später den eigentlichen Start der lokalen Audiodatei.
  /// Aktuell kann dort zunächst nur Logging erfolgen.
  void schedule({
    required int interactionId,
    required Duration delay,
    required ThinkingFeedbackCallback onPlay,
  }) {
    if (_isDisposed) {
      return;
    }

    cancel();

    _scheduledInteractionId = interactionId;

    _delayTimer = Timer(delay, () async {
      if (_isDisposed) {
        return;
      }

      if (_scheduledInteractionId != interactionId) {
        return;
      }

      _delayTimer = null;
      _scheduledInteractionId = null;
      _playingInteractionId = interactionId;

      try {
        await onPlay();
      } catch (error, stackTrace) {
        debugPrint(
          'ThinkingFeedbackService: '
          'Thinking-Feedback konnte nicht gestartet werden: $error',
        );
        debugPrintStack(stackTrace: stackTrace);
      } finally {
        if (_playingInteractionId == interactionId) {
          _playingInteractionId = null;
        }
      }
    });
  }

  /// Bricht eine geplante oder laufende Thinking-Rückmeldung logisch ab.
  ///
  /// Die tatsächliche Audiowiedergabe wird in Sprint 2 über einen eigenen
  /// AudioPlayer zusätzlich gestoppt.
  void cancel() {
    _delayTimer?.cancel();
    _delayTimer = null;

    _scheduledInteractionId = null;
    _playingInteractionId = null;
  }

  /// Bricht nur ab, wenn die angegebene Interaktion noch aktiv ist.
  void cancelForInteraction(int interactionId) {
    final matchesScheduled =
        _scheduledInteractionId == interactionId;

    final matchesPlaying =
        _playingInteractionId == interactionId;

    if (matchesScheduled || matchesPlaying) {
      cancel();
    }
  }

  void dispose() {
    if (_isDisposed) {
      return;
    }

    _isDisposed = true;
    cancel();
  }
}