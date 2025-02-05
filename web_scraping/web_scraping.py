from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.trebesin.cz/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser") #html.parser předpřipravené procházení html

    paragraph = soup.p

    print(f"První odtsavec je: {paragraph.text}")

    gym = soup.find(id="favimagehover-title4") #class se značí jako - class_
    print(f"nazev oboru: {gym.text}")
    gym2 = soup.select("#favimagehover-title4") #na komplikovanejsi

    # all_p = soup.find_all("p")
    
    # for p in all_p:
    #       print(p.text)


if __name__ == "__main__":
        main()
