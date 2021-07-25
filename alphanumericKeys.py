import tkinter
from keyPressed import keyPressed



buttonFont = ("Arial", 16, "bold")


def createAlphanumericPad(panel):
    
    # * Create layers

    layerOne = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerOne.grid(row=1, column=0, pady=0, padx=0,sticky="W")

    layerTwo = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerTwo.grid(row=2, column=0, pady=0, padx=0)

    layerThree = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerThree.grid(row=3, column=0, pady=0, padx=0)

    layerFour = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerFour.grid(row=4, column=0, pady=0, padx=0)

    layerFive = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerFive.grid(row=5, column=0, pady=0, padx=0)

    px=4
    py=16

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer One !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnBacktick = tkinter.Button(layerOne, text='`', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnBacktick.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBacktick.grid(row=0, column=0, ipadx=px, ipady=py)

    btn1 = tkinter.Button(layerOne, text='1', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn1.grid(row=0, column=1, ipadx=px, ipady=py)

    btn2 = tkinter.Button(layerOne, text='2', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn2.grid(row=0, column=2, ipadx=px, ipady=py)

    btn3 = tkinter.Button(layerOne, text='3', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn3.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn3.grid(row=0, column=3, ipadx=px, ipady=py)

    btn4 = tkinter.Button(layerOne, text='4', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn4.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn4.grid(row=0, column=4, ipadx=px, ipady=py)

    btn5 = tkinter.Button(layerOne, text='5', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn5.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn5.grid(row=0, column=5, ipadx=px, ipady=py)

    btn6 = tkinter.Button(layerOne, text='6', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn6.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn6.grid(row=0, column=6, ipadx=px, ipady=py)

    btn7 = tkinter.Button(layerOne, text='7', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn7.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn7.grid(row=0, column=7, ipadx=px, ipady=py)

    btn8 = tkinter.Button(layerOne, text='8', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn8.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn8.grid(row=0, column=8, ipadx=px, ipady=py)

    btn9 = tkinter.Button(layerOne, text='9', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn9.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn9.grid(row=0, column=9, ipadx=px, ipady=py)

    btn0 = tkinter.Button(layerOne, text='0', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn0.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn0.grid(row=0, column=10, ipadx=px, ipady=py)

    btnDiv = tkinter.Button(layerOne, text='-', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnDiv.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnDiv.grid(row=0, column=11, ipadx=px, ipady=py)

    btnEqual = tkinter.Button(layerOne, text='=', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnEqual.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnEqual.grid(row=0, column=12, ipadx=px, ipady=py)
    
    btnBackspace = tkinter.Button(layerOne, text='Backspace', width=8,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnBackspace.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBackspace.grid(row=0, column=12, ipadx=px, ipady=py)  

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Two !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnTab = tkinter.Button(layerTwo, text='Tab', width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnTab.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnTab.grid(row=0, column=0, ipadx=px, ipady=py)

    btnQ = tkinter.Button(layerTwo, text='Q', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnQ.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnQ.grid(row=0, column=1, ipadx=px, ipady=py)

    btnW = tkinter.Button(layerTwo, text='W', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnW.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnW.grid(row=0, column=2, ipadx=px, ipady=py)

    btnE = tkinter.Button(layerTwo, text='E', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnE.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnE.grid(row=0, column=3, ipadx=px, ipady=py)

    btnR = tkinter.Button(layerTwo, text='R', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnR.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnR.grid(row=0, column=4, ipadx=px, ipady=py)

    btnT = tkinter.Button(layerTwo, text='T', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnT.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnT.grid(row=0, column=5, ipadx=px, ipady=py)

    btnY = tkinter.Button(layerTwo, text='Y', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnY.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnY.grid(row=0, column=6, ipadx=px, ipady=py)

    btnU = tkinter.Button(layerTwo, text='U', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnU.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnU.grid(row=0, column=7, ipadx=px, ipady=py)

    btnI = tkinter.Button(layerTwo, text='I', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnI.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnI.grid(row=0, column=8, ipadx=px, ipady=py)

    btnO = tkinter.Button(layerTwo, text='O', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnO.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnO.grid(row=0, column=9, ipadx=px, ipady=py)

    btnP = tkinter.Button(layerTwo, text='P', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnP.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnP.grid(row=0, column=10, ipadx=px, ipady=py)

    btnOpenSqrBr = tkinter.Button(layerTwo, text='[', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnOpenSqrBr.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnOpenSqrBr.grid(row=0, column=11, ipadx=px, ipady=py)

    btnCloseSqrBr = tkinter.Button(layerTwo, text=']', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnCloseSqrBr.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnCloseSqrBr.grid(row=0, column=12, ipadx=px, ipady=py)

    btnBackSlash = tkinter.Button(layerTwo, text='\\', width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnBackSlash.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBackSlash.grid(row=0, column=13, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Three !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnA = tkinter.Button(layerThree, text='A', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnA.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnA.grid(row=0, column=0, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Four !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnZ = tkinter.Button(layerFour, text='Z', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnZ.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnZ.grid(row=0, column=0, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Five !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnStart = tkinter.Button(layerFive, text='⊞', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnStart.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnStart.grid(row=0, column=0, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!