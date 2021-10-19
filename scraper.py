from bs4 import BeautifulSoup
import requests
import json
import os
import random


main_url = "https://cocuklar-duymasin.fandom.com"
start_url = "/tr/wiki/Haluk"

character_urls = set()
character_urls.add(start_url)
visited_urls = set()

characters = []

while len(visited_urls) != len(character_urls):

    diff = character_urls - visited_urls
    sel = random.sample(diff, 1)[0]

    r = requests.get(main_url + sel)
    soup = BeautifulSoup(r.content, "lxml")

    c = {}
    c["url"] = sel
    c["title"] = soup.find("h1", {"class": "page-header__title"}).text.strip()

    try:  # Medeni Hali
        medeni_hal_div = soup.find("div", {"data-source": "medeni_hali"})
        medeni_hal_link = medeni_hal_div.find("a")
        c["medeni_hali"] = {
            "url": medeni_hal_link["href"],
            "title": medeni_hal_link["title"],
        }
        character_urls.add(c["medeni_hali"]["url"])
    except:
        c["medeni_hali"] = None

    try:
        ailesi_div = soup.find("div", {"data-source": "ailesi"})
        ailesi_links = ailesi_div.find_all("a")
        c["ailesi"] = [
            {"url": link["href"], "title": link["title"]} for link in ailesi_links
        ]
        for char in c["ailesi"]:
            character_urls.add(char["url"])
    except:
        c["ailesi"] = None

    try:
        ailesi_div = soup.find("div", {"data-source": "arkadaşlar"})
        ailesi_links = ailesi_div.find_all("a")
        c["arkadaşlar"] = [
            {"url": link["href"], "title": link["title"]} for link in ailesi_links
        ]
        for char in c["arkadaşlar"]:
            character_urls.add(char["url"])
    except:
        c["arkadaşlar"] = None

    try:
        ailesi_div = soup.find("div", {"data-source": "sevgili"})
        ailesi_links = ailesi_div.find_all("a")
        c["sevgili"] = [
            {"url": link["href"], "title": link["title"]} for link in ailesi_links
        ]
        for char in c["sevgili"]:
            character_urls.add(char["url"])
    except:
        c["sevgili"] = None

    visited_urls.add(sel)
    characters.append(c)

with open("characters.json", "w") as f:
    json.dump(characters, f)
