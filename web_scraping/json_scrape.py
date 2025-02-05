from bs4 import BeautifulSoup
import requests
import json

def main():
        url = "https://www.trebesin.cz/"

        response = requests.get(url) #pythnovina
        soup = BeautifulSoup(response.content, "html.parser")

        all_p = soup.find_all("p") #jde i select
    
        # for p in all_p:
        #     print(p.text)

        array = []

        for p in all_p:
            array.append(p.text)

        with open("trebesin_data.json", mode="w") as soubor:
            json.dump(array, soubor, indent=4, ensure_ascii=False)
            



if __name__ == "__main__":
        main()