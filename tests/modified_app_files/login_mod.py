import sys
from software.app_files.database import getUser
from software.app_files.database import createUser

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
		return True
	elif user['role'] == 'N':
		return True
	elif user['role'] == 'A':
		return True
	return False

def start(username, password, boolNewUser):

	user = getUser(encrypt(username), encrypt(password)) # return obj of user info, or None if can't be found

	if user is not None:
		return "Begin user flow"
	else:
		if boolNewUser:
			user = createUser(raw_input("Role (D, N or A) "), raw_input("Name "), encrypt(username), encrypt(password))
			return "Create user flow"
		else:
			return "start()"
