

import sqlite3

with sqlite3.connect('Roster.db') as conn:
    c = conn.cursor()
    roster = ("""CREATE TABLE IF NOT EXISTS tbl_roster""")
