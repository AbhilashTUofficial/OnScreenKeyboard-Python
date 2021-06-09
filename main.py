import tkinter

win=tkinter.Tk();
win_width=1000;
win_height=800;
result_display_width=800;
result_display_height=400;

def window_setup():
    win.attributes('-topmost',True);
    win.geometry("{}x{}".format(win_width,win_height));
    # win.eval('tk::PlaceWindow . center');
    canvas = tkinter.Canvas(win, bg = "darkgray", height = result_display_height, width = result_display_width);
    canvas.pack()
    win.mainloop();
    


window_setup();