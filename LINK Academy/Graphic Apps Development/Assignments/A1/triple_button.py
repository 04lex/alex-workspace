import tkinter as tk
import os

def label_click():
    global click_count
    os.system('cls')
    click_count += 1

    if click_count == 3:
        print("Three clicks")
        click_count = 0
    else:
        label.after(5000, reset_click_count)

def reset_click_count():
    global click_count
    click_count = 0

window = tk.Tk()
window.geometry("200x100+300+300")

label = tk.Label(window, text="Click me")
label.pack()

click_count = 0

label.bind("<Button-1>", lambda event: label_click())

window.mainloop()