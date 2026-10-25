import 'dart:math' as math;
import 'package:flutter/material.dart';

class AmbientParticles extends StatefulWidget {
  const AmbientParticles({super.key});
  @override State<AmbientParticles> createState()=>_AmbientParticlesState();
}
class _AmbientParticlesState extends State<AmbientParticles> with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final List<_Particle> particles;
  @override void initState(){super.initState();particles=List.generate(35,(_)=>_Particle.random());_controller=AnimationController(vsync:this,duration:const Duration(seconds:30))..repeat();}
  @override void dispose(){_controller.dispose();super.dispose();}
  @override Widget build(BuildContext context)=>RepaintBoundary(child:CustomPaint(
    painter:_ParticlePainter(particles,_controller),size:Size.infinite));
}
class _Particle {final double x,y,radius,speed;const _Particle({required this.x,required this.y,required this.radius,required this.speed});
 factory _Particle.random(){final r=math.Random();return _Particle(x:r.nextDouble(),y:r.nextDouble(),radius:1+r.nextDouble()*2,speed:.02+r.nextDouble()*.05);}}
class _ParticlePainter extends CustomPainter {
 final List<_Particle> particles; final Animation<double> animation;
 _ParticlePainter(this.particles,this.animation):super(repaint:animation);
 @override void paint(Canvas canvas,Size size){final paint=Paint()..color=Colors.cyanAccent.withValues(alpha:.15);final progress=animation.value;
  for(final p in particles){final y=(p.y+progress*p.speed)%1.0;canvas.drawCircle(Offset(p.x*size.width,y*size.height),p.radius,paint);}}
 @override bool shouldRepaint(covariant _ParticlePainter oldDelegate)=>oldDelegate.particles!=particles||oldDelegate.animation!=animation;
}
