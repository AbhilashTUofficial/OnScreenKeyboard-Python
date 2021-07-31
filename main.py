# * Window Setup

from onScreenKeyboard import onScreenKeyboard
import tkinter
from tkinter import ttk
from tkinter import font


window = tkinter.Tk()

window.title('On Screen Num-Pad')
unit = 76
winHeight = unit*7
winWidth = unit*23
window.geometry(f'{winHeight}x{winWidth}')
window.maxsize(width=winWidth, height=winHeight)
window.minsize(width=winWidth, height=winHeight)

# * Style Setup

style = ttk.Style()
window.configure(bg='gray27')
style.configure('TButton', background='gray21')
style.configure('TButton', foreground='white')
_displayFont = ("Arial", 16, "bold")

# * Display Setup

input = tkinter.StringVar(window, "")
display = tkinter.Entry(window, state='readonly',
                        textvariable=input, font=_displayFont)
display.grid(rowspan=1, columnspan=99, ipadx=900, ipady=34)


# * Num Pad
numPad = tkinter.LabelFrame(window, padx=10, pady=10)
numPad.grid(row=1, column=3, pady=10, padx=10)

# * Nav Pad
navPad = tkinter.LabelFrame(window, padx=10, pady=10)
navPad.grid(row=1, column=2, pady=10, padx=10)

onScreenKeyboard(numPad,navPad)
