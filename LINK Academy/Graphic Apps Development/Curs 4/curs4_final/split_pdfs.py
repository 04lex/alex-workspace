import tkinter as tk
from splitter.split_files import *
from tkinter import filedialog


def browse_files():
    global filepath
    filepath = filedialog.askopenfilename(initialdir="/Users/stefan/Desktop/LinkAcademy/Python_Track/__22_23/Graphic Applications/curs4/")
    file_label.config(text=filepath)
    start_page_entry.delete(0, tk.END)
    start_page_entry.insert(0, "1")
    stop_page_entry.delete(0, tk.END)
    stop_page_entry.insert(0, get_pages_count(filepath))

    output_filename_entry.delete(0, tk.END)
    output_filename_entry.insert(0, filepath.replace(".pdf", "_cut.pdf"))

def create_new_file():
    start_page = int(start_page_entry.get())
    stop_page = int(stop_page_entry.get())
    output_path = output_filename_entry.get()
    cut_pdf(filepath, start_page, stop_page, output_path)

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

start_page_label.grid(row=0, column=0)
start_page_entry.grid(row=1, column=0)
stop_page_label.grid(row=0, column=1)
stop_page_entry.grid(row=1, column=1)

create_file_button = tk.Button(window, text="Create file", command=create_new_file)
create_file_button.pack()

output_filename_label = tk.Label(window, text="Output file")
output_filename_label.pack()

output_filename_entry = tk.Entry(window)
output_filename_entry.pack()

window.mainloop()

