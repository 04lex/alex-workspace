import tkinter as tk

class  Window(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

VOCALE = ["a", "e", "i", "o", "u"]

def tradu(event):
        value = entry.get()
        # # VARIANTA 1
        # for vocala in VOCALE:
        #      value = value.replace(f"{vocala}", f"{vocala}p{vocala}")

        # VARIANTA 2
        lista_de_litere = [ litera if litera not in VOCALE else litera + "p" + litera for litera in value ]
        value = "".join(lista_de_litere)


        pasareasca.set(value)

if __name__ == "__main__":
    window = Window("Pasareasca", "600x600+300+300")

    entry = tk.Entry(window)
    entry.pack()

    entry.bind("<KeyRelease>", tradu)

    pasareasca = tk.StringVar()
    pasareasca.set("Traducerea")

    label = tk.Label(window, textvariable=pasareasca)
    label.pack()

    window.mainloop()