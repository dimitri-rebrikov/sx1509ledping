class LEDControl:
    from SX1509 import SX1509
    
    
    def __init__(self, sx: SX1509):
        self.sx = sx
        self.init()

    def reset(self):
        self.sx.write(self.sx.RegReset, 0x12)
        self.sx.write(self.sx.RegReset, 0x34)

    def init(self):
        self.reset()
        # disable input
        self.sx.write(self.sx.RegInputDisableA, 0b11111111) 
        self.sx.write(self.sx.RegInputDisableB, 0b11111111) 
        # disable pull up
        self.sx.write(self.sx.RegPullUpA, 0b00000000)
        self.sx.write(self.sx.RegPullUpB, 0b00000000)
        # enable drain
        self.sx.write(self.sx.RegOpenDrainA, 0b11111111)
        self.sx.write(self.sx.RegOpenDrainB, 0b11111111)
        # register all pins to output
        self.sx.write(self.sx.RegDirA, 0b00000000)
        self.sx.write(self.sx.RegDirB, 0b00000000)
        # enable internal oscillator
        self.sx.write(self.sx.RegClock, 0b01000000)
        # define frequency
        self.sx.write(self.sx.RegMisc, 0b00110100)
        # enable led driver for all pins
        self.sx.write(self.sx.RegLEDDriverEnableA, 0b11111111)
        self.sx.write(self.sx.RegLEDDriverEnableB, 0b11111111)
        # turn off all leds
        self.sx.write(self.sx.RegDataA, 0b11111111)
        self.sx.write(self.sx.RegDataB, 0b11111111)

    def __led(self, id: int, on: bool):
        reg = self.sx.RegDataA
        shift = id
        if(shift > 7):
            shift = shift - 8
            reg = self.sx.RegDataB
        if(on):
            self.sx.write(reg, self.sx.read(reg) & ~ (1 << shift))
        else:
            self.sx.write(reg, self.sx.read(reg) | 1 << shift)

    def __blink(self, id: int, blink: bool):
        self.sx.write(self.sx.RegTOn[id], 0b00000111 if blink else 0b00000000)
        self.sx.write(self.sx.RegOff[id], 0b00111000 if blink else 0b00000000)

    def ledOn(self, id: int):
        self.__blink(id, False)
        self.__led(id, True)             

    def ledOff(self, id: int):
        self.__blink(id, False)
        self.__led(id, False)

    def ledBlink(self, id: int):
        self.__blink(id, True)
        self.__led(id, True)
