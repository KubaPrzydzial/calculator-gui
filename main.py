import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title('Calculator')

expression = ""


def button_press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def press_equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

    except:
        equation.set("error")
        expression=""


def clear():
    global expression
    expression = ""
    equation.set("")


def widget():
    entry_window = Entry(window, font = 'Arial 22', textvariable=equation).grid(columnspan=4)
    b_clear = Button(window, text='C', width=22, height=4, bg='red', command=clear).grid(row=1, columnspan=2)
    b_pow = Button(window, text='POW', width=10, height=4, command=lambda: button_press("**")).grid(row=1, column=2)
    b_div = Button(window, text='/', width=10, height=4, command=lambda: button_press("/")).grid(row=1,column=3)

    b_seven = Button(window, text='7', width=10, height=4, command=lambda: button_press(7)).grid(row=2)
    b_eight = Button(window, text='8', width=10, height=4, command=lambda: button_press(8)).grid(row=2, column=1)
    b_nine = Button(window, text='9', width=10, height=4, command=lambda: button_press(9)).grid(row=2, column=2)
    b_multiply = Button(window, text='X', width=10, height=4, command=lambda: button_press("*")).grid(row=2, column=3)

    b_four = Button(window, text='4', width=10, height=4, command=lambda: button_press(4)).grid(row=3)
    b_five = Button(window, text='5', width=10, height=4, command=lambda: button_press(5)).grid(row=3, column=1)
    b_six = Button(window, text='6', width=10, height=4, command=lambda: button_press(6)).grid(row=3, column=2)
    b_substract= Button(window, text='-', width=10, height=4, command=lambda: button_press("-")).grid(row=3, column=3)

    b_one = Button(window, text='1', width=10, height=4, command=lambda: button_press(1)).grid(row=4)
    b_two = Button(window, text='2', width=10, height=4, command=lambda: button_press(2)).grid(row=4, column=1)
    b_three = Button(window, text='3', width=10, height=4, command=lambda: button_press(3)).grid(row=4, column=2)
    b_add = Button(window, text='+', width=10, height=4, command=lambda: button_press("+")).grid(row=4, column=3)

    b_zero = Button(window, text='0', width=10, height=4, command=lambda: button_press(0)).grid(row=5)
    b_zero = Button(window, text='.', width=10, height=4, command=lambda: button_press(".")).grid(row=5, column=1)
    b_equation = Button(window, text='=',width=22, height=4, bg='green', command=press_equal).grid(row=5, column=2, columnspan=2)

equation = StringVar()

widget()

window.geometry('328x500')
window.resizable(False, False)
window.mainloop()