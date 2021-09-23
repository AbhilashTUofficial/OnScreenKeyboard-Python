import tkinter
from keyPressed import keyPressed


buttonFont = ("Arial", 16, "bold")


def createFunctionPad(panel):


    # * Create layers



    section1=tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    section1.grid(row=0, column=0, pady=10, padx=10,sticky="W")

    section2=tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    section2.grid(row=0, column=1, pady=10, padx=10,sticky="W")

    section3=tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    section3.grid(row=0, column=2, pady=10, padx=10,sticky="W")

    section4=tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    section4.grid(row=0, column=3, pady=10, padx=10,sticky="W")

    section5=tkinter.LabelFrame(panel, padx=0, pady=0,background='gray27',border=0)
    section5.grid(row=0, column=4, pady=10, padx=10,sticky="W")

    px=4#4
    py=4#16

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!! Section 1 !!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    btnEsc = tkinter.Button(section1, text='Esc',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnEsc.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnEsc.grid(row=0, column=1, ipadx=px, ipady=py+12,padx=36)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!! Section 2 !!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnF1 = tkinter.Button(section2, text='F1',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF1.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF1.grid(row=0, column=0, ipadx=px, ipady=py+12)

    btnF2 = tkinter.Button(section2, text='F2',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF2.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF2.grid(row=0, column=1, ipadx=px, ipady=py+12)

    btnF3 = tkinter.Button(section2, text='F3',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF3.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF3.grid(row=0, column=2, ipadx=px, ipady=py+12)

    btnF4 = tkinter.Button(section2, text='F4',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF4.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF4.grid(row=0, column=3, ipadx=px, ipady=py+12)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!! Section 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnF5 = tkinter.Button(section3, text='F5',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF5.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF5.grid(row=0, column=0, ipadx=px, ipady=py+12)

    btnF6 = tkinter.Button(section3, text='F6',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF6.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF6.grid(row=0, column=1, ipadx=px, ipady=py+12)

    btnF7 = tkinter.Button(section3, text='F7',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF7.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF7.grid(row=0, column=2, ipadx=px, ipady=py+12)

    btnF8 = tkinter.Button(section3, text='F8',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF8.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF8.grid(row=0, column=3, ipadx=px, ipady=py+12)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!! Section 4 !!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnF9 = tkinter.Button(section4, text='F9',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF9.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF9.grid(row=0, column=0, ipadx=px, ipady=py+12)

    btnF10 = tkinter.Button(section4, text='F10',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF10.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF10.grid(row=0, column=1, ipadx=px, ipady=py+12)

    btnF11 = tkinter.Button(section4, text='F11',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF11.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF11.grid(row=0, column=2, ipadx=px, ipady=py+12)

    btnF12 = tkinter.Button(section4, text='F12',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    btnF12.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnF12.grid(row=0, column=3, ipadx=px, ipady=py+12)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!! Section 5 !!!!!!!!!!!!!!!!!!!!!!!!!!!

    btnPS = tkinter.Button(section5, text='Print\nScreen',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=("Arial", 10, "bold"))
    btnPS.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnPS.grid(row=0, column=0,  ipadx=px+8, ipady=py+8)

    btnSL = tkinter.Button(section5, text='Scroll\nLock',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=("Arial", 10, "bold"))
    btnSL.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnSL.grid(row=0, column=1,  ipadx=px+8, ipady=py+8)

    btnPB = tkinter.Button(section5, text='Pause\nBreak',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=("Arial", 10, "bold"))
    btnPB.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    btnPB.grid(row=0, column=2,  ipadx=px+8, ipady=py+8)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!