# trying to learn sqlite3 xDDD

from team import *
import sqlite3


class Database:
    conn = sqlite3.connect("match.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    def __init__(self):
        self.create_table()

    def create_table(self):
        with self.conn:
            self.c.execute(
                """
                CREATE TABLE IF NOT EXISTS matches (
                    date TEXT,
                    team_a_name TEXT,
                    team_a_odd_rv REAL,
                    team_a_odd_tp REAL,
                    team_b_name TEXT,
                    team_b_odd_rv REAL,
                    team_b_odd_tp REAL
                )
            """
            )

    def insert_match(self, match):
        with self.conn:
            # check if match already exists
            if not self.fetch_match(match):
                self.c.execute(
                    "INSERT INTO matches VALUES (\
                    :date, \
                    :team_a_name,  \
                    :team_a_odd_rv, \
                    :team_a_odd_tp, \
                    :team_b_name,  \
                    :team_b_odd_rv, \
                    :team_b_odd_tp)",
                    {
                        "date": match.date,
                        "team_a_name": match.team_a.name,
                        "team_a_odd_rv": match.team_a.odd_rv,
                        "team_a_odd_tp": match.team_a.odd_tp,
                        "team_b_name": match.team_b.name,
                        "team_b_odd_rv": match.team_b.odd_rv,
                        "team_b_odd_tp": match.team_b.odd_tp,
                    },
                )
 
    def get_all_matches(self):
        rows = self.conn.execute("SELECT * FROM matches").fetchall()
        lst = []
        for i in rows:
            lst.append(dict(i))
        return lst

    def fetch_match(self, match):
        with self.conn:
            self.c.execute(
                "SELECT * FROM matches WHERE \
                    date=:date AND \
                    team_a_name=:team_a_name AND \
                    team_b_name=:team_b_name ",
                {
                    "date": match.date,
                    "team_a_name": match.team_a.name,
                    "team_b_name": match.team_b.name,
                },
            )
        return self.c.fetchall()

    def update_match(self, match):
        pass
        # with self.conn:
        #     if self.fetch_match(match):
        #         self.c.execute("""""")

    def delete_match(self, match):
        with self.conn:
            if self.fetch_match(match):
                self.c.execute(
                    "DELETE FROM matches WHERE \
                    date=:date AND \
                    team_a_name=:team_a_name AND \
                    team_b_name=:team_b_name ",
                    {
                        "date": match.date,
                        "team_a_name": match.team_a.name,
                        "team_b_name": match.team_b.name,
                    },
                )

    def close_db(self):
        # exits our sqlite3 connection
        self.conn.close()

# conn = sqlite3.connect("match.db")
# c = conn.cursor()
# rows = conn.execute('SELECT * FROM matches').fetchall()

# for row in rows:
#     print(dict(row))
