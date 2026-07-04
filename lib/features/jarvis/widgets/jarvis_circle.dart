import 'package:flutter/material.dart';

import '../../../core/jarvis_state.dart';
import '../../../core/constants.dart';

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

  late AnimationController _pulseController;
  
  late AnimationController _outerRotation;
  late AnimationController _middleRotation;
  late AnimationController _innerRotation;

  late Animation<double> _pulse;

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
        return 15;

      case JarvisState.speaking:
        return 35;

      case JarvisState.error:
        return 55;
    }
  }

  double _speed() {
    switch (widget.state) {
      case JarvisState.idle:
        return 1.0;

      case JarvisState.listening:
        return 1.4;

      case JarvisState.thinking:
        return 0.8;

      case JarvisState.speaking:
        return 1.2;

      case JarvisState.error:
        return 1.6;
    }
  }

  Widget _rotatingRing({
    required AnimationController controller,
    required double size,
    required Color color,
    required double strokeWidth,
  }) {
    return AnimatedBuilder(
      animation: controller,
      builder: (_, child) {
        return Transform.rotate(
          angle: controller.value * 2 * 3.141592653589793,
          child: child,
        );
      },
      child: Container(
        width: size,
        height: size,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          border: Border.all(
            color: color.withOpacity(0.8),
            width: strokeWidth,
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _pulseController.dispose();
    _outerRotation.dispose();
    _middleRotation.dispose();
    _innerRotation.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final color = _color();

    return AnimatedBuilder(
      animation: _pulseController,
      builder: (context, child) {
        return Transform.scale(
          scale: _pulse.value,
          child: SizedBox(
            width: 260,
            height: 260,
            child: Stack(
              alignment: Alignment.center,
              children: [
                _rotatingRing(
                  controller: _outerRotation,
                  size: 250,
                  color: color,
                  strokeWidth: 2,
                ),
                _rotatingRing(
                  controller: _middleRotation,
                  size: 220,
                  color: color,
                  strokeWidth: 2,
                ),
                _rotatingRing(
                  controller: _innerRotation,
                  size: 190,
                  color: color,
                  strokeWidth: 2,
                ),
                //Glowing Circle
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
                        color: color.withOpacity(0.6),
                        blurRadius: _glow(),
                        spreadRadius: 6,
                      ),
                    ],
                  ),
                ),

                //Kern
                Container(
                  width: 80,
                  height: 80,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: color.withOpacity(0.8),
                      boxShadow: [
                        BoxShadow(
                          color: color.withOpacity(0.8),
                          blurRadius: 20,
                        ),
                      ],
                  ),
                ),
              ],
            )
          ),
        );
      },
    );
  }
}