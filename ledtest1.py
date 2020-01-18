import SX1509
import LEDControl
import time

addr = 0x3e
sx = SX1509.SX1509(addr)
ctl = LEDControl.LEDControl(sx)

for i in range(0, 15): 
    ctl.led(i, True)
    time.sleep(1)

