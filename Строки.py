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