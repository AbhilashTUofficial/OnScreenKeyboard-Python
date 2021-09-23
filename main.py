# * Window Setup
from functionKeys import createFunctionPad
from alphanumericKeys import createAlphanumericPad
from threading import Thread, ThreadError
from navigationKeys import createNavigationPad
from numericKeys import createNumericPad
import tkinter
from tkinter import ttk
from tkinter import font


window = tkinter.Tk()

window.title('OnScreen Keyboard')
unit = 76
winHeight = unit*7
winWidth = unit*22
window.geometry(f'{winHeight}x{winWidth}')
window.maxsize(width=winWidth, height=winHeight)
window.minsize(width=winWidth, height=winHeight)

# * Style Setup

style = ttk.Style()
window.configure(bg='gray27')
style.configure('TButton', background='gray21')
style.configure('TButton', foreground='white')
_displayFont = ("Arial", 16, "bold")

# # * Display Setup

# input = tkinter.StringVar(window, "")
# display = tkinter.Entry(window, state='readonly',
#                         textvariable=input, font=_displayFont)
# display.grid(rowspan=1, columnspan=99, ipadx=900, ipady=34)


# * Num Pad
numPad = tkinter.LabelFrame(window, padx=0, pady=0,background='gray27',border=0)
numPad.grid(row=1, column=3, pady=10, padx=10)

# * Nav Pad
navPad = tkinter.LabelFrame(window, padx=0, pady=0,background='gray27',border=0)
navPad.grid(row=1, column=2, pady=10, padx=10)

# * Alpha Pad
alphaPad = tkinter.LabelFrame(window, padx=0, pady=0,background='gray27',border=0)
alphaPad.grid(row=1, column=1, pady=10, padx=10)

# * Func Pad
funcPad = tkinter.LabelFrame(window, padx=0, pady=0,background='gray27',border=0)
funcPad.grid(row=0, column=0,columnspan=6, pady=10, padx=10,sticky="W")

def onScreenKeyboard(numPad,navPad,alphaPad):

    Thread(target=createNumericPad(numPad)).start()
    Thread(target=createNavigationPad(navPad)).start()
    Thread(target=createAlphanumericPad(alphaPad)).start()
    Thread(target=createFunctionPad(funcPad)).start()
    window.mainloop()

onScreenKeyboard(numPad,navPad,alphaPad)
