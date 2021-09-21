import tkinter
from tkinter import ttk
from tkinter import font

# * Window Setup

window = tkinter.Tk()

window.title('On Screen Num-Pad')
winHeight = 560
winWidth = 420
window.geometry(f'{winHeight}x{winWidth}')
window.maxsize(width=winWidth, height=winHeight)
window.minsize(width=winWidth, height=winHeight)

# * Style Setup

style = ttk.Style()
window.configure(bg='gray27')
style.configure('TButton', background='gray21')
style.configure('TButton', foreground='white')
# ! Display font
_buttonFont = ("Arial", 20, "bold")
_sysKeyFont=("Arial", 8, "bold")
# * Display Setup

inputNum = tkinter.StringVar(window, "")
display = ttk.Entry(window, state='readonly', textvariable=inputNum)
display.grid(rowspan=1, columnspan=4, ipadx=127, ipady=30)


def keyPressed(key):
    pass


def createSysBtns():
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    copyBtn = tkinter.Button(window, text='Copy', width=10,
                         command=lambda: keyPressed('copy'),font=_sysKeyFont)
    copyBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    copyBtn.grid(row=1, column=0, ipadx=0, ipady=0,padx=5,pady=0)

    pasteBtn = tkinter.Button(window, text='Paste', width=10,
                         command=lambda: keyPressed('copy'),font=_sysKeyFont)
    pasteBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    pasteBtn.grid(row=1, column=1, ipadx=0, ipady=0,padx=5,pady=0)

    clearBtn = tkinter.Button(window, text='Clear', width=10,
                         command=lambda: keyPressed('copy'),font=_sysKeyFont)
    clearBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    clearBtn.grid(row=1, column=2, ipadx=0, ipady=0,padx=5,pady=0)

    backspaceBtn = tkinter.Button(window, text='⌫', width=10,
                         command=lambda: keyPressed('copy'),font=_sysKeyFont)
    backspaceBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    backspaceBtn.grid(row=1, column=3, ipadx=0, ipady=0,padx=5,pady=0)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def createButtons():
    createSysBtns()
    pad=6
    #
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    numLock = tkinter.Button(window, text='⇭', width=4,
                         command=lambda: keyPressed('nl'),font=_buttonFont)
    numLock.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    numLock.grid(row=2, column=0, ipadx=0, ipady=14,padx=pad,pady=pad)

    divBtn = tkinter.Button(window, text='/', width=4,
                        command=lambda: keyPressed('/'),font=_buttonFont)
    divBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    divBtn.grid(row=2, column=1, ipadx=0, ipady=14,padx=pad,pady=pad)

    mulBtn = tkinter.Button(window, text='*', width=4,
                        command=lambda: keyPressed('*'),font=_buttonFont)
    mulBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    mulBtn.grid(row=2, column=2, ipadx=0, ipady=14,padx=pad,pady=pad)

    subBtn = tkinter.Button(window, text='-', width=4,
                        command=lambda: keyPressed('-'),font=_buttonFont)
    subBtn.configure(background='gray21',highlightbackground='gray27',foreground="white",highlightcolor="gray27")
    subBtn.grid(row=2, column=3, ipadx=0, ipady=14,padx=pad,pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    numLock = ttk.Button(window,text='7', width=6,
                         command=lambda: keyPressed('nl'),padding=6)
    numLock.grid(row=3, column=0, ipadx=10, ipady=20,padx=pad,pady=pad)

    divBtn = ttk.Button(window, text='8', width=6,
                        command=lambda: keyPressed('/'),padding=6)
    divBtn.grid(row=3, column=1, ipadx=10, ipady=20,padx=pad,pady=pad)

    mulBtn = ttk.Button(window, text='9', width=6,
                        command=lambda: keyPressed('*'),padding=6)
    mulBtn.grid(row=3, column=2, ipadx=10, ipady=20,padx=pad,pady=pad)

    subBtn = ttk.Button(window, text='+', width=6,
                        command=lambda: keyPressed('-'),padding=6)
    subBtn.grid(row=3, column=3,rowspan=2, ipadx=10, ipady=64,padx=pad,pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    numLock = ttk.Button(window, text='4', width=6,
                         command=lambda: keyPressed('nl'),padding=6)
    numLock.grid(row=4, column=0, ipadx=10, ipady=20,padx=pad,pady=pad)

    divBtn = ttk.Button(window, text='5', width=6,
                        command=lambda: keyPressed('/'),padding=6)
    divBtn.grid(row=4, column=1, ipadx=10, ipady=20,padx=pad,pady=pad)

    mulBtn = ttk.Button(window, text='6', width=6,
                        command=lambda: keyPressed('*'),padding=6)
    mulBtn.grid(row=4, column=2, ipadx=10, ipady=20,padx=pad,pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    numLock = ttk.Button(window, text='1', width=6,
                         command=lambda: keyPressed('nl'),padding=6)
    numLock.grid(row=5, column=0, ipadx=10, ipady=20,padx=pad,pady=pad)

    divBtn = ttk.Button(window, text='2', width=6,
                        command=lambda: keyPressed('/'),padding=6)
    divBtn.grid(row=5, column=1, ipadx=10, ipady=20,padx=pad,pady=pad)

    mulBtn = ttk.Button(window, text='3', width=6,
                        command=lambda: keyPressed('*'),padding=6)
    mulBtn.grid(row=5, column=2, ipadx=10, ipady=20,padx=pad,pady=pad)

    subBtn = ttk.Button(window, text='E', width=6,
                        command=lambda: keyPressed('-'),padding=6)
    subBtn.grid(row=5, column=3,rowspan=2, ipadx=10, ipady=64,padx=pad,pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    numLock = ttk.Button(window, text='0', width=6,
                         command=lambda: keyPressed('nl'),padding=6)
    numLock.grid(row=6, column=0,columnspan=2, ipadx=64, ipady=20,padx=pad,pady=pad)

    mulBtn = ttk.Button(window, text='.', width=6,
                        command=lambda: keyPressed('*'),padding=6)
    mulBtn.grid(row=6, column=2, ipadx=10, ipady=20,padx=pad,pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    window.mainloop()


createButtons()
