import pynput.keyboard

#from tkinter import *
keyCount = 0

def process_key_press(key):
    
    global keyCount 
    keyCount +=1
    print(keyCount)




keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    keyboard_listener.join()
    
    
 

