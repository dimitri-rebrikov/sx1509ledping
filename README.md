# sx1509ledping
Shows the ping status of several IP's on a SX1509 based LED panel

## How to use
1. solder the SX1509 based LED panel with 16 LED's. The LED shall be connected using the "sink current" variant. See the "Typical LED Connection" chapter in the SX1509 spec. 
1. install smbus python package (python3)
1. rename the Config.py.tmplate file into Config.py and fill it with the addresses you like to observe
1. start "python3 Main.py"