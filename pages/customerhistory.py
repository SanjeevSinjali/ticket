# customerhistory.py

import tkinter as tk
from tkinter import ttk
from components import dashboard

class CustomerPage(tk.Frame):
    def __init__(self, master=None, dashboard=None):
        super().__init__(master)
        self.master = master
        self.master.title("Customer History Page")
        self.master.geometry("700x650")
        self.master.resizable(False, False)
        self.dashboard = dashboard
        
        self.Page()

    def Page(self):
        # Dashboard section
        self.dashboard.pack(side="left", fill="y",expand=True)

        # Content section
        content_frame = tk.Frame(self.master)
        content_frame.pack(side="right", expand=True)

        welcome_lbl = ttk.Label(content_frame, text="History!")
        welcome_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        next_btn = ttk.Button(content_frame, text="Next")
        next_btn.grid(row=1, column=0, padx=10, pady=10, sticky="e")
