#Что такое переменная
x =  5 # Переменная x равна 5
x = 10 # Присваиваем переменной x новое значение 10
print(x) # Выводит 10

# Объявление константы для значения Пи
PI = 3.14159
# Использование константы в вычислениях
radius = 10
area = PI * radius ** 2

print("Площадь круга радиуса", radius, "равна", area)

#Магические числа
radius = 5
area = 3.14 * radius ** 2
print(area)
# 3.14 является магическим числом

PI = 3.14 # Создаем константу, которую в дальнейшем можно будет легко изменить
radius = 5
area = PI * radius ** 2
print(area)

#Выражения в определениях
a = 5
b = 2
c = a + b # Выражение "a + b" означает сумму переменных a и b
d = a * b # Выражение "a * b" означает произведение переменных a и b
e = (a + b) * c # Выражение в скобках сначала вычисляется, затем умножается на c
print(e)

who = "Привет, " + 'мир!' # Используем выражение в переменной
print(who) # Выводим переменную

name = "Андрей"
age = 25 + 2
job = "инженер"
company = "Ростелеком"
person_info = name + ": " + str(age) + " лет, " + job + " в " + company
# Производим вычисление выражения
print(person_info) # Выводим значение выражение в переменной

#Переменные и конкатенация
# вычисляем значение переменной при помощи конкатенации двух строк
all = "Кофе" + 'машина'
print(all)

#объединяем две переменные, в которых записаны строки и строку с пробелом
first_name = "Иван"
last_name = "Иванов"
full_name = first_name + " " + last_name
print(full_name)

# объединяем строку и переменную, используя оператор +
name = "Иван"
message = "Привет, " + name + "!"
print(message)