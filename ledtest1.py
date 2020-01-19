import SX1509
import LEDControl
import time

addr = 0x3e
sx = SX1509.SX1509(addr)
ctl = LEDControl.LEDControl(sx)

for i in range(0, 16): 
    ctl.ledOn(i)
    time.sleep(0.2)

for i in range(0, 16): 
    ctl.ledOff(i)
    time.sleep(0.2)

for i in range(0, 16): 
    ctl.ledBlink(i)
    time.sleep(0.2)

#time.sleep(5)

#for i in range(0, 16): 
#    ctl.ledStopBlink(i)
#    time.sleep(0.2)

