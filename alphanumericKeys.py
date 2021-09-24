from createButton import createButton
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

    createButton(layerOne,0,0,2,"~\n`","`")
    createButton(layerOne,0,1,2,"!\n1","!1")
    createButton(layerOne,0,2,2,"@\n2","@2")
    createButton(layerOne,0,3,2,"#\n3","#3")
    createButton(layerOne,0,4,2,"$\n4","$4")
    createButton(layerOne,0,5,2,"%\n5","%5")
    createButton(layerOne,0,6,2,"^\n6","^6")
    createButton(layerOne,0,7,2,"&\n7","&7")
    createButton(layerOne,0,8,2,"*\n8","*8")
    createButton(layerOne,0,9,2,"(\n9","(9")
    createButton(layerOne,0,10,2,")\n0",")0")
    createButton(layerOne,0,11,2,"_\n-","`_-")
    createButton(layerOne,0,12,2,"+\n=","+=")
    
    btnBackspace = tkinter.Button(layerOne, text='Backspace',anchor="nw", width=12,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnBackspace.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnBackspace.grid(row=0, column=13, ipadx=px, ipady=py+15)  

    createButton(layerTwo,0,0,2.3,"Tab\n","tab")
    createButton(layerTwo,0,1,1,"Q","q")
    createButton(layerTwo,0,2,1,"W","w")
    createButton(layerTwo,0,3,1,"E","e")
    createButton(layerTwo,0,4,1,"R","r")
    createButton(layerTwo,0,5,1,"T","t")
    createButton(layerTwo,0,6,1,"Y","y")
    createButton(layerTwo,0,7,1,"U","u")
    createButton(layerTwo,0,8,1,"I","i")
    createButton(layerTwo,0,9,1,"O","o")
    createButton(layerTwo,0,10,1,"P","p")
    createButton(layerTwo,0,11,2,"{\n[","{[")
    createButton(layerTwo,0,12,2,"}\n","}]")
    createButton(layerTwo,0,13,2.2,"|\n\\","|\\")

    createButton(layerThree,0,0,3.2,"Caps\nLock","caplock")
    createButton(layerThree,0,1,1,"A","a")
    createButton(layerThree,0,2,1,"S","s")
    createButton(layerThree,0,3,1,"D","d")
    createButton(layerThree,0,4,1,"F","f")
    createButton(layerThree,0,5,1,"G","g")
    createButton(layerThree,0,6,1,"H","h")
    createButton(layerThree,0,7,1,"J","j")
    createButton(layerThree,0,8,1,"K","k")
    createButton(layerThree,0,9,1,"L","l")
    createButton(layerThree,0,10,2,":\n;",":;")
    createButton(layerThree,0,11,2,"\"\n\'","\"\'")
    createButton(layerThree,0,12,3.3,"Enter \n","en")

    btnShift1 = tkinter.Button(layerFour, text='Shift',anchor="nw", width=13,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnShift1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnShift1.grid(row=0, column=0, ipadx=px, ipady=19)

    createButton(layerFour,0,1,1,"Z","z")
    createButton(layerFour,0,2,1,"X","x")
    createButton(layerFour,0,3,1,"C","c")
    createButton(layerFour,0,4,1,"V","v")
    createButton(layerFour,0,5,1,"B","b")
    createButton(layerFour,0,6,1,"N","n")
    createButton(layerFour,0,7,1,"M","m")
    createButton(layerFour,0,8,2,"<\n,","<,")
    createButton(layerFour,0,9,2,">\n.",">.")
    createButton(layerFour,0,10,2,"?\n/","?/")

    btnShift2 = tkinter.Button(layerFour, text='Shift',anchor="nw", width=18,
                             command=lambda: keyPressed('nl'), font=("Arial",12,"bold"))
    btnShift2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnShift2.grid(row=0, column=11, ipadx=4, ipady=19)

    createButton(layerFive,0,0,2.3,"Ctrl\n","crl")
    createButton(layerFive,0,1,3.1,"⊞\n","start")
    createButton(layerFive,0,2,3.1,"Alt\n","alt")
    createButton(layerFive,0,4,3.1,"Alt\n","alt")
    createButton(layerFive,0,5,3.1,"⊞\n","start")
    createButton(layerFive,0,6,3.1,"☰\n","opt")
    createButton(layerFive,0,7,3.1,"Ctrl\n","crl")

    btnSpace = tkinter.Button(layerFive, text=' ',anchor="nw", width=32,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnSpace.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnSpace.grid(row=0, column=3, ipadx=8, ipady=16)
