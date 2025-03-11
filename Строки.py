#Интерполяция
# Использование конкатенации строк
name = "Bob"
age = 30
print("Привет, меня зовут " + name + " и мне " + str(age) + " лет.")

# Использование интерполяции строк
name = "Alice"
age = 25
print(f"Привет, меня зовут {name} и мне {age} лет.") # Создаем f-строку

store = 'App Store'
what_is_it = f'{store} - магазин приложений'
print(what_is_it)  # Результат: App Store - магазин приложений

#Извлечение символов из строки
text = "Привет, мир!"
first_char = text[0] # Извлекаем символ с индексом 0
print(first_char)  # Результат: П

first_name = 'Привет, мир'
print(first_name[-1])  # Результат: р ( если необходимо извлечь элемент из конца строки)

first_name = 'Иван'
index = 0
print(first_name[index])  # Результат: И ( можно использовать переменную)

first_name = 'Иван'
print(first_name[1])

first_name = 'еденица'
print(first_name[0])

first_name ='антропогинез'
print(first_name[2])

#Срезы строк

