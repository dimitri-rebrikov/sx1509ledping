from LEDControl import LEDControl
from typing import Tuple, List
import os
import time

class PingTarget:

    def __init__(self, pingAddress: str, important: bool):
        self.pingAddress = pingAddress
        self.important = important

class LEDPingStatus:

    BusyLed = 7

    LedMapping = [
        0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15
    ]
    
    def __init__(self, ledControl: LEDControl, pingTargets: List[PingTarget]):
        while True:
            ledId = 0;
            ledControl.ledOn(self.BusyLed)
            for pingTarget in pingTargets:
                ok = os.system("ping -c 1 -w2 " + pingTarget.pingAddress) # + " > /dev/null 2>&1")
                if ok == 0:
                    ledControl.ledOn(self.LedMapping[ledId])
                elif pingTarget.important:
                    ledControl.ledBlink(self.LedMapping[ledId])
                else:
                    ledControl.ledOff(self.LedMapping[ledId])
                ledId += 1
            ledControl.ledOff(self.BusyLed)
            time.sleep(3)
