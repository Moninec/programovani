import tkinter as tk

root = tk.Tk()
root.title("Skvělé GUI")
root.geometry("400x300")

label = tk.Label(root, text="meow")
label.pack()

def on_click():
    label.config(text="MEOW")

button = tk.Button(root, text=":3", command=on_click)
button.pack()


root.mainloop()