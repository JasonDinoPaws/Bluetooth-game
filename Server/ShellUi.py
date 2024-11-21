from tkinter import *
import threading
saved = []
window:Tk = None
Can:Canvas = None

def start():
    global window,Can
    root = Tk()
    root.configure()
    root.wm_title("Shell")
    xSize = root.winfo_screenwidth()/2.5
    ySize = root.winfo_screenheight()/3

    c = Canvas(root,width=xSize,bg='#000000',height=ySize,borderwidth=0,highlightthickness=0)
    c.pack()

    window = root
    Can = c
    root.mainloop()

def textupdate(text):
    global window,Can
    Can.delete("all")
    if len(text) == 0:
        saved.append("")
    else:
        saved[len(saved)-1] = text
    
    if len(saved) > 10:
        saved.pop(0)

    for i in range(len(text)):
        Can.create(2,i*15,text=saved[i],font="Segoe 15")
    window.update()

thr = threading.Thread(target=start)
thr.start()