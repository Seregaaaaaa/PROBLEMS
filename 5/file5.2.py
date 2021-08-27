#Словарь №1:
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
x = {'besh_barmak' : 130}
menu.update(x)
print(menu)
menu.update({'lagman': 135})
print(menu)
menu.pop('borsh')
print(menu)
menu.update({'drinks': ['Cola-Cola', 'Sprite', 'Fanta']})
print(menu)
#Список № 2
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
#problem 020
set = {'.add("*")','.remove("*")','.clear()','.difference("*")','.update("*")','.discard("*")','.intersection("*")','.intersection_update(*)','.pop()'}
set2 = {'.clear()','.get("*")','.keys()','.values()','.items()','.update("*")'}
print(set.intersection(set2))
#problem 31
x = 0
set = {}
while x < 3:
	name = input("Введите ваше имя>")
	password = input("Введите ваш пароль>")
	set.update({name: password })
	x = x + 1
print(set)
#problem 27
prof = {'Anton': 'podvodnik' , 'Andrew': 'pojarnik', 'Leha': 'vrach', 'Merbek': 'programmist', 'mashsa': 'kassir'}
