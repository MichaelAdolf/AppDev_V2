import 'dart:math' as math;
import 'package:flutter/material.dart';

class AmbientConnections extends StatefulWidget {const AmbientConnections({super.key});@override State<AmbientConnections> createState()=>_AmbientConnectionsState();}
class _AmbientConnectionsState extends State<AmbientConnections> with SingleTickerProviderStateMixin {
 late final AnimationController _controller; late final List<_HudConnection> _connections;
 @override void initState(){super.initState();_connections=_createConnections();_controller=AnimationController(vsync:this,duration:const Duration(seconds:14))..repeat();}
 List<_HudConnection> _createConnections()=>const [
  _HudConnection(points:[Offset(.08,.18),Offset(.28,.18),Offset(.34,.24),Offset(.48,.24)],phase:0),
  _HudConnection(points:[Offset(.63,.17),Offset(.74,.17),Offset(.78,.22),Offset(.90,.22)],phase:.12),
  _HudConnection(points:[Offset(.12,.37),Offset(.30,.37),Offset(.30,.44),Offset(.42,.44)],phase:.25),
  _HudConnection(points:[Offset(.58,.39),Offset(.72,.39),Offset(.72,.46),Offset(.86,.46)],phase:.38),
  _HudConnection(points:[Offset(.10,.62),Offset(.25,.62),Offset(.31,.68),Offset(.44,.68)],phase:.52),
  _HudConnection(points:[Offset(.60,.63),Offset(.75,.63),Offset(.81,.69),Offset(.92,.69)],phase:.64),
  _HudConnection(points:[Offset(.16,.79),Offset(.34,.79),Offset(.34,.84),Offset(.50,.84)],phase:.76),
  _HudConnection(points:[Offset(.52,.82),Offset(.66,.82),Offset(.72,.87),Offset(.88,.87)],phase:.88),
  _HudConnection(points:[Offset(.20,.28),Offset(.25,.28),Offset(.25,.33),Offset(.38,.33)],phase:.18),
  _HudConnection(points:[Offset(.67,.30),Offset(.78,.30),Offset(.78,.35),Offset(.91,.35)],phase:.44),
  _HudConnection(points:[Offset(.08,.53),Offset(.19,.53),Offset(.23,.57),Offset(.35,.57)],phase:.68),
  _HudConnection(points:[Offset(.66,.55),Offset(.80,.55),Offset(.84,.59),Offset(.93,.59)],phase:.82),
 ];
 @override void dispose(){_controller.dispose();super.dispose();}
 @override Widget build(BuildContext context)=>IgnorePointer(child:RepaintBoundary(child:CustomPaint(
  painter:_AmbientConnectionPainter(connections:_connections,animation:_controller),size:Size.infinite)));
}
class _HudConnection {final List<Offset> points;final double phase;const _HudConnection({required this.points,required this.phase});}
class _AmbientConnectionPainter extends CustomPainter {
 final List<_HudConnection> connections;final Animation<double> animation;
 _AmbientConnectionPainter({required this.connections,required this.animation}):super(repaint:animation);
 @override void paint(Canvas canvas,Size size){for(final c in connections){final path=_path(c.points,size);_base(canvas,path);_glow(canvas,path);_shimmer(canvas,path,c.phase);_nodes(canvas,c.points,size);}}
 Path _path(List<Offset> pts,Size size){final p=Path();if(pts.isEmpty)return p;final first=Offset(pts.first.dx*size.width,pts.first.dy*size.height);p.moveTo(first.dx,first.dy);for(var i=1;i<pts.length;i++){final q=Offset(pts[i].dx*size.width,pts[i].dy*size.height);p.lineTo(q.dx,q.dy);}return p;}
 void _base(Canvas c,Path p)=>c.drawPath(p,Paint()..style=PaintingStyle.stroke..strokeWidth=1..strokeCap=StrokeCap.round..color=Colors.cyanAccent.withValues(alpha:.07));
 void _glow(Canvas c,Path p)=>c.drawPath(p,Paint()..style=PaintingStyle.stroke..strokeWidth=3..strokeCap=StrokeCap.round..color=Colors.cyanAccent.withValues(alpha:.025)..maskFilter=const MaskFilter.blur(BlurStyle.normal,5));
 void _shimmer(Canvas c,Path p,double phase){final metrics=p.computeMetrics();if(metrics.isEmpty)return;final m=metrics.first;if(m.length<=0)return;final prog=(animation.value+phase)%1;final start=m.length*prog;final end=math.min(start+m.length*.18,m.length);final sp=m.extractPath(start,end);c.drawPath(sp,Paint()..style=PaintingStyle.stroke..strokeWidth=2..strokeCap=StrokeCap.round..color=Colors.cyanAccent.withValues(alpha:.22)..maskFilter=const MaskFilter.blur(BlurStyle.normal,2.5));final tangent=m.getTangentForOffset(end);if(tangent!=null)c.drawCircle(tangent.position,2.8,Paint()..color=Colors.cyanAccent.withValues(alpha:.45)..maskFilter=const MaskFilter.blur(BlurStyle.normal,4));}
 void _nodes(Canvas c,List<Offset> pts,Size size){for(final p in pts){final pos=Offset(p.dx*size.width,p.dy*size.height);c.drawCircle(pos,5,Paint()..color=Colors.cyanAccent.withValues(alpha:.10)..maskFilter=const MaskFilter.blur(BlurStyle.normal,6));c.drawCircle(pos,2,Paint()..color=Colors.cyanAccent.withValues(alpha:.30));}}
 @override bool shouldRepaint(covariant _AmbientConnectionPainter oldDelegate)=>oldDelegate.connections!=connections||oldDelegate.animation!=animation;
}
