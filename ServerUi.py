from tkinter import *

clientsallowed = []
window = Tk()
window.configure()
window.attributes("-fullscreen",True)
window.wm_title("Game")

c = Canvas(window,width=window.winfo_screenwidth(),bg='#36342f',height=window.winfo_screenheight(),borderwidth=0,highlightthickness=0)
c.pack()



window.mainloop()