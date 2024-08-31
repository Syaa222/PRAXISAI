import cv2
import json
import pathlib, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

current_dir = pathlib.Path(__file__).parent
img_dir = current_dir.joinpath('img')
data_path = current_dir.joinpath('webcam.json')

if not img_dir.exists():
    os.makedirs(img_dir)

if data_path.exists():
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f'Gagal membuka file {data_path}. Coba hapus file tersebut.')
        exit()
else:
    data = []

def create_window(frame):
    # Buat jendela utama
    window = tk.Tk()
    window.title('Aplikasi Data Pengguna')
    window.geometry('500x400')
    window.resizable(False, False)

    # Styling untuk widget
    style = ttk.Style()
    style.configure('TLabel', font=('Times New Roman', 12), background='lightblue')
    style.configure('TEntry', font=('Times New Roman', 12))
    style.configure('TButton', font=('Times New Roman', 12), padding=10, relief='raised')
    style.configure('TNotebook.Tab', font=('Times New Roman', 12))

    # Fungsi untuk menyimpan data
    def save_command():
        name = name_entry.get()
        kelas = kelas_entry.get()
        sekolah = sekolah_entry.get()

        timestamp = datetime.now().timestamp()
        img_path = img_dir.joinpath(f'{int(timestamp)}.jpg')
        cv2.imwrite(img_path, frame)
        
        data.append({
            'name': name,
            'kelas': kelas,
            'sekolah': sekolah,
            'path': str(img_path)
        })

        print(data)
        
        with open(data_path, 'w') as f:
            json.dump(data, f)
        
        messagebox.showinfo('Info', f'Data berhasil disimpan, {name}!')

    # Menu Bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Save', command=save_command)
    file_menu.add_command(label='Exit', command=window.quit)
    menu_bar.add_cascade(label='File', menu=file_menu)

    # Tab Control
    tab_control = ttk.Notebook(window)

    # Tab 1: Data Entry
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Data Siswa')

    tk.Label(tab1, text='Nama Lengkap', font=('Times New Roman', 12)).pack(pady=5)
    name_entry = ttk.Entry(tab1)
    # name_entry.insert(tk.END, data['name'])
    name_entry.pack(pady=5, padx=10, fill=tk.X)

    tk.Label(tab1, text='Level Kelas', font=('Times New Roman', 12)).pack(pady=5)
    kelas_entry = ttk.Entry(tab1)
    # kelas_entry.insert(tk.END, data['kelas'])
    kelas_entry.pack(pady=5, padx=10, fill=tk.X)

    tk.Label(tab1, text='Sekolah', font=('Times New Roman', 12)).pack(pady=5)
    sekolah_entry = ttk.Entry(tab1)
    # sekolah_entry.insert(tk.END, data['sekolah'])
    sekolah_entry.pack(pady=5, padx=10, fill=tk.X)

    # Button to save data
    save_button = ttk.Button(tab1, text='Check', command=save_command)
    save_button.pack(pady=20)

    # Tab 2: About
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Hasil Data')

    # Display saved data
    tk.Label(tab2, text='Hasil Data Siswa', font=('Times New Roman', 16, 'bold')).pack(pady=10)
    # tk.Label(tab2, text=f'Nama: {data["name"]}', font=('Times New Roman', 12)).pack(pady=5)
    # tk.Label(tab2, text=f'Kelas: {data["kelas"]}', font=('Times New Roman', 12)).pack(pady=5)
    # tk.Label(tab2, text=f'Sekolah: {data["sekolah"]}', font=('Times New Roman', 12)).pack(pady=5)


    tab_control.pack(expand=1, fill='both')

    # Jalankan aplikasi
    window.mainloop()

    def finish_wizard(self):
            messagebox.showinfo("Summary", f"Name: {self.user_data['name']}\nAge: {self.user_data['age']}\nEmail: {self.user_data['email']}")
            self.root.quit()

# def save_image(frame):
#     root = tk.Tk()
#     tk.Label(root, text='Masukkan nama').pack()
#     name_entry = tk.Entry(root)
#     name_entry.pack()

#     def save():
#         name = name_entry.get()
#         timestamp = datetime.now().timestamp()
#         img_path = img_dir.joinpath(f'{int(timestamp)}.jpg')
#         cv2.imwrite(img_path, frame)

#         data.append({
#             'name': name,
#             'path': str(img_path)
#         })
#         with open(data_path, 'w') as f:
#             json.dump(data, f)
#         root.destroy()

#     tk.Button(text='Simpan', command=save).pack()

#     root.mainloop()

cap = cv2.VideoCapture(0)

running = True
while running:
    frame = cap.read()[1]

    c = cv2.waitKey(1)
    if c == ord('q'):
        running = False
    elif c == ord('s'):
        create_window(frame)
        # create_window()

    cv2.putText(frame, 'Tekan [s] untuk menyimpan, [q] untuk keluar', (0, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('Camera', frame)

cap.release()
cv2.destroyAllWindows()