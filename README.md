
class _VoiceRingPainter
    extends CustomPainter {

  final Color color;
  final double progress;
  final bool speaking;

  _VoiceRingPainter({
    required this.color,
    required this.progress,
    required this.speaking,
  });

  @override
  void paint(
    Canvas canvas,
    Size size,
  ) {

    final center =
        size.center(Offset.zero);

    const segmentCount = 96;

    final baseRadius =
        size.width / 2 - 6;

    final linePaint = Paint()
      ..color = color.withValues(
        alpha: speaking ? 0.95 : 0.45,
      )
      ..strokeWidth = 2.1
      ..strokeCap = StrokeCap.round;

    final glowPaint = Paint()
      ..color = color.withValues(
        alpha: speaking ? 0.18 : 0.08,
      )
      ..strokeWidth = 6
      ..strokeCap = StrokeCap.round
      ..maskFilter =
          const MaskFilter.blur(
        BlurStyle.normal,
        6,
      );

    for (int i = 0;
        i < segmentCount;
        i++) {

      final angle =
          (2 * math.pi /
                  segmentCount) *
              i;

      double amplitude = 2;

      if (speaking) {

        final wave1 =
            math.sin(
              angle * 6 +
                  progress *
                      math.pi *
                      10,
            );

        final wave2 =
            math.sin(
              angle * 17 -
                  progress *
                      math.pi *
                      8,
            );

        final wave3 =
            math.sin(
              angle * 31 +
                  progress *
                      math.pi *
                      5,
            );

        amplitude =
            3 +
            ((wave1 +
                        wave2 +
                        wave3) /
                    3)
                .abs() *
                18;
      }

      final startRadius =
          baseRadius;

      final endRadius =
          baseRadius + amplitude;

      final start = Offset(
        center.dx +
            math.cos(angle) *
                startRadius,
        center.dy +
            math.sin(angle) *
                startRadius,
      );

      final end = Offset(
        center.dx +
            math.cos(angle) *
                endRadius,
        center.dy +
            math.sin(angle) *
                endRadius,
      );

      canvas.drawLine(
        start,
        end,
        glowPaint,
      );

      canvas.drawLine(
        start,
        end,
        linePaint,
      );
    }
  }

  @override
  bool shouldRepaint(
      covariant _VoiceRingPainter
          oldDelegate) {
    return true;
  }
}
