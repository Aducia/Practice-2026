import tkinter as tk
from tkinter import colorchooser, filedialog

class GraphicsApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Графіка")

       self.draw_color = "black"
       self.draw_mode = tk.StringVar(value="circle")  # circle або line
       self.start_x = None
       self.start_y = None

       toolbar = tk.Frame(root)
       toolbar.pack(side="top", fill="x")

       tk.Button(toolbar, text="Вибрати колір", command=self.choose_color).pack(side="left", padx=5)
       tk.Radiobutton(toolbar, text="Коло", variable=self.draw_mode, value="circle").pack(side="left")
       tk.Radiobutton(toolbar, text="Лінія", variable=self.draw_mode, value="line").pack(side="left")
       tk.Button(toolbar, text="Очистити", command=self.clear_canvas).pack(side="left", padx=5)
       tk.Button(toolbar, text="Зберегти", command=self.save_canvas).pack(side="left", padx=5)

       self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
       self.canvas.pack()

       self.canvas.bind("<Button-1>", self.on_click)
       self.canvas.bind("<B1-Motion>", self.on_drag)
       self.canvas.bind("<ButtonRelease-1>", self.on_release)

   def choose_color(self):
       color_code = colorchooser.askcolor(title="Виберіть колір")[1]
       if color_code:
           self.draw_color = color_code

   def clear_canvas(self):
       self.canvas.delete("all")

   def save_canvas(self):
       file_path = filedialog.asksaveasfilename(defaultextension=".ps",
                                                filetypes=[("PostScript files", "*.ps")])
       if file_path:
           self.canvas.postscript(file=file_path)
           tk.messagebox.showinfo("Збережено", f"Зображення збережено у {file_path}")

   def on_click(self, event):
       self.start_x = event.x
       self.start_y = event.y
       if self.draw_mode.get() == "circle":
           self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill=self.draw_color, outline=self.draw_color)

   def on_drag(self, event):
       if self.draw_mode.get() == "line":
           self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.draw_color)
           self.start_x = event.x
           self.start_y = event.y
       elif self.draw_mode.get() == "circle":
           self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill=self.draw_color, outline=self.draw_color)

   def on_release(self, event):
       self.start_x = None
       self.start_y = None

root = tk.Tk()
app = GraphicsApp(root)
root.mainloop()

