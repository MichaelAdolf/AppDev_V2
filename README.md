import 'dart:async';

class JarvisWakewordBus {

  static final StreamController<void>
      _controller =
      StreamController.broadcast();

  static Stream<void> get stream =>
      _controller.stream;

  static void fire() {
    _controller.add(null);
  }
}
