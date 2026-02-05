import tkinter as tk
from tkinter import ttk, colorchooser
import os

CONFIG_FILE = "config.txt"

DEFAULT_COLOR = "#F6D6E8"

def save_color(color):
    with open(CONFIG_FILE, "w") as f:
        f.write(color)

def load_color():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    return DEFAULT_COLOR

def choose_color():
    color_code = colorchooser.askcolor(title="Виберіть колір фону")[1]
    if color_code:
        root.config(bg=color_code)
        main_tab.config(bg=color_code)
        settings_tab.config(bg=color_code)
        about_tab.config(bg=color_code)
        info_label.config(bg=color_code)
        save_color(color_code)

root = tk.Tk()
root.title("Програма з вкладками")
root.geometry("500x400")

bg_color = load_color()
root.config(bg=bg_color)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# --- Головна вкладка ---
main_tab = tk.Frame(notebook, bg=bg_color)
notebook.add(main_tab, text="Головна")

tk.Label(main_tab, text="Ім'я:", bg=bg_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(main_tab)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(main_tab, text="Вік:", bg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_age = tk.Entry(main_tab)
entry_age.grid(row=1, column=1, padx=10, pady=10)

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    info_label.config(text=f"Ім'я: {name}\nВік: {age}")

tk.Button(main_tab, text="Відправити", command=submit_form).grid(
    row=2, column=0, columnspan=2, pady=10
)

info_label = tk.Label(main_tab, text="", justify="left", bg=bg_color)
info_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# --- Налаштування ---
settings_tab = tk.Frame(notebook, bg=bg_color)
notebook.add(settings_tab, text="Налаштування")

tk.Label(settings_tab, text="Виберіть колір фону:", bg=bg_color).pack(pady=20)
tk.Button(settings_tab, text="Обрати колір", command=choose_color).pack(pady=10)

# --- Про програму ---
about_tab = tk.Frame(notebook, bg=bg_color)
notebook.add(about_tab, text="Про програму")

tk.Label(
    about_tab,
    text="Красивий записничок \nкористуватись з задоволенням",
    bg=bg_color,
    font=("Arial", 16, "bold"),
).pack(pady=50)

root.mainloop()
