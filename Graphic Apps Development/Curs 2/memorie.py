import tkinter
import random


VALUES = ["Dinamo", "Steaua", "Rapid", "Craiova", "Farul", "Otelul", "CFR", "UTA"]
print(max([len(i) for i in VALUES]))

VALUES *= 2
random.shuffle(VALUES)
print(VALUES)


MAX_LENGTH = max([len(i) for i in VALUES ])

def justify(string, length=MAX_LENGTH):
    left = (length - len(string)) // 2
    return string.rjust(len(string)+left, " ").ljust(length, " ")


count = 0

# Valori castigate (corect gasite)
REVEALED_BUTTONS_INDEX = []
# Valori intoarse
PUSHED_BUTTONS_INDEX = []


def push(index):
    global count
    count += 1
    print(f"A fost apasat butonul de {count} ori")
    button = all_buttons[index]
    button.config(text=f"de {count} ori")

def hide():
    first_button = all_buttons[PUSHED_BUTTONS_INDEX[0]]
    second_button = all_buttons[PUSHED_BUTTONS_INDEX[1]]
    first_button.config(text= justify(f"{PUSHED_BUTTONS_INDEX[0]}"))
    second_button.config(text= justify(f"{PUSHED_BUTTONS_INDEX[1]}"))
    PUSHED_BUTTONS_INDEX.clear()


def reveal(index):
    global PUSHED_BUTTONS_INDEX

    if index in PUSHED_BUTTONS_INDEX or index in REVEALED_BUTTONS_INDEX:
        return

    PUSHED_BUTTONS_INDEX.append(index)
    button = all_buttons[index]
    button.config(text=f"{VALUES[index]}")
    if len(PUSHED_BUTTONS_INDEX) == 2:
        first_button = all_buttons[PUSHED_BUTTONS_INDEX[0]]
        second_button = all_buttons[PUSHED_BUTTONS_INDEX[1]]
        print(first_button['text'])
        print(second_button['text'])
        if first_button['text'] == second_button['text']:
            print("Aceeasi valoare")
            REVEALED_BUTTONS_INDEX.append(PUSHED_BUTTONS_INDEX.pop())
            REVEALED_BUTTONS_INDEX.append(PUSHED_BUTTONS_INDEX.pop())
        else:
            print("Nu sunt de acceasi valoare")
            first_button.after(500, hide)
           

window =  tkinter.Tk()
window.title("Memorie")
window.geometry("600x600+300+300")

all_buttons = []

# i - [0, 1, 2, ... 15] 
COLUMNS  = 4
ROWS = 4
for i in range(COLUMNS * ROWS):
    button = tkinter.Button(window, text= justify(f"{i}"), command=lambda x=i: reveal(x))
    button.grid(row= i //COLUMNS , column= i%COLUMNS)
    all_buttons.append(button)




# 4. Creare functie

def restart_game():
    # 4.1.  Stergere PUSHED_BUTTONS_INDEX
    PUSHED_BUTTONS_INDEX.clear()
    # 4.2. Stergere REVEALED_BUTTONS_INDEX
    REVEALED_BUTTONS_INDEX.clear()
    

    # 4.3. Butoanele sa fie configurate cu valorile numerice (i in range(16))
    for index, button in enumerate(all_buttons):
        button.config(text=justify(f"{index}"))

    # 4.4 Shuffle de optiuni
    random.shuffle(VALUES)


# 1. Creare buton + # 3. Adaugare comanda pe buton
reset_button = tkinter.Button(window, text=justify("Restart"), command=restart_game)

# 2. Adaugare buton in grid
reset_button.grid()














window.mainloop()


 