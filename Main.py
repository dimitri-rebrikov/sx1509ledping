import SX1509
import LEDControl
from LEDPingStatus import LEDPingStatus
from Config import sx1509Addr, pingTargets

sx = SX1509.SX1509(sx1509Addr)
ctl = LEDControl.LEDControl(sx)
st = LEDPingStatus(ctl, pingTargets)