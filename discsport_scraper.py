import requests
from time import sleep
from bs4 import BeautifulSoup
import re

SLEEPY_TIME = 60 * 20


def is_available(url) -> bool:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    for i, lead in enumerate(soup.findAll("div", attrs={'class': re.compile(r".*lead")})):
        if "Slutsåld" in lead.text:
            return False
    return True
        


if __name__ == "__main__":
    reference_item = "https://discsport.se/art/2966" # Should be in stock
    wanted_item = "https://discsport.se/art/3093"
    while not is_available(wanted_item):
        if not is_available(reference_item):
            print("[*] Reference item does not seem to be available. Check your code or find a new reference item thats in stock!")
        print("[*] Item is not available...")
        sleep(SLEEPY_TIME)
    print("[!] Item is available!")





