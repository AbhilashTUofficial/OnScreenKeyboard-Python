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
_buttonFont = ("Arial", 20, "bold")
_sysKeyFont = ("Arial", 8, "bold")
_displayFont = ("Arial", 16, "bold")

# * Display Setup

input = tkinter.StringVar(window, "")
display = tkinter.Entry(window, state='readonly',
                        textvariable=input, font=_displayFont)
display.grid(rowspan=1, columnspan=5, ipadx=90, ipady=34)


def keyPressed(key):
    if(key == "nl"):
        pass
    elif(key == "e"):

        input.set("\n")
    else:
        val = display.get()+str(key)
        input.set(val)


def createSysBtns():
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    copyBtn = tkinter.Button(window, text='Copy', width=10,
                             command=lambda: keyPressed('copy'), font=_sysKeyFont)
    copyBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    copyBtn.grid(row=1, column=0, ipadx=0, ipady=0, padx=5, pady=0)

    pasteBtn = tkinter.Button(window, text='Paste', width=10,
                              command=lambda: keyPressed('copy'), font=_sysKeyFont)
    pasteBtn.configure(background='gray21', highlightbackground='gray27',
                       foreground="white", highlightcolor="gray27")
    pasteBtn.grid(row=1, column=1, ipadx=0, ipady=0, padx=5, pady=0)

    clearBtn = tkinter.Button(window, text='Clear', width=10,
                              command=lambda: keyPressed('copy'), font=_sysKeyFont)
    clearBtn.configure(background='gray21', highlightbackground='gray27',
                       foreground="white", highlightcolor="gray27")
    clearBtn.grid(row=1, column=2, ipadx=0, ipady=0, padx=5, pady=0)

    backspaceBtn = tkinter.Button(window, text='⌫', width=10,
                                  command=lambda: keyPressed('copy'), font=_sysKeyFont)
    backspaceBtn.configure(background='gray21', highlightbackground='gray27',
                           foreground="white", highlightcolor="gray27")
    backspaceBtn.grid(row=1, column=3, ipadx=0, ipady=0, padx=5, pady=0)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def createButtons():
    createSysBtns()
    pad = 6
    #
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    numLock = tkinter.Button(window, text='⇭', width=4,
                             command=lambda: keyPressed('nl'), font=_buttonFont)
    numLock.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    numLock.grid(row=2, column=0, ipadx=0, ipady=14, padx=pad, pady=pad)

    divBtn = tkinter.Button(window, text='/', width=4,
                            command=lambda: keyPressed('/'), font=_buttonFont)
    divBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    divBtn.grid(row=2, column=1, ipadx=0, ipady=14, padx=pad, pady=pad)

    mulBtn = tkinter.Button(window, text='*', width=4,
                            command=lambda: keyPressed('*'), font=_buttonFont)
    mulBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    mulBtn.grid(row=2, column=2, ipadx=0, ipady=14, padx=pad, pady=pad)

    subBtn = tkinter.Button(window, text='-', width=4,
                            command=lambda: keyPressed('-'), font=_buttonFont)
    subBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    subBtn.grid(row=2, column=3, ipadx=0, ipady=14, padx=pad, pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num7 = tkinter.Button(window, text='7', width=4,
                          command=lambda: keyPressed('7'), font=_buttonFont)
    num7.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num7.grid(row=3, column=0, ipadx=0, ipady=14, padx=pad, pady=pad)

    num8 = tkinter.Button(window, text='8', width=4,
                          command=lambda: keyPressed('8'), font=_buttonFont)
    num8.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num8.grid(row=3, column=1, ipadx=0, ipady=14, padx=pad, pady=pad)

    num9 = tkinter.Button(window, text='9', width=4,
                          command=lambda: keyPressed('9'), font=_buttonFont)
    num9.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num9.grid(row=3, column=2, ipadx=0, ipady=14, padx=pad, pady=pad)

    addBtn = tkinter.Button(window, text='+', width=4,
                            command=lambda: keyPressed('+'), font=_buttonFont)
    addBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    addBtn.grid(row=3, column=3, rowspan=2, ipadx=0,
                ipady=56, padx=pad, pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num4 = tkinter.Button(window, text='4', width=4,
                          command=lambda: keyPressed('4'), font=_buttonFont)
    num4.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num4.grid(row=4, column=0, ipadx=0, ipady=14, padx=pad, pady=pad)

    num5 = tkinter.Button(window, text='5', width=4,
                          command=lambda: keyPressed('5'), font=_buttonFont)
    num5.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num5.grid(row=4, column=1, ipadx=0, ipady=14, padx=pad, pady=pad)

    num6 = tkinter.Button(window, text='6', width=4,
                          command=lambda: keyPressed('6'), font=_buttonFont)
    num6.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num6.grid(row=4, column=2, ipadx=0, ipady=14, padx=pad, pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num1 = tkinter.Button(window, text='1', width=4,
                          command=lambda: keyPressed('1'), font=_buttonFont)
    num1.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num1.grid(row=5, column=0, ipadx=0, ipady=14, padx=pad, pady=pad)

    num2 = tkinter.Button(window, text='2', width=4,
                          command=lambda: keyPressed('2'), font=_buttonFont)
    num2.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num2.grid(row=5, column=1, ipadx=0, ipady=14, padx=pad, pady=pad)

    num3 = tkinter.Button(window, text='3', width=4,
                          command=lambda: keyPressed('3'), font=_buttonFont)
    num3.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num3.grid(row=5, column=2, ipadx=0, ipady=14, padx=pad, pady=pad)

    enterBtn = tkinter.Button(window, text='E', width=4,
                              command=lambda: keyPressed('e'), font=_buttonFont)
    enterBtn.configure(background='gray21', highlightbackground='gray27',
                       foreground="white", highlightcolor="gray27")
    enterBtn.grid(row=5, column=3, rowspan=2, ipadx=0,
                  ipady=56, padx=pad, pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num0 = tkinter.Button(window, text='0', width=4,
                          command=lambda: keyPressed('0'), font=_buttonFont)
    num0.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num0.grid(row=6, column=0, columnspan=2,
              ipadx=52, ipady=14, padx=pad, pady=pad)

    pointBtn = tkinter.Button(window, text='.', width=4,
                              command=lambda: keyPressed('.'), font=_buttonFont)
    pointBtn.configure(background='gray21', highlightbackground='gray27',
                       foreground="white", highlightcolor="gray27")
    pointBtn.grid(row=6, column=2, ipadx=0, ipady=14, padx=pad, pady=pad)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    window.mainloop()


createButtons()
