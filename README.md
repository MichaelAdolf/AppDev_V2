import 'dart:math' as math;
import 'package:flutter/material.dart';

import '../../../core/jarvis_state.dart';

class JarvisCircle extends StatefulWidget {
  final JarvisState state;

  const JarvisCircle({
    super.key,
    required this.state,
  });

  @override
  State<JarvisCircle> createState() => _JarvisCircleState();
}

class _JarvisCircleState extends State<JarvisCircle>
    with TickerProviderStateMixin {
  late final AnimationController _pulseController;

  late final AnimationController _outerRotation;
  late final AnimationController _middleRotation;
  late final AnimationController _innerRotation;
  late final AnimationController _scannerRotation;

  late final Animation<double> _pulse;

  @override
  void initState() {
    super.initState();

    _pulseController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1400),
    )..repeat(reverse: true);

    _pulse = Tween<double>(
      begin: 1.0,
      end: 1.08,
    ).animate(
      CurvedAnimation(
        parent: _pulseController,
        curve: Curves.easeInOut,
      ),
    );

    _outerRotation = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 18),
    )..repeat();

    _middleRotation = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 12),
    )..repeat(reverse: true);

    _innerRotation = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 6),
    )..repeat();

    _scannerRotation = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 3),
    )..repeat();
  }

  @override
  void dispose() {
    _pulseController.dispose();
    _outerRotation.dispose();
    _middleRotation.dispose();
    _innerRotation.dispose();
    _scannerRotation.dispose();

    super.dispose();
  }

  Color _color() {
    switch (widget.state) {
      case JarvisState.idle:
        return Colors.cyanAccent;
      case JarvisState.listening:
        return Colors.blueAccent;
      case JarvisState.thinking:
        return Colors.orangeAccent;
      case JarvisState.speaking:
        return Colors.greenAccent;
      case JarvisState.error:
        return Colors.redAccent;
    }
  }

  double _glow() {
    switch (widget.state) {
      case JarvisState.idle:
        return 25;
      case JarvisState.listening:
        return 45;
      case JarvisState.thinking:
        return 18;
      case JarvisState.speaking:
        return 38;
      case JarvisState.error:
        return 58;
    }
  }

  double _pulseSpeedFactor() {
    switch (widget.state) {
      case JarvisState.idle:
        return 1.00;
      case JarvisState.listening:
        return 1.03;
      case JarvisState.thinking:
        return 0.98;
      case JarvisState.speaking:
        return 1.04;
      case JarvisState.error:
        return 1.06;
    }
  }

  double _scannerOpacity() {
    switch (widget.state) {
      case JarvisState.idle:
        return 0.45;
      case JarvisState.listening:
        return 0.90;
      case JarvisState.thinking:
        return 0.75;
      case JarvisState.speaking:
        return 0.85;
      case JarvisState.error:
        return 1.00;
    }
  }

  double _scannerSweepAngle() {
    switch (widget.state) {
      case JarvisState.idle:
        return math.pi / 5.5;
      case JarvisState.listening:
        return math.pi / 3.8;
      case JarvisState.thinking:
        return math.pi / 4.5;
      case JarvisState.speaking:
        return math.pi / 3.5;
      case JarvisState.error:
        return math.pi / 3.0;
    }
  }

  Widget _rotatingRing({
    required AnimationController controller,
    required double size,
    required Color color,
    required double strokeWidth,
    double opacity = 0.8,
  }) {
    return AnimatedBuilder(
      animation: controller,
      builder: (_, child) {
        return Transform.rotate(
          angle: controller.value * 2 * math.pi,
          child: child,
        );
      },
      child: Container(
        width: size,
        height: size,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          border: Border.all(
            color: color.withValues(alpha: opacity),
            width: strokeWidth,
          ),
        ),
      ),
    );
  }

  Widget _scannerRing({
    required double size,
    required Color color,
  }) {
    return AnimatedBuilder(
      animation: _scannerRotation,
      builder: (context, child) {
        return Transform.rotate(
          angle: _scannerRotation.value * 2 * math.pi,
          child: CustomPaint(
            size: Size.square(size),
            painter: _ScannerRingPainter(
              color: color,
              opacity: _scannerOpacity(),
              sweepAngle: _scannerSweepAngle(),
            ),
          ),
        );
      },
    );
  }

  Widget _radialTickRing({
    required double size,
    required Color color,
  }) {
    return CustomPaint(
      size: Size.square(size),
      painter: _TickRingPainter(
        color: color,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final color = _color();

    return AnimatedBuilder(
      animation: _pulseController,
      builder: (context, child) {
        return Transform.scale(
          scale: _pulse.value * _pulseSpeedFactor(),
          child: SizedBox(
            width: 280,
            height: 280,
            child: Stack(
              alignment: Alignment.center,
              children: [
                // Dezente technische Tick-Markierungen außen
                _radialTickRing(
                  size: 270,
                  color: color,
                ),

                // Äußerer Ring
                _rotatingRing(
                  controller: _outerRotation,
                  size: 250,
                  color: color,
                  strokeWidth: 1.5,
                  opacity: 0.45,
                ),

                // Scanner-Bogen
                _scannerRing(
                  size: 248,
                  color: color,
                ),

                // Mittlerer Ring
                _rotatingRing(
                  controller: _middleRotation,
                  size: 220,
                  color: color,
                  strokeWidth: 2,
                  opacity: 0.65,
                ),

                // Innerer Ring
                _rotatingRing(
                  controller: _innerRotation,
                  size: 190,
                  color: color,
                  strokeWidth: 2,
                  opacity: 0.75,
                ),

                // Glowing Circle
                Container(
                  width: 160,
                  height: 160,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    border: Border.all(
                      color: color,
                      width: 4,
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: color.withValues(alpha: 0.55),
                        blurRadius: _glow(),
                        spreadRadius: 6,
                      ),
                    ],
                  ),
                ),

                // Innerer transparenter Layer
                Container(
                  width: 122,
                  height: 122,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    border: Border.all(
                      color: color.withValues(alpha: 0.25),
                      width: 1,
                    ),
                    color: color.withValues(alpha: 0.04),
                  ),
                ),

                // Kern
                Container(
                  width: 82,
                  height: 82,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: color.withValues(alpha: 0.18),
                    boxShadow: [
                      BoxShadow(
                        color: color.withValues(alpha: 0.80),
                        blurRadius: 24,
                        spreadRadius: 2,
                      ),
                    ],
                  ),
                ),

                // Innerer Punkt
                Container(
                  width: 28,
                  height: 28,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: color.withValues(alpha: 0.75),
                    boxShadow: [
                      BoxShadow(
                        color: color.withValues(alpha: 0.9),
                        blurRadius: 18,
                        spreadRadius: 3,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}

class _ScannerRingPainter extends CustomPainter {
  final Color color;
  final double opacity;
  final double sweepAngle;

  _ScannerRingPainter({
    required this.color,
    required this.opacity,
    required this.sweepAngle,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final rect = Offset.zero & size;

    final scannerPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 7
      ..strokeCap = StrokeCap.round
      ..shader = SweepGradient(
        colors: [
          color.withValues(alpha: 0.0),
          color.withValues(alpha: opacity * 0.35),
          color.withValues(alpha: opacity),
          color.withValues(alpha: 0.0),
        ],
        stops: const [
          0.0,
          0.35,
          0.70,
          1.0,
        ],
      ).createShader(rect);

    final glowPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 13
      ..strokeCap = StrokeCap.round
      ..color = color.withValues(alpha: opacity * 0.18)
      ..maskFilter = const MaskFilter.blur(
        BlurStyle.normal,
        8,
      );

    final arcRect = Rect.fromCircle(
      center: size.center(Offset.zero),
      radius: size.width / 2 - 10,
    );

    canvas.drawArc(
      arcRect,
      -math.pi / 2,
      sweepAngle,
      false,
      glowPaint,
    );

    canvas.drawArc(
      arcRect,
      -math.pi / 2,
      sweepAngle,
      false,
      scannerPaint,
    );
  }

  @override
  bool shouldRepaint(covariant _ScannerRingPainter oldDelegate) {
    return oldDelegate.color != color ||
        oldDelegate.opacity != opacity ||
        oldDelegate.sweepAngle != sweepAngle;
  }
}

class _TickRingPainter extends CustomPainter {
  final Color color;

  _TickRingPainter({
    required this.color,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final center = size.center(Offset.zero);
    final radiusOuter = size.width / 2 - 6;
    final radiusInnerShort = radiusOuter - 7;
    final radiusInnerLong = radiusOuter - 14;

    final paint = Paint()
      ..color = color.withValues(alpha: 0.22)
      ..strokeWidth = 1.2
      ..strokeCap = StrokeCap.round;

    const tickCount = 64;

    for (int i = 0; i < tickCount; i++) {
      final angle = (2 * math.pi / tickCount) * i;

      final isLongTick = i % 8 == 0;
      final innerRadius = isLongTick ? radiusInnerLong : radiusInnerShort;

      final outer = Offset(
        center.dx + math.cos(angle) * radiusOuter,
        center.dy + math.sin(angle) * radiusOuter,
      );

      final inner = Offset(
        center.dx + math.cos(angle) * innerRadius,
        center.dy + math.sin(angle) * innerRadius,
      );

      canvas.drawLine(
        inner,
        outer,
        paint,
      );
    }
  }

  @override
  bool shouldRepaint(covariant _TickRingPainter oldDelegate) {
    return oldDelegate.color != color;
  }
}
