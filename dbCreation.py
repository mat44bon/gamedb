import os
import sqlite3
from mylib import *
from gamedblib import *

gameDB = sqlite3.connect('game.db')
cursor = gameDB.cursor()

cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\';')
tables = cursor.fetchall()

if len(tables) == 0:
	createDB(cursor, gameDB)

dataNames = ['Name', 'Release date (dd.mm.yyyy)', 'Developer', 'Publisher', 'Platform']

menu = 0
while not(menu == 4):
	menu = main_menu()
	if menu == 1:
		show_games(cursor, dataNames)
	elif menu == 2:
		add_game(cursor, gameDB, dataNames)
	elif menu == 3:
		delete_game(cursor, gameDB)
os.system('clear')
gameDB.close()