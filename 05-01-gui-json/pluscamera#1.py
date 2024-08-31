import os
import tkinter as tk
from tkinter import messagebox, ttk
import json
import cv2
import dlib
from PIL import Image, ImageTk
from datetime import datetime

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

# Setup deteksi wajah
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.right(), face.bottom())
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
        
        landmarks = predictor(gray, face)
        for point in landmarks.parts():
            cv2.circle(frame, (point.x, point.y), 2, (255, 0, 0), -1)
    return frame

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Aplikasi Data Pengguna')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        self.video_source = cv2.VideoCapture(0)
        if not self.video_source.isOpened():
            messagebox.showerror("Error", "Kamera tidak ditemukan.")
            self.root.quit()

        # Create frames and tabs
        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)  # Tab untuk video feed
        self.tab4 = ttk.Frame(self.tab_control)  # Tab untuk waktu

        self.tab_control.add(self.tab1, text='Data Entry')
        self.tab_control.add(self.tab2, text='About')
        self.tab_control.add(self.tab3, text='Face Detection')
        self.tab_control.add(self.tab4, text='Time')

        self.tab_control.pack(expand=1, fill='both')

        self.create_data_entry_tab()
        self.create_about_tab()
        self.create_face_detection_tab()
        self.create_time_tab()

    def create_data_entry_tab(self):
        tk.Label(self.tab1, text='Nama Lengkap', font=('Times new romance', 12)).pack(pady=5)
        self.name_entry = ttk.Entry(self.tab1)
        self.name_entry.insert(tk.END, data['name'])
        self.name_entry.pack(pady=5, padx=10, fill=tk.X)

        tk.Label(self.tab1, text='Level Kelas', font=('Times new romance', 12)).pack(pady=5)
        self.kelas_entry = ttk.Entry(self.tab1)
        self.kelas_entry.insert(tk.END, data['kelas'])
        self.kelas_entry.pack(pady=5, padx=10, fill=tk.X)

        tk.Label(self.tab1, text='Umur', font=('Times new romance', 12)).pack(pady=5)
        self.umur_entry = ttk.Entry(self.tab1)
        self.umur_entry.insert(tk.END, data['umur'])
        self.umur_entry.pack(pady=5, padx=10, fill=tk.X)

        tk.Label(self.tab1, text='Tanggal/Tempat Lahir', font=('Times new romance', 12)).pack(pady=5)
        self.biodata_entry = ttk.Entry(self.tab1)
        self.biodata_entry.insert(tk.END, data['biodata'])
        self.biodata_entry.pack(pady=5, padx=10, fill=tk.X)

        save_button = ttk.Button(self.tab1, text='Save', command=self.save_command)
        save_button.pack(pady=20)

    def create_about_tab(self):
        tk.Label(self.tab2, text='Tentang Aplikasi', font=('Times new romance', 16, 'bold')).pack(pady=10)
        tk.Label(self.tab2, text='Aplikasi ini dibuat menggunakan Tkinter untuk mendemonstrasikan GUI dengan berbagai fitur.', font=('Times new romance', 12)).pack(pady=10)

    def create_face_detection_tab(self):
        self.video_label = tk.Label(self.tab3)
        self.video_label.pack(expand=True, fill=tk.BOTH)
        self.update_video()

    def create_time_tab(self):
        self.time_label = tk.Label(self.tab4, font=('Times new romance', 16))
        self.time_label.pack(pady=20)
        self.update_time()

    def save_command(self):
        name = self.name_entry.get()
        kelas = self.kelas_entry.get()
        umur = self.umur_entry.get()
        biodata = self.biodata_entry.get()

        data = {
            'name': name,
            'kelas': kelas,
            'umur': umur,
            'biodata': biodata
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f)
        
        messagebox.showinfo('Info', f'Data berhasil disimpan, {name}!')

    def update_video(self):
        ret, frame = self.video_source.read()
        if ret:
            frame = detect_faces(frame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            photo = ImageTk.PhotoImage(image=image)

            self.video_label.config(image=photo)
            self.video_label.image = photo

        self.root.after(10, self.update_video)

    def update_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  # Update every second

    def __del__(self):
        self.video_source.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
