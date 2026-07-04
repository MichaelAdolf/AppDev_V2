import 'package:flutter/material.dart';

class HudPanel extends StatelessWidget {
  final String title;
  final List<String> lines;

  const HudPanel({
    super.key,
    required this.title,
    required this.lines,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 150,
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.cyanAccent.withValues(alpha: 0.35),
        ),
      borderRadius: BorderRadius.circular(12),
      color: Colors.black.withValues(alpha: 0.30),
      ),

      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: const TextStyle(
              color: Colors.cyanAccent,
              fontWeight: FontWeight.bold,
              letterSpacing: 1.5,
            ),
          ),

          const SizedBox(height: 8),

          ...lines.map((e) => Padding(
                padding: const EdgeInsets.only(bottom: 4),
                child: Text(
                  e,
                  style: const TextStyle(
                    color: Colors.white70,
                    fontSize: 12,
                  ),
                ),
              ),
            ),
          ],
        ),
      );
    }
  }