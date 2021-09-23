import tkinter
from keyPressed import keyPressed


buttonFont = ("Arial", 10, "bold")


def createFunctionPad(panel):


    # * Create layers

    layerOne = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerOne.grid(row=1, column=0, pady=0, padx=0,sticky="W")

    px=4#4
    py=4#16

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    btnBacktick = tkinter.Button(layerOne, text='~\n`',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnBacktick.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBacktick.grid(row=0, column=0, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!