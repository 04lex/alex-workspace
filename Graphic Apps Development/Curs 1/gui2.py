import tkinter
import os

window = tkinter.Tk()
count = 1

def printeaza():
    global count

    ## Clear terminal
    os.system('cls')
    text = f"Ai dat click de {count} ori"
    stringvar.set(text)
    print(text)
    count+=1

button = tkinter.Button(window, text="Start", command=printeaza)
button.pack()

stringvar = tkinter.StringVar(value="Butonul nu a fost apasat")
label = tkinter.Label(window, textvar=stringvar)
label.pack()

window.mainloop()
