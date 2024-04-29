from bs4 import BeautifulSoup
import requests


# update rivalry.html
def update_rivalry_html():
    response = requests.get("https://www.rivalry.com/esports/valorant-betting")
    soup = BeautifulSoup(response.content, "html.parser")

    with open("rivalry.html", "a", encoding="utf-8") as file:
        file.write(soup.prettify())


# parse rivalry html
def parse_rivalry():
    with open("rivalry.html", "r", encoding="utf-8") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
        bets = [i for i in soup.find_all(class_="betline m-auto betline-wide mb-0")]

    rivalry_parsed = dict()
    for i in bets:
        # [BLEED, PRX]
        teams = [
            " ".join(j.get_text().split()) for j in i.find_all(class_="outcome-name")
        ]
        # [5.0, 1.9]
        odds = [
            " ".join(j.get_text().split()) for j in i.find_all(class_="outcome-odds")
        ]
        # Apr 27 08:00 UTC
        time = " ".join(
            i.find(class_="text-navy dark:text-[#CFCFD1] leading-3 text-[11px]")
            .get_text()
            .split()
        )
        # {BLEED: 5.0, PRX:1.9}
        bundle = dict(zip(teams, odds))
        rivalry_parsed[time] = bundle

    return rivalry_parsed

print(parse_rivalry())
