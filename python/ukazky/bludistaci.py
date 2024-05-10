import csv, sys


def main():
    bludistaci = {}

    nactiTo(bludistaci)
    print("Zdravím cestovateli")
    print("Zvol možnost")
    print("pro vypsání všech bludišťáků zvol 1")
    print("pro vypsání jednoho studenta zvol 2")
    print("pro přidání bludišťáka zvol 3")
    print("pro odebrání bludišťáka zvol 4")
    print("pro vypsání nejlepšího studenta zvol 5")
    print("pro přidání studenta zvol 6")
    print("pro ukončení zvol 7")

    while True:
        try:
            zvolena_moznost = int(input())
            break
        except ValueError:
            print("AAAAAAAAA JÁ NEVIM")

    match zvolena_moznost:
        case 1:
            vypisVse(bludistaci)
        case 2:
            vypisBludistakyPro(bludistaci)
        case 3:
            pridejBludistaka(bludistaci)
        case 4:
            odeberBludistaka(bludistaci)
        case 5:
            nejvyssiSkore(bludistaci)
        case 6:
            pridejStudenta(bludistaci)
        case 7:
            print("byeeee")
            sys.exit()
        case _:
            print("Zvol číslo 1-7")

    ulozTo(bludistaci)


def vypisBludistakyPro(bludistaci):
    jmeno = input("Koho chceš zkontrolovat? ").capitalize()
    print(jmeno, bludistaci[jmeno])


def vypisVse(bludistaci):
    for i in bludistaci:
        print(i, bludistaci[i])


def pridejBludistaka(bludistaci):
    pridat = input("Komu chceš bludišťáka přidat? ").capitalize()
    bludistaci[pridat] += 1
    print(pridat, bludistaci[pridat])


def odeberBludistaka(bludistaci):
    odebrat = input("Komu chceš bludišťáka odebrat? ").capitalize()
    bludistaci[odebrat] -= 1
    print(odebrat, bludistaci[odebrat])


def pridejStudenta(bludistaci):
    student = input("Přidej studenta/ku: ").capitalize()
    bludistaci[student] = 1
    print(student, bludistaci[student])


def nejvyssiSkore(bludistaci):
    nejvic = max(bludistaci, key=bludistaci.get)
    print("Nejvíce bludišťáku má: ")
    print(nejvic, bludistaci[nejvic])


def ulozTo(bludistaci):
    with open("H:\\programovani\\python\\ukazky\\data.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")

        for name, number in bludistaci.items():
            writer.writerow([name, number])


def nactiTo(bludistaci):
    with open("H:\\programovani\\python\\ukazky\\data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")

        for lines in reader:
            bludistaci[lines[0]] = int(lines[1])

    print(bludistaci)


if __name__ == "__main__":
    main()
