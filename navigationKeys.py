import tkinter
from keyPressed import keyPressed


buttonFont = ("Arial", 10, "bold")


def createNavigationPad(panel):

    px=11
    py=21

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    insertBtn = tkinter.Button(panel, text='Insert',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    insertBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    insertBtn.grid(row=0, column=0, ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    homeBtn = tkinter.Button(panel, text='Home',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    homeBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    homeBtn.grid(row=0, column=1,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    pageUpBtn = tkinter.Button(panel, text='Page\nUp',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    pageUpBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    pageUpBtn.grid(row=0, column=2,  ipadx=px, ipady=py-8)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    deleteBtn = tkinter.Button(panel, text='Delete',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    deleteBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    deleteBtn.grid(row=1, column=0,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    endBtn = tkinter.Button(panel, text='End',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    endBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    endBtn.grid(row=1, column=1,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    pageDownBtn = tkinter.Button(panel, text='Page\nDown',anchor="nw", width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    pageDownBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    pageDownBtn.grid(row=1, column=2,  ipadx=px, ipady=py-8)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    tkinter.Label(panel,text="",width=0,height=4,background='gray27',border=0).grid(row=2,columnspan=3,column=1)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    upBtn = tkinter.Button(panel, text='↑', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    upBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    upBtn.grid(row=3, column=1,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    downDownBtn = tkinter.Button(panel, text='↓', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    downDownBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    downDownBtn.grid(row=4, column=1,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    leftDownBtn = tkinter.Button(panel, text='←', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    leftDownBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    leftDownBtn.grid(row=4, column=0,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    rightDownBtn = tkinter.Button(panel, text='→', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    rightDownBtn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    rightDownBtn.grid(row=4, column=2,  ipadx=px, ipady=py)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
