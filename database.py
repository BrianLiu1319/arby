# trying to learn sqlite3 xDDD

from team import *
import sqlite3

matches = [
    Match(
        date="2024-06-24",
        team_a=Team(name="RTZN", odd_rv="2.89", odd_tp=3.3),
        team_b=Team(name="VX300", odd_rv="1.35", odd_tp=1.28),
    ),
    Match(
        date="2024-06-24",
        team_a=Team(name="Eternal Fire", odd_rv="2.21", odd_tp=2.2),
        team_b=Team(name="Fenerbahce", odd_rv="1.57", odd_tp=1.58),
    ),
    Match(
        date="2024-06-24",
        team_a=Team(name="Acend", odd_rv="2.82", odd_tp=2.8),
        team_b=Team(name="Diamant", odd_rv="1.37", odd_tp=1.38),
    ),
    Match(
        date="2024-06-24",
        team_a=Team(name="DSYRE", odd_rv="1.34", odd_tp=1.32),
        team_b=Team(name="NOVO", odd_rv="2.90", odd_tp=3.1),
    ),
    Match(
        date="2024-06-24",
        team_a=Team(name="Cloud9", odd_rv="2.83", odd_tp=2.9),
        team_b=Team(name="G2", odd_rv="1.36", odd_tp=1.35),
    ),
    Match(
        date="2024-06-25",
        team_a=Team(name="OXEN", odd_rv="2.79", odd_tp=2.8),
        team_b=Team(name="All Knights", odd_rv="1.37", odd_tp=1.38),
    ),
    Match(
        date="2024-06-26",
        team_a=Team(name="ARENA Internet Cafe", odd_rv="1.07", odd_tp=1.1),
        team_b=Team(name="EDGE", odd_rv="6.71", odd_tp=5.8),
    ),
    Match(
        date="2024-06-27",
        team_a=Team(name="BOBO", odd_rv="1.77", odd_tp=1.8),
        team_b=Team(name="JFT", odd_rv="1.91", odd_tp=1.9),
    ),
    Match(
        date="2024-06-27",
        team_a=Team(name="FOCUSGG", odd_rv="1.34", odd_tp=1.35),
        team_b=Team(name="Rub n Pug", odd_rv="2.92", odd_tp=2.9),
    ),
    Match(
        date="2024-06-29",
        team_a=Team(name="OnlyFins", odd_rv="9.26", odd_tp=8.0),
        team_b=Team(name="Apeks", odd_rv="1.03", odd_tp=1.04),
    ),
]

conn = sqlite3.connect("match.db")

c = conn.cursor()



c.execute('''
    CREATE TABLE IF NOT EXISTS matches (
        date TEXT,
        team_a_name TEXT,
        team_a_odd_rv REAL,
        team_a_odd_tp REAL,
        team_b_name TEXT,
        team_b_odd_rv REAL,
        team_b_odd_tp REAL
    )
''')

match = matches[0]


def insert_match(match):
    with conn:
        c.execute("INSERT INTO matches VALUES (\
            :date, \
            :team_a_name,  \
            :team_a_odd_rv, \
            :team_a_odd_tp, \
            :team_b_name,  \
            :team_b_odd_rv, \
            :team_b_odd_tp)",
            {
                "date": match.date, \
                "team_a_name": match.team_a.name, \
                "team_a_odd_rv": match.team_a.odd_rv, \
                "team_a_odd_tp": match.team_a.odd_tp, \
                "team_b_name": match.team_b.name, \
                "team_b_odd_rv": match.team_b.odd_rv, \
                "team_b_odd_tp": match.team_b.odd_tp \
            }
        )

def get_matches():
    c.execute("SELECT * FROM matches")
    return c.fetchall()



# # commit the change action!
# conn.commit()
insert_match(matches[0])
print(get_matches())
# exits our sqlite3 connection
conn.close()


"""

@dataclass
class Team:
    name: str
    odd_rv : float
    odd_tp : float
            
    def __init__(self, name, odd_rv, odd_tp ):
        self.name = name
        self.odd_rv = odd_rv
        self.odd_tp = odd_tp
        
@dataclass
class Match:
    date: str
    team_a : Team
    team_b : Team
    
    def __init__(self, date, team_a, team_b):
        self.date = date
        self.team_a = team_a
        self.team_b = team_b
        
"""
