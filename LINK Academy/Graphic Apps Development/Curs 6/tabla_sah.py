import tkinter as tk
from regine_logica import calculeaza_solutii

N = 6

RECTANGLE_DIMENSION = 100
CANVAS_DIMENSIONS = N * RECTANGLE_DIMENSION


def deseneaza_tabla():
    for j in range(N):
        for i in range(N):
            color = "black" if (i+j) % 2 == 0 else "white"
            canvas.create_rectangle(RECTANGLE_DIMENSION * i, RECTANGLE_DIMENSION * j, RECTANGLE_DIMENSION * (i + 1), RECTANGLE_DIMENSION * (j+1), fill=color, tag='patrat')

def sterge_tabla():
    canvas.delete('patrat')
    sterge_reginele()


SOLUTII = calculeaza_solutii(N)
# SOLUTIE_HARDCODATA = [2, 4, 1, 3]
INDEX_SOLUTIE_CURENTA = 0


def recreeaza_tabla():
    global N, SOLUTII, CANVAS_DIMENSIONS
    N = int(choice.get())
    print('New N: ', N)
    sterge_tabla()
    CANVAS_DIMENSIONS = N * RECTANGLE_DIMENSION
    
    SOLUTII = calculeaza_solutii(N)
    deseneaza_tabla()
    deseneaza_reginele()


def deseneaza_reginele():
    SOLUTIE_CURENTA = SOLUTII[INDEX_SOLUTIE_CURENTA]
    for j, i in enumerate(SOLUTIE_CURENTA):
        canvas.create_text(RECTANGLE_DIMENSION/2 + (i-1) * RECTANGLE_DIMENSION, RECTANGLE_DIMENSION/2 + RECTANGLE_DIMENSION * j, text='♛', font=('Arial', int(RECTANGLE_DIMENSION)), fill='red', tag='regina')


def sterge_reginele():
    canvas.delete('regina')


def solutia_urmatoare():
    global INDEX_SOLUTIE_CURENTA, SOLUTIE_CURENTA
    INDEX_SOLUTIE_CURENTA += 1
    if len(SOLUTII) == INDEX_SOLUTIE_CURENTA:
        INDEX_SOLUTIE_CURENTA = 0
    sterge_reginele()
    deseneaza_reginele()

window = tk.Tk()
canvas = tk.Canvas(window, width=CANVAS_DIMENSIONS, height=CANVAS_DIMENSIONS, bg="yellow")
canvas.pack()

button = tk.Button(window, text="Urmatoarea solutie", command=solutia_urmatoare)
button.pack()

choice = tk.Spinbox(window, from_=4, to=10, command=recreeaza_tabla)
choice.pack()

deseneaza_tabla()
deseneaza_reginele()

window.mainloop()

# ♛

