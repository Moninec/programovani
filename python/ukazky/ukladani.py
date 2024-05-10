with open("H:\\programovani\\python\\ukazky\\data.txt", "r") as soubor:
    print(soubor.read())

#soubor = open("H:\\programovani\\python\\ukazky\\data.txt", "r") #otevrit program, cist
#file.close()

with open("H:\\programovani\\python\\ukazky\\data.txt", "a") as soubor:
    text = "\nNOOOOOO"
    soubor.write(text)