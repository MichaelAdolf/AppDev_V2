import 'package:flutter/material.dart';
enum JarvisLayoutClass { compact, standard, landscape, wide }
@immutable
class JarvisLayout {
 const JarvisLayout._({required this.layoutClass,required this.viewport,required this.outerPadding,required this.gap,required this.orbSize,required this.controlSize,required this.conversationHeight,required this.titleFontSize});
 final JarvisLayoutClass layoutClass; final Size viewport;
 final double outerPadding,gap,orbSize,controlSize,conversationHeight,titleFontSize;
 bool get isCompact=>layoutClass==JarvisLayoutClass.compact;
 bool get usesLandscapeComposition=>layoutClass==JarvisLayoutClass.landscape||layoutClass==JarvisLayoutClass.wide;
 double get panelGap=>gap; double get maxContentWidth=>usesLandscapeComposition?1500:720;
 static JarvisLayout from(BoxConstraints c){final w=c.maxWidth,h=c.maxHeight,land=w>h;
  final cls=land?(w>=1100?JarvisLayoutClass.wide:JarvisLayoutClass.landscape):(w<430?JarvisLayoutClass.compact:JarvisLayoutClass.standard);
  final pad=cls==JarvisLayoutClass.wide?16.0:10.0;final gap=cls==JarvisLayoutClass.wide?14.0:(cls==JarvisLayoutClass.standard?14.0:10.0);
  final orb=(land?h*.38:w*.54).clamp(land?145.0:185.0,land?215.0:270.0).toDouble();
  return JarvisLayout._(layoutClass:cls,viewport:Size(w,h),outerPadding:pad,gap:gap,orbSize:orb,
   controlSize:(orb*.24).clamp(48.0,62.0).toDouble(),conversationHeight:land?(h*.17).clamp(78.0,105.0).toDouble():(h*.15).clamp(118.0,158.0).toDouble(),
   titleFontSize:land?(orb*.13).clamp(22.0,28.0).toDouble():(orb*.115).clamp(24.0,34.0).toDouble());}
}
