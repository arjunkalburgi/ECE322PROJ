import sys
from .database import getUser
from .database import createUser
from .doctor import flow as d_flow
from .nurse import flow as n_flow
from .admin import flow as a_flow

def encrypt(s):
	r = ""
	for char in s:
		r = r + chr(ord(char) + 2)
	return r

def decrypt(s):
	r = ""
	for char in s:
		r = r + chr(ord(char) - 2)
	return r

def beginFlow(user):
	if user['role'] == 'D':
		d_flow(user)
	elif user['role'] == 'N':
		n_flow(user)
	elif user['role'] == 'A':
		a_flow(user)

def start():
	username = raw_input('Please login with your username: ')
	password = raw_input('And password: ')

	user = getUser(encrypt(username), encrypt(password)) # return obj of user info, or None if can't be found

	if user is not None:
		beginFlow(user)
	else:
		if raw_input("Not a user, would you like to make a new user with this username and password? (y) ") == "y":
			user = createUser(raw_input("Role (D, N or A) "), raw_input("Name "), encrypt(username), encrypt(password))
			beginFlow(user)
		else:
			start()
