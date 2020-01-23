from SX1509 import SX1509
from LEDControl import LEDControl
from LEDPingStatus import LEDPingStatus
from Config import sx1509Addr, pingTargets
import signal
import sys

sx = SX1509(sx1509Addr)
ctl = LEDControl(sx)
st = LEDPingStatus(ctl, pingTargets)

def cancelSignalHandler(sig, frame):
    st.stop()

signal.signal(signal.SIGINT, cancelSignalHandler)
signal.signal(signal.SIGTERM, cancelSignalHandler)

st.start()
