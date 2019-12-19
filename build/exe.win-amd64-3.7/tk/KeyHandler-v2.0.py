import pynput.keyboard
import tkinter as tk
#from tkinter import *

keyCount = 0

def process_key_press(key):
    
    global keyCount
    keyCount += 1
    num.set(keyCount)
    
    

ventana = tk.Tk()
num = tk.IntVar(value=keyCount)

ventana.title("KeyHandler")
ventana.geometry('200x175') #AnchoXAlto
ventana.configure(background = 'snow')
etiqueta = tk.Label(ventana, textvariable = num, bg = "snow", fg = "black", font = ("Times 22 bold"))
etiqueta.pack(padx = 61, pady = 66)



keyboard_listener = pynput.keyboard.Listener(on_press = process_key_press)


#2 threads at same time
with keyboard_listener:
    while ventana.mainloop():
        keyboard_listener.join()
    

   
    
 

