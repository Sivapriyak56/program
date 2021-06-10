import tkinter
from tkinter import *
import pandas as pd
from tkinter import filedialog
import os
from plyer import notification
import time
import schedule



def file():
    fn = filedialog.askopenfilename(initialdir="C:/", title="select file", filetypes=(("xlsx files",".xlsx"),("all files", "*.*")))
    print(fn)
    for f in fn:
        os.system(r'C:\Users\user\Desktop\excel.xlsx\Book1.xlsx')
        os.close(fd=0)


def notification_ok(message):
    notification.notify(message=message, title="rmd",timeout=30)
    time.sleep(60)


root = tkinter.Tk()
root.title("your reminder")
root.configure(bg="yellow")
root.geometry("220x220")

def ok():
    fl =[]
    ok_label = Label(root,text="done",bg="violet").place(x=108, y=180)
    print(ok_label)
    file = pd.read_excel(r'C:\Users\user\Desktop\excel.xlsx\Book1.xlsx')
    for f in file:
        fl.append(f)
        message = f
        notification_ok(message)
    print(fl)


def reminder():
    file = pd.read_excel(r'C:\Users\user\Desktop\excel.xlsx\Book1.xlsx')
    print(file)
    remind_lbl = Label(root,text=file).place(x=70, y=200)
    return remind_lbl




file_btn = Button(root, text="file", bg ="blue",command=file).place(x=108, y=50)
ok_btn = Button(root, text='ok', bg="green",command=ok).place(x=110, y= 90)
reminder_btn = Button(root, text="remind",bg="red",command=reminder).place(x=100, y=140)


root.mainloop()





 



