from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
import dateparser


# update rivalry.html
def update_rivalry_html():
    """
    simply update html for rivalry
    
    # input : none 
    # output : none - just output a html file
    """
    # response = requests.get("https://www.rivalry.com/esports/valorant-betting")
    # soup = BeautifulSoup(response.content, "html.parser")
    

    # with open("rivalry.html", "a", encoding="utf-8") as file:
    #     file.write(soup.prettify())
        
    options = webdriver.ChromeOptions()
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
    options.add_argument(f"user-agent={userAgent}")
    driver = webdriver.Chrome(options=options)
    url = "https://www.rivalry.com/esports/valorant-betting"
    driver.get(url)
    
    
    
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, 'text-sm text-orange text-center uppercase cursor-pointer hover:text-bloodorange-dark')))
    driver.find_element_by_class_name('text-sm text-orange text-center uppercase cursor-pointer hover:text-bloodorange-dark').click()
    
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, "html.parser")

    with open("rivalry.html", "a", encoding="utf-8") as file:
        file.write(soup.prettify())
        
update_rivalry_html()

# parse rivalry html
def parse_rivalry():
    """
    simply parse thru html
    
    # input: none (just read from html)
    # output : dict {'time' : {'teama': odd, 'teamb': odd} }

    """
    with open("rivalry.html", "r", encoding="utf-8") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
        bets = [i for i in soup.find_all(class_="betline m-auto betline-wide mb-0")]

    parsed_dict = dict()
    for i in bets:
        teams = [
            " ".join(j.get_text().split()) for j in i.find_all(class_="outcome-name")
        ]
        odds = [
            " ".join(j.get_text().split()) for j in i.find_all(class_="outcome-odds")
        ]
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


