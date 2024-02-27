# settings_page.py

import tkinter as tk
from tkinter import ttk
from components import dashboard

class SettingsPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Settings Page")
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        
        self.Page()

    def Page(self):
        # Dashboard integration
        dashboard_page = dashboard.Dashboard(self)
        dashboard_page.pack(fill="both", expand=True)

        # Other components specific to the settings page
        ttk.Label(self, text="Settings Page Content").pack()
