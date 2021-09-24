from createButton import createButton
import tkinter

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
    
    createButton(section1,0,0,3,"Esc\n","esc")
    createButton(section1,0,1,0,"","")
    createButton(section2,0,0,3,"F1\n","f1")
    createButton(section2,0,1,3,"F2\n","f2")
    createButton(section2,0,2,3,"F3\n","f3")
    createButton(section2,0,3,3,"F4\n","f4")
    createButton(section3,0,0,3,"F5\n","f5")
    createButton(section3,0,1,3,"F6\n","f6")
    createButton(section3,0,2,3,"F7\n","f7")
    createButton(section3,0,3,3,"F8\n","f8")
    createButton(section4,0,0,3,"F9\n","f9")
    createButton(section4,0,1,3,"F10\n","f10")
    createButton(section4,0,2,3,"F11\n","f11")
    createButton(section4,0,3,3,"F12\n","f12")
    createButton(section5,0,0,3,"Print\nScreen","prtsrc")
    createButton(section5,0,1,3,"Scroll\nLock","srllock")
    createButton(section5,0,2,3,"Pause\nBreak","pb")