# --- gameDB.py
# --- Made by zaba
# --- https://github.com/mat44bon
# --- Feel free to make your own modifications from this program !

import os, sqlite3
from gamedblib import *

gameDB = sqlite3.connect('game.db')
cursor = gameDB.cursor()

cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\';')
tables = cursor.fetchall()

if len(tables) == 0:
	createDB(cursor, gameDB) # checking if the table exists, if not, it will create it

dataNames = ['Name', 'Release date (dd.mm.yyyy)', 'Developer', 'Publisher', 'Platform', 'Web site'] # values in the database for each line

menu = ''
while not(menu == '4'):
	menu = main_menu()	# check gamedblib.py for the following functions
	if menu == '1':
		show_games(cursor)
	elif menu == '2':
		add_game(cursor, gameDB, dataNames)
	elif menu == '3':
		delete_game(cursor, gameDB)

os.system('clear')
gameDB.close()