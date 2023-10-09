from tkinter import *
import tkinter.messagebox

window = Tk()

window.title("Hello Python!!!")
window.resizable(False,False)
window.geometry('%dx%d+%d+%d' % (600, 400, (window.winfo_screenwidth()/2)-300, window.winfo_screenheight()/2-200))

lbl = Label(window, text="START GAME") 
lbl.place(x=300, y=200, anchor="center")
lbl.config(width=400)

def start(event):
    tkinter.messagebox.showwarning('Sorry bro! The game will start, as soon as you implement her',parent=window) 

lbl.bind('<Button-1>', start)

window.mainloop()