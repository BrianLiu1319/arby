import rivalry as rv
import thunderpick as tp
from bs4 import BeautifulSoup
import requests
import sqlite3


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
    print("successfully updated rv")
    tp.update_tp_html()
    print("successfully updated tp")
    
# parse html
def parse_html():
    '''
    parse thru html and return tuple of TEAMA and TEAMB
    input: none 
    output: {TEAMA, TEAMB}
    '''
    import os
    
    if not os.path.exists("rivalry.html") or not os.path.exists("thunderpick.html"):
        print("html not available, exiting")
        exit()
        
# update html
update_html()

    



# Make a team class for easier storage:
# class team: event,time,odds
# we want two fucntions to return tuples of : {event, time, TEAM_A, TEAM_B}
# fuzzy match with events, teama and teamb to pair and return {{tp ,{tuple}}, {rv, {tuple}}}


# TODO 
# match up teams between both data sets
# pair them up into sqllite
# host on ac3
# perform arbitrage
# create a front facing website?


