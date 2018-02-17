#!/usr/bin/env python3
import rtmidi_python as rtmidi
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MidiNode(Node):
    def __init__(self):
        super().__init__('midi')
        self.midi_out = rtmidi.MidiOut(b'output')
        self.midi_out.open_port(1)
        self.alarm_sub = self.create_subscription(Int32, 'alarm', self.alarm_cb)
        self.bongo_id = 60
    def alarm_cb(self, msg):
        if msg.data > 0:
            self.midi_out.send_message([0x99, self.bongo_id, 100])
        if self.bongo_id == 60:
            self.bongo_id = 61
        else:
            self.bongo_id = 60
        #self.get_logger().info('I heard: "%d"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    midi_node = MidiNode()
    rclpy.spin(midi_node)
    midi_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
