import cv2
import pytesseract
from icecream import ic
import numpy as np
import pydobot
from serial.tools import list_ports
from time import sleep, time

#list available port
available_ports = list_ports.comports()

#select port
port = available_ports[0].device

#connect to dobot
device = pydobot.Dobot(port=port, verbose=True)


#move dobot to home position
def go_home():
    device.move_to(194.25,121.771,101.414,32.08, wait=True)

#move dobot to get box
def go_get_box():
    device.move_to(150.245,56.614,15.043,20.644, wait=True)
    device.suck(True)

#drop package at a position
def go_a_position():
    device.move_to(261.33,105.57,66.89,2.0, wait=True)
    device.suck(False)

#drop package at b position
def go_b_position():
    device.move_to(210.187,180.527,50.092,40.661, wait=True)
    device.suck(False)

#make rgb image to grayscale
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#connect to camera
cap = cv2.VideoCapture(0)

go_home()

#get time
prev_time = int(time())

#while connect to camera
while cap.isOpened():

    #read image from camera
    success, frame = cap.read()

    #if read image success
    if success:

        #convert image to grayscale
        gray = get_grayscale(frame[350:440,300:400])

        #ocr processes
        d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

        #show current image
        cv2.imshow("Camera", gray)

        #check if detect lar in list that ocr processes
        is_large = any("lar" in s.lower() for s in d["text"])
        #check if detect sma in list that ocr processes
        is_small = any("sma" in s.lower() for s in d["text"])

        #get current time
        current_time = int(time())

        #show output in console
        ic(current_time)
        ic(is_large)
        ic(is_small)
        ic("-----------------------")

        #check previous time pass 5 second
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

#disconnect camera
cap.release()

#close image window
cv2.destroyAllWindows()
