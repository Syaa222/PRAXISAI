import os
import tkinter as tk
import json
from tkinter import messagebox

filename = 'nama.json'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
else:
    data = {
        'nama': '',
        'kelas': '',
        'umur': '',
        'biodata': '',
    }

window = tk.Tk()

tk.Label(window, text='Masukkan Nama Lengkap').pack()
name_entry = tk.Entry(window)
name_entry.insert(tk.INSERT, data['nama'])
name_entry.pack()

tk.Label(window, text='Masukkan Level kelas').pack()
kelas_entry = tk.Entry(window)
kelas_entry.insert(tk.INSERT, data['kelas'])
kelas_entry.pack()

tk.Label(window, text='Masukkan Umur').pack()
umur_entry = tk.Entry(window)
umur_entry.insert(tk.INSERT, data['umur'])
umur_entry.pack()

tk.Label(window, text='Masukkan Tanggal/Tempat Lahir').pack()
biodata_entry = tk.Entry(window)
biodata_entry.insert(tk.INSERT, data['biodata'])
biodata_entry.pack()

def save_command():
    name = name_entry.get()
    kelas = kelas_entry.get()
    umur = umur_entry.get()
    biodata = biodata_entry.get()

    data = {
        'nama': name,
        'kelas': kelas,
        'umur': umur,
        'biodata': biodata
    }
    
    with open('nama.json', 'w') as f:
        json.dump(data, f)
    messagebox.showinfo('Info', f'Welcome to my GUI, {name}!')

# Button to save data
save_button = tk.Button(window, text='Save', command=save_command)
save_button.pack()

window.mainloop()
