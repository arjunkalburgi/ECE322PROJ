import sqlite3
import os
import app_files.login as login
import app_files.database as database

database.connectDB()
login.start()
