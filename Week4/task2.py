import tkinter as tk

root = tk.Tk()
root.title("Програма з кнопками")
root.geometry("400x200")

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

def greet():
   label.config(text="Вітаю, користувач!")

def clear():
   label.config(text="")

def exit_program():
   root.destroy()

btn_greet = tk.Button(root, text="Привітати", command=greet, width=15)
btn_clear = tk.Button(root, text="Очистити", command=clear, width=15)
btn_exit = tk.Button(root, text="Вийти", command=exit_program, width=15)

btn_greet.pack(pady=5)
btn_clear.pack(pady=5)
btn_exit.pack(pady=5)

root.mainloop()
