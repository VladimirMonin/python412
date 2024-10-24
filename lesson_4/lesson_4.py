"""
Lesson 4
Булева логика
Какие значения возвращает bool от разных типов данных?
Операторы сравнения
Приоритеты в сравнениях OR NOT AND ()
Знакомство с методами строк
Условные операторы и ветвления
"""
import random
# Boolean - логический тип данных
# bool - boolean - логический тип данных

# True - истина
# False - ложь

# bool(значение) - функция которая приведет значение к булевому типу

# Приведем каждый тип данных в Python к булевому типу

# int - integer - целое число
# float - дробное число
# str - string - строка 
# bool - boolean - логический тип данных
# NoneType - None - пустой тип данных
# list - список
# tuple - кортеж
# set - множество
# dict - словарь

# integer - целое число float - дробное число (Только 0 отдаст False)
print(f'{bool(0) = }')
print(f'{bool(0.0) = }')
print(f'{bool(0.1) = }')
print(f'{bool(1) = }')
print(f'{bool(-1) = }')

# string - строка
print(f'{bool("") = }')
print(f'{bool(" ") = }')
print(f'{bool("0") = }')
print(f'{bool("1") = }')

# bool - boolean - логический тип данных
print(f'{bool(True) = }')
print(f'{bool(False) = }')

# NoneType - None - пустой тип данных
print(f'{bool(None) = }')
a = None
b = None
print(f'{id(a) = }')
print(f'{id(b) = }')
# Проверка is - проверяет id объектов. 
# Проверка == - проверяет значения объектов.
print((f'{a is b = }'))


# list - список
# tuple - кортеж
# set - множество
# dict - словарь

print(f'{bool([]) = }')
print(f'{bool([1, 2, 3]) = }')

print(f'{bool(()) = }')
print(f'{bool((1, 2, 3)) = }')

print(f'{bool(set()) = }')
print(f'{bool({1, 2, 3}) = }')

print(f'{bool({}) = }')
print(f'{bool({1: 100}) = }')

## Методы - функции которые привязаны к объекту
# Методы строк
'''
1. split() - разделение строки на список по разделителю (по умолчанию пробел)
2. strip() - удаление пробельных символов в начале и конце строки
3. replace(old, new) - замена подстроки old на new
4. lower() - преобразование строки в нижний регистр
5. upper() - преобразование строки в верхний регистр
6. join() - объединение списка строк в одну строку с указанным разделителем
7. startswith(prefix) - проверка начинается ли строка с prefix
8. endswith(suffix) - проверка заканчивается ли строка на suffix
9. find(sub) - поиск подстроки, возвращает индекс первого вхождения или -1
10. count(sub) - подсчет количества вхождений подстроки
11. isdigit() - проверка состоит ли строка только из цифр
12. isalpha() - проверка состоит ли строка только из букв
isalnum() - проверка состоит ли строка только из букв и цифр
isspace() - проверка состоит ли строка только из пробельных символов
13. capitalize() - первый символ строки в верхний регистр, остальные в нижний
14. title() - первые буквы всех слов в верхний регистр
15. lstrip() - удаление пробельных символов слева
16. rstrip() - удаление пробельных символов справа
17. center(width) - центрирование строки в поле заданной ширины
18. zfill(width) - дополнение строки нулями слева до указанной ширины
19. partition(sep) - разделение строки на кортеж (до разделителя, разделитель, после)
20. format() - форматирование строки с подстановкой значений
'''

cities = 'Москва Санкт-Петербург'
print(type(cities))
cities_list = cities.split() # разделитель пробел по умолчанию ['Москва', 'Санкт-Петербург']
print(cities_list)

# Некоторые методы возвращают новый объект, некоторые изменяют объект на месте
new_cities = random.shuffle(cities_list)
print(new_cities)

a = 5
b = print(a)
print(b)
print(print(a))

####### Проверка пароля

# len() - длина строки
# isdigit() - проверка состоит ли строка только из цифр
# isalpha() - проверка состоит ли строка только из букв
# isalnum() - проверка состоит ли строка только из букв и цифр
# if in ' ' - проверка вхождения пробела

password = '&&&&&&&&&&&&&&&&&&'

print(f'{len(password) = }')
print(f'{password.isdigit() = }')
print(f'{password.isalpha() = }')
print(f'{password.isalnum() = }')
print(f'{" " in password = }') # пробел в пароле - вернет Bool

# 0. Наличие пробела
# 1. Длина не менее 8 знаков
# 2. isalnum - false - значит есть спецзнаки

# Логические операторы. 
# () - группировка условий - высший приоритет
# not - отрицание первый приоритет
# and - второй приоритет
# or - третий приоритет

"""
true and true = true
true and false = false
false and true = false
false and false = false
true or true = true
true or false = true
false or true = true
false or false = false
not true = false
not false = true
"""


print(f'Пароль хороший: {" " not in password and not password.isalnum() and len(password) >= 8}')


# Васька - домашний кот. У него есть 3 состояния:
is_hungry = True  # Голодный
is_sleepy = True  # Хочет спать
is_angry = False  # Злой

# AND - нужно чтобы все условия были True
# Васька будет мяукать если голодный И сонный
print("Васька мяукает:", is_hungry and is_sleepy)  # True

# OR - достаточно одного True
# Васька царапает диван если голодный ИЛИ злой
print("Васька царапает диван:", is_hungry or is_angry)  # True

# NOT - инверсия значения
# Васька НЕ злой, значит ласковый
print("Васька ласковый:", not is_angry)  # True

# Сложные комбинации:
# Васька будет спать если: (НЕ голодный И НЕ злой) ИЛИ очень сонный
will_sleep = (not is_hungry and not is_angry) or is_sleepy
print("Васька пойдет спать:", will_sleep)  # True

# Васька побежит к миске если: голодный И (НЕ спит ИЛИ злой)
will_run_to_food = is_hungry and (not is_sleepy or is_angry)
print("Васька бежит к миске:", will_run_to_food)  # False

# Операторы сравнения возвращают bool - True или False
# = - присвоение
# == - равно '1' == 1 - False
# != - не равно
# > - больше
# < - меньше
# >= - больше или равно
# <= - меньше или равно

"""
1. Валидация email
Используйте input для получения строки от пользователя.
Проверьте, содержит ли введенный email символ @ и точку

2. Счастливое число
Используйте input для получения строки от пользователя.
Вам потребуется обращение к элементам строки по индексу.
Вы можете сделать это в формате input_string[0]
Для преобразования строки в число используйте функцию int()     int(input_string[0])
Проверьте, равна ли сумма первых трех цифр шестизначного числа сумме последних трех.

3.
Проверьте, являются ли последние 4 цифры номера телефона одинаковыми.

"""

# 1.
email = input('Введите email: ')
print(f'Результат проверки email: {"@" in email and "." in email}')

# 2.
number = input('Введите шестизначное число: ')

print(f'Результат проверки числа: {int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5])}')

# 3.
phone = input('Введите номер телефона: ')
print(f'Результат проверки номера телефона: {phone[-4] == phone[-3] == phone[-2] == phone[-1]}')


# 4. Проверка емейл с индексами rfind
mail = "monin.vladimir2016@yandex.ru"

email = input('Введите email: ')
print(f'Результат проверки пароля: {email.rfind("@") < email.rfind(".") and "@" in email and "." in email}')


print(f'Введеный email валидный: {"@" in email and "." in email and email.find("@") < email.rfind(".",email.find("@"))}')

