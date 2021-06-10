import time
from tkinter import *

top = Tk()

top.title("DIGITAL CLOCK")

def digital():
    dtime = time.strftime('%H:%M:%S')
    clock.config(text = dtime)
    clock.after(100,digital)

clock = Label(top,font=("time",100,"bold"),bg="green")
clock.grid()
digital()
top.mainloop()