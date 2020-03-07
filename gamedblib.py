import os
from mylib import *
def createDB(cursor, gameDB):
	cursor.execute('CREATE TABLE GAMES ( Name VARCHAR(50), Release VARCHAR(10), Developer VARCHAR(50), Publisher VARCHAR(50), Platform VARCHAR(10))')
	gameDB.commit()

def main_menu():
	os.system('clear')
	print(f'{bcolors.BOLD}Welcome in my games database !!!{bcolors.ENDC}\n'
		'1 - Display games\n'
		'2 - Add game\n'
		'3 - Delete game\n'
		'4 - Leave\n')
	choice = int(input(':'))
	return(choice)

def add_game(cursor, gameDB, dataNames):
	os.system('clear')
	print('Adding a game\n')
	tData = []
	for i in range(0,5):
		tData.append(str(input(f'{dataNames[i]} : ')))
	query = f"INSERT INTO GAMES VALUES ('{tData[0]}', '{tData[1]}', '{tData[2]}', '{tData[3]}', '{tData[4]}')"
	cursor.execute(query)
	gameDB.commit()

def show_games(cursor, dataNames):
	#os.system('clear')
	choice = str(input('Which values do you want to select? ( * for all) '))
	print('\n')
	cursor.execute(f'SELECT {choice} FROM GAMES')
	rows = cursor.fetchall()
	for row in rows:
		line = str()
		for data in row:
			if len(data) > 20:
				data = data[0:16] + '...|'
			else:
				delimiter = (19 - len(data)) * ' '
				data = data + delimiter + '|'
			line += data
		print(line)
	end = str(input('\nPress Enter to continue'))

def delete_game(cursor, gameDB):
	os.system('clear')
	print('Deleting a game\n')
	name = str(input('Enter the name of the game you want to delete : '))
	sure = str(input(f'Are you sure you want to delete this game : {name} [y/n]'))
	while not(sure == 'y') :
		sure = str(input(f'Are you sure you want to delete this game : {name} [y/n]'))
	cursor.execute(f'DELETE FROM GAMES WHERE Name = \'{name}\'')
	gameDB.commit()