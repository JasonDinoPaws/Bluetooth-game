from tkinter import *
start = False

window = Tk()
window.configure()
window.attributes("-fullscreen",True)
window.wm_title("Game")
xSize = window.winfo_screenwidth()
ySize = window.winfo_screenheight()

c = Canvas(window,width=xSize,bg='#000000',height=ySize,borderwidth=0,highlightthickness=0)
c.pack()

def viewcleints(clients):
    window.update()
    c.delete("all")

    x1 = .1*xSize
    x2 = xSize-x1
    y1 = .05*ySize
    y2 = .15*ySize
    for _,add,hn,alo in clients:
        c.create_rectangle(x1,y1,x2,y2,fill="gray")
        c.create_text(x1+(.01*xSize),y1,text=hn,anchor="nw")
        c.create_text(x2+(.01*xSize),y1,text="addr",anchor="ne")
    window.update()
