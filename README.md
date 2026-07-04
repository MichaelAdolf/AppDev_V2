import 'package:flutter/material.dart';

class HudOverlay extends StatelessWidget {
  const HudOverlay({super.key});

  @override
  Widget build(BuildContext context) {
    return IgnorePointer(
      child: CustomPaint(
        painter: _HudPainter(),
        size: Size.infinite,
      ),
    );
  }
}

class _HudPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.cyanAccent.withValues(
        alpha: 0.18,
      )
      ..strokeWidth = 1;

    const corner = 40.0;

    // Oben links
    canvas.drawLine(
      const Offset(15, 15),
      const Offset(15 + corner, 15),
      paint,
    );

    canvas.drawLine(
      const Offset(15, 15),
      const Offset(15, 15 + corner),
      paint,
    );

    // Oben rechts
    canvas.drawLine(
      Offset(size.width - 15, 15),
      Offset(size.width - 15 - corner, 15),
      paint,
    );

    canvas.drawLine(
      Offset(size.width - 15, 15),
      Offset(size.width - 15, 15 + corner),
      paint,
    );

    // Unten links
    canvas.drawLine(
      Offset(15, size.height - 15),
      Offset(15 + corner, size.height - 15),
      paint,
    );

    canvas.drawLine(
      Offset(15, size.height - 15),
      Offset(15, size.height - 15 - corner),
      paint,
    );

    // Unten rechts
    canvas.drawLine(
      Offset(size.width - 15, size.height - 15),
      Offset(size.width - 15 - corner,
          size.height - 15),
      paint,
    );

    canvas.drawLine(
      Offset(size.width - 15, size.height - 15),
      Offset(size.width - 15,
          size.height - 15 - corner),
      paint,
    );

    // Horizontale Scannerlinien

    final scanner =
        Colors.cyanAccent.withValues(
      alpha: 0.04,
    );

    final scannerPaint = Paint()
      ..color = scanner
      ..strokeWidth = 1;

    for (double y = 100;
        y < size.height;
        y += 80) {
      canvas.drawLine(
        Offset(40, y),
        Offset(size.width - 40, y),
        scannerPaint,
      );
    }
  }

  @override
  bool shouldRepaint(_) => false;
}
