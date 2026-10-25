import 'package:flutter/material.dart';
class HudPanel extends StatelessWidget {
 const HudPanel({super.key,required this.title,required this.lines,this.indicatorColor=Colors.cyanAccent,this.width,this.height,this.compact=false});
 final String title; final List<String> lines; final Color indicatorColor; final double? width; final double? height; final bool compact;
 @override Widget build(BuildContext context)=>Container(width:width,height:height,padding:EdgeInsets.all(compact?10:12),
  decoration:BoxDecoration(color:Colors.black.withValues(alpha:.35),borderRadius:BorderRadius.circular(12),border:Border.all(color:Colors.cyanAccent.withValues(alpha:.25)),boxShadow:[BoxShadow(color:Colors.cyanAccent.withValues(alpha:.08),blurRadius:12)]),
  child:Column(crossAxisAlignment:CrossAxisAlignment.start,children:[Row(children:[Container(width:compact?9:10,height:compact?9:10,decoration:BoxDecoration(shape:BoxShape.circle,color:indicatorColor,boxShadow:[BoxShadow(color:indicatorColor,blurRadius:8)])),const SizedBox(width:8),Expanded(child:Text(title,maxLines:1,overflow:TextOverflow.ellipsis,style:TextStyle(color:Colors.cyanAccent,fontWeight:FontWeight.bold,fontSize:compact?9:10,letterSpacing:compact?1.35:1.8)))]),const SizedBox(height:6),Divider(color:Colors.cyanAccent.withValues(alpha:.3),thickness:.5,height:8),const SizedBox(height:2),...lines.map((e)=>Padding(padding:const EdgeInsets.only(bottom:4),child:Text(e,maxLines:1,overflow:TextOverflow.ellipsis,style:TextStyle(color:Colors.white70,fontSize:compact?9:10,letterSpacing:.4))))]));
}
