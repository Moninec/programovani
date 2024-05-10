import csv

# with open("H:\\programovani\\python\\ukazky\\data.csv", "r") as f:
#     reader = csv.reader(f, delimiter=";")
#     for x in reader:
#         print(x)

with open("H:\\programovani\\python\\ukazky\\data.csv", "a", newline="") as f:
    jmeno = input("Zadek jméno: ")
    pocet = int(input("Zadek počet: "))
    writer = csv.writer(f, delimiter=";")
    writer.writerow([jmeno, pocet])