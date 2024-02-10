import tkinter as tk 
from tkinter import messagebox
import requests

def login():
    print("Butonul de autentificare a fost apasat.")
    numar_cont = numar_cont_entry.get()
    parola = parola_entry.get()

    # server request pentru auth
    response = requests.post('http://127.0.0.1:5000/login', json={'numar_cont':numar_cont, 'parola':parola})

    if response.status_code == 200:
        token = response.json()['token']
        messagebox.showinfo('Succes', f'Autentificare reusita! Token:{token}')

    else:
        messagebox.showerror('Eroare', 'Autentificare nereusita, verifica datele contului.')


# main window
root = tk.Tk()
root.title('Autentificare')

# cont
numar_cont_label = tk.Label(root, text='Numar de cont:')
numar_cont_label.grid(row=0, column=0, padx=10, pady=5)

numar_cont_entry = tk.Entry(root)
numar_cont_entry.grid(row=0, column=1, padx=10, pady=5)

# parola
parola_label = tk.Label(root, text='Parola:')
parola_label.grid(row=1, column=0, padx=10, pady=5)

parola_entry = tk.Entry(root, show='*')
parola_entry.grid(row=1, column=1, padx=10, pady=5)

# buton login
login_button = tk.Button(root, text='Autentificare', command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()