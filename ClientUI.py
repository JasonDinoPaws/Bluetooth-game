from tkinter import *

window = Tk()
window.configure()
window.wm_attributes('-transparentcolor','#000000')
window.attributes("-fullscreen",True)
window.wm_title("Game")

c = Canvas(window,width=window.winfo_screenwidth(),bg='#000000',height=window.winfo_screenheight(),borderwidth=0,highlightthickness=0)
c.pack()

window.mainloop()