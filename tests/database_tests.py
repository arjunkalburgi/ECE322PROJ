import sys
import sqlite3
from time import strftime

# start sqlite database connection
def connectDB():
    global conn
    global c
    conn = sqlite3.connect('test_db_files/test.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

