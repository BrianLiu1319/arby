import rivalry as rv
import thunderpick as tp

from bs4 import BeautifulSoup
import requests
import sqlite3

# response = requests.get("https://thunderpick.io/esports/valorant")
# soup = BeautifulSoup(response.content, "html.parser")
# with open("thunderpick.html", "a", encoding="utf-8") as file:
#     file.write(soup.prettify())

# print(soup.prettify())


def update_html():
    '''
    simply update html of both rv and tp
    input : none
    output: none
    '''
    
    # check if html exists delete elsewise
    
    import os
    if os.path.exists("rivalry.html"):
        os.remove("rivalry.html")
        print("successfully removed rv")
        
    
    if os.path.exists("thunderpick.html"):
        os.remove("thunderpick.html")
        print("successfully removed tp")
        
    rv.update_rivalry_html()
    print("updated rv")
    tp.update_tp_html()
    print("updated tp")
    
# update html
update_html()

# parse html



# Make a team class for easier storage:
# class team: event,time,odds
# we want two fucntions to return tuples of : {event, time, {teama,odds}, {teamb,odds}}
# fuzzy match with events, teama and teamb to pair and return {{tp ,{tuple}}, {rv, {tuple}}}


# TODO 
# match up teams between both data sets
# pair them up into sqllite
# host on ac3
# perform arbitrage
# create a front facing website?


