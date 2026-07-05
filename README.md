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

    const pointCount = 360;

    final path = Path();

    for (int i = 0;
        i <= pointCount;
        i++) {

      final angle =
          (2 * math.pi /
                  pointCount) *
              i;

      double offset = 0;

      if (speaking) {

        final hotspot1 =
            math.exp(
              -math.pow(
                    angle -
                        (progress *
                            2 *
                            math.pi),
                    2,
                  ) /
                  0.35,
            ) *
            7;

        final hotspot2 =
            math.exp(
              -math.pow(
                    angle -
                        ((progress +
                                    0.33) %
                                1.0) *
                            2 *
                            math.pi,
                    2,
                  ) /
                  0.25,
            ) *
            4;

        final hotspot3 =
            math.exp(
              -math.pow(
                    angle -
                        ((progress +
                                    0.70) %
                                1.0) *
                            2 *
                            math.pi,
                    2,
                  ) /
                  0.18,
            ) *
            3;

        offset =
            hotspot1 +
            hotspot2 +
            hotspot3;
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
      ..strokeWidth = 10
      ..color = color.withValues(
        alpha: 0.18,
      )
      ..maskFilter =
          const MaskFilter.blur(
        BlurStyle.normal,
        8,
      );

    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 4
      ..color = color;

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
              oldDelegate) =>
      true;
}
