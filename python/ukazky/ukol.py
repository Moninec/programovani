bludistaci = {"Jirka": 1, "Jan": 3, "Petr": 2, "Marie": 1}



def vypisBludistakyPro():
  jmeno = input("Koho chceš zkontrolovat? ").capitalize()
  #if jmeno in bludistaci:
  print(jmeno, bludistaci[jmeno])


def vypisVse():
  for i in bludistaci:
    print(i, bludistaci[i])


def pridejBludistaka():
  pridat = input("Komu chceš bludišťáka přidat? ").capitalize()
  bludistaci[pridat] += 1
  print(pridat, bludistaci[pridat])


def odeberBludistaka():
  odebrat = input("Komu chceš bludišťáka odebrat? ").capitalize()
  bludistaci[odebrat] -= 1
  print(odebrat, bludistaci[odebrat])


def pridejStudenta():
  student = input("Přidej studenta/ku: ").capitalize()
  bludistaci[student] = 1
  print(student, bludistaci[student])


def nejvyssiSkore():
  nejvic = max(bludistaci, key=bludistaci.get)
  print("Nejvíce bludišťáku má: ").capitilize()
  print(nejvic, bludistaci[nejvic])

vypisBludistakyPro()
vypisVse()
pridejBludistaka()
odeberBludistaka()
pridejStudenta()
nejvyssiSkore()