from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def update_tp_html():
    driver = webdriver.Chrome()
    url = "https://thunderpick.io/esports/valorant"
    driver.get(url)

    driver.implicitly_wait(5)

    html_source =  driver.page_source

    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, 'html.parser')

    with open("thunderpick.html", "a", encoding="utf-8") as file:
            file.write(soup.prettify())
            
# # def parse_rivalry():
#     with open("rivalry.html", "r", encoding="utf-8") as file:
#         contents = file.read()
#         soup = BeautifulSoup(contents, "html.parser")
#         bets = [i for i in soup.find_all(class_="betline m-auto betline-wide mb-0")]

#     rivalry_parsed = dict()
#     for i in bets:
#         # [BLEED, PRX]
#         teams = [
#             " ".join(j.get_text().split()) for j in i.find_all(class_="outcome-name")
#         ]
#         # [5.0, 1.9]
#         odds = [
#             " ".join(j.get_text().split()) for j in i.find_all(class_="outcome-odds")
#         ]
#         # Apr 27 08:00 UTC
#         time = " ".join(
#             i.find(class_="text-navy dark:text-[#CFCFD1] leading-3 text-[11px]")
#             .get_text()
#             .split()
#         )
#         # {BLEED: 5.0, PRX:1.9}
#         bundle = dict(zip(teams, odds))
#         rivalry_parsed[time] = bundle

#     return rivalry_parsed


with open("thunderpick.html", "r", encoding="utf-8") as file:
    contents = file.read()
    soup = BeautifulSoup(contents, "html.parser")
    
a = soup.find_all(class_='match-group')

print(len(a))









