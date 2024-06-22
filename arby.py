import rivalry as rv
import thunderpick as tp
from bs4 import BeautifulSoup
import requests
import sqlite3


def update_html():
    """
    simply update html of both rv and tp
    
    input : none
    output: none
    """

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
    """
    parse thru html of rv and tp
    
    input: none
    output: dict (rv), dict (tp) 
    """
    import os

    if not os.path.exists("rivalry.html") or not os.path.exists("thunderpick.html"):
        print("html not available, exiting")
        exit()
        
    rv_dict = rv.parse_rivalry()
    tp_dict = tp.parse_thunderpick()
    
    return rv_dict, tp_dict
    

# update html
# update_html()


rv_dict, tp_dict = parse_html()

print(rv_dict.keys())
print('\n\n\n\n')
print(rv_dict)
print('\n\n\n\n')
print(tp_dict)

# get list of dates and now we want to 

# TODO
# match up teams between both data sets
# pair them up into sqllite
# host on ac3
# perform arbitrage
# create a front facing website?
