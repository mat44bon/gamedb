# --- mylib.py
# --- Made by zaba
# --- https://github.com/mat44bon
# --- Feel free to add more functions and useful thing here !


# this will add some colors to your program
'''
usage :
print(f'{bcolors.RED}this text will be red{bcolors.ENDC}')

ENDC reset the formatting of the text
'''
class bcolors:
	RED = '\033[91m'
	GREEN = '\033[92m'
	BLUE = '\033[94m'
	MAGENTA = '\033[95m'
	YELLOW = '\033[93m'
	CYAN = '\033[96m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	ITALIC = '\033[3m'
	ENDC = '\033[0m'