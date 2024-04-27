import rivalry as rv

from bs4 import BeautifulSoup
import requests
import sqlite3

response = requests.get("https://thunderpick.io/esports/valorant")
soup = BeautifulSoup(response.content, "html.parser")
with open("thunderpick.html", "a", encoding="utf-8") as file:
    file.write(soup.prettify())

# print(soup.prettify())




