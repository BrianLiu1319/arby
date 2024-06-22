from bs4 import BeautifulSoup
import requests
import dateparser


# update rivalry.html
def update_rivalry_html():
    response = requests.get("https://www.rivalry.com/esports/valorant-betting")
    soup = BeautifulSoup(response.content, "html.parser")

    with open("rivalry.html", "a", encoding="utf-8") as file:
        file.write(soup.prettify())


# parse rivalry html
def parse_rivalry():
    """
    # input: none (just read from html)
    # output : dict {'time' : {'teama': odd, 'teamb': odd} }

    """
    with open("rivalry.html", "r", encoding="utf-8") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
        bets = [i for i in soup.find_all(class_="betline m-auto betline-wide mb-0")]

    parsed_dict = dict()
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
        time = (
            i.find(class_="text-navy dark:text-[#CFCFD1] leading-3 text-[11px]")
            .get_text()
            .split()
        )
        time.insert(2, "2024")
        time = " ".join(time)
        time = dateparser.parse(time)
        time = time.strftime("%Y-%m-%d")
        

        bundle = dict(zip(teams, odds))
        
        if time in parsed_dict:
            parsed_dict[time].append(bundle)
        else:
            parsed_dict[time] = list()
            parsed_dict[time].append(bundle)

    return parsed_dict

print(parse_rivalry())