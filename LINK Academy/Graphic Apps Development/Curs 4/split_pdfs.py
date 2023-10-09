import tkinter as tk
from splitter.split_files import cut_pdf
from tkinter import filedialog

def browse_files():
    pass

def create_new_file():
    pass


window = tk.Tk()

window.title("Lucru cu PDF-uri")
window.geometry("600x600+300+300")

file_label = tk.Label(window, text="Path-ul fisierului")
file_label.pack()

browse_button = tk.Button(window, text="Browse files", command=browse_files)
browse_button.pack()

pages_frame = tk.Frame(window)
pages_frame.pack()

start_page_label = tk.Label(pages_frame, text="Start Page")
start_page_entry = tk.Entry(pages_frame)

stop_page_label = tk.Label(pages_frame, text="Stop Page")
stop_page_entry = tk.Entry(pages_frame)

start_page_label.grid(row=0 , column=0 )
start_page_entry.grid(row=1 , column=0 )
stop_page_label.grid(row=0 , column=1 )
stop_page_entry.grid(row=1 , column=1 )

create_file_button = tk.Button(window, text="Create file", command=create_new_file)
create_file_button.pack()

output_filename_label = tk.Label(window, text="Output file")
output_filename_label.pack()

output_filename_entry = tk.Entry(window)
output_filename_entry.pack()

window.mainloop()