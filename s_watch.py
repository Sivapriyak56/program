from tkinter import *
from tkinter.ttk import *

sc = 0
mn = 0
h = 0
stp = 0


def start():
    global sc, mn, h
    sc = sc + 1
    if sc == 60:
        mn = mn + 1
        sc = 0
    if mn == 60:
        h = h + 1
        mn = 0
    if stp == 0:
        lbl = Label(root, text='%i:%i:%i' % (h, mn, sc), font=("arial", 30, "bold"))
        lbl.after(300, start)
        lbl.place(x=50, y=30)


def stop():
    global stp
    stp = 1


root = Tk()

root.title("stop_watch")
root.geometry("210*160")
root.configure(bg='black')
root.resizable(False, False)

start = Button(root, text='start', command=start).place(x=10, y=100)
stop = Button(root, text='stop', command=stop).place(x=110, y=100)

root.mainloop()

