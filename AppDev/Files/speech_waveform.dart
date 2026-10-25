import 'dart:math' as math;
import 'package:flutter/material.dart';

class SpeechWaveform extends StatefulWidget {
  final Color color;
  final double width;
  final double height;

  const SpeechWaveform({
    super.key,
    this.color = Colors.greenAccent,
    this.width = 180,
    this.height = 42,
  });

  @override
  State<SpeechWaveform> createState() => _SpeechWaveformState();
}

class _SpeechWaveformState extends State<SpeechWaveform> with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  static const int _barCount = 18;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 900),
    )..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  double _barHeight(int index, double animationValue) {
    final phase = animationValue * 2 * math.pi;
    final wave = math.sin(phase + index * 0.55);
    final normalized = (wave + 1) / 2;

    return 8 + normalized * (widget.height - 8);
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: widget.width,
      height: widget.height,
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, child) {
          return Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: List.generate(_barCount, (index) {
              final height = _barHeight(index, _controller.value);
              return Container(
                width: 4,
                height: height,
                decoration: BoxDecoration(
                  color: widget.color.withValues(alpha: 0.45),
                  borderRadius: BorderRadius.circular(6),
                  boxShadow: [
                    BoxShadow(
                      color: widget.color.withValues(alpha: 0.45),
                      blurRadius: 8,
                      spreadRadius: 1,
                    ),
                  ],
                ),
              );
            }),
          );
        },
      ),
    );
  }
}