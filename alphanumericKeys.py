import tkinter
from keyPressed import keyPressed



buttonFont = ("Arial", 16, "bold")


def createAlphanumericPad(panel):
    
    # * Create layers

    layerOne = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerOne.grid(row=1, column=0, pady=0, padx=0,sticky="W")

    layerTwo = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerTwo.grid(row=2, column=0, pady=0, padx=0,sticky="W")

    layerThree = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerThree.grid(row=3, column=0, pady=0, padx=0,sticky="W")

    layerFour = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerFour.grid(row=4, column=0, pady=0, padx=0,sticky="W")

    layerFive = tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    layerFive.grid(row=5, column=0, pady=0, padx=0,sticky="W")

    px=4#4
    py=4#16

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer One !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnBacktick = tkinter.Button(layerOne, text='~\n`',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnBacktick.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBacktick.grid(row=0, column=0, ipadx=px, ipady=py)

    btn1 = tkinter.Button(layerOne, text='!\n1',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn1.grid(row=0, column=1, ipadx=px, ipady=py)

    btn2 = tkinter.Button(layerOne, text='@\n2',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn2.grid(row=0, column=2, ipadx=px, ipady=py)

    btn3 = tkinter.Button(layerOne, text='#\n3',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn3.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn3.grid(row=0, column=3, ipadx=px, ipady=py)

    btn4 = tkinter.Button(layerOne, text='$\n4',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn4.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn4.grid(row=0, column=4, ipadx=px, ipady=py)

    btn5 = tkinter.Button(layerOne, text='%\n5',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn5.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn5.grid(row=0, column=5, ipadx=px, ipady=py)

    btn6 = tkinter.Button(layerOne, text='^\n6',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn6.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn6.grid(row=0, column=6, ipadx=px, ipady=py)

    btn7 = tkinter.Button(layerOne, text='&\n7',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn7.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn7.grid(row=0, column=7, ipadx=px, ipady=py)

    btn8 = tkinter.Button(layerOne, text='*\n8',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn8.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn8.grid(row=0, column=8, ipadx=px, ipady=py)

    btn9 = tkinter.Button(layerOne, text='(\n9',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn9.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn9.grid(row=0, column=9, ipadx=px, ipady=py)

    btn0 = tkinter.Button(layerOne, text=')\n0',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btn0.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btn0.grid(row=0, column=10, ipadx=px, ipady=py)

    btnDiv = tkinter.Button(layerOne, text='_\n-',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnDiv.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnDiv.grid(row=0, column=11, ipadx=px, ipady=py)

    btnEqual = tkinter.Button(layerOne, text='+\n=',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnEqual.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnEqual.grid(row=0, column=12, ipadx=px, ipady=py)
    
    btnBackspace = tkinter.Button(layerOne, text='Backspace',anchor="nw", width=12,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnBackspace.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBackspace.grid(row=0, column=13, ipadx=px, ipady=py+15)  

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Two !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnTab = tkinter.Button(layerTwo, text='Tab',anchor="nw", width=6,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnTab.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnTab.grid(row=0, column=0, ipadx=px, ipady=py+12)

    btnQ = tkinter.Button(layerTwo, text='Q',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnQ.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnQ.grid(row=0, column=1, ipadx=px, ipady=py+12)

    btnW = tkinter.Button(layerTwo, text='W',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnW.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnW.grid(row=0, column=2, ipadx=px, ipady=py+12)

    btnE = tkinter.Button(layerTwo, text='E',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnE.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnE.grid(row=0, column=3, ipadx=px, ipady=py+12)

    btnR = tkinter.Button(layerTwo, text='R',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnR.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnR.grid(row=0, column=4, ipadx=px, ipady=py+12)

    btnT = tkinter.Button(layerTwo, text='T',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnT.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnT.grid(row=0, column=5, ipadx=px, ipady=py+12)

    btnY = tkinter.Button(layerTwo, text='Y',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnY.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnY.grid(row=0, column=6, ipadx=px, ipady=py+12)

    btnU = tkinter.Button(layerTwo, text='U',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnU.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnU.grid(row=0, column=7, ipadx=px, ipady=py+12)

    btnI = tkinter.Button(layerTwo, text='I',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnI.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnI.grid(row=0, column=8, ipadx=px, ipady=py+12)

    btnO = tkinter.Button(layerTwo, text='O',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnO.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnO.grid(row=0, column=9, ipadx=px, ipady=py+12)

    btnP = tkinter.Button(layerTwo, text='P',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnP.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnP.grid(row=0, column=10, ipadx=px, ipady=py+12)

    btnOpenSqrBr = tkinter.Button(layerTwo, text='{\n[',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnOpenSqrBr.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnOpenSqrBr.grid(row=0, column=11, ipadx=px, ipady=py)

    btnCloseSqrBr = tkinter.Button(layerTwo, text='}\n]',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnCloseSqrBr.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnCloseSqrBr.grid(row=0, column=12, ipadx=px, ipady=py)

    btnBackSlash = tkinter.Button(layerTwo, text='|\n\\',anchor="nw", width=6,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnBackSlash.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBackSlash.grid(row=0, column=13, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Three !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnCapsLock = tkinter.Button(layerThree, text='Caps\nLock',anchor="nw", width=10,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnCapsLock.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnCapsLock.grid(row=0, column=0, ipadx=px, ipady=py+5)

    btnA = tkinter.Button(layerThree, text='A',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnA.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnA.grid(row=0, column=1, ipadx=px, ipady=py+12)
    
    btnS = tkinter.Button(layerThree, text='S',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnS.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnS.grid(row=0, column=2, ipadx=px, ipady=py+12)

    btnD = tkinter.Button(layerThree, text='D',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnD.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnD.grid(row=0, column=3, ipadx=px, ipady=py+12)

    btnF = tkinter.Button(layerThree, text='F',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF.grid(row=0, column=4, ipadx=px, ipady=py+12)

    btnG = tkinter.Button(layerThree, text='G',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnG.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnG.grid(row=0, column=5, ipadx=px, ipady=py+12)

    btnH = tkinter.Button(layerThree, text='H',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnH.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnH.grid(row=0, column=6, ipadx=px, ipady=py+12)

    btnJ = tkinter.Button(layerThree, text='J',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnJ.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnJ.grid(row=0, column=7, ipadx=px, ipady=py+12)

    btnK = tkinter.Button(layerThree, text='K',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnK.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnK.grid(row=0, column=8, ipadx=px, ipady=py+12)

    btnL = tkinter.Button(layerThree, text='L',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnL.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnL.grid(row=0, column=9, ipadx=px, ipady=py+12)
    
    btnSemiCol = tkinter.Button(layerThree, text=':\n;',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnSemiCol.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnSemiCol.grid(row=0, column=10, ipadx=px, ipady=py)

    btnQuotes = tkinter.Button(layerThree, text="\"\n\'",anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnQuotes.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnQuotes.grid(row=0, column=11, ipadx=px, ipady=py)

    btnEnter = tkinter.Button(layerThree, text='Enter',anchor="nw", width=14,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnEnter.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnEnter.grid(row=0, column=12, ipadx=px, ipady=py+15)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Four !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnShift1 = tkinter.Button(layerFour, text='Shift',anchor="nw", width=14,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnShift1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnShift1.grid(row=0, column=0, ipadx=px, ipady=py+15)

    btnZ = tkinter.Button(layerFour, text='Z',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnZ.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnZ.grid(row=0, column=1, ipadx=px, ipady=py+12)

    btnX = tkinter.Button(layerFour, text='X',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnX.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnX.grid(row=0, column=2, ipadx=px, ipady=py+12)

    btnC = tkinter.Button(layerFour, text='C',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnC.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnC.grid(row=0, column=3, ipadx=px, ipady=py+12)

    btnV = tkinter.Button(layerFour, text='V',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnV.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnV.grid(row=0, column=4, ipadx=px, ipady=py+12)

    btnB = tkinter.Button(layerFour, text='B',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnB.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnB.grid(row=0, column=5, ipadx=px, ipady=py+12)

    btnN = tkinter.Button(layerFour, text='N',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnN.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnN.grid(row=0, column=6, ipadx=px, ipady=py+12)

    btnM = tkinter.Button(layerFour, text='M',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnM.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnM.grid(row=0, column=7, ipadx=px, ipady=py+12)

    btnComma = tkinter.Button(layerFour, text="<\n,",anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnComma.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnComma.grid(row=0, column=8, ipadx=px, ipady=py)

    btnDot = tkinter.Button(layerFour, text=">\n.",anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnDot.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnDot.grid(row=0, column=9, ipadx=px, ipady=py)

    btnForwardSlash = tkinter.Button(layerFour, text="?\n/",anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnForwardSlash.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnForwardSlash.grid(row=0, column=10, ipadx=px, ipady=py)

    btnShift2 = tkinter.Button(layerFour, text='Shift',anchor="nw", width=18,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnShift2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnShift2.grid(row=0, column=11, ipadx=px, ipady=py+15)


    # !!!!!!!!!!!!!!!!!!!!!!!!!!! Layer Five !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnCrl1 = tkinter.Button(layerFive, text='Ctrl',anchor="nw", width=6,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnCrl1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnCrl1.grid(row=0, column=0, ipadx=px, ipady=py+12)

    btnStart1 = tkinter.Button(layerFive, text='⊞',anchor="nw", width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnStart1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnStart1.grid(row=0, column=1, ipadx=px+4, ipady=py+12)

    btnAlt1 = tkinter.Button(layerFive, text='Alt',anchor="nw", width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnAlt1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnAlt1.grid(row=0, column=2, ipadx=px+4, ipady=py+12)

    btnSpace = tkinter.Button(layerFive, text=' ',anchor="nw", width=32,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnSpace.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnSpace.grid(row=0, column=3, ipadx=px, ipady=py+12)

    btnAlt2 = tkinter.Button(layerFive, text='Alt',anchor="nw", width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnAlt2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnAlt2.grid(row=0, column=4, ipadx=px+4, ipady=py+12)

    btnStart2 = tkinter.Button(layerFive, text='⊞',anchor="nw", width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnStart2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnStart2.grid(row=0, column=5, ipadx=px+4, ipady=py+12)

    btnOption = tkinter.Button(layerFive, text='☰',anchor="nw", width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnOption.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnOption.grid(row=0, column=6, ipadx=px+4, ipady=py+12)

    btnCrl2 = tkinter.Button(layerFive, text='Ctrl',anchor="nw", width=4,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnCrl2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnCrl2.grid(row=0, column=7, ipadx=px+4, ipady=py+12)


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!