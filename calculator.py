from tkinter import *


root = Tk()
root.title("CALCULATOR")


def btn_click(item):
    global exp
    exp = exp + str(item)
    input_text.set(exp)

def btn_clear():
    global exp
    exp = ""
    input_text.set("")


def btn_equel():
    global exp
    result = str(eval(exp))
    input_text.set(result)
    exp= ""

exp = ""
input_text = StringVar()

input_frame = Frame(root, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame,width=50,textvariable=input_text,justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btn_frame = Frame(root, width=312, height=272.5)
btn_frame.pack()

add = Button(btn_frame,text="+",cursor = "hand2",command = lambda :btn_click("+")).place(x=250,y=50)
sub = Button(btn_frame,text="-", cursor = "hand2",command = lambda :btn_click("-")).place(x=250,y=90)
mul = Button(btn_frame,text="*", cursor = "hand2",command =lambda :btn_click("*")).place(x=250,y=130)
div = Button(btn_frame,text="/",cursor = "hand2",command = lambda :btn_click("/")).place(x=250,y=170)
e_to = Button(btn_frame,text="=",cursor = "hand2",command=lambda:btn_equel()).place(x=250,y=210)
seven = Button(btn_frame,text="7",cursor = "hand2",command=lambda :btn_click(7)).place(x=10,y=50)
eight = Button(btn_frame,text="8",cursor = "hand2",command=lambda :btn_click(8)).place(x=80,y=50)
nine = Button(btn_frame,text="9",cursor = "hand2",command = lambda :btn_click(9)).place(x=150,y=50)
four = Button(btn_frame,text="4",cursor = "hand2",command=lambda :btn_click(4)).place(x=10,y=90)
five = Button(btn_frame,text="5",cursor = "hand2",command = lambda :btn_click(5)).place(x=80,y=90)
six = Button(btn_frame,text="6",cursor = "hand2",command = lambda :btn_click(6)).place(x=150,y=90)
three = Button(btn_frame,text="3",cursor = "hand2",command =lambda :btn_click(3) ).place(x=10,y=130)
two = Button(btn_frame,text="2",cursor = "hand2",command = lambda :btn_click(2)).place(x=80,y=130)
one = Button(btn_frame,text="1",cursor = "hand2",command = lambda :btn_click(1)).place(x=150,y=130)
zero = Button(btn_frame,text="0",cursor = "hand2",command = lambda :btn_click(0)).place(x=80,y=170)
clear = Button(btn_frame,text="c",cursor = "hand2",command = lambda :btn_clear()).place(x=150,y=170)
point = Button(btn_frame,text=".",cursor = "hand2",command = lambda :btn_click(".")).place(x=10,y=170)

root.mainloop()

# from tkinter import *
#
# win = Tk()  # This is to create a basic window
# win.geometry("312x324")  # this is for the size of the window
# win.resizable(0, 0)  # this is to prevent from resizing the window
# win.title("Calculator")
#
#
# ###################Starting with functions ####################
# # 'btn_click' function :
# # This Function continuously updates the
# # input field whenever you enters a number
#
# def btn_click(item):
#     global expression
#     expression = expression + str(item)
#     input_text.set(expression)
#
#
# # 'bt_clear' function :This is used to clear
# # the input field
#
# def bt_clear():
#     global expression
#     expression = ""
#     input_text.set("")
#
#
# # 'bt_equal':This method calculates the expression
# # present in input field
#
# def bt_equal():
#     global expression
#     result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
#     input_text.set(result)
#     expression = ""
#
#
# expression = ""
#
# # 'StringVar()' :It is used to get the instance of input field
#
# input_text = StringVar()
#
# # Let us creating a frame for the input field
#
# input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
#                     highlightthickness=2)
#
# input_frame.pack(side=TOP)
#
# # Let us create a input field inside the 'Frame'
#
# input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
#                     justify=RIGHT)
#
# input_field.grid(row=0, column=0)
#
# input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field
#
# # Let us creating another 'Frame' for the button below the 'input_frame'
#
# btns_frame = Frame(win, width=312, height=272.5, bg="grey")
#
# btns_frame.pack()
#
# # first row
#
# clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
#                command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
#
# divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                 command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
#
# # second row
#
# seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#                command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
#
# eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#                command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
#
# nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
#
# multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                   command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
#
# # third row
#
# four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
#
# five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
#
# six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#              command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
#
# minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
#
# # fourth row
#
# one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#              command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
#
# two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#              command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
#
# three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
#                command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
#
# plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#               command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
#
# # fourth row
#
# zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
#               command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
#
# point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
#
# equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
#                 command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)
#
# win.mainloop()