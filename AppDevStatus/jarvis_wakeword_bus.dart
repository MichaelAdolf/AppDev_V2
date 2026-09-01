import 'dart:async';

class JarvisWakewordBus {

static final StreamController _controller = StreamController.broadcast();

static Stream get stream => _controller.stream;

static void fire() { _controller.add(null); } }