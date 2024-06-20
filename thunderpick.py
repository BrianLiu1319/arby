from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time



# convert pst to utc
from datetime import datetime, timedelta, timezone

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
        # section.append(str(i))   
        temp_soup = BeautifulSoup(str(i), "html.parser")
        
        # get batch match date: class="match-group-title section-header"
        dates = temp_soup.find(class_='match-group-title section-header').text
        
        # get time for each individual match : <div class="Igl6giMaBcs0doY3mQ6Y"> <span class=""> 02:00 </span>
        time = [" ".join(i.get_text().split()) for j in temp_soup.find_all(class_='Igl6giMaBcs0doY3mQ6Y')]    
        
        # convert time
        
        # get team_as []
        teams_a = [" ".join(i.get_text().split()) for j in temp_soup.find_all(class_='JQKgtcAgUQTANhiXNrDX gcdjvGuPdJzgc15U5aZA')]
        # get team_bs []
        teams_b = [" ".join(i.get_text().split()) for j in temp_soup.find_all(class_='ndI7usEcCflSQxesRMDy gcdjvGuPdJzgc15U5aZA')]
        
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
        
        # print(dates)
        print(teams_a)
        # print(odds_a)
        # print(teams_b)
        # print(odds_b)
        
        
        # check if class="odds-button__icon-container odds-button__icon-container--center" exists for odds change to NAN
        # maybe possibly by odds-button odds-button--theme-market odds-button--variant-dark and check if its disabled
        
        
        
        
    
    # contains teamsa, teamsb and odds, need to if else if <i class="ft ft-lock-2"> is contained to manually put 'NA'
    
    # teams_a = [" ".join(i.get_text().split()) for i in temp_soup.find_all(class_='JQKgtcAgUQTANhiXNrDX gcdjvGuPdJzgc15U5aZA')]
    # teams_b = [" ".join(i.get_text().split()) for i in temp_soup.find_all(class_='ndI7usEcCflSQxesRMDy gcdjvGuPdJzgc15U5aZA')]
    # odds = [odds_converter(int(" ".join(i.get_text().split()))) for i in temp_soup.find_all(class_='odds-button__odds')]   
    # odds = temp_soup.find_all(class_='odds-button odds-button--theme-market odds-button--variant-dark')
    
    
    
        
    
    
    
    
    #['April 29, 14:00', '00:00', '01:30', '02:30', '03:00', '03:30', '05:30', '13:00', '15:00', '16:30', '18:00', '02:30', '05:30', '08:00', '11:00', '02:30', '05:00', '05:30', '08:00', '11:00', '01:00', '04:00', '05:00', '08:00', '11:00', '02:00', '02:00', '05:00', '02:00', '05:00']
    # time = [" ".join(i.get_text().split()) for i in soup.find_all(class_='Igl6giMaBcs0doY3mQ6Y')]
    
    # TODO: PDT -> UTC converter
    # TODO: Figure which matches have which days
    # TODO: JAM date + time together
    # TODO: REMOVE UTC from rivalry
    # TODO: JAM matches + date+time
    
    # we need to figure our which matches for which dates.
    # print(dates)
    # print(time)
    
    # ['13:46', '12:00', '15:00', '18:00', '09:00', '10:00', '11:00', '12:00', '13:00', '16:00']
    # ['21:46', '20:00', '23:00', '02:00', '17:00', '18:00', '19:00', '20:00', '21:00', '00:00']

    


parse_thunderpick()






