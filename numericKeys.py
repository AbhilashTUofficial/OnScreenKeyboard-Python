from keyPressed import keyPressed
import tkinter


buttonFont = ("Arial", 20, "bold")


def createNumericPad(panel):
    # * Create Numpad
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num7 = tkinter.Button(panel, text='7', width=3,
                          command=lambda: keyPressed('7'), font=buttonFont)
    num7.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num7.grid(row=3, column=0, ipadx=0, ipady=14)

    num8 = tkinter.Button(panel, text='8', width=3,
                          command=lambda: keyPressed('8'), font=buttonFont)
    num8.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num8.grid(row=3, column=1, ipadx=0, ipady=14)

    num9 = tkinter.Button(panel, text='9', width=3,
                          command=lambda: keyPressed('9'), font=buttonFont)
    num9.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num9.grid(row=3, column=2, ipadx=0, ipady=14)

    addBtn = tkinter.Button(panel, text='+', width=3,
                            command=lambda: keyPressed('+'), font=buttonFont)
    addBtn.configure(background='gray21', highlightbackground='gray27',
                     foreground="white", highlightcolor="gray27")
    addBtn.grid(row=3, column=3, rowspan=2, ipadx=0,
                ipady=50)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num4 = tkinter.Button(panel, text='4', width=3,
                          command=lambda: keyPressed('4'), font=buttonFont)
    num4.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num4.grid(row=4, column=0, ipadx=0, ipady=14)

    num5 = tkinter.Button(panel, text='5', width=3,
                          command=lambda: keyPressed('5'), font=buttonFont)
    num5.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num5.grid(row=4, column=1, ipadx=0, ipady=14)

    num6 = tkinter.Button(panel, text='6', width=3,
                          command=lambda: keyPressed('6'), font=buttonFont)
    num6.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num6.grid(row=4, column=2, ipadx=0, ipady=14)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num1 = tkinter.Button(panel, text='1', width=3,
                          command=lambda: keyPressed('1'), font=buttonFont)
    num1.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num1.grid(row=5, column=0, ipadx=0, ipady=14)

    num2 = tkinter.Button(panel, text='2', width=3,
                          command=lambda: keyPressed('2'), font=buttonFont)
    num2.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num2.grid(row=5, column=1, ipadx=0, ipady=14)

    num3 = tkinter.Button(panel, text='3', width=3,
                          command=lambda: keyPressed('3'), font=buttonFont)
    num3.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num3.grid(row=5, column=2, ipadx=0, ipady=14)

    enterBtn = tkinter.Button(panel, text='E', width=3,
                              command=lambda: keyPressed('e'), font=buttonFont)
    enterBtn.configure(background='gray21', highlightbackground='gray27',
                       foreground="white", highlightcolor="gray27")
    enterBtn.grid(row=5, column=3, rowspan=2, ipadx=0,
                  ipady=50)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    num0 = tkinter.Button(panel, text='0', width=3,
                          command=lambda: keyPressed('0'), font=buttonFont)
    num0.configure(background='gray21', highlightbackground='gray27',
                   foreground="white", highlightcolor="gray27")
    num0.grid(row=6, column=0, columnspan=2,
              ipadx=36, ipady=14)

    pointBtn = tkinter.Button(panel, text='.', width=3,
                              command=lambda: keyPressed('.'), font=buttonFont)
    pointBtn.configure(background='gray21', highlightbackground='gray27',
                       foreground="white", highlightcolor="gray27")
    pointBtn.grid(row=6, column=2, ipadx=0, ipady=14)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    panel.mainloop()