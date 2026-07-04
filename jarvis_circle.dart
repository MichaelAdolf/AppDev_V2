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

    const points = 180;

    for (int i = 0;
        i <= points;
        i++) {

      final angle =
          (2 * math.pi / points) * i;

      double wave = 0;

      if (speaking) {
        wave =
            math.sin(
                  angle * 10 +
                  progress *
                      math.pi *
                      8,
                ) *
                4;
      }

      final r = radius + wave;

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

    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..color =
          color.withValues(
        alpha: 0.95,
      );

    final glowPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 8
      ..color =
          color.withValues(
        alpha: 0.15,
      )
      ..maskFilter =
          const MaskFilter.blur(
        BlurStyle.normal,
        8,
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
    covariant _VoiceRingPainter oldDelegate,
  ) {
    return oldDelegate.progress !=
            progress ||
        oldDelegate.speaking !=
            speaking ||
        oldDelegate.color != color;
  }
}
