import 'package:flutter/material.dart';

class HudPanel extends StatelessWidget {
  final String title;
  final List<String> lines;
  final Color indicatorColor;

  const HudPanel({
    super.key,
    required this.title,
    required this.lines,
    this.indicatorColor = Colors.cyanAccent,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 150,
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.black.withValues(
          alpha: 0.35,
        ),
        borderRadius: BorderRadius.circular(
          10,
        ),
        border: Border.all(
          color: Colors.cyanAccent.withValues(
            alpha: 0.25,
          ),
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.cyanAccent.withValues(
              alpha: 0.08,
            ),
            blurRadius: 12,
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment:
            CrossAxisAlignment.start,
        children: [

          // Header
          Row(
            children: [
              Container(
                width: 10,
                height: 10,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: indicatorColor,
                  boxShadow: [
                    BoxShadow(
                      color:
                          indicatorColor,
                      blurRadius: 8,
                    ),
                  ],
                ),
              ),

              const SizedBox(width: 8),

              Expanded(
                child: Text(
                  title,
                  style: const TextStyle(
                    color:
                        Colors.cyanAccent,
                    fontWeight:
                        FontWeight.bold,
                    fontSize: 10,
                    letterSpacing: 1.8,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 8),

          Divider(
            color: Colors.cyanAccent
                .withValues(
              alpha: 0.3,
            ),
            thickness: 0.5,
          ),

          const SizedBox(height: 4),

          ...lines.map(
            (e) => Padding(
              padding:
                  const EdgeInsets.only(
                bottom: 5,
              ),
              child: Text(
                e,
                style: const TextStyle(
                  color: Colors.white70,
                  fontSize: 10,
                  letterSpacing: 0.4,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}