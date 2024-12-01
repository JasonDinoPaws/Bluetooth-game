from tkinter import *
import threading
from PIL import Image, ImageTk
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
    if len(saved) > 0:
        saved[len(saved)-1].config(text=saved[len(saved)-1].cget("text")[:-1])

    lav = Label(window,font="Segoe 15",background="#000000",fg="#ffffff",justify="left")
    saved.append(lav)
    lav.pack(pady=5,padx=10, anchor="w")

def Line(settext="",nl = False):
    global window,saved

    saved[len(saved)-1].config(text=settext+"|")

    if nl:
        newLine()

    if len(saved) > 20:
        saved[0].destroy()
        saved.pop(0)

    window.update()

def Simage(image:PhotoImage):
    global window,saved

    saved[len(saved)-1].config(img = image)
    newLine()


thr = threading.Thread(target=start)
thr.start()

while window == None:
    pass
newLine()