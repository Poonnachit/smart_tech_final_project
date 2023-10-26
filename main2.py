import pydobot
from serial.tools import list_ports
from icecream import ic
from time import sleep

available_ports = list_ports.comports()
ic(available_ports)

port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=True)

def go_home():
    device.move_to(194.25,121.771,101.414,32.08, wait=True)

def go_get_box():
    device.move_to()

def go_a_position():
    device.move_to(261.33,105.57,66.89,22.0, wait=True)
while True:
    (x,y,z,r,j1,j2,j3,j4) = device.pose()
    ic(x,y,z,r)
    sleep(1)
    # go_home()
    # go_a_position()
