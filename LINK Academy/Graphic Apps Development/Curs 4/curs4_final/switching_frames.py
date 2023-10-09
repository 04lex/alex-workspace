import tkinter as tk


window = tk.Tk()
window.title("Schimbare")
window.geometry("600x600+300+300")
window.config(bg="green")


colors = ["red","blue", "yellow", "green", "black", "white"]

def switch_next():
    penultimul = frames[-2]
    penultimul.tkraise()
    ultimul = frames.pop()
    frames.insert(0, ultimul)

def switch_previous():
    primul = frames[0]
    primul.tkraise()
    primul = frames.pop(0)
    frames.append(primul)


frames = []

for color in colors:
    frame = tk.Frame(window, bg=color)
    frame.grid(row=0, column=0, sticky="nesw")
    frames.append(frame)

    label = tk.Label(frame, text=color)
    label.pack()

    next_button = tk.Button(frame, text="Next", bg=color, command=switch_next)
    next_button.pack()

    previous_button = tk.Button(frame, text="Previous", bg=color, command=switch_previous)
    previous_button.pack()

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()