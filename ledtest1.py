import SX1509
import time

addr = 0x3e
sx = SX1509.SX1509(addr)
# reset the device
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
# set tON
sx.write(sx.RegTOn0, 0b00001111)
# set tOff
sx.write(sx.RegOff0, 0b01111000)
# turn on all leds
sx.write(sx.RegDataA, 0b00000000)
sx.write(sx.RegDataB, 0b00000000)
time.sleep(5)
# stop blinking
sx.write(sx.RegTOn0, 0b00000000);
time.sleep(5)
# turn off all leds
sx.write(sx.RegDataA, 0b11111111)
sx.write(sx.RegDataB, 0b11111111)





