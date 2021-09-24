import tkinter


# from pyautogui import press, typewrite, hotkey
# press('a')
#         # typewrite('quick brown fox')
#         # hotkey('ctrl', 'w')

# ! Key Pressed function


def keyPressed(key):
    if(key == 'a'):
        print("A pressed")


def createButton(panel, r, c, context, key, font, pad, size, span):
    btn = tkinter.Button(panel, text=context, anchor="nw", width=size[0], height=size[1],
                         command=lambda: keyPressed(key), font=font)
    btn.configure(background='gray21', highlightbackground='gray27',
                  foreground="white", highlightcolor="gray27")
    btn.grid(row=r, column=c,
             ipadx=pad[0], ipady=pad[1], rowspan=span[0], columnspan=span[1])


