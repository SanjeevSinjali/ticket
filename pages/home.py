# home_page.py

import tkinter as tk
from tkinter import ttk
from components import dashboard
from pages import customerhistory

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Home Page")
        self.master.geometry("700x650")
        self.master.resizable(False, False)

        self.dashboard = dashboard.Dashboard(self)

        self.Page()

    def Page(self):
        # Dashboard section
        self.dashboard.pack(side="left", fill="y", expand=True)  # Corrected line

        # Content section
        content_frame = tk.Frame(self.master)
        content_frame.pack(side="right", fill="both", expand=True)  # Adjusted side and fill

        welcome_lbl = ttk.Label(content_frame, text="Welcome Back!")
        welcome_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        next_btn = ttk.Button(content_frame, text="Next", command=self.nextPage)
        next_btn.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    def nextPage(self):
        
        next_page = customerhistory.CustomerPage(self.master, self.dashboard)
        self.destroy()

