# Code to check if left or right mouse buttons were pressed 
import win32api
import pyautogui as pg
import time 

state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

lastPosition = None
rightmousedown = False

def RevertToLastPosition():
    if rightmousedown == False:
        return
    pg.moveTo(x=lastPosition.x, y=lastPosition.y)

while True: 
    b = win32api.GetKeyState(0x02) 
    
    if b != state_right:  # Button state changed 
        state_right = b 
        #print(b) 
        if b < 0: 
            rightmousedown = True
            lastPosition = pg.position(x=None,y=None)
            #print(lastPosition.x, lastPosition.y)
        else:
            RevertToLastPosition()
            rightmousedown = False
    time.sleep(0.001) 

Input("Press ENTER to Exit")