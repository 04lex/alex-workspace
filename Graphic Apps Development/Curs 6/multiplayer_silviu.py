import tkinter as tk
from random import randint
from tkinter import messagebox

COLORS = ["red", "blue", "green", "yellow", "pink"]

window = tk.Tk()

FULL_WIDTH = 800
FULL_HEIGHT = 800

# Punctul de unde incepe mingea
START_X = 100
START_Y = 300

DIAMETRU_MINGE = 50

canvas = tk.Canvas(window, width=FULL_WIDTH, height=FULL_HEIGHT, bg="white")
canvas.pack()

minge = canvas.create_oval(START_X, START_Y, START_X + DIAMETRU_MINGE , START_Y + DIAMETRU_MINGE, fill="red")

# Dimensiunile paletei
BOARD_WIDTH = 10
BOARD_HEIGHT = 200 
DISTANCE_TO_MARGIN = 20



paleta_stanga = canvas.create_rectangle( DISTANCE_TO_MARGIN, (FULL_HEIGHT - BOARD_HEIGHT)/2  , DISTANCE_TO_MARGIN + BOARD_WIDTH , (FULL_HEIGHT - BOARD_HEIGHT)/2 + BOARD_HEIGHT, fill="black" )


paleta_dreapta = canvas.create_rectangle( FULL_WIDTH - DISTANCE_TO_MARGIN -  BOARD_WIDTH, (FULL_HEIGHT - BOARD_HEIGHT)/2  , FULL_WIDTH - DISTANCE_TO_MARGIN  , (FULL_HEIGHT - BOARD_HEIGHT)/2 + BOARD_HEIGHT, fill="black" )




# print(canvas.coords(paleta_dreapta))


SPEED_paleta = 10
#### VARIANTA 1
# def misca_paleta_dreapta(direction):
#     canvas.move(paleta_dreapta, direction * SPEED_paleta, 0)

# canvas.bind_all("<KeyRelease-Left>",  lambda x : misca_paleta_dreapta(-1))
# canvas.bind_all("<KeyRelease-Right>", lambda x : misca_paleta_dreapta(1))
#####



## VARIANTA 2

PRESSED_KEYS = []

def oprire(event):
    PRESSED_KEYS.pop(PRESSED_KEYS.index(event.keysym))

def apasare(event):
    print(event)
    print(event.keysym)
    print(event.keycode)

    if not event.keysym in PRESSED_KEYS:
        PRESSED_KEYS.append(event.keysym)

    for key in PRESSED_KEYS:
        if key == "w":
            misca_sus_paleta_stanga(event)
        if key == "Up":
            misca_sus_paleta_dreapta(event)
        if key == "s":
            misca_jos_paleta_stanga(event)
        if key == "Down":
            misca_jos_paleta_dreapta(event)

    

def misca_sus_paleta_dreapta(event):
    canvas.move(paleta_dreapta, 0, - SPEED_paleta)
def misca_jos_paleta_dreapta(event):
    canvas.move(paleta_dreapta, 0,  SPEED_paleta)

def misca_sus_paleta_stanga(event):
    canvas.move(paleta_stanga, 0,  - SPEED_paleta)
def misca_jos_paleta_stanga(event):
    canvas.move(paleta_stanga, 0,  SPEED_paleta)

canvas.bind_all("<KeyPress>", apasare)
canvas.bind_all("<KeyRelease>", oprire)

#######

SPEED_Y = 4
SPEED_X = 4 
INCRESE_VALUE = 0

canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])


def misca_mingea():
    global SPEED_Y, SPEED_X
    canvas.move(minge, SPEED_X, SPEED_Y)
    

    x0, y0, x1, y1 = canvas.coords(minge)
    x0_PD, y0_PD, x1_PD, y1_PD   = canvas.coords(paleta_dreapta)
    x0_PS, y0_PS, x1_PS, y1_PS   = canvas.coords(paleta_stanga)


    # Verificam daca mingea loveste paleta_dreapta sau nu
    if y1 > FULL_HEIGHT :
        SPEED_Y = -SPEED_Y+INCRESE_VALUE
        canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])

    # # Tavan
    elif y0 < 0:
        SPEED_Y = -SPEED_Y+INCRESE_VALUE
        canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])

    # Perete dreapta
    if x1 > FULL_WIDTH - BOARD_WIDTH - DISTANCE_TO_MARGIN:
        if y0 > y0_PD and y1 < y1_PD:
            SPEED_X = -SPEED_X-INCRESE_VALUE
            canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])
        else:
            messagebox.showerror(message="STANGA castiga!!!, Apuca-te de invatat")
            return
    # Perete stanga
    elif x0 < 0 + BOARD_WIDTH + DISTANCE_TO_MARGIN:
        if y0 > y0_PS and y1 < y1_PS:
            SPEED_X = -SPEED_X+INCRESE_VALUE
            canvas.itemconfig(minge, fill=COLORS[randint(0, len(COLORS)-1)])
        else: 
            messagebox.showerror(message="DREAPTA castiga!!!, Apuca-te de invatat")
            return

    canvas.after(10, misca_mingea)
    

canvas.after(3000, misca_mingea)

window.mainloop()
