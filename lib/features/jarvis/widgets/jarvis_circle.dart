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
  late final AnimationController _rippleController;
  late final AnimationController _voiceRingController;

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

    _rippleController = AnimationController(
      vsync: this,
      duration: const Duration(
        milliseconds: 1800
      ),
    )..repeat();
  
    _voiceRingController = AnimationController(
      vsync: this,
      duration: const Duration(
        milliseconds: 1200,
        ),
    )..repeat();
  
  }

  @override
  void dispose() {
    _pulseController.dispose();
    _outerRotation.dispose();
    _middleRotation.dispose();
    _innerRotation.dispose();
    _scannerRotation.dispose();
    _rippleController.dispose();
    _voiceRingController.dispose();

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

  Widget _dataRing({
    required double size,
    required Color color,
  }) {
    return AnimatedBuilder(
      animation: _middleRotation,
      builder: (context, child) {
        return Transform.rotate(
          angle: _middleRotation.value * 2 * math.pi,
          child: CustomPaint(
            size: Size.square(size),
            painter: _DataRingPainter(
              color: color,
            ),
          ),
        );
      },
    );
  }

  Widget _rippleRing({
    required Color color,
    required double delay,
  }) {
    return AnimatedBuilder(
      animation: _rippleController,
      builder: (context, child) {
        double progress = 
          ( _rippleController.value + delay) % 1.0;
          return Opacity(
          opacity: (1- progress) * 0.35,
          child: Container(
            width: 140,
            height: 140,
            decoration : BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(
                color: color,
                width: 2,
              ),
            ),
          ),
        );
      }
    );
  }

  Widget _voiceReactiveRing({
    required Color color,
  }) {
    return AnimatedBuilder(
      animation: _voiceRingController, 
      builder: (context, child) {
        return CustomPaint(
          size: const Size.square(160),
          painter: _VoiceRingPainter(
            color: color,
            progress:
              _voiceRingController.value,
            speaking:
              widget.state == JarvisState.speaking,
          ),
        );
      },
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
            width: 240,
            height: 240,
            child: Stack(
              alignment: Alignment.center,
              children: [
                // Dezente technische Tick-Markierungen außen
                _radialTickRing(
                  size: 230,
                  color: color,
                ),

                // Äußerer Ring
                _rotatingRing(
                  controller: _outerRotation,
                  size: 215,
                  color: color,
                  strokeWidth: 1.5,
                  opacity: 0.45,
                ),

                // Scanner-Bogen
                _scannerRing(
                  size: 213,
                  color: color,
                ),

                _dataRing(
                  size: 205,
                  color: color,
                ),

                // Mittlerer Ring
                _rotatingRing(
                  controller: _middleRotation,
                  size: 190,
                  color: color,
                  strokeWidth: 2,
                  opacity: 0.65,
                ),

                // Innerer Ring
                _rotatingRing(
                  controller: _innerRotation,
                  size: 160,
                  color: color,
                  strokeWidth: 2,
                  opacity: 0.75,
                ),

                if (widget.state == JarvisState.speaking)
                  _rippleRing(
                    color: color, 
                    delay: 0,
                  ),

                if (widget.state == JarvisState.speaking)
                  _rippleRing(
                    color: color, 
                    delay: 0.4,
                  ),

                if (widget.state == JarvisState.speaking)
                  _rippleRing(
                    color: color, 
                    delay: 0.8,
                  ),

                _voiceReactiveRing(
                  color: color,
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

class _DataRingPainter
  extends CustomPainter {
  final Color color;

  _DataRingPainter({
    required this.color,
  });

  @override
  void paint(
    Canvas canvas,
    Size size,
  ) {
    final center = size.center(Offset.zero);

    final radius = size.width / 2 - 8;

    final paint = Paint()
      ..color = color.withValues(alpha: 0.35)
      ..strokeWidth = 2
      ..strokeCap = StrokeCap.round;

    for (int i = 0; i < 40; i++) {
      if (i % 3 == 0) continue;

      final angle = (2 * math.pi / 40) * i;

      final outer = Offset(
        center.dx + math.cos(angle) * radius,
        center.dy + math.sin(angle) * radius,
        );

      final inner = Offset (
        center.dx + math.cos(angle) * (radius - 8),
        center.dy + math.sin(angle) * (radius - 8),
      );

      canvas.drawLine(
        inner,
        outer,
        paint,
      );
    }
  }
  @override
  bool shouldRepaint(_) => true;
}

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