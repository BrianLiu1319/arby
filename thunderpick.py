from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



driver = webdriver.Chrome()
url = "https://thunderpick.io/esports/valorant"
driver.get(url)

driver.implicitly_wait(5)

html_source =  driver.page_source

html_source_code = driver.execute_script("return document.body.innerHTML;")
soup = BeautifulSoup(html_source_code, 'html.parser')

with open("thunderpick.html", "a", encoding="utf-8") as file:
        file.write(soup.prettify())









