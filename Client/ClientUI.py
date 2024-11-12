from tkinter import *

root = Tk()
root.configure()
root.attributes('-alpha',0)
root.attributes("-fullscreen",True)
root.wm_title("event")

Can = Canvas(root,width=root.winfo_screenwidth(),height=root.winfo_screenheight(),background="#000000", bd = 0.5, highlightthickness=0,)
Can.pack()

def Connect():
    Can.config(bd=)
    root.attributes('-alpha',1)

Connect()
try:
    while root.winfo_exists():
        root.update()

except (EOFError,KeyboardInterrupt):
    pass

root.destroy()