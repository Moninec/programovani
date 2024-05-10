import sys

def kladne_zaporne(x):
    if x > 0:
        print ("Číslo je kladné")
    elif x < 0:
        print("číslo je záporné")
    else:
        print("číslo je nula")

while True:
    try: 
        cislo = int(input("Zadek číslo: "))
        kladne_zaporne(cislo)
        break
    except KeyboardInterrupt:
        print("Program odešel")
        sys.exit()
    except ValueError: #kdyby tam nebylo valuerror, tak není možné kod ukončit
        print("AAAAAAAAA JÁ NEVIM")
    else:
        print("Kod probehl uspesne")
        # break - muze bejt aj tady, aby se to ukazalo
    finally:
        print("Finally se vypíše vždycky")


