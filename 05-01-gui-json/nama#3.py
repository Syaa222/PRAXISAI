import os
import tkinter as tk
import json
from tkinter import messagebox

filename = 'nama.json'

if os.path.exists(filename):
 with open ('nama.json', 'r') as f:
   data = json.load(f)
else:
   data = {
      'nama': '',
      'kelas': '',
      'umur': '',
      'biodata': '',
   }

window = tk.Tk()

tk.Label(window,text='Masukkan Nama Lengkap').pack()
name_entry = tk.Entry(window)
name_entry.insert(tk.INSERT, data['name'])
name_entry.pack()

tk.Label(window,text='Masukkan Level kelas').pack()
kelas_entry = tk.Entry(window)
kelas_entry.insert(tk.INSERT, data['kelas'])
kelas_entry.pack()

tk.Label(window,text='Masukkan Umur').pack()
umur_entry = tk.Entry(window)
umur_entry.insert(tk.INSERT, data['Umur'])
umur_entry.pack()

tk.Label(window,text='masukkan tangal/tempat lahir').pack()
biodata_entry = tk.Entry(window)
biodata_entry.insert(tk.INSERT, data['biodata'])
biodata_entry.pack()


def save_command():
    #1
    name = name_entry.get()
    kelas = kelas_entry.get()
    umur = umur_entry.get()
    biodata = biodata_entry.get()

    data = {
    'name' : name,
    'kelas': kelas,
    'umur' : umur,
    'biodata' : biodata
    }
    
    with open('nama.json', 'w') as f:
        json.dump(data, f)
    messagebox.showinfo('info', f'Welcome to my gui {name}!')

    tk.Button(window, text='Saved', command=save_command).pack()


window.mainloop()

#messagebox.showinfo('info', 'Welcome to my gui')
#entry untuk input
