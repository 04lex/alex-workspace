import tkinter as tk

window = tk.Tk()

c = tk.Canvas(window, width=600, height=600, bg="white")
c.pack()

# fata
fata = c.create_oval(150, 100, 150+300, 100+400, fill="pink")
# ochi stang
ochi_stang = c.create_oval(150+70, 100+100, 150+70+50, 100+100+50, fill="white")

clipit = c.create_rectangle(150+300-70, 100+100, 150+300-70-50, 100+100+25, fill="pink", outline="pink", tag="blink")
# ochi drept
ochi_drept = c.create_oval(150+300-70, 100+100, 150+300-70-50, 100+100+50, fill="white", tag="ochi")


# gura
gura = c.create_arc(150+100, 100+230, 150+100+100, 100+230+100, fill="white", extent=-180)

# un dinte
dinte = c.create_rectangle(150+100+40, 100+230+50, 150+100+40+20, 100+230+50+20, fill="yellow")

inchide = True
def clipeste():
    c.tag_raise("blink")
    c.after(1000, deschide)

def deschide():
    c.tag_raise("ochi")
    c.after(1000, clipeste)

c.after(1000, clipeste)



window.mainloop()
