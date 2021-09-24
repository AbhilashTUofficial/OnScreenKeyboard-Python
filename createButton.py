
from tkinter import font
from keyPressed import keyPressed
import tkinter


def createButton(panel, r, c, type, context, key):
    global px
    global py
    global buttonFont
    global w
    global cs
    global rs

    btn = tkinter.Button()

    if(type == 0):  # ! Empty key space.

        tkinter.Label(panel, text="", width=8, height=4, background='gray27',
                      border=0, padx=6).grid(row=r, columnspan=3, column=c)

    else:

        btn = tkinter.Button(panel, text=context, anchor="nw",
                             command=lambda: keyPressed(key),)

        if(type == 1):  # ! Square key, single char notation on top left corner.

            #! Keys: / * - 7 8 9 4 5 6 1 2 3 . up down left right q w e r t y u i o
            #!       p a s d f g h j k l z x c v b n m

            px = 4
            py = 16
            buttonFont = ("Arial", 16, "bold")
            w = 3
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, columnspan=cs,
                     rowspan=rs, ipadx=px, ipady=py)

        # ! Elongated to left, single char notation on top left corner.
        elif(type == 1.2):

            #! Keys: 0

            px = 4
            py = 16
            buttonFont = ("Arial", 16, "bold")
            w = 9
            cs = 2
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, columnspan=2, ipadx=px, ipady=py)

        # ! Elongated to bottom, char notation on top left corner.
        elif(type == 1.3):

            #! Keys: en +

            px = 4
            py = 16
            buttonFont = ("Arial", 12, "bold")
            w = 4
            cs = 1
            rs = 2

            btn.configure(width=w,height=5,font=buttonFont)
            btn.grid(row=r, column=c, rowspan=2, ipadx=px,
                     ipady=py)

        elif(type == 2):  # ! Square key, double char notation on top left corner.

            #! Keys: ~` !1 @2 #3 $4 %5 ^6 &7 *8 (9 )0 _- += {[ ]} :; "' <, >. ?

            px = 8
            py = 10
            buttonFont = ("Arial", 12, "bold")
            w = 3
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        # ! Width 6 key, double char notation on top left corner.
        elif(type == 2.2):

            #! Keys: |\

            px = 8
            py = 10
            buttonFont = ("Arial", 12, "bold")
            w = 6
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        # ! Width 7 key, double string notation on top left corner.
        elif(type == 2.3):

            #! Keys: tab crl(L)

            px = 8
            py = 10
            buttonFont = ("Arial", 12, "bold")
            w = 7
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        elif(type == 3):  # ! Square key, string notation on top left corner.

            #! Keys: nl ist home pup del end pdown esc f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 prtsrc scrllock pb

            px = 4
            py = 12
            buttonFont = ("Arial", 10, "bold")
            w = 5
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        elif(type == 3.1):  # ! Width 5 key, string notation on top left corner.

            #! Keys: start crl alt opt

            px = 8
            py = 10
            buttonFont = ("Arial", 12, "bold")
            w = 5
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        elif(type == 3.2):  # ! Width 9 key, string notation on top left corner.

            #! Keys: caplock

            px = 8
            py = 9
            buttonFont = ("Arial", 12, "bold")
            w = 9
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        elif(type == 3.3):  # ! Width 8 key, string notation on top left corner.

            #! Keys: en(L)

            px = 8
            py = 9
            buttonFont = ("Arial", 12, "bold")
            w = 12
            cs = 1
            rs = 1

            btn.configure(width=w,font=buttonFont)
            btn.grid(row=r, column=c, ipadx=px, ipady=py)

        btn.configure(background='gray21', highlightbackground='gray27',
                      foreground="white", highlightcolor="gray27")
