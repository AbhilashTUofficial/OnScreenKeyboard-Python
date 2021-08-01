import tkinter
from tkinter import ttk
from tkinter import font

# * Window Setup

window = tkinter.Tk()

window.title('On Screen Num-Pad')
winHeight = 600
winWidth = 1680
window.geometry(f'{winHeight}x{winWidth}')
window.maxsize(width=winWidth, height=winHeight)
window.minsize(width=winWidth, height=winHeight)

# * Style Setup

style = ttk.Style()
window.configure(bg='gray27')
style.configure('TButton', background='gray21')
style.configure('TButton', foreground='white')
# _buttonFont = ("Arial", 20, "bold")
# _sysKeyFont = ("Arial", 8, "bold")
_displayFont = ("Arial", 16, "bold")

# * Display Setup

input = tkinter.StringVar(window, "")
display = tkinter.Entry(window, state='readonly',
                        textvariable=input, font=_displayFont)
display.grid(rowspan=1, columnspan=99, ipadx=900, ipady=34)

window.mainloop()