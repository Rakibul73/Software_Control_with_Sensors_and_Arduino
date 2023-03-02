import time
from pymata4 import pymata4
import os
import subprocess
from pynput.keyboard import Key, Controller
keyboard = Controller()



trigpin = 11       # trigger pin no
ecopin = 12        # echo pin no
gggg = 0

board = pymata4.Pymata4()

def the_callback(data):
    global gggg
    
    print("distance: ", data[2])    # data list has 4 index, we need only distance which stores in data[2] index
    if data[2] < 10 and gggg == 0:  # if distance 10 , then execute 
        gggg = 1
        os.startfile("C:\\Users\\spry-shanto\\Desktop\\testing.xlsx") # opens a excel file with given path
    elif gggg == 1 and data[2] > 10:
        keyboard.press(Key.ctrl)         # press ctrl+s 
        keyboard.press('s')              # press ctrl+s 
        keyboard.release('s')            # press ctrl+s 
        keyboard.release(Key.ctrl)       # press ctrl+s 
        subprocess.call("TASKKILL /F /IM EXCEL.EXE", shell=True)  #kills the excel.exe forcefully
        gggg = 0


# def the_callback(data):
#     print("distance: ", data[2] , " ", data[0] , " " , data[1] , "\n" , date)
#     if data[2] < 10:
        
#         os.startfile("D:\\Mine\\Anime_Online_Site_List.txt")
#     else:
#         subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)


board.set_pin_mode_sonar(trigpin, ecopin, the_callback)
while True:
    try:
        time.sleep(0.1)
        board.sonar_read(trigpin)
    except:
        board.shutdown()