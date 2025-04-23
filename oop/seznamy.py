seznam_ovoce = ["jablko", "mandarinka", "pomeranč", "banán"]

seznam_ovoce.append("kiwi")

print(seznam_ovoce[1])

print(len(seznam_ovoce)) #počet prvků v seznamu

seznam_ovoce[0] = "hruška"

odebrane_ovoce = seznam_ovoce.pop(1) #odebere prvek
print(f"Bylo odebráno ovoce: {odebrane_ovoce}")

for index, ovoce in enumerate(seznam_ovoce):
    print(f"{index+1}. {ovoce}")

if "pomeranč" in seznam_ovoce:
    print("YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY")

tel_seznam = {
    "Květoslav": "777 123 456",
    "Jarmila": "666 666 666",
    "Kazi": "369 562 856"
}

for key in tel_seznam.keys():
    print(key)

    
for v in tel_seznam.values():
    print(v)

for x in tel_seznam: #dělá to stejné jako keys
    print(x)

for key, value in tel_seznam.items():
    print(key, value)


tel_seznam["Kazi"]
tel_seznam.get("Kazi", "Nic tu není") #get umožňuje napsat alternativní výpis, pokud tam originální není