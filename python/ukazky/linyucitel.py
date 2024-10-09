import random
import tkinter as tk

znamky = [1, 2, 3, 4, 5]

root = tk.Tk()
root.title("Guacamole")

# sum = 0
# count = 0

random_znamka = ""
aver = ""
aver_mark = []
def znamka():
    # jmeno = input("Jméno studenta?")
    jmeno = entry.get()
      

    if jmeno == "Monika":
        random_znamka = random.choices(znamky, weights=(40, 20, 20, 20, 0), k=1)
        print(random_znamka[0])
        aver_mark.append(random_znamka[0])
        
    else:
        random_znamka = random.choice(znamky)
        print(random_znamka)
        aver_mark.append(random_znamka)
         
    aver = sum(aver_mark)/len(aver_mark)
    cislo.config(text=random_znamka)
    prumer.config(text=aver)

    
label = tk.Label(root, text="Jméno studenta?")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

cislo = tk.Label(root, text= random_znamka)
cislo.pack(pady=10)

prumer = tk.Label(root, text= aver)
prumer.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=znamka)
submit_button.pack(pady=5)



root.mainloop()
