#1
from tkinter import messagebox
messagebox.showinfo('info', 'Welcome to my gui')

#2
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

tk.Label(window,text='Masukkan Biodata anda').pack()
name_entry = tk.Entry(window)
name_entry.pack()
tk.Entry(window).pack() #entry untuk input

def save_command():
 name = name_entry.get()
 messagebox.showinfo('info', f'Welcome to my gui {name}!')

tk.Button(window, text='Next', command=save_command).pack()

window.mainloop()

#messagebox.showinfo('info', 'Welcome to my gui')