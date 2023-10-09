import tkinter as tk
from tkinter import messagebox
from random import randint
from time import time

window = tk.Tk()
window.title("Tamagotchi")
window.geometry("600x600+300+300")

label = tk.Label(window, text="I'm Not Hungry")
label.pack()

def push():
    if not has_started:
        messagebox.showinfo("Prea devreme")
    else:
        stop_time = time()
        delta = stop_time - start_time
        delta = round(delta, 2)
        messagebox.showinfo(message=f"Ai castigat in {delta}")
        

has_started = False

def start_game():
    global has_started, start_time
    label.config(text="I'm Hungry")
    button.config(text="Feed me")
    has_started = True
    start_time = time()

button = tk.Button(window, text="Wait for it", command=push)
button.pack()

ms = randint(1, 5 * 1000)

button.after(ms, start_game)

window.mainloop()