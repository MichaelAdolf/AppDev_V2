import 'package:flutter/material.dart';

import '../../../core/conversation_entry.dart';

class ConversationTimeline extends StatelessWidget {
  final List<ConversationEntry> entries;

  const ConversationTimeline({
    super.key,
    required this.entries,
  });

  String _formatTime(DateTime time) {
    final hour = time.hour.toString().padLeft(2, '0');
    final minute = time.minute.toString().padLeft(2, '0');

    return '$hour:$minute';
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 135,
      margin: const EdgeInsets.symmetric(
        horizontal: 18,
      ),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.black.withValues(alpha: 0.38),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(
          color: Colors.cyanAccent.withValues(alpha: 0.35),
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.cyanAccent.withValues(alpha: 0.10),
            blurRadius: 18,
            spreadRadius: 1,
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Text(
                'CONVERSATION LOG',
                style: TextStyle(
                  color: Colors.cyanAccent,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 1.6,
                ),
              ),
              SizedBox(width: 8),
              Expanded(
                child: Divider(
                  color: Colors.cyanAccent,
                  thickness: 0.4,
                ),
              ),
            ],
          ),

          const SizedBox(height: 8),

          if (entries.isEmpty)
            const Expanded(
              child: Center(
                child: Text(
                  'NO ACTIVE CONVERSATION',
                  style: TextStyle(
                    color: Colors.white38,
                    fontSize: 11,
                    letterSpacing: 1.2,
                  ),
                ),
              ),
            )
          else
            Expanded(
              child: ListView.builder(
                padding: EdgeInsets.zero,
                physics: const BouncingScrollPhysics(),
                itemCount: entries.length,
                itemBuilder: (context, index) {
                  final entry = entries[index];

                  final color = entry.isUser
                      ? Colors.blueAccent
                      : Colors.greenAccent;

                  final label = entry.isUser
                      ? 'USER'
                      : 'JARVIS';

                  return Padding(
                    padding: const EdgeInsets.only(
                      bottom: 6,
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        SizedBox(
                          width: 38,
                          child: Text(
                            _formatTime(entry.timestamp),
                            style: const TextStyle(
                              color: Colors.white38,
                              fontSize: 10,
                            ),
                          ),
                        ),

                        SizedBox(
                          width: 48,
                          child: Text(
                            label,
                            style: TextStyle(
                              color: color,
                              fontSize: 10,
                              fontWeight: FontWeight.bold,
                              letterSpacing: 0.8,
                            ),
                          ),
                        ),

                        Expanded(
                          child: Text(
                            entry.text,
                            maxLines: 2,
                            overflow: TextOverflow.ellipsis,
                            style: TextStyle(
                              color: entry.isUser
                                  ? Colors.white70
                                  : Colors.greenAccent,
                              fontSize: 11,
                            ),
                          ),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ),
        ],
      ),
    );
  }
}