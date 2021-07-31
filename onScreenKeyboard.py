from navigationKeys import createNavigationPad
from numericKeys import createNumericPad
from threading import Thread, ThreadError

import tkinter

def onScreenKeyboard(numPad,navPad):

    Thread(target=createNumericPad(numPad)).start()
    Thread(target=createNavigationPad(navPad)).start()
