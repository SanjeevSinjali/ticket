# register_page.py

import tkinter as tk
from tkinter import ttk
import re
from pages import login

class RegisterPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Register Page")
        self.master.geometry("700x650")
        self.master.resizable(False, False)
        
        self.Page()

    def Page(self):
        # Image on the left
        img_label = tk.Label(self.master)
        img_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        img = tk.PhotoImage(file="./data/images/bus.png")
        img_label.config(image=img)
        img_label.image = img

        # Registration components on the right
        register_frame = tk.Frame(self.master)
        register_frame.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.5)

        register_lbl = ttk.Label(register_frame,text="Register")
        register_lbl.grid(row=0, column=1,padx=0, pady=10, sticky="e")
        
        ttk.Label(register_frame, text="Full Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_fullname = ttk.Entry(register_frame)
        self.entry_fullname.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(register_frame, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_email = ttk.Entry(register_frame)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(register_frame, text="Phone Number:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_phone = ttk.Entry(register_frame)
        self.entry_phone.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(register_frame, text="Password:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry_password = ttk.Entry(register_frame, show="*")
        self.entry_password.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(register_frame, text="Re-enter Password:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.entry_repassword = ttk.Entry(register_frame, show="*")
        self.entry_repassword.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        # Buttons
        ttk.Button(register_frame, text="Register", command=self.register).grid(row=6, column=1, padx=10, pady=10, sticky="e")

    def register(self):
        fullname = self.entry_fullname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        password = self.entry_password.get()
        repassword = self.entry_repassword.get()

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_pattern, email):
            print("Invalid email address")
            return

        if password != repassword:
            print("Password did not match")
            return

        print("Full Name:", fullname)
        print("Email:", email)
        print("Phone Number:", phone)
        print("Password:", password)
        print("Re-entered Password:", repassword)

        self.destroy()

        login_page = login.LoginPage(self.master)
