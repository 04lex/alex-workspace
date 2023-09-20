import tkinter as tk

window = tk.Tk()
window.title("Schimbare")
window.geometry("600x600+300+300")
window.config(bg="green")

colors = ["red", "yellow", "blue"]

def switch():
    penultimul = frames[-2]
    penultimul.tkraise()

    ultimul = frames.pop()
    frames.insert(0, ultimul)

frames = []

for color in colors:
    frame = tk.Frame(window, bg=color)
    frame.grid(row=0, column=0, sticky="nesw")
    frames.append(frame)

    label = tk.Label(frame, text=color)
    label.pack()

    button = tk.Button(frame, text="Next", bg=color, command=switch)
    button.pack()

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)



window.mainloop()