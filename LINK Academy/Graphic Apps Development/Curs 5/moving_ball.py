import tkinter as tk
from random import randint

COLORS = ["red", "blue", "green", "yellow", "pink"]

window = tk.Tk()

FULL_WIDTH= 1000
FULL_HEIGHT= 1000

START_X = 100
START_Y = 300

DIAMETRU_MINGE = 50


canvas = tk.Canvas(window, width=FULL_WIDTH, height=FULL_HEIGHT, bg="white")
canvas.pack()

minge = canvas.create_oval(START_X, START_Y, START_X + DIAMETRU_MINGE, START_Y + DIAMETRU_MINGE, fill="black")

# valori paleta
BOARD_HEIGHT = 10
BOARD_WIDTH = 200
paleta = canvas.create_rectangle((FULL_WIDTH-BOARD_WIDTH)/2, FULL_HEIGHT - BOARD_HEIGHT - 20, (FULL_WIDTH-BOARD_WIDTH)/2 + BOARD_WIDTH,  FULL_HEIGHT - BOARD_HEIGHT - 10, fill="black")


SPEED_PALETA = 4

#### VARIANTA 1
# def misca_paleta(direction):
#     canvas.move(paleta, direction * SPEED_PALETA, 0)

# canvas.bind_all("<KeyRelease-Left>", lambda x: misca_paleta(-1))
# canvas.bind_all("<KeyRelease-Right>", lambda x: misca_paleta(1))
#####

##### varianta 2
def misca_stanga(event):
    canvas.move(paleta, -SPEED_PALETA, 0)

def misca_dreapta(event):
    canvas.move(paleta, SPEED_PALETA, 0)

canvas.bind_all("<KeyRelease-Left>", misca_stanga)
canvas.bind_all("<KeyRelease-Right>", misca_dreapta)
######

# valori minge
SPEED_Y = 4
SPEED_X = 4
INCREASE_VALUE = 1

canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])

def misca_mingea():
    global SPEED_X, SPEED_Y
    canvas.move(minge, SPEED_X, SPEED_Y)
    canvas.after(10, misca_mingea)

    x0, y0, x1, y1 = canvas.coords(minge)
    if y1 > FULL_HEIGHT:
        SPEED_Y = -SPEED_Y-INCREASE_VALUE
        canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])
    elif y0 < 0:
        SPEED_Y = -SPEED_Y+INCREASE_VALUE
        canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])

    if x1 > FULL_WIDTH:
        SPEED_X = -SPEED_X-INCREASE_VALUE
        canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])
    elif x0 < 0:
        SPEED_X = -SPEED_X+INCREASE_VALUE
        canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])


canvas.after(3000, misca_mingea)



window.mainloop()