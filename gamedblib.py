# --- gamedblib.py
# --- Made by zaba
# --- https://github.com/mat44bon
# --- Feel free to add more functions and useful thing here !

import os
from mylib import *

def createDB(cursor, gameDB): # creates the table if it doesn't exist
	cursor.execute('CREATE TABLE GAMES ( Name VARCHAR(50), Release VARCHAR(10), Developer VARCHAR(50), Publisher VARCHAR(50), Platform VARCHAR(10))')
	gameDB.commit()

# creates the main menu of the database
# uses the formatting from mylib.py
def main_menu():
	os.system('clear')
	print(f'{bcolors.BOLD}Welcome in my games database !!!{bcolors.ENDC}\n'
		'1 - Display games\n'
		'2 - Add game\n'
		'3 - Delete game\n'
		'4 - Leave')
	choice = getch()
	return(choice)


def add_game(cursor, gameDB, dataNames): # needs the cursor, the database and the list of columns of the table
	os.system('clear')
	print('Adding a game\n')
	tData = []
	for i in range(0,5):
		tData.append(str(input(f'{dataNames[i]} : '))) # for each column, it asks to enter a value
	query = f"INSERT INTO GAMES VALUES ('{tData[0]}', '{tData[1]}', '{tData[2]}', '{tData[3]}', '{tData[4]}')"
	cursor.execute(query)
	gameDB.commit()



def show_games(cursor): # needs the cursor
	choice = str(input('Which values do you want to select? ( * for all) ')) # asks for the name of the game to delete
	print('\n')
	cursor.execute(f'SELECT {choice} FROM GAMES') # execute the SELECT query, returns all the games in a table
	rows = cursor.fetchall() # enter all the table in the rows variable
	for row in rows:
		line = str()
		for data in row:
			if len(data) > 20:
				data = data[0:16] + '...|' # if the data is longer than 20 characters, it will cut the name to a maximum of 20
			else:
				delimiter = (19 - len(data)) * ' ' # else, it will add spaces until reaching 20 characters
				data = data + delimiter + '|'
			line += data
		print(line) # prints the row of data all at once
	end = str(input('\nPress Enter to continue'))


def delete_game(cursor, gameDB): # needs the cursor and the database
	LANG = 'en'
	os.system('clear')
	print('Deleting a game\n')
	name = str(input('Enter the name of the game you want to delete : '))
	sure = str(input(f'Are you sure you want to delete this game : {name} [y/n]'))
	invalid(sure, LANG)
	if sure == 'y':
		cursor.execute(f'DELETE FROM GAMES WHERE Name = \'{name}\'') # deletes the game(s) where the name is the one selected
		gameDB.commit()
	else:
		print('No row deleted')