from pprint import pformat

result = 2+3*4 #14
print(result)
result = (2+3)*4 #20
print(result)
print("\\") # отобразится слэш
print("Он сказал: \"Привет, мир!\"") # Используем экранирование кавычек
print("завтра будет хороший день?\nДа!")
print('Колонка1 Колонка2\tКолонка3')
print('привет!')
print("\n")
print('Иван')

text = "Please update your payment information."
intro = "We have noticed some unusual activity on your account."
name = 'Sansa'
welcome = 'Dear' # BEGIN
header = welcome + " " + name + "!"
main_text = '''We have noticed some unusual activity on your account.
Please update your payment information.'''
print(header)
print(main_text) # END

surname = "Зубенко"
name = "Михаил"
patronymic = "Петрович"
age = 45
print(f"меня зовут {surname} {name} {patronymic} и мне {age}")

first_number = 10
second_number = 42
c = first_number + second_number
d = first_number * second_number
print('Сумма:', c)
print('Произведение:', d)
print((3+(5*2)-(6/3)))