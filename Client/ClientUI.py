from tkinter import *

window = Tk()
window.configure()
window.wm_attributes('-transparentcolor','#000000')
window.attributes("-fullscreen",True)
window.wm_title("Game")

c = Canvas(window,width=window.winfo_screenwidth(),bg='#000000',height=window.winfo_screenheight(),borderwidth=0,highlightthickness=0)
c.pack()

Cx = window.winfo_screenwidth()/2
Cy = window.winfo_screenheight()/2

def Connect():
    c.create_rectangle(Cx-50,Cy-50,Cx+50,Cy+50,fill="grey56", outline="")

try:
    while window.winfo_exists():
        
        window.update()

except (EOFError,KeyboardInterrupt):
    window.destroy()