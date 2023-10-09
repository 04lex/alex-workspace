import tkinter as tk
import enum

class Processor(enum.Enum):
    VISA = 1
    MASTERCARD =  2
    PAYPAL = 3
    MAESTRO = 4

class  Window(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

def calculate(percentage):
    value = valueEntry.get()
    try:
        value = float(value)
        new_value = value + percentage * value / 100
    except ValueError:
        new_value = "Incorect"
    finally:
        fee_var.set(new_value)

if __name__ == "__main__":
    window = Window("Payment fees", "600x600+300+300")
    fee_var =  tk.StringVar()
    fee_var.set("Current value")

    label = tk.Label(window, textvariable=fee_var) 
    label.grid(row=0, column=1)

    valueEntry = tk.Entry(window)
    valueEntry.grid(row=1, column=1)

    for index, procesator in enumerate(Processor):
        # button = tk.Button(window, text=procesator.name.lower().capitalize(), command= lambda x=procesator.value: calculate(x) )
        button = tk.Button(window, text=procesator.name.lower().capitalize())
        button.bind('<Button>', lambda x=procesator.value: calculate(x))
        button.grid(row=3, column=index)

    window.mainloop()
