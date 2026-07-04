import 'dart:math' as math;
import 'package:flutter/material.dart';

class AmbientParticles extends StatefulWidget {
  const AmbientParticles({super.key});

  @override
  State<AmbientParticles> createState() =>
      _AmbientParticlesState();
}

class _AmbientParticlesState
    extends State<AmbientParticles>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  final List<_Particle> particles =
      List.generate(
    35,
    (_) => _Particle.random(),
  );

  @override
  void initState() {
    super.initState();

    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 30),
    )..repeat();

    _controller.addListener(() {
      setState(() {});
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      painter: _ParticlePainter(
        particles,
        _controller.value,
      ),
      size: Size.infinite,
    );
  }
}

class _Particle {
  final double x;
  final double y;
  final double radius;
  final double speed;

  _Particle({
    required this.x,
    required this.y,
    required this.radius,
    required this.speed,
  });

  factory _Particle.random() {
    final random = math.Random();

    return _Particle(
      x: random.nextDouble(),
      y: random.nextDouble(),
      radius:
          1 + random.nextDouble() * 2,
      speed:
          0.02 + random.nextDouble() * 0.05,
    );
  }
}

class _ParticlePainter extends CustomPainter {
  final List<_Particle> particles;
  final double progress;

  _ParticlePainter(
    this.particles,
    this.progress,
  );

  @override
  void paint(
    Canvas canvas,
    Size size,
  ) {
    final paint = Paint()
      ..color =
          Colors.cyanAccent.withValues(
        alpha: 0.15,
      );

    for (final particle in particles) {
      final y =
          (particle.y +
                  progress *
                      particle.speed) %
              1.0;

      canvas.drawCircle(
        Offset(
          particle.x * size.width,
          y * size.height,
        ),
        particle.radius,
        paint,
      );
    }
  }

  @override
  bool shouldRepaint(
    covariant _ParticlePainter oldDelegate,
  ) {
    return true;
  }
}
