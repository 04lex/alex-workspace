import tkinter as tk
from regine_logica import calculeaza_solutii

CANVAS_DIMENSIONS = 500
N = 4

RECTANGLE_DIMENSION = CANVAS_DIMENSIONS / N

window = tk.Tk()
canvas = tk.Canvas(window, width=CANVAS_DIMENSIONS, height=CANVAS_DIMENSIONS, bg="yellow")
canvas.pack()

for j in range(N):
    for i in range(N):
        color = "black" if (i+j) % 2 == 0 else "white"
        canvas.create_rectangle(RECTANGLE_DIMENSION * i, RECTANGLE_DIMENSION * j, RECTANGLE_DIMENSION * (i + 1), RECTANGLE_DIMENSION * (j+1), fill=color)

canvas.create_text(RECTANGLE_DIMENSION/2, RECTANGLE_DIMENSION/2, text='♛', font=("Arial", 50), fill="red")

SOLUTIE_HARDCODATA = [2, 4, 1, 3]

for j in range(N):
    for i in range(N):
        if SOLUTIE_HARDCODATA[j] == i+1:
            canvas.create_rectangle(RECTANGLE_DIMENSION/2 + i * RECTANGLE_DIMENSION, RECTANGLE_DIMENSION/2 + RECTANGLE_DIMENSION * j, text="♛", font=("Arial", int(RECTANGLE_DIMENSION)), fill="red")

window.mainloop()