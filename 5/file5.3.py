#problem 11
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
print(south_american_countries)
x = set(south_american_countries)
print(x)
#problem 101
suitcase = []
x = 0
while x < 5:
	vesh = input("вещь>")
	suitcase.append(vesh)
	x += 1
print(suitcase)
suitcase.pop(-1)
print(suitcase)
























#problem 27
prof = {'Anton': 'podvodnik' , 'Andrew': 'pojarnik', 'Leha': 'vrach', 'Merbek': 'programmist', 'Mashsa': 'kassir'}
keys = []
keys.extend(prof.keys())
x = 0 
while x < len(keys):
	name =  keys[x]
	proff = prof.get(name)
	print(f"Hello, {name}! Good profession {proff}!")
	x += 1
#problem 22
set = []
x = 0
while x < 20:
	password = int(input("Ведите чило>"))
	x += 1
	set.append(password)
	print(set)
tuple(set)

