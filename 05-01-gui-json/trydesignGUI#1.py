import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

# Nama file JSON untuk menyimpan data
filename = 'data.json'

# Cek apakah file JSON ada dan baca isinya
if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
else:
    data = {
        'name': '',
        'kelas': '',
        'umur': '',
        'biodata': '',
    }

# Buat jendela utama
window = tk.Tk()
window.title('Aplikasi Data Pengguna')
window.geometry('400x300')
window.resizable(False, False)

# Styling untuk widget
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12), padding=10)

# Label dan Entry untuk Nama
tk.Label(window, text='Masukkan Nama Lengkap', font=('Arial', 12)).pack(pady=5)
name_entry = ttk.Entry(window)
name_entry.insert(tk.END, data['name'])
name_entry.pack(pady=5, padx=10, fill=tk.X)

# Label dan Entry untuk Kelas
tk.Label(window, text='Masukkan Level Kelas', font=('Arial', 12)).pack(pady=5)
kelas_entry = ttk.Entry(window)
kelas_entry.insert(tk.END, data['kelas'])
kelas_entry.pack(pady=5, padx=10, fill=tk.X)

# Label dan Entry untuk Umur
tk.Label(window, text='Masukkan Umur', font=('Arial', 12)).pack(pady=5)
umur_entry = ttk.Entry(window)
umur_entry.insert(tk.END, data['umur'])
umur_entry.pack(pady=5, padx=10, fill=tk.X)

# Label dan Entry untuk Biodata
tk.Label(window, text='Masukkan Tanggal/Tempat Lahir', font=('Arial', 12)).pack(pady=5)
biodata_entry = ttk.Entry(window)
biodata_entry.insert(tk.END, data['biodata'])
biodata_entry.pack(pady=5, padx=10, fill=tk.X)

# Fungsi untuk menyimpan data
def save_command():
    name = name_entry.get()
    kelas = kelas_entry.get()
    umur = umur_entry.get()
    biodata = biodata_entry.get()

    data = {
        'name': name,
        'kelas': kelas,
        'umur': umur,
        'biodata': biodata
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f)
    
    messagebox.showinfo('Info', f'Data berhasil disimpan, {name}!')

# Tombol untuk menyimpan data
save_button = ttk.Button(window, text='Simpan', command=save_command)
save_button.pack(pady=20)

# Jalankan aplikasi
window.mainloop()
