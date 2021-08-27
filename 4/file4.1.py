names = ['5', 'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', '6' , '7', 'Jhon', 'Jimmy', 'Jackson', '89', 'Jhon','Jack', 'Jimmy','87654', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack']
numbers = []
letters = []
x = 0
z = len(names)
while x < z:
	a = names[x]
	if  a.isnumeric():
		print(f"{a} является числом")
		numbers.append(a)
		print(f"Добавляем {a} в спсиок numbers...")
		print(f"Теперь список numbers состоит из {numbers}")
		x = x + 1
	else :
		print(f"{a} является словом")
		letters.append(a)
		print(f"Добавляем {a} в спсиок letters...")
		print(f"Теперь список letters  состоит из {letters}")
		x = x + 1
print("Операция закончина")
print(f'Список numbers состоит из {numbers}')
print(f'Список letters состоит из {letters}')
