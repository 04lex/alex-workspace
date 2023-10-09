import tkinter as tk

window = tk.Tk()

canvas_width = 500
canvas_height = 500

rectangle_width = 50
rectangle_height = 50

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

x1 = ((canvas_width - rectangle_width) // 2) - 15
y1 = ((canvas_height - rectangle_height) // 2) - 10

x2 = x1 + rectangle_width
y2 = y1 + rectangle_height

rectangle_spacing = 51

patrat_blue = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
patrat_red = canvas.create_rectangle(x1 + rectangle_spacing, y1, x2 + rectangle_spacing, y2, fill="red")
patrat_yellow = canvas.create_rectangle(x1, y1 + 100, x2, y2, fill="yellow")
patrat_green = canvas.create_rectangle(x1 + rectangle_spacing, y1 + 100, x2 + rectangle_spacing, y2, fill="green")

SPEED_PATRAT = 2

def retrage():
    global SPEED_PATRAT
    # blue
    canvas.move(patrat_blue, -SPEED_PATRAT, -2)
    # red
    canvas.move(patrat_red, SPEED_PATRAT, -2)
    # yellow
    canvas.move(patrat_yellow, -SPEED_PATRAT, 2)
    # green
    canvas.move(patrat_green, SPEED_PATRAT, 2)

    canvas.after(10, retrage)


canvas.after(1500, retrage)

window.mainloop()