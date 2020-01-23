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
        self.ledControl = ledControl
        self.pingTargets = pingTargets

    def start(self):
        self.run = True
        while self.run:
            ledId = 0;
            self.ledControl.ledOn(self.BusyLed)
            for pingTarget in self.pingTargets:
                if not self.run:
                    break
                ok = os.system("ping -c 1 " + pingTarget.pingAddress) # + " > /dev/null 2>&1")
                if ok == 0:
                    self.ledControl.ledOn(self.LedMapping[ledId])
                elif pingTarget.important:
                    self.ledControl.ledBlink(self.LedMapping[ledId])
                else:
                    self.ledControl.ledOff(self.LedMapping[ledId])
                ledId += 1
            self.ledControl.ledOff(self.BusyLed)
            if self.run:
                time.sleep(3)
        for i in range(0, 16):
            self.ledControl.ledOff(i)

    def stop(self):
        self.run = False
        
