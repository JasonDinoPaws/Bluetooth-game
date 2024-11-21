from tkinter import *
from PIL import Image, ImageTk
from random import *

window:Tk = None

def CreateWindow(color = '#fcbd5d'):
    root = Tk()
    root.configure(background=color)
    root.wm_attributes('-transparentcolor','#fcbd5d')
    root.attributes("-fullscreen",True)
    root.wm_title("event")
    xSize = root.winfo_screenwidth()
    ySize = root.winfo_screenheight()
    
    Can = Canvas(root,width=xSize,height=ySize,background=color, highlightthickness=0)

    return root,Can,xSize,ySize

def Create_Button(root:Tk, Canvas:Canvas, x1,y1,x2,y2, Text="Hello", FontSize = '15',clicked = "<Button 1>"):
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    IsOver = (x >= x1 and x <= x2) and (y >= y1 and y <= y2)

    Canvas.create_rectangle(x1,y1,x2,y2,outline=IsOver and "White" or "gray",fill="")
    Canvas.create_text((x2+x1)/2, (y2+y1)/2,text=Text,font="Segoe "+FontSize,anchor="center",fill="White")



def Connect(device="Fsih"):
    global window
    root, Can, xSize, ySize = CreateWindow()
    window = root


    mess = StringVar()
    x1 = .37*xSize
    y1 = .3916*ySize
    x2 = xSize-x1
    y2 = ySize-y1
    Fysize = y2-y1
    Fxsize = x2-x1
    

    def press(de):
        mess.set(de)

    Can.create_rectangle(0,0,xSize,ySize,fill="#000000",stipple="gray50")
    Can.create_rectangle(x1,y1,x2,y2,fill="#2B2B2B", outline="")
    Can.create_rectangle(x1,y1+(.57264*Fysize),x2,y2,fill="#202020", outline="")

    Can.create_text(x1+(.03*Fxsize),y1+(.1709*Fysize),text=f"Allow {device} to connect to this device",font= 'Segoe 15',anchor="nw",fill="#ffffff")
    Can.create_text(x1+(.03*Fxsize),y1+(.37179*Fysize),text=f"This could cause harm to your device",font= 'Segoe 10',anchor="nw",fill="#ffffff")

    Can.pack() 
    yesf = LabelFrame(root,highlightcolor="#ffffff",highlightthickness = 2, bd=0,background="#2B2B2B")
    yesf.place(x=x1+(.07537*Fxsize),y=y2-(.320*Fysize),width=(.42211*Fxsize),height=(.2094*Fysize))
    yes = Button(yesf,text="Yes",font="Segoe 15",command=lambda: press("yes"),background="#FA9A45",highlightcolor="#FA9A45")
    yes.place(x=1,y=1,width=(.4070*Fxsize),height=(.1752*Fysize))

    nof = LabelFrame(root,highlightcolor="#ffffff",highlightthickness = 2, bd=0,background="#2B2B2B")
    nof.place(x=x2-(.4974*Fxsize),y=y2-(.320*Fysize),width=(.42211*Fxsize),height=(.2094*Fysize))
    no = Button(nof,text="No",font="Segoe 15",command=lambda: press("no"),background="#FA9A45",highlightcolor="#FA9A45")
    no.place(x=1,y=1,width=(.4070*Fxsize),height=(.1752*Fysize))

    while mess.get() not in ["yes","no"]:
        root.update()

    root.destroy()
    window = None
    return mess.get()

images = ["Lucky.png","melancholy.png","Wana.png","evil.jpg","linux.png","miuk.jpg","moast.png","nef.jpg","romain.jpg","youtube.png"]
sfx = ["Clown","Rick"]
def Virus():
    global window
    root, Can, xSize, ySize = CreateWindow("#000000")
    window = root

    if True:
        num = int(random()*len(images))
        imop = Image.open(images[num])
        img = ImageTk.PhotoImage(imop)
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
    else:
        num = int(random()*len(images))
        imop = Image.open(sfx[num]+".png")
        img = ImageTk.PhotoImage(imop)
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()
