from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
    response = requests.get("https://www.rivalry.com/esports/valorant-betting")
    soup = BeautifulSoup(response.content, "html.parser")
    

    with open("rivalry.html", "a", encoding="utf-8") as file:
        file.write(soup.prettify())
    
    # for future brian idk i kinda give up -> pressing button 2 hard
    
    # options = webdriver.ChromeOptions()
    # userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
    # options.add_argument(f"user-agent={userAgent}")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # url = "https://www.rivalry.com/esports/valorant-betting"
    # driver.get(url)
    
    # css_selector = '.text-sm.text-orange.text-center.uppercase.cursor-pointer.hover\\:text-bloodorange-dark'
    
    # div_element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    # )
    # div_element.click()
    # # div_element = driver.find_element('text-sm text-orange text-center uppercase cursor-pointer hover:text-bloodorange-dark').click()
    
    # html_source_code = driver.execute_script("return document.body.innerHTML;")
    # soup = BeautifulSoup(html_source_code, "html.parser")

    # with open("rivalry.html", "a", encoding="utf-8") as file:
    #     file.write(soup.prettify())
        
    # driver.quit()

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


