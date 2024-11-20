from tkinter import *
import threading
Start = False

window = Tk()
window.configure()
window.attributes("-fullscreen",True)
window.wm_title("Game")
xSize = window.winfo_screenwidth()
ySize = window.winfo_screenheight()

c = Canvas(window,width=xSize,bg='#000000',height=ySize,borderwidth=0,highlightthickness=0)
c.pack()

exit = Button(window,text="X",background="red",command=lambda: window.destroy())
exit.place(width=.025*xSize,height=.05*ySize,x=5,y=5)

def viewcleints(clients=[]):
    c.delete("all")

    x1 = .1*xSize
    x2 = xSize-x1
    y1 = .05*ySize
    y2 = .1*ySize

    for _,add,hn,alo in clients:
        c.create_rectangle(x1,y1,x2,y2,fill="gray")
        c.create_text(x1+(.01*xSize),(y1+y2)/2,text=hn,anchor="w",font= 'Segoe 15')
        c.create_text((x2+x1)/2,(y1+y2)/2,text=add[0],anchor="center",font= 'Segoe 15')
        c.create_text(x2-(.01*xSize),(y1+y2)/2,text=alo,anchor="e",font= 'Segoe 15')
        y1 += y2/1.5
        y2 += y2/1.5

    window.update()