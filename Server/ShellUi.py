from tkinter import *
import threading
saved = [""]
obj = []
window:Tk = None

def start():
    global window
    root = Tk()
    root.configure(background="#000000")
    root.wm_title("Shell")
    xSize = root.winfo_screenwidth()
    ySize = root.winfo_screenheight()

    window = root
    root.mainloop()

def textupdate(text=""):
    global window
    for i in obj:
        i.destroy()

    if len(text) == 0:
        saved.append("")
    else:
        saved[len(saved)-1] = text
    
    if len(saved) > 10:
        saved.pop(0)

    for t in saved:
        lav = Label(window,text=t,font="Segoe 15",anchor="ne")
        obj.append(lav)
        lav.pack(pady=window.winfo_height()*.005)
    window.update()

thr = threading.Thread(target=start)
thr.start()