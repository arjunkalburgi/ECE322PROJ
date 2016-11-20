import sys
from software.app_files import database as db
from time import strftime
import pytest

def __init__(): 
	db.connectDB()

def test_getCurrentTime(): 
	assert db.getCurrentTime() == strftime("%Y-%m-%d %H:%M:%S")

