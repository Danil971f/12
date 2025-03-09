#Арифметика
print("1)", 5 + 3)  # 8 - сложение
print("2)", 7 - 2)  # 5 - вычетание
print("3)", 4 * 6)  # 24 - умножение
print("4)", 10 / 3)  # 3.33333... - деление
print("5)", 2 ** 3)  # 8 - возведение числа в степень

#Целочисленное деление и остаток от деления
print("6)", 10 // 3)  # 3 - целочисленное деление
print("7)", 10 % 3)  # 1 - # остаток от деления

#Приоритет операции
result = 2 + 3 * 4  # 14
print("8)", result)
result = (2 + 3) * 4  # 20
print("9)", result)

#Операторы и операнды
print("10)", 5+3) #  Здесь "+" является оператором, а "5" и "3" операндами.

#Работа с операциями
print("11)", 3 * 6 * 7 * 9) # Операции умножения происходят последовательно.
print("12)", 1 + 3 * 3)  # Результат: 10
print("13)", 2 ** (5 - 3))  # Результат: 4
print("14)", 5 * 2 + (3 / 3) - (6 + (4 - 2)))  # Результат: 3
# Первый вариант
print("15)",6 / 3 + 4 - -6 / 3)  # Результат: 8
# Второй вариант
print((( 6 / 3) + 4) - (-6 / 3))  # Результат: 8

#Кавычки
print('Привет, мир!') # Используем одинарные кавычки
print("Привет, мир!") # Используем двойные кавычки
print("""Привет, 
мир!""") # Используем тройные кавычки для многострочных строк
print("Father's car") # Строка находится между двойных кавычек
print("Dad's friend said \"No\"") # Кавычки вокруг No экранируются обратным слэшом
print("\\") # Отобразится слэш

#Экранированные последовательности
print("Он сказал: \"Привет, мир!\"") # Используем экранирование кавычек
print("Первая строка\nВторая строка") # Используем символ переноса строки
print("Колонка 1\tКолонка 2\tКолонка 3") # Используем символ табуляции
print("Путь к файлу: C:\\Users\\Admin\\Documents\\file.txt") # Экранируем обратный слэш
print('Привет')
print("\n") # Пустая строка
print('Иван')
print("Привет, Андрей \\n") # Используем экранирование

#Конкатенация
print('Кофе' + 'машина') #  При соединении получаем Кофемашина
#  Первый пример
print('Кофе' + 'машина')

# Второй пример
print("Кофе" + "машина")

# Третий пример
print("Кофе" + 'машина')

#Пробел в левой части
print("Kофе " + "Машина")  # Результат: Кофе Машина

# Пробел в правой части
print("Кофе" + " Машина")  # Результат: Кофе Машина