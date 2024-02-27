import tkinter as tk
from tkinter import ttk

class Dashboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.selected_button = tk.StringVar(value="Home")  # Variable to store the selected button

        # Image at the top
        img_label = tk.Label(self)
        img_label.pack(side="top", pady=10)
        img = tk.PhotoImage(file="/home/sanjeev/Desktop/Ticket/data/images/logo.png")
        img_label.config(image=img)
        img_label.image = img

        # Buttons in a column
        self.btn_home = ttk.Button(self, text="Home", command=lambda: self.set_selected_button("Home"))
        self.btn_home.pack(side="top", fill="x", padx=10, pady=5)

        self.btn_history = ttk.Button(self, text="History", command=lambda: self.set_selected_button("History"))
        self.btn_history.pack(side="top", fill="x", padx=10, pady=5)

        self.btn_settings = ttk.Button(self, text="Settings", command=lambda: self.set_selected_button("Settings"))
        self.btn_settings.pack(side="top", fill="x", padx=10, pady=5)

        self.buttons = [self.btn_home, self.btn_history, self.btn_settings]
        self.update_selected_button()

    def set_selected_button(self, button_name):
        print(button_name)
        self.selected_button.set(button_name)
        self.update_selected_button()

    def update_selected_button(self):
        for button in self.buttons:
            if button.cget("text") == self.selected_button.get():
                button.config(style="Selected.TButton")
            else:
                button.config(style="TButton")
