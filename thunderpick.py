from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



def update_tp_html():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    url = "https://thunderpick.io/esports/valorant"
    driver.get(url)

    driver.implicitly_wait(5)
    
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, 'html.parser')

    with open("thunderpick.html", "a", encoding="utf-8") as file:
            file.write(soup.prettify())
            
def odds_converter(odd):
    '''
    If the American odds are positive the formula is as follows: (American odds / 100) + 1 = decimal odds. 
    If the American odds are negative, the formula is as follows: (100 / American odds) + 1 = decimal odds.
    '''
    
    if odd < 0:
        bet = 100/odd + 1
    elif odd > 0:
        bet = odd/100 + 1
    else:
        bet = 0
    
    return round(bet,2)

def parse_thunderpick():
    with open("thunderpick.html", "r", encoding="utf-8") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
        
    teams_a = [" ".join(i.get_text().split()) for i in soup.find_all(class_='JQKgtcAgUQTANhiXNrDX gcdjvGuPdJzgc15U5aZA')]
    teams_b = [" ".join(i.get_text().split()) for i in soup.find_all(class_='ndI7usEcCflSQxesRMDy gcdjvGuPdJzgc15U5aZA')]
    odds = [odds_converter(int(" ".join(i.get_text().split()))) for i in soup.find_all(class_='odds-button__odds')]          
    
    odds_a = odds[1::2]
    odds_b = odds[::2]
   
    #somehow get it into Apr 27 08:00 UTC
   
    #['Featured', 'Tuesday, April 30th', 'Wednesday, May 1st', 'Thursday, May 2nd', 'Friday, May 3rd', 'Saturday, May 4th', 'Sunday, May 5th']
    dates = [" ".join(i.get_text().split()) for i in soup.find_all(class_='match-group-title section-header')]
    #['April 29, 14:00', '00:00', '01:30', '02:30', '03:00', '03:30', '05:30', '13:00', '15:00', '16:30', '18:00', '02:30', '05:30', '08:00', '11:00', '02:30', '05:00', '05:30', '08:00', '11:00', '01:00', '04:00', '05:00', '08:00', '11:00', '02:00', '02:00', '05:00', '02:00', '05:00']
    time = [" ".join(i.get_text().split()) for i in soup.find_all(class_='Igl6giMaBcs0doY3mQ6Y')]
    
    # TODO: PDT -> UTC converter
    # TODO: Figure which matches have which days
    # TODO: JAM date + time together
    # TODO: REMOVE UTC from rivalry
    # TODO: JAM matches + date+time
    
    print(dates)
    print(time)
    

    


    
# update_tp_html()
# parse_thunderpick()







