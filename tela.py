#!/usr/bin/env python3
#from tkinter import *
import tkinter as tk
import serial
import os
import time

green="green"
thisdir = "~/Desktop/workplace/scholar/PROGRAMACAO/arduino/servo_GUI"
def reload():
	#os.system('killall ./sbuffer.sh')
	#print("parei ./sbuferf")
	os.system('./reload.sh')
	#Time.sleep(10)
	#os.system('./sbuffer.py')

def loop():
	f=open("status","r")
	line=f.readline()
	f.close()
	if line=="ok":
		f=open("buffer","r")
		_angle ="current: "+f.readline().replace('\n','º')
		lab1.config(text=_angle)
		lab2.config(bg=green)
		f.close()

	root.after(50,loop)



def send():
    print(ent1.get())
    try:
    	ser = serial.Serial('/dev/ttyACM0',9600)
    	ser.write(ent1.get().encode("utf_8"))
    	ser.close()
    except:
    	ser = serial.Serial('/dev/ttyACM1',9600)
    	ser.write(ent1.get().encode("utf_8"))
    	ser.close()
    #f=open("buffer","r")
    #_angle ="current angle: "+f.readline()+"º"
    #lab1.text=_angle
    #f.close()



root =tk.Tk()

lab1=tk.Label(text="current")
lab1.grid(column=0,row=1,sticky = "nsew")


lab2 = tk.Label(root, bg="red")
lab2.grid(column=0,row=0,sticky = "nsew")

ent1 = tk.Entry(root)
ent1.grid(column=0,row=2,sticky = "nsew")

but1 = tk.Button(root , width=50, text="atualizar", command=send)
but1.grid(column=0,row=3,sticky = "nsew")

butload=tk.Button(root , text="reaload" ,command=reload)
butload.grid(column=0,row=4,sticky = "nsew")

loop()
tk.mainloop()
#global root 

#class tela:
#     def __init__(self, root):
#        self.root     = Tk()
#        self.setButtons()
#    
#     def setButtons(self):
#        but1 = Button(self.root , text="red")
#        but1.grid(column=0,row=1)
#
#       but2 = Button(self.root , text="y")
#        but2.grid(column=0,row=2)
#
#        but3 = Button(self.root , text="g")
#        but3.grid(column=0,row=2)
