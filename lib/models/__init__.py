import sqlite3

CONN = sqlite3.connect('planet.db')
CURSOR = CONN.cursor()
