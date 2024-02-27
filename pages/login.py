# login_page.py

import tkinter as tk
from tkinter import ttk
from pages import signup,home

class LoginPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Login Page")
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

        # Login components on the right

        login_frame = tk.Frame(self.master)
        login_frame.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.4)

        welcome_lbl = ttk.Label(login_frame,text="Welcome Back!")
        welcome_lbl.grid(row=0, column=0,padx=0, pady=10, sticky="e")

        btn_create_acc = ttk.Button(login_frame, text="Create Account", command=self.createAccount)
        btn_create_acc.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        lbl_username = ttk.Label(login_frame, text="Username:")
        lbl_username.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = ttk.Entry(login_frame)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lbl_password = ttk.Label(login_frame, text="Password:")
        lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = ttk.Entry(login_frame, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        btn_forgot = ttk.Button(login_frame, text="Forgot Password", command=self.forgotPassword)
        btn_forgot.grid(row=3, column=0, padx=10, pady=0, sticky="e")
        
        btn_login = ttk.Button(login_frame, text="Login", command=self.login)
        btn_login.grid(row=3, column=1, padx=10, pady=0, sticky="e")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print("Username:", username)
        print("Password:", password)

        # Create and show the Home page
        home_page = home.HomePage(self.master)
        home_page.pack(fill="both", expand=True)

        # Destroy the Login page (optional)
        self.destroy()
    
    def createAccount(self):
        print("Account Created!!!!!")
        self.destroy()
        signup_page = signup.RegisterPage(self.master)


    def forgotPassword(self):
        print("You forgot your password!!!!!")
