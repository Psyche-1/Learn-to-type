'''
https://www.youtube.com/watch?v=cK-hvG-Q9B0


Посмотреть, может можно через stdin или создать bat или ещё как-то, чтобы не запускать консоль для следующей команды

pyuic5 "E:\Временные\ПО\Код с редакцией на ноутбуке\Новые\Учиться печатать\Typing_view.ui" -x -o "E:\Временные\ПО\Код с редакцией на ноутбуке\Новые\Учиться печатать\Typing_view.py"
'''

def start():
	
	while True:
		mode = input('''Chose mode:
		1 for use standart text
		0 for paste your text
		''')
	
		if mode in ['0', '1', '']:
			break
	
	
	

	language = input('''Chose language:
	1 English
	2 Русский язык
	3 Українська мова
	0 Аll language				??????????
	''')


	if mode == '1' or mode == '':
		with open('Текст.TXT') as f:
			text = f.read()

	elif mode == '0':
		text = input('Paste text for typing:\n')

#start()


symbols = {}

with open('Symbol - move.TXT') as f:
	for symbol in f.readlines():
		symbol, move = symbol.rstrip().split(' = ')
		symbols[symbol] = move.split(' - ')

#print(symbols[' '])  # use for check some symbol



input('Exit')