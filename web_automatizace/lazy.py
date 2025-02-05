from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

def main():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False) #vytvoření prohlížeče, (headless=False) = vidíme prohlížeč, jinak se to dějě na pozadí
        page = browser.new_page() #otevřeme novou stránku

        page.goto("https://www.moodle-trebesin.cz/") #jdeme na stránku třebešín moodle

        page.click('span[class="login pl-2"]')

        page.fill('input[id="username"]', login)
        page.fill('input[id="password"]', password)

        page.click('button[id="loginbtn"]')

        # prg_class = page.locator('span:has_text=("PRG - 4G - 24/25")')
        # print(prg_class)

        page.goto("https://moodle-trebesin.cz/course/view.php?id=277")
        page.locator('span:has_text=("PRG - 4G - 24/25")')

        page.goto("https://www.moodle-trebesin.cz/mod/quiz/view.php?id=20378")
        page.click('button[class="btn btn-primary"]')
        page.click('input[id="id_submitbutton"]')


        input("KLikni na cokoliv pro zavření prohlížeče")
        browser.close()

if __name__ == "__main__":
    main()