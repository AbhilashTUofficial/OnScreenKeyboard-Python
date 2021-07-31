import tkinter
from keyPressed import keyPressed


buttonFont = ("Arial", 20, "bold")


def createNavigationPad(panel):
    
    numLock = tkinter.Button(panel, text='⇭', width=3,
                             command=lambda: keyPressed('nl'), font=buttonFont)
    numLock.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
    numLock.grid(row=2, column=0, ipadx=0, ipady=14)

    divBtn = tkinter.Button(panel, text='/', width=3,
                            command=lambda: keyPressed('/'), font=buttonFont)
    divBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    divBtn.grid(row=2, column=1, ipadx=0, ipady=14)

    mulBtn = tkinter.Button(panel, text='*', width=3,
                            command=lambda: keyPressed('*'), font=buttonFont)
    mulBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    mulBtn.grid(row=2, column=2, ipadx=0, ipady=14)

    subBtn = tkinter.Button(panel, text='-', width=3,
                            command=lambda: keyPressed('-'), font=buttonFont)
    subBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    subBtn.grid(row=2, column=3, ipadx=0, ipady=14)

    panel.mainloop()