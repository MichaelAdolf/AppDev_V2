import 'package:flutter/material.dart';
class HudOverlay extends StatelessWidget {const HudOverlay({super.key});@override Widget build(BuildContext context)=>const IgnorePointer(child:RepaintBoundary(child:CustomPaint(painter:_HudPainter(),size:Size.infinite)));}
class _HudPainter extends CustomPainter {const _HudPainter();
 @override void paint(Canvas canvas,Size size){_corners(canvas,size);_lines(canvas,size);}
 void _corners(Canvas c,Size s){final p=Paint()..color=Colors.cyanAccent.withValues(alpha:.20)..strokeWidth=1.5;const m=15.0,l=45.0;
  c.drawLine(const Offset(m,m),const Offset(m+l,m),p);c.drawLine(const Offset(m,m),const Offset(m,m+l),p);
  c.drawLine(Offset(s.width-m,m),Offset(s.width-m-l,m),p);c.drawLine(Offset(s.width-m,m),Offset(s.width-m,m+l),p);
  c.drawLine(Offset(m,s.height-m),Offset(m+l,s.height-m),p);c.drawLine(Offset(m,s.height-m),Offset(m,s.height-m-l),p);
  c.drawLine(Offset(s.width-m,s.height-m),Offset(s.width-m-l,s.height-m),p);c.drawLine(Offset(s.width-m,s.height-m),Offset(s.width-m,s.height-m-l),p);}
 void _lines(Canvas c,Size s){final p=Paint()..color=Colors.cyanAccent.withValues(alpha:.05)..strokeWidth=1;for(double y=100;y<s.height;y+=80){c.drawLine(Offset(40,y),Offset(s.width-40,y),p);}}
 @override bool shouldRepaint(covariant _HudPainter oldDelegate)=>false;
}
