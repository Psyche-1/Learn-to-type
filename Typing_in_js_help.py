
symbols = {}

def check_some_symbol(file_name, some_symbol=' ', pr=False):
	# use for check some symbol

	with open('symbols/' + file_name + '.TXT') as f:
		for symbol in f.readlines():
			symbol, move = symbol.rstrip().split(' = ')
			symbols[symbol] = move.split(' - ')
	
	if pr:
		print(symbols[some_symbol])


text = []

def list_from_text(file_name, pr=False):
	# Do list from text for JS

	with open('text/' + file_name + '.TXT') as f:
		for line in f.readlines():
			line = line.rstrip()
			line = line.split()
			for w in range(len(line)):
				line[w] = line[w] + ' '
			
			text.extend(line)
	if pr:
		print(text)


wrong_symbols = []

def check_text(checking_text):
	global wrong_symbols
	
	for word in checking_text:
		for symbol in word:
			if symbol not in symbols:
				wrong_symbols.extend(symbol)
	
	wrong_symbols = list(set(wrong_symbols))
	for symbol in wrong_symbols:
		print(symbol + ' not in symbols')


replaces = {
	'eng': {
		#'r': 'Right', 'l': 'Left', 'rl': 'Right or Left',
		'r': '<img src="Typing_files/images/R.png" height=25px>', 'l': '<img src="Typing_files/images/L.png" height=25px>', 'rl': '<img src="Typing_files/images/L.png" height=25px><img src="Typing_files/images/R.png" height=25px>',
		's': 'Shift +', 'n': '', 'sa': 'Shift + Right Alt +', 'a': 'Right Alt +',
		'rw': '→', 'lw': '←', 'u': '↑', 'd': '↓', 'h': 'here',
		'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'
	},

		'rus': {
		#'r': 'Правой', 'l': 'Левой', 'rl': 'Правой или Левой',
		'r': '<img src="Typing_files/images/R.png" height=25px>', 'l': '<img src="Typing_files/images/L.png" height=25px>', 'rl': '<img src="Typing_files/images/L.png" height=25px><img src="Typing_files/images/R.png" height=25px>',
		's': 'Shift +', 'n': '', 'sa': 'Shift + Правый Alt +', 'a': 'Right Alt +',
		'rw': '→', 'lw': '←', 'u': '↑', 'd': '↓', 'h': 'на месте',
		'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'
	},

		'ukr': {
		#'r': 'Правою', 'l': 'Лівою', 'rl': 'Правою чи Лівою',
		'r': '<img src="Typing_files/images/R.png" height=25px>', 'l': '<img src="Typing_files/images/L.png" height=25px>', 'rl': '<img src="Typing_files/images/L.png" height=25px><img src="Typing_files/images/R.png" height=25px>',
		's': 'Shift +', 'n': '', 'sa': 'Shift + Правий Alt +', 'a': 'Right Alt +',
		'rw': '→', 'lw': '←', 'u': '↑', 'd': '↓', 'h': 'на місці',
		'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'
	}
}

def turn_symbol_to_js_dict(file_name):
	symbols_list = ''
	quote_all = "'"
	
	with open('symbols/' + file_name + '.TXT') as f:
		for symbol in f.readlines():
			symbol, move = symbol.rstrip().split(' = ')
			
			moves_str = ''
			moves = move.split(' - ')
			for move in moves:
				moves_str = moves_str + replaces[file_name][move] + ' '
			
			if symbol == "'":
				quote_all, quote_img = '"', "'"
			
			symbol = quote_all + symbol + quote_all + ': ' + quote_all + moves_str + quote_all +  ', '
			
			if quote_all != "'":
				quote_all, quote_img = "'", '"'
			
			symbols_list = symbols_list + symbol
	
	symbols_list = symbols_list.replace('''"'": " <img src="Typing_files/images/R.png" height=25px>''', '''"'": " <img src='Typing_files/images/R.png' height=25px>''')
	symbols_list = symbols_list.replace('''"'": " <img src="Typing_files/images/L.png" height=25px>''', '''"'": " <img src='Typing_files/images/L.png' height=25px>''')
	print(symbols_list)


def launch(language):
	check_some_symbol(language)  # Also add symbols in symbols
	#list_from_text(language)  #, True  # text for JS
	check_text(text)  # Do text have wrong_symbols which no in symbols?
	turn_symbol_to_js_dict(language)

#launch('ukr')  # 'eng', 'rus', 'ukr'
# python Typing_in_js_help.py

input('Exit')












