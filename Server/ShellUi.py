from tkinter import *
import threading
saved = []
window:Tk = None

def start():
    global window,saved
    root = Tk()
    root.configure(background="#000000")
    root.wm_title("Shell")
    xSize = root.winfo_screenwidth()
    ySize = root.winfo_screenheight()

    window = root
    root.mainloop()

def newLine():
    global window, saved
    lav = Label(window,font="Segoe 15",background="#000000",fg="#ffffff",justify="left")
    saved.append(lav)
    lav.pack(pady=5,padx=10, anchor="w")

def Line(settext="",nl = False):
    global window,saved

    saved[len(saved)-1].config(text=settext)

    if nl:
        newLine()

    if len(saved) > 20:
        saved[0].destroy()
        saved.pop(0)

    window.update()

thr = threading.Thread(target=start)
thr.start()

while window == None:
    pass
newLine()