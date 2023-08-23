import tkinter
import random
import os

VALUES = ["Dinamo","Steaua","Rapid","Craiova","Farul","Otelul","CFR","UTA"]
VALUES = VALUES * 2
random.shuffle(VALUES)

PUSHED_BUTTONS_INDEX = 0
count = 0

# Valori corecte
REVEALED_BUTTONS_INDEX = []
# Valori intoarse
PUSHED_BUTTONS_INDEX = []

def push(index):
    global count
    count += 1
    print(f"A fost apasat butonul de {count} ori")
    button = all_buttons[index]
    button.config(text=f"{count} click-uri")

def reveal(index):
    global PUSHED_BUTTONS_INDEX
    PUSHED_BUTTONS_INDEX.append(index)
    button = all_buttons[index]
    button.config(text=f"{VALUES[index]}")
    if len(PUSHED_BUTTONS_INDEX) == 2:
        first_button = all_buttons[PUSHED_BUTTONS_INDEX[0]]
        second_button = all_buttons[PUSHED_BUTTONS_INDEX[1]]
        print(first_button['text'])
        print(second_button['text'])
        if first_button['text'] == second_button['text']:
            print('Aceeasi valoare')
            REVEALED_BUTTONS_INDEX.append(PUSHED_BUTTONS_INDEX[0])
            REVEALED_BUTTONS_INDEX.append(PUSHED_BUTTONS_INDEX[1])
        else:
            print("Nu sunt aceeasi valoare")




window = tkinter.Tk()
window.title("League of Legends")
window.geometry("600x600+300+500")


all_buttons = []
COLUMNS = 4
ROWS = 4
# i - [0, 1, 2 ... 15]
for i in range(COLUMNS * ROWS):
    button = tkinter.Button(window, text=f"{VALUES[i]}", command=lambda x=i: reveal(x))
    button.grid(row= i // COLUMNS ,column= i % COLUMNS)
    all_buttons.append(button)

window.mainloop()



