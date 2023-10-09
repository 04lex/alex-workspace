import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=600, height=600, bg="yellow")
canvas.pack()

canvas.create_line(10, 20, 40, 100, fill="red")
canvas.create_line(10, 20, 50, 20, fill="red")
canvas.create_line(50, 20, 40, 100, fill="red")

canvas.create_line(70, 20, 80, 20, 80, 40, 70, 20, fill="red")

# x1, y1, x2, y2
canvas.create_rectangle(200, 20, 240, 100, fill="blue")

canvas.create_rectangle(240, 240, 550, 550, outline="black", width=10)
canvas.create_rectangle(340, 340, 450, 450, fill="red")

canvas.create_oval(340, 340, 450, 450, fill="orange")

canvas.create_text(300, 300, text="Ce mai faci?", fill="black")

window.mainloop()