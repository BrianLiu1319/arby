# trying to learn sqlite3 xDDD

import sqlite3


conn = sqlite3.connect('match.db')

c = conn.cursor()

c.execute("""CREATE TABLE matches(
        date text
        team_a text
        team_b text
    )""")

# commit the change action!
conn.commit()

# exits our sqlite3 connection
conn.close()
