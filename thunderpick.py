from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# convert pst to utc
from datetime import datetime, timedelta, timezone





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


def convert_time(p_time):
    # Parse the input time string
    pdt_pst_hour, pdt_pst_minute = map(int, p_time.split(':'))

    # Get the current UTC time
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)

    # Calculate the current time in Pacific Time (PT) timezone
    pt_now = utc_now.astimezone(timezone(timedelta(hours=-7 if is_pdt() else -8)))

    # Replace the hour and minute with the parsed PT time
    pt_now = pt_now.replace(hour=pdt_pst_hour, minute=pdt_pst_minute, second=0, microsecond=0)

    # Convert PT time to UTC
    utc_time = pt_now.astimezone(timezone.utc)

    return utc_time.strftime('%H:%M')

def is_pdt():
    # Check if the current date is within the daylight saving time period (March - November)
    current_month = datetime.utcnow().month
    return current_month > 3 and current_month < 11

def parse_thunderpick():
    # input : none - just read html file from update html
    # output : tuple {{teama,odd}, {teamb,odds}, date, time}
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
    time = [convert_time(i) for i in time]
    
    # TODO: PDT -> UTC converter
    # TODO: Figure which matches have which days
    # TODO: JAM date + time together
    # TODO: REMOVE UTC from rivalry
    # TODO: JAM matches + date+time
    
    # we need to figure our which matches for which dates.
    print(len(dates))
    print(time)
    
    # ['13:46', '12:00', '15:00', '18:00', '09:00', '10:00', '11:00', '12:00', '13:00', '16:00']
    # ['21:46', '20:00', '23:00', '02:00', '17:00', '18:00', '19:00', '20:00', '21:00', '00:00']

    










