'''#problem 1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'Rust', 'javascript', 'ruby']
#Обязательное условие: если переменная в списке, то нужно вывести на экран 
for i in languages:
	if i == lang1:
		print('this languages is in list')

#Если этого языка нет в списке, ничего не нужно выводить.


#problem 2
#2. Будем работать с тем же списком: 
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
9. Сгенерировать 200 чисел от -100 до 100:
  1. Каждое число которое делиться на 13 без остатка возводить в квадрат если оно чётное
  2. Каждое 7 число проверять на НЕчестность и выводить на экран если оно нечётное.
  3. Посчитать сколько чисел подходят под первое условие
  4. Посчитать сколько чисел подходят под второе условие	if i == 'php':
		break
	print(i)
#С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит до “php”, цикл должен быть прерван.

#problem 3

# Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз.
i = 0
x = 7
while i < 5:
	x *= 7
	print(x)
	i += 1
#4. Напишите код, который выведет на экран список языков с нумерацией.
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
x = 1
for i in languages:
	print(x, i)
	x += 1
'''
'''Вывод:
 0 go
 1 java
 2 php
 3 python
 4 javascript
 5 ruby
'''
'''5. Напишите цикл который выведет на экран: 1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
Усиление:
Получите такой же результат но с ОДНИМ циклом
'''
'''
x = 0
a = 1
while True:
	x += 1
	print(x) #, end=", ")
	if x == 10:
		while True:
			x -= 1
			print(x) #, end=",")
			if x == 1:
				a = 1
				break
	if a == 1:
		break		 
'''
x = []
for i in range(1,11):
	x.append(i)
t = str(x[0:-1] + x[::-1])
y = list(t)
y.remove("[")
y.remove("]")
print(t)


















