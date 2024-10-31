"""
Lesson 5
Тернарный оператор - это сокращенный способ записи условных выражений в Python.

Срезы строк:
- Синтаксис срезов [start:end:step]
- Отрицательные индексы
- Пропуск параметров в срезах
- Обратный порядок через срезы
- Копирование строк через срезы

Работа с исключениями
    - Try - попытка - мы пытаемся сделать то, что может упасть с ошибкой
    - Except - мы отлавливаем эту ошибку и что-то делаем с ней
    - Else - если ошибки НЕ было, мы попадаем сюда
    - Finally - мы это делаем в любом случае

Итерация строк:
- Перебор символов в строке
- Работа с индексами при переборе

- Цикл for


Циклы:
- Цикл while ???
- Операторы break и continue ???
- Вложенные циклы ???
- Цикл for с range()


- Функция enumerate()
- Подсчёт символов


Списки:
- Создание списков
- Индексация элементов
- Изменение элементов
- Основные методы списков (append, insert, remove, pop)
- Срезы списков
- Копирование списков

Практические задания:
- Работа со строками через срезы
- Подсчёт символов в строке
- Создание и изменение списков
- Решение задач с использованием циклов
"""
import os

some_str = "Не шалю, никого не трогаю, починяю примус"

# Упорядоченная коллекция символов. Итерируемая. Неизменяемая.

sym0 = some_str[0]
print(f"{sym0 = }")

sym_end_1 = some_str[-3]

# some_str[0] = 'M'

# Срезы. [start:stop:step] SSS
print(f"{some_str[0:-1:1] = }")  # Полная копия
print(f"{some_str[::] = }")  # Полная копия
print(f"{some_str[0:3:1] = }")  # Не включая 3
print(f"{some_str[0:10:2] = }")  # С шагом 2 (через символ)

print(f"{some_str[0:10:] = }")  # Значения по умолчанию можно не определять
print(f"{some_str[0:10] = }")  # Даже двоеточие можно не ставить
print(f"{some_str[:10] = }")  # Даже ноль можно сократить

print(
    f"{some_str[7:] = }"
)  # Или так. Оставив stop и step по умолчанию (stop -1, step 1)

# Отрицательные индексы
print(f"{some_str[::-1] = }")  # Полная копия зеркало (читается наоборот)

print(f"{some_str[-5:-20:-1] = }")
print(f"{some_str[20:5:-1] = }") # Срез с отрицательным шагом (если мы делаем старт и стоп положительными, то отрицательный шаг рушит всё и у нас индекс начала оказывается больше чем конечный)
print(f"{some_str[0:20][::-1]}")


# Короткая строка для демонстрации
test_str = "Python"
print("\nПримеры со строкой:", test_str)
print(f"Длина строки: {len(test_str)}")

# Демонстрация проблемы с положительными индексами и отрицательным шагом
print(f"{test_str[0:4:-1] = }")  # Пустая строка, так как 0 < 4 при шаге -1 (т.е. мы заказываем срез с 4 по 0 строку)
print(f"{test_str[4:0:-1] = }")  # Работает правильно: 'ohty'

# Правильное использование с отрицательным шагом
print(f"{test_str[5:1:-1] = }")  # 'nohty'
print(f"{test_str[-1:-6:-1] = }")  # 'nohty'

"""
Практика:
1. Получите у пользователя строку
2. Приведите её в нижний регистр
3. Сделайте зеркальную строку через срез
4. Сравните их на == 
5. Если равны - это палиндром, иначе - не палиндром

казак, топот шалаш, доход

# Сложная версия :)
А роза упала на лапу Азора
Аргентина манит негра
"""


user_word = 'дед'
word = user_word.lower().replace(' ', '') # Мы меняем пробел на ничего и приводим к нижнему регистру

# Зеркалим через срез
mirror_word = word[::-1]

if word == mirror_word:
    print(f'Слово "{user_word}" является палиндромом')
else:
    print(f'Слово "{user_word}" не является палиндромом')



os.system('cls') # Очистка консоли. Мы не увидим принты выше!!!!

# Однострочный иф - тернарный оператор

a = 5
b = 5

print(f'{a = }')
print(f'{b = }')
# ЧТО если ИНАЧЕ другое
result = 'А равно Б' if a == b else 'А не равно Б'
print(f'{result}')

"""
Практика!
Запросите у пользователя число.
Сделайте переменную, с использованием тернарного оператора if
Если "число" проходит проверку isdigit() - примените к нему int если не проходит - None
"""

# user_num = input('Введите число: ')
# result = int(user_num) if user_num.isdigit() else None
# print(type(result))
# is_digit = type(result) == int

# if is_digit:
#     print('Число')
# else:
#     print('Не число')

# print('Число') if result else print('Не число')

# print(f'{"Число" if result else "Не число"}')

# # Вариант от Григория
# print(f'{"Число" if input("Введите число").isdigit() else None} ')



os.system('cls') # Очистка консоли. Мы не увидим принты выше!!!!

# user_num = input('Введите число: ')


# try: # Попробуй сделать это
#     result = int(user_num)
# except TypeError as e: # Если упал с ошибкой
#     # as e - мы помещаем текст ошибки в переменную e
#     print(f'Упал с ошибкой TypeError {e}')

# except ValueError as e:
#     print(f'Упал с ошибкой ValueError {e}')

# else: 
#     print('Всё ок')

# Практика 
"""
1. Запросите у пользователя число а
2. Запросите у пользователя число б
3. Сделайте блок try и ипопробуйте их отинтовать
4. Отловите исключение ValueError
5. Сделайте блок try и попробуйте их поделить одно на другое
6. Отловите 2 исключения по очереди. 1. ZerroDivisionError, 2. ValueError (Или общий Exception)
"""

# a = input('Введите число a: ')
# b = input('Введите число b: ')

# a_int = None
# b_int = None
# try: # Попробуй сделать это
#     a_int = int(a)
#     b_int = int(b)

# except ValueError as e:
#     print(f'Похоже что {a} или {b} не являются числами. {e}')


# try:
#     result = a_int / b_int
# except ZeroDivisionError as e:
#     print(f'Похоже что {b} равно нулю. {e}')

# except TypeError as e:
#     print(f'Похоже что числа не поступили. {e}')


# for - ключевое слово которое запускает цикл
# for ПЕРЕМЕННАЯ in ПОСЛЕДОВАТЕЛЬНОСТЬ:

some_str = "Не шалю, никого не трогаю, починяю примус"
sym = 0
# for sym in some_str:
#     print(sym, end='')

# гласные буквы
vowels = 'аеёиоуыэюя'
# соглансые буквы 
consonants = 'бвгджзйклмнпрстфхцчшщ'

# Счетчик гласных и согласных
vowels_count = 0
consonants_count = 0
for sym in some_str:
    if sym.lower() in vowels:
        vowels_count += 1
    elif sym.lower() in consonants:
        consonants_count += 1
    else:
        print(f'Символ "{sym}" не является русской буквой')
    
print(f'Гласных: {vowels_count}')
print(f'Согласных: {consonants_count}')
print(f'Всего русских букв: {vowels_count + consonants_count}')
print(f'Всего символов: {len(some_str)}')
print(f'Всего слов: {len(some_str.split())}')
print(f'Всего символов без пробелов: {len(some_str.replace(" ", ""))}')


# Анализатор пароля. Продвинутая версия с циклами.

spec_syms = '!@#$%^&*()_+-='
password = "qwerty12345Aa!++"

len_threshold = 8
upper_threshold = 1
lower_threshold = 1
digit_threshold = 1
spec_sym_threshold = 1

is_len = False
is_upper = False
is_lower = False
is_digit = False
is_spec_sym = False

bad_report_string = ''

for symbol in password:
    # Проверка длины
    if len(password) >= len_threshold:
        is_len = True
    else:
        bad_report_string += f'Пароль должен быть не менее {len_threshold} символов\n'

    # Является ли это буквой
    if symbol.isalpha():
        # Это является буквой. Мы можем проверить на регистр
        if symbol.isupper():
            is_upper = True
        else:
            is_lower = True
    
    # Это не буква. Проверим на вхождение в спец знаки
    else:
        if symbol in spec_syms:
            is_spec_sym = True

        elif symbol.isdigit():
            is_digit = True
       



if is_len and is_upper and is_lower and is_digit and is_spec_sym and not bad_report_string:
    print('Пароль надежный')
else:
    print('Пароль не надежный')
    print(bad_report_string)


# Вариант от Ивана :)

print(f'Пароль надежный') if all([
    any(s in spec_sym for s in password),
    len(password) > 8,
    any(s.isdigit() for s in password),
    any(s.isupper() for s in password),
    any(s.isalpha() for s in password),
]) else print(f'Пароль не надежный')