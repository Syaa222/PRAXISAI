import tkinter as tk
from tkinter import ttk, messagebox

class WizardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wizard Application")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Create a container for the wizard steps
        self.container = ttk.Frame(self.root)
        self.container.pack(expand=True, fill="both")

        # Dictionary to keep track of user input
        self.user_data = {
            'name': '',
            'age': '',
            'email': ''
        }
        
        # Create frames for each step
        self.frames = {
            "Step1": ttk.Frame(self.container),
            "Step2": ttk.Frame(self.container),
            "Step3": ttk.Frame(self.container),
        }
        
        self.create_steps()
        self.current_step = "Step1"
        self.show_frame(self.current_step)

    def create_steps(self):
        # Step 1: Enter Name
        tk.Label(self.frames["Step1"], text="Step 1: Enter Your Name").pack(pady=10)
        self.name_entry = ttk.Entry(self.frames["Step1"])
        self.name_entry.pack(pady=5)
        self.frames["Step1"].pack(fill="both", expand=True)

        # Step 2: Enter Age
        tk.Label(self.frames["Step2"], text="Step 2: Enter Your Age").pack(pady=10)
        self.age_entry = ttk.Entry(self.frames["Step2"])
        self.age_entry.pack(pady=5)
        self.frames["Step2"].pack(fill="both", expand=True)

        # Step 3: Enter Email
        tk.Label(self.frames["Step3"], text="Step 3: Enter Your Email").pack(pady=10)
        self.email_entry = ttk.Entry(self.frames["Step3"])
        self.email_entry.pack(pady=5)
        self.frames["Step3"].pack(fill="both", expand=True)

        # Navigation Buttons
        self.button_frame = ttk.Frame(self.container)
        self.button_frame.pack(pady=10, side="bottom", fill="x")

        self.back_button = ttk.Button(self.button_frame, text="Back", command=self.go_back)
        self.back_button.pack(side="left", padx=5)
        
        self.next_button = ttk.Button(self.button_frame, text="Next", command=self.go_next)
        self.next_button.pack(side="right", padx=5)

    def show_frame(self, step_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[step_name].pack(fill="both", expand=True)

        if step_name == "Step1":
            self.back_button.config(state="disabled")
            self.next_button.config(text="Next")
        elif step_name == "Step3":
            self.next_button.config(text="Finish")
        else:
            self.back_button.config(state="normal")
            self.next_button.config(text="Next")

    def go_back(self):
        if self.current_step == "Step2":
            self.current_step = "Step1"
        elif self.current_step == "Step3":
            self.current_step = "Step2"
        self.show_frame(self.current_step)

    def go_next(self):
        if self.current_step == "Step1":
            self.user_data['name'] = self.name_entry.get()
            self.current_step = "Step2"
        elif self.current_step == "Step2":
            self.user_data['age'] = self.age_entry.get()
            self.current_step = "Step3"
        elif self.current_step == "Step3":
            self.user_data['email'] = self.email_entry.get()
            self.finish_wizard()
            return
        self.show_frame(self.current_step)

    def finish_wizard(self):
        messagebox.showinfo("Summary", f"Name: {self.user_data['name']}\nAge: {self.user_data['age']}\nEmail: {self.user_data['email']}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = WizardApp(root)
    root.mainloop()
