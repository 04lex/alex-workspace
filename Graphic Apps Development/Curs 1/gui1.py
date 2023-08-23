import tkinter as tk

window = tk.Tk()
# window.geometry("500x500+100+0")


## width * height, margin_x, margin_y
# window.geometry("500x600")


## Fullscreen - v1
# window.attributes("-fullscreen", True)


## Fullscreen - v2
max_width = window.winfo_screenwidth()
max_height = window.winfo_screenheight()

window.geometry(f"{max_width}x{max_height}")

## Titlu
window.title("League of Legends")

window.grid_columnconfigure(0, minsize=200)
window.grid_rowconfigure(0, minsize=200)

label1 = tk.Label(window, text="Hello")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="World!")
label2.grid(row=0, column=2)

label4 = tk.Label(window, text="World!")
label4.grid(row=0, column=2)




window.mainloop()