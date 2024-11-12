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
def Connect():
    mess = None

    def yesp():
        mess = "yes"
        
    def nop():
        mess = "no"

    Can.create_image(0,0,image=img,anchor="nw")
    Can.create_rectangle(0,ySize/2-(.15*ySize),xSize,ySize/2+(.15*ySize),fill="white")
    yes = Button(Can,text="Yes", command=yesp)
    yes.pack()
    no = Button(Can,text="no", command=nop)
    no.pack()
    while mess == None:
        print()
    return mess

try:
    while root.winfo_exists():
        root.update()

except (EOFError,KeyboardInterrupt):
    pass

root.destroy()