from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.configure()
root.wm_attributes('-transparentcolor','#000000')
root.attributes("-fullscreen",True)
root.wm_title("event")

xSize = root.winfo_screenwidth()
ySize = root.winfo_screenheight()

Can = Canvas(root,width=xSize,height=ySize,background="#000000", highlightthickness=0)
Can.pack()

img = ImageTk.PhotoImage(Image.open("Client/ConnectPixel.png").resize((xSize,ySize)))
mess = None

def yesp():
        global mess 
        mess = "yes"
        print("clicked yes")
            
def nop():
        global mess
        mess = "no"
        print("Clicked no")
def Connect():
    global mess
    mess = None

    ##Can.create_image(0,0,image=img,anchor="nw")
    Can.create_rectangle(0,ySize/2-(.15*ySize),xSize,ySize/2+(.15*ySize),fill="white")
    yes = Button(Can,text="Yes", command=yesp)
    yes.pack()
    no = Button(Can,text="No", command=nop)
    no.pack()
    
    while mess == None:
        root.update()
    Can.delete("all")
    return mess

root.update()