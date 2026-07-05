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

    final radius =
        size.width / 2 - 3;

    final path = Path();

    const pointCount = 220;

    for (int i = 0;
        i <= pointCount;
        i++) {

      final angle =
          (2 * math.pi /
                  pointCount) *
              i;

      double offset = 0;

      if (speaking) {

        final wave1 =
            math.sin(
              angle * 2.0 +
                  progress * 2.5,
            );

        final wave2 =
            math.sin(
              angle * 3.5 -
                  progress * 1.7,
            );

        offset =
            wave1 * 3 +
            wave2 * 1.5;
      }

      final r =
          radius + offset;

      final x =
          center.dx +
          math.cos(angle) * r;

      final y =
          center.dy +
          math.sin(angle) * r;

      if (i == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }

    path.close();

    final glowPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 8
      ..color = color.withValues(
        alpha: 0.12,
      )
      ..maskFilter =
          const MaskFilter.blur(
        BlurStyle.normal,
        8,
      );

    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..color = color.withValues(
        alpha: 0.95,
      );

    canvas.drawPath(
      path,
      glowPaint,
    );

    canvas.drawPath(
      path,
      paint,
    );
  }

  @override
  bool shouldRepaint(
      covariant _VoiceRingPainter
          oldDelegate) {
    return true;
  }
}
