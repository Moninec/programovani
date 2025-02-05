import json  # Importuje modul json pro práci s JSON soubory

# Vytvoření slovníku s kategoriemi filmů a jejich hodnotami
filmy = {
    "komedie": "Tropická bouře",  # Klíč 'komedie' obsahuje jeden film jako řetězec
    "horror": ["Sinister", "To"],  # Klíč 'horror' obsahuje seznam dvou filmů
    "animák": ["Spongebob", "Na vlásku", "Lví král"],  # Klíč 'animák' obsahuje seznam tří filmů
    "muzikál": "Hamilton"  # Klíč 'muzikál' obsahuje jeden film jako řetězec
}

# Zápis slovníku 'filmy' do souboru 'data.json' ve formátu JSON
with open("data.json", mode="w") as soubor:  # Otevření souboru v režimu pro zápis ('w')
    json.dump(filmy, soubor, indent=4, ensure_ascii=False)  # Zápis dat do souboru s odsazením a podporou diakritiky

# Čtení dat ze souboru 'data.json' zpět do proměnné
with open("data.json", mode="r") as soubor:  # Otevření souboru v režimu pro čtení ('r')
    nactena_data = json.load(soubor)  # Načtení obsahu souboru do proměnné 'nactena_data'

# Vytištění načtených dat na konzoli
print(nactena_data)  # Výsledek: slovník se stejným obsahem, jaký byl uložen
