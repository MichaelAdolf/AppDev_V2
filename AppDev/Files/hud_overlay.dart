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
    _drawCorners(canvas, size);
    _drawScannerLines(canvas, size);
  }

  void _drawCorners(
    Canvas canvas,
    Size size,
  ) {
    final paint = Paint()
      ..color = Colors.cyanAccent.withValues(
        alpha: 0.20,
      )
      ..strokeWidth = 1.5;

    const double cornerLength = 45;

    // ===== oben links =====

    canvas.drawLine(
      const Offset(15, 15),
      const Offset(
        15 + cornerLength,
        15,
      ),
      paint,
    );

    canvas.drawLine(
      const Offset(15, 15),
      const Offset(
        15,
        15 + cornerLength,
      ),
      paint,
    );

    // ===== oben rechts =====

    canvas.drawLine(
      Offset(size.width - 15, 15),
      Offset(
        size.width - 15 - cornerLength,
        15,
      ),
      paint,
    );

    canvas.drawLine(
      Offset(size.width - 15, 15),
      Offset(
        size.width - 15,
        15 + cornerLength,
      ),
      paint,
    );

    // ===== unten links =====

    canvas.drawLine(
      Offset(
        15,
        size.height - 15,
      ),
      Offset(
        15 + cornerLength,
        size.height - 15,
      ),
      paint,
    );

    canvas.drawLine(
      Offset(
        15,
        size.height - 15,
      ),
      Offset(
        15,
        size.height - 15 - cornerLength,
      ),
      paint,
    );

    // ===== unten rechts =====

    canvas.drawLine(
      Offset(
        size.width - 15,
        size.height - 15,
      ),
      Offset(
        size.width - 15 - cornerLength,
        size.height - 15,
      ),
      paint,
    );

    canvas.drawLine(
      Offset(
        size.width - 15,
        size.height - 15,
      ),
      Offset(
        size.width - 15,
        size.height - 15 - cornerLength,
      ),
      paint,
    );
  }

  void _drawScannerLines(
    Canvas canvas,
    Size size,
  ) {
    final paint = Paint()
      ..color = Colors.cyanAccent.withValues(
        alpha: 0.05,
      )
      ..strokeWidth = 1;

    for (
      double y = 100;
      y < size.height;
      y += 80
    ) {
      canvas.drawLine(
        const Offset(40, 0) +
            Offset(0, y),
        Offset(
          size.width - 40,
          y,
        ),
        paint,
      );
    }
  }

  @override
  bool shouldRepaint(_) => false;
}