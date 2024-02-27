# import tkinter as tk
# from tkinter import ttk

# class LoginPage(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Login Page")
#         self.master.geometry("640x650")
#         self.master.resizable(False, False)
        
#         self.Page()

#     def Page(self):
#         # Image on the left
#         img_label = tk.Label(self.master)
#         img_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)
#         img = tk.PhotoImage(file="./data/images/bus.png")
#         img_label.config(image=img)
#         img_label.image = img

#         # Login components on the right


#         login_frame = tk.Frame(self.master)
#         login_frame.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.4)


#         welcome_lbl = ttk.Label(login_frame,text="Welcome Back!")
#         welcome_lbl.grid(row=0, column=0,padx=0, pady=10, sticky="e")

#         btn_create_acc = ttk.Button(login_frame, text="Create Account", command=self.createAccount)
#         btn_create_acc.grid(row=0, column=1, padx=10, pady=10, sticky="e")

#         lbl_username = ttk.Label(login_frame, text="Username:")
#         lbl_username.grid(row=1, column=0, padx=10, pady=10, sticky="e")

#         self.entry_username = ttk.Entry(login_frame)
#         self.entry_username.grid(row=1, column=1, padx=10, pady=10, sticky="w")

#         lbl_password = ttk.Label(login_frame, text="Password:")
#         lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

#         self.entry_password = ttk.Entry(login_frame, show="*")
#         self.entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

#         btn_forgot = ttk.Button(login_frame, text="Forgot Password", command=self.forgotPassword)
#         btn_forgot.grid(row=3, column=0, padx=10, pady=0, sticky="e")
        
#         btn_login = ttk.Button(login_frame, text="Login", command=self.login)
#         btn_login.grid(row=3, column=1, padx=10, pady=0, sticky="e")

#     def login(self):
#         username = self.entry_username.get()
#         password = self.entry_password.get()
#         print("Username:", username)
#         print("Password:", password)
    
#     def createAccount(self):
#         print("Account Created!!!!!")

#     def forgotPassword(self):
#         print("You forgot your password!!!!!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LoginPage(master=root)
#     app.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import re

# class RegisterPage(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Register Page")
#         self.master.geometry("700x650")
#         self.master.resizable(False, False)
        
#         self.Page()

#     def Page(self):
#         # Image on the left
#         img_label = tk.Label(self.master)
#         img_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)
#         img = tk.PhotoImage(file="./data/images/bus.png")
#         img_label.config(image=img)
#         img_label.image = img

#         # Registration components on the right
#         register_frame = tk.Frame(self.master)
#         register_frame.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.5)

#         # Labels and entries

#         register_lbl = ttk.Label(register_frame,text="Register")
#         register_lbl.grid(row=0, column=1,padx=0, pady=10, sticky="e")
        
#         ttk.Label(register_frame, text="Full Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
#         self.entry_fullname = ttk.Entry(register_frame)
#         self.entry_fullname.grid(row=1, column=1, padx=10, pady=10, sticky="w")

#         ttk.Label(register_frame, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
#         self.entry_email = ttk.Entry(register_frame)
#         self.entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")

#         ttk.Label(register_frame, text="Phone Number:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
#         self.entry_phone = ttk.Entry(register_frame)
#         self.entry_phone.grid(row=3, column=1, padx=10, pady=10, sticky="w")

#         ttk.Label(register_frame, text="Password:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
#         self.entry_password = ttk.Entry(register_frame, show="*")
#         self.entry_password.grid(row=4, column=1, padx=10, pady=10, sticky="w")

#         ttk.Label(register_frame, text="Re-enter Password:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
#         self.entry_repassword = ttk.Entry(register_frame, show="*")
#         self.entry_repassword.grid(row=5, column=1, padx=10, pady=10, sticky="w")

#         # Buttons
#         ttk.Button(register_frame, text="Register", command=self.register).grid(row=6, column=1, padx=10, pady=10, sticky="e")

#     def register(self):
#         fullname = self.entry_fullname.get()
#         email = self.entry_email.get()
#         phone = self.entry_phone.get()
#         password = self.entry_password.get()
#         repassword = self.entry_repassword.get()

#         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#         if not re.match(email_pattern, email):
#             print("Invalid email address")
#             return

#         if password != repassword:
#             print("Password didnot match")
#             return

#         print("Full Name:", fullname)
#         print("Email:", email)
#         print("Phone Number:", phone)
#         print("Password:", password)
#         print("Re-entered Password:", repassword)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = RegisterPage(master=root)
#     app.mainloop()


import tkinter as tk
from pages import login,signup,home

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("640x480")

        # self.show_login_page()
        home_page = home.HomePage(self)

    def show_login_page(self):
        self.login_page = login.LoginPage(self)
        self.login_page.pack(fill="both", expand=True)

    def show_register_page(self):
        self.login_page.destroy()
        self.register_page = signup.RegisterPage(self)
        self.register_page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
