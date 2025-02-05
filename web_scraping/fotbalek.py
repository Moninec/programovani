from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.arsenal.com/results"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    all_scores = soup.find_all(class_="scores__score")
    arsenal = soup.find(class_="scores__score--arsenal")
    # enemy = soup.find(class_="scores__score")

    # print (all_scores[1].text)

    score_a = int(arsenal.text)
    score_e = int(all_scores[1].text)

    if score_a > score_e:
          print("Učitel je spokojen")
    elif score_e > score_a:
          print("Učitel dá všem pětky")
    elif score_a == score_e:
          print("Učitel je zklamán")


    

if __name__ == "__main__":
        main()    