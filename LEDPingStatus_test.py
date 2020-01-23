from SX1509 import SX1509
from LEDControl import LEDControl
from LEDPingStatus import LEDPingStatus, PingTarget
import signal
import sys

addr = 0x3e
sx = SX1509(addr)
ctl = LEDControl(sx)
targets = [
    PingTarget('127.0.0.1', True),
    PingTarget('8.8.8.8', True),
    PingTarget('blubbblubb', False),
    PingTarget('blahblah', True)
]
st = LEDPingStatus(ctl, targets)

def cancelSignalHandler(sig, frame):
    st.stop()

signal.signal(signal.SIGINT, cancelSignalHandler)

st.start()
