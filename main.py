import cv2
import pytesseract
from icecream import ic
import numpy as np
import pydobot
from serial.tools import list_ports
from time import sleep, time

available_ports = list_ports.comports()

port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=True)

def go_home():
    device.move_to(194.25,121.771,101.414,32.08, wait=True)

def go_get_box():
    device.move_to(150.245,56.614,15.043,20.644, wait=True)
    device.suck(True)

def go_a_position():
    device.move_to(261.33,105.57,66.89,2.0, wait=True)
    device.suck(False)

def go_b_position():
    device.move_to(210.187,180.527,50.092,40.661, wait=True)
    device.suck(False)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cap = cv2.VideoCapture(0)

go_home()

prev_time = int(time())

while cap.isOpened():
    # go_home()
    success, frame = cap.read()

    if success:
        gray = get_grayscale(frame[350:440,300:400])
        # gray = get_grayscale(frame)
        
        d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        
        cv2.imshow("Camera", gray)
        
        is_large = any("lar" in s.lower() for s in d["text"])
        is_small = any("sma" in s.lower() for s in d["text"])
        
        current_time = int(time())
        
        ic(current_time)
        ic(is_large)
        ic(is_small)
        ic("-----------------------")
        
        if current_time-prev_time > 5:
            if is_large:
                ic("Large")
                go_get_box()
                go_b_position()
                go_home()
                prev_time = int(time())
        
            elif is_small:
                ic("Small")
                go_get_box()
                go_a_position()
                go_home()
                prev_time = int(time())
    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()
