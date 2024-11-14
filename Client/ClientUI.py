from tkinter import *
from PIL import Image, ImageTk

def CreateWindow():
    root = Tk()
    root.configure(background='#fcbd5d')
    root.wm_attributes('-transparentcolor','#fcbd5d')
    root.attributes("-fullscreen",True)
    root.wm_title("event")
    xSize = root.winfo_screenwidth()
    ySize = root.winfo_screenheight()
    
    Can = Canvas(root,width=xSize,height=ySize,background="#fcbd5d", highlightthickness=0)

    return root,Can,xSize,ySize

def Create_Button(root:Tk, Canvas:Canvas, x1,y1,x2,y2, Text="Hello", FontSize = '15'):
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    IsOver = (x >= x1 and x <= x2) and (y >= y1 and y <= y2)

    Canvas.create_rectangle(x1,y1,x2,y2,outline=IsOver and "White" or "gray",fill="")
    Canvas.create_text((x2+x1)/2, (y2+y1)/2,text=Text,font="Segoe "+FontSize,anchor="center",fill="White")
    root.winfo_pointer



def Connect(device="Fsih"):
    root, Can, xSize, ySize = CreateWindow()
    mess = StringVar()
    Cy = ySize/2
    Cx = xSize/2

    def press(de):
        mess.set(de)

    Can.create_rectangle(0,0,xSize,ySize,fill="#000000",stipple="gray50")
    Can.create_rectangle((0,Cy-(.15*ySize),xSize,Cy+(.15*ySize)),fill="#0f0f0f", outline="")

    Can.create_text(Cx, Cy-(.075*ySize),text=f"Allow {device} to connect to this device",font= 'Segoe 35',anchor="s",fill="#ffffff")
    Can.create_text(Cx, Cy-(.075*ySize),text=f"This could cause harm to your device",font= 'Segoe 25',anchor="n",fill="#ffffff")
    
    Can.pack()

    while mess.get() not in ["yes","no"]:
        Create_Button(root, Can, (.25*xSize),Cy+(.025*ySize),Cx-(.025*xSize),Cy+(.1*ySize),"Yes","25")
        Create_Button(root, Can, Cx+(.025*xSize),Cy+(.025*ySize),Cx+(.25*xSize),Cy+(.1*ySize),"No","25")
        root.update()

    root.destroy()
    return mess.get()

print(Connect())