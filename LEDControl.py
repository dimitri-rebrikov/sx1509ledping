class LEDControl:
    from SX1509 import SX1509

    def __init__(self, sx: SX1509):
        self.sx = sx
        # reset 
        sx.write(sx.RegReset, 0x12)
        sx.write(sx.RegReset, 0x34)
        # disable input
        sx.write(sx.RegInputDisableA, 0b11111111) 
        sx.write(sx.RegInputDisableB, 0b11111111) 
        # disable pull up
        sx.write(sx.RegPullUpA, 0b00000000)
        sx.write(sx.RegPullUpB, 0b00000000)
        # enable drain
        sx.write(sx.RegOpenDrainA, 0b11111111)
        sx.write(sx.RegOpenDrainB, 0b11111111)
        # register all pins to output
        sx.write(sx.RegDirA, 0b00000000)
        sx.write(sx.RegDirB, 0b00000000)
        # enable internal oscillator
        sx.write(sx.RegClock, 0b01000000)
        # define frequency
        sx.write(sx.RegMisc, 0b00110000)
        # enable led driver for all pins
        sx.write(sx.RegLEDDriverEnableA, 0b11111111)
        sx.write(sx.RegLEDDriverEnableB, 0b11111111)
        # turn off all leds
        sx.write(sx.RegDataA, 0b11111111)
        sx.write(sx.RegDataB, 0b11111111)

    def led(self, id: int, on: bool):
        reg = self.sx.RegDataA
        shift = id
        if(shift > 7):
            shift = shift - 8
            reg = self.sx.RegDataB
        if(on):
            self.sx.write(reg, self.sx.read(reg) & ~ 1 << shift)
        else:
            self.sx.write(reg, self.sx.read(reg) | 1 << shift)

    def ledOn(self, id: int):
        led(self, id, True)             

    def ledOff(id: int):
        led(self, id, False)

    def ledBlink(id: int):
        print(id)
    