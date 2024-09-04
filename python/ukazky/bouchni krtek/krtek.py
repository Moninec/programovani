import tkinter as tk
import random

root = tk.Tk()
root.title("Guacamole")

score = 0

current_mole = None
moles = []

def choose_mole():
    global moles, current_mole
    current_mole = random.choice(moles)
    current_mole.config(bg="red")

def whac(event):
    global score
    if event.widget == current_mole: #widget = na co klikneš
        score += 1
        label.config(text=f"Score: {score}")
    # if event.widget

def create_grid():
    for row in range(3):
        for col in range(3):
            mole = tk.Button(root, text="", width=12, height=5, bg="green")
            mole.bind("<Button-1>", whac) #<Button-1> je levý talčítko myši
            mole.grid(row=row, column=col)
            moles.append(mole)

create_grid()

label = tk.Label(root, text=f"Score: {score} ")
label.grid(row=4, column=0)


root.mainloop()