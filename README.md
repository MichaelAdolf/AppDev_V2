import 'dart:math' as math;
import 'package:flutter/material.dart';

class AmbientConnections extends StatefulWidget {
  const AmbientConnections({super.key});

  @override
  State<AmbientConnections> createState() =>
      _AmbientConnectionsState();
}

class _AmbientConnectionsState
    extends State<AmbientConnections>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  late final List<_HudConnection> _connections;

  @override
  void initState() {
    super.initState();

    _connections = _createConnections();

    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 14),
    )..repeat();
  }

  List<_HudConnection> _createConnections() {
    return [
      _HudConnection(
        points: const [
          Offset(0.08, 0.18),
          Offset(0.28, 0.18),
          Offset(0.34, 0.24),
          Offset(0.48, 0.24),
        ],
        phase: 0.00,
      ),
      _HudConnection(
        points: const [
          Offset(0.63, 0.17),
          Offset(0.74, 0.17),
          Offset(0.78, 0.22),
          Offset(0.90, 0.22),
        ],
        phase: 0.12,
      ),
      _HudConnection(
        points: const [
          Offset(0.12, 0.37),
          Offset(0.30, 0.37),
          Offset(0.30, 0.44),
          Offset(0.42, 0.44),
        ],
        phase: 0.25,
      ),
      _HudConnection(
        points: const [
          Offset(0.58, 0.39),
          Offset(0.72, 0.39),
          Offset(0.72, 0.46),
          Offset(0.86, 0.46),
        ],
        phase: 0.38,
      ),
      _HudConnection(
        points: const [
          Offset(0.10, 0.62),
          Offset(0.25, 0.62),
          Offset(0.31, 0.68),
          Offset(0.44, 0.68),
        ],
        phase: 0.52,
      ),
      _HudConnection(
        points: const [
          Offset(0.60, 0.63),
          Offset(0.75, 0.63),
          Offset(0.81, 0.69),
          Offset(0.92, 0.69),
        ],
        phase: 0.64,
      ),
      _HudConnection(
        points: const [
          Offset(0.16, 0.79),
          Offset(0.34, 0.79),
          Offset(0.34, 0.84),
          Offset(0.50, 0.84),
        ],
        phase: 0.76,
      ),
      _HudConnection(
        points: const [
          Offset(0.52, 0.82),
          Offset(0.66, 0.82),
          Offset(0.72, 0.87),
          Offset(0.88, 0.87),
        ],
        phase: 0.88,
      ),
      _HudConnection(
        points: const [
          Offset(0.20, 0.28),
          Offset(0.25, 0.28),
          Offset(0.25, 0.33),
          Offset(0.38, 0.33),
        ],
        phase: 0.18,
      ),
      _HudConnection(
        points: const [
          Offset(0.67, 0.30),
          Offset(0.78, 0.30),
          Offset(0.78, 0.35),
          Offset(0.91, 0.35),
        ],
        phase: 0.44,
      ),
      _HudConnection(
        points: const [
          Offset(0.08, 0.53),
          Offset(0.19, 0.53),
          Offset(0.23, 0.57),
          Offset(0.35, 0.57),
        ],
        phase: 0.68,
      ),
      _HudConnection(
        points: const [
          Offset(0.66, 0.55),
          Offset(0.80, 0.55),
          Offset(0.84, 0.59),
          Offset(0.93, 0.59),
        ],
        phase: 0.82,
      ),
    ];
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return IgnorePointer(
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, child) {
          return CustomPaint(
            painter: _AmbientConnectionPainter(
              connections: _connections,
              progress: _controller.value,
            ),
            size: Size.infinite,
          );
        },
      ),
    );
  }
}

class _HudConnection {
  final List<Offset> points;
  final double phase;

  const _HudConnection({
    required this.points,
    required this.phase,
  });
}

class _AmbientConnectionPainter extends CustomPainter {
  final List<_HudConnection> connections;
  final double progress;

  _AmbientConnectionPainter({
    required this.connections,
    required this.progress,
  });

  @override
  void paint(Canvas canvas, Size size) {
    for (final connection in connections) {
      final path = _buildPath(connection.points, size);

      _drawBaseLine(canvas, path);
      _drawGlowLine(canvas, path);
      _drawMovingShimmer(canvas, path, connection.phase);
      _drawNodes(canvas, connection.points, size);
    }
  }

  Path _buildPath(
    List<Offset> normalizedPoints,
    Size size,
  ) {
    final path = Path();

    if (normalizedPoints.isEmpty) {
      return path;
    }

    final first = Offset(
      normalizedPoints.first.dx * size.width,
      normalizedPoints.first.dy * size.height,
    );

    path.moveTo(first.dx, first.dy);

    for (int i = 1; i < normalizedPoints.length; i++) {
      final point = Offset(
        normalizedPoints[i].dx * size.width,
        normalizedPoints[i].dy * size.height,
      );

      path.lineTo(point.dx, point.dy);
    }

    return path;
  }

  void _drawBaseLine(Canvas canvas, Path path) {
    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1
      ..strokeCap = StrokeCap.round
      ..color = Colors.cyanAccent.withValues(alpha: 0.07);

    canvas.drawPath(path, paint);
  }

  void _drawGlowLine(Canvas canvas, Path path) {
    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round
      ..color = Colors.cyanAccent.withValues(alpha: 0.025)
      ..maskFilter = const MaskFilter.blur(
        BlurStyle.normal,
        5,
      );

    canvas.drawPath(path, paint);
  }

  void _drawMovingShimmer(
    Canvas canvas,
    Path path,
    double phase,
  ) {
    final metric = path.computeMetrics().isEmpty
        ? null
        : path.computeMetrics().first;

    if (metric == null || metric.length <= 0) {
      return;
    }

    final shimmerProgress = (progress + phase) % 1.0;

    final shimmerLength = metric.length * 0.18;
    final start = metric.length * shimmerProgress;
    final end = math.min(
      start + shimmerLength,
      metric.length,
    );

    final shimmerPath = metric.extractPath(
      start,
      end,
    );

    final shimmerPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2
      ..strokeCap = StrokeCap.round
      ..color = Colors.cyanAccent.withValues(alpha: 0.22)
      ..maskFilter = const MaskFilter.blur(
        BlurStyle.normal,
        2.5,
      );

    canvas.drawPath(
      shimmerPath,
      shimmerPaint,
    );

    final headTangent = metric.getTangentForOffset(end);

    if (headTangent != null) {
      final dotPaint = Paint()
        ..color = Colors.cyanAccent.withValues(alpha: 0.45)
        ..maskFilter = const MaskFilter.blur(
          BlurStyle.normal,
          4,
        );

      canvas.drawCircle(
        headTangent.position,
        2.8,
        dotPaint,
      );
    }
  }

  void _drawNodes(
    Canvas canvas,
    List<Offset> normalizedPoints,
    Size size,
  ) {
    for (final point in normalizedPoints) {
      final position = Offset(
        point.dx * size.width,
        point.dy * size.height,
      );

      final glowPaint = Paint()
        ..color = Colors.cyanAccent.withValues(alpha: 0.10)
        ..maskFilter = const MaskFilter.blur(
          BlurStyle.normal,
          6,
        );

      final dotPaint = Paint()
        ..color = Colors.cyanAccent.withValues(alpha: 0.30);

      canvas.drawCircle(
        position,
        5,
        glowPaint,
      );

      canvas.drawCircle(
        position,
        2,
        dotPaint,
      );
    }
  }

  @override
  bool shouldRepaint(
    covariant _AmbientConnectionPainter oldDelegate,
  ) {
    return oldDelegate.progress != progress;
  }
}
