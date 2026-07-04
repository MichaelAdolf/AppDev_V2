import 'package:flutter/material.dart';

class JarvisTheme {
  static const Color primary = Colors.cyanAccent;
  static const Color background = Colors.black;
  static const Color success = Colors.greenAccent;
  static const Color warning = Colors.orangeAccent;
  static const Color error = Colors.redAccent;
  static const Color mutedText = Colors.white70;

  static ThemeData darkTheme = ThemeData(
    brightness: Brightness.dark,
    scaffoldBackgroundColor: background,
    colorScheme: const ColorScheme.dark(
      primary: primary,
      surface: background,
      error: error,
    ),
    textTheme: const TextTheme(
      bodyMedium: TextStyle(
        color: mutedText,
      ),
    ),
    useMaterial3: true,
  );
}