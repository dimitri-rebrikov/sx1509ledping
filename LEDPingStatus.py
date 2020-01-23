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
        15, 14, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1
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
                ok = os.system("ping -c 1 -w 5 " + pingTarget.pingAddress + " > /dev/null")
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
        
