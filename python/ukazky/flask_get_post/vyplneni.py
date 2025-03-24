from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

name = "Souhrada"
trida = "69"
message = "pomoc"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000/form") #AHOJ VŠICHNI 

        page.fill('input[id="name"]', name)
        page.fill('input[id="class"]', trida)
        page.fill('textarea[id="message"]', message)

        page.click('button[id="button"]')

        # page.click('button[id="loginbtn"]')


        input("KLikni na cokoliv pro zavření prohlížeče")
        browser.close()



if __name__ == "__main__":
    main()
