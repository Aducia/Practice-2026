import tkinter as tk
from logic import process_text

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modular App")

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(padx=10, pady=5)

        self.button = tk.Button(self.root, text="Process", command=self.on_click)
        self.button.pack(pady=5)

        self.label = tk.Label(self.root, text="")
        self.label.pack(pady=5)

    def on_click(self):
        text = self.entry.get()
        result = process_text(text)
        self.label.config(text=result)

    def run(self):
        self.root.mainloop()