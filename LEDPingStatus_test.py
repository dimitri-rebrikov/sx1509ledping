import SX1509
import LEDControl
import time
from LEDPingStatus import LEDPingStatus, PingTarget

addr = 0x3e
sx = SX1509.SX1509(addr)
ctl = LEDControl.LEDControl(sx)
targets = [
    PingTarget('127.0.0.1', True),
    PingTarget('8.8.8.8', True),
    PingTarget('blubbblubb', False),
    PingTarget('blahblah', True)
]
st = LEDPingStatus(ctl, targets)