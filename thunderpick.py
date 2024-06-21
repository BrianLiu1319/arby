from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

from datetime import datetime, timedelta, timezone

def pacific_to_utc(pacific_time_str):
    # Define Pacific Time Zone (PT)
    PT = timezone(timedelta(hours=-8))  # PT is UTC-8
    
    # Parse the input time string
    pacific_time = datetime.strptime(pacific_time_str, "%H:%M")
    
    # Localize the time to PT
    pacific_time = pacific_time.replace(tzinfo=PT)
    
    # Convert to UTC
    utc_time = pacific_time.astimezone(timezone.utc)
    
    # Return the UTC time as a string
    return utc_time.strftime("%H:%M")


def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    while True:
        last_height = driver.execute_script("return document.body.scrollHeight")
        curr_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
        next_height = "window.scrollTo("+ str(curr_height) + "," + str(curr_height + 1000) + ");"
        
        # Scroll down to the bottom.
        driver.execute_script(next_height)
        
        # Wait to load the page.
        time.sleep(1)
        
        # Calculate new scroll height and compare with last scroll height.
        if curr_height >= last_height:
            break

        
def update_tp_html():
    options = webdriver.ChromeOptions()
    userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(options=options)
    url = "https://thunderpick.io/esports/valorant"
    driver.get(url)

    scroll_down(driver)
    
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, 'html.parser')

    with open("thunderpick.html", "a", encoding="utf-8") as file:
            file.write(soup.prettify())   
            
def odds_converter(odds):
    """
    Convert American odds to Decimal odds.
    
    Parameters:
    odds (int): American odds
    
    Returns:
    float: Decimal odds
    """
    if odds > 0:
        decimal_odds = 1 + (odds / 100)
    else:
        decimal_odds = 1 + (100 / abs(odds))
    
    return round(decimal_odds, 2)


def parse_thunderpick():
    """
    # input : none - just read html file from update html
    # output : dict {'time' : {'teama': odd, 'teamb': odd} }
    """
    
    with open("thunderpick.html", "r", encoding="utf-8") as file:
        contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
   
    # dates = soup.find(class_='match-group-title section-header')
    section = []
    # parse by each batch match bc this is weird
    ## match-group gives us all the matches happening on that date
    for i in soup.find_all(class_ = 'match-group'):
        section.append(str(i))   
        temp_soup = BeautifulSoup(str(i), "html.parser")
        
        # get batch match date: class="match-group-title section-header"
        dates = " ".join(temp_soup.find(class_='match-group-title section-header').text.split())
        
        # get time for each individual match : <div class="Igl6giMaBcs0doY3mQ6Y"> <span class=""> 02:00 </span>
        time = [" ".join(j.get_text().split()) for j in temp_soup.find_all(class_='Igl6giMaBcs0doY3mQ6Y')]  
        time = [pacific_to_utc(i)  for i in time]  
        
        # convert time
        
        # get team_as []
        teams_a = [" ".join(j.get_text().split()) for j in temp_soup.find_all(class_='JQKgtcAgUQTANhiXNrDX gcdjvGuPdJzgc15U5aZA')]
        # get team_bs []
        teams_b = [" ".join(j.get_text().split()) for j in temp_soup.find_all(class_='ndI7usEcCflSQxesRMDy gcdjvGuPdJzgc15U5aZA')]
        
        # get odds
        buttons = temp_soup.find_all('button')
        odds = []
        for k in buttons:
            t = k.get_text().split()
            if t:
                odds.append(odds_converter(int(t[0])))
            else:
                odds.append('nan')
        odds_a = odds[::2] 
        odds_b = odds[1::2]
        
        print(dates)
        print(time)
        # print(teams_a)
        # print(odds_a)
        # print(teams_b)
        # print(odds_b)
        
        # bundle team_a : odd and team_b : oddb
        team_dict = {}
        
        for i in range(len(teams_a)):
            team_dict[teams_a[i]] = odds_a[i]
            team_dict[teams_b[i]] = odds_b[i] 
            
        # bundle : {'dates + time': {teama:odd} {teamb:odd}, .... } 
        
   
    
parse_thunderpick()






