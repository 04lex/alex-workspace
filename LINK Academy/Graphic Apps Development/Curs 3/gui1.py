import tkinter as tk
from math import pi

class Window(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)


def calculate():
    input_value = input_field.get()
    try:
        input_value = float(input_value)
        aria = pi * input_value ** 2
    except:
        aria = "Nu se poate calcula"
    finally:
        value_var.set = aria


if __name__ == "__main__":
    window = Window("Exercitiu", "600x600+300+300")

    value_var = tk.StringVar()
    value_var.set("Calculeaza aria cercului")

    label = tk.Label(window, textvariable=value_var)
    label.pack()

    input_field = tk.Entry(window)
    input_field.pack()
    input_field.insert(0, "1")
    input_field.insert(0, "2")
    input_field.insert(0, "3")
    input_field.insert(0, "4")


    button = tk.Button(window, text="Calculeaza", command=calculate)
    button.pack()

    window.mainloop()