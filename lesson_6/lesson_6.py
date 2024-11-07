"""
Lesson 6

Циклы:
    
2. Операторы управления циклом
    - break (досрочное прерывание цикла)
    - continue (пропуск текущей итерации)
    - else в циклах (выполняется, если цикл завершился без break)

3. Вложенные циклы
    - Циклы внутри циклов
    - Примеры использования
    - Выход из вложенных циклов

4. Работа с range()
    - Создание последовательностей чисел
    - Параметры range(start, stop, step)
    - Использование в цикле for

5. Функция enumerate()
    - Получение индекса и значения при переборе
    - Практическое применение

1. Цикл while
    - Синтаксис и базовое использование
    - Условия выхода из цикла
    - Бесконечные циклы
    
6. Практические задания:
    - Работа с while
    - Использование break и continue
    - Создание вложенных циклов
    - Применение range и enumerate
"""
import os
# Краткий разбор инструментов для ДЗ
# ord() - получает код символа
# chr() - получает символ по коду

char = 'т'


index_char = ord(char)
index_char += 1

char_index = chr(index_char)
print(char_index)

decode_char = chr(index_char - 1)
print(decode_char)

# - exit - выход из программы
# - break (досрочное прерывание цикла)
# - continue (пропуск текущей итерации)
# - else в циклах (выполняется, если цикл завершился без break)




r_words = ['рука', 'река', 'гора', 'пора', 'раствор', 'разговор', 'рассказ', 'регистратор', 'рефрижератор', 'бронетранспортёр', 'чебурек', 'реставратор'] 

for word in r_words:
    if word.lower().count('р') <= 2:
        continue # Пропуск работы на этом круге цикла

    
    if word.lower().count('р') >= 6:
        break # Выход из цикла
    
    print(word)

else:
    # Цикл завершился без break - только в этом случае мы попадаем сюда!
    print('Цикл завершился без break')

"""
Практика

Допишите этот код. Давайте сделаем сортировщик слов по количеству букв "р".
1. Над циклом создайте переменные one_r_word и two_r_word
2. В цикле сделайте условие на букв р больше двух - в этом случае пропускаем цикл через continue
3. В цикле сделайте условие на одну букву "р" и на две буквы "р"
4. Добавление в соответствующие списки.

Пустой список 

one_r_word = []

Метод добавления в список название_списка.append(значение)
"""
os.system('cls')
r_words = ['рука', 'река', 'гора', 'пора', 'раствор', 'разговор', 'рассказ', 'регистратор', 'рефрижератор', 'бронетранспортёр', 'чебурек', 'реставратор'] 

one_r_word = []
two_r_word = []
for word in r_words:
    if word.lower().count('р') > 2:
        continue

    if word.lower().count('р') == 1:
        one_r_word.append(word)
    elif word.lower().count('р') == 2:
        two_r_word.append(word)


print(f'Список с одной буквой "р": {one_r_word}')
print(f'Список с двумя буквами "р": {two_r_word}')

one_r_word = [word for word in r_words if word.lower().count('р') == 1]
two_r_word = [word for word in r_words if word.lower().count('р') == 2]

print(id(r_words))
r_words_copy = r_words
r_words_copy.append('Ещё одно слово')
print(id(r_words_copy))

print(r_words)
print(r_words_copy)

r_words_copy2 = r_words.copy()
print(id(r_words_copy2))

# List Comprehension - Списковое выражение - Списковое включение
r_words_copy3 = [word for word in r_words]
[print(word) for word in r_words]
print(id(r_words_copy3))

r_words_copy4 = []

for word in r_words:
    print(word)
    r_words_copy4.append(word)


################ СПИСКИ ################
# Список - изменяемая, индексируемая, упорядоченная, итерируемая коллекция. Которая может содержать РАЗНЫЕ типы данных в себе.

# Создание списка
my_list = []
my_list = list()

my_list = ['Привет', 2, True, 3.4, None, [1, 2, 3]]
my_list = list('Привет') # ['П', 'р', 'и', 'в', 'е', 'т']

print(my_list)

# Положить что-то в список названиесписка.append(значение)
my_list.append('Новый элемент')

# Получить элемент списка по индексу названиесписка[индекс]
new_item = my_list[-1]
print(new_item)

new_item = 'Обновление'
my_list[-1] = new_item
print(my_list)

# Удаление элемента
# del my_list[-1]
item = my_list.pop(1)
print(my_list)

# CRUD - create, read, update, delete

# Методы списков

# Часто используемые методы списков:

# .append(item) # Добавляет элемент в конец списка
# .extend(iterable) # Расширяет список, добавляя элементы из итерируемого объекта
# .pop([index]) # Удаляет и возвращает элемент по индексу (по умолчанию последний)
# .remove(item) # Удаляет первое вхождение указанного элемента
# .clear() # Очищает список
# .copy() # Создает поверхностную копию списка
# .index(item[, start[, end]]) # Возвращает индекс первого вхождения элемента
# .count(item) # Подсчитывает количество вхождений элемента
# .sort(*, key=None, reverse=False) # Сортирует список на месте (key - функция для сортировки)
# .reverse() # Разворачивает список на месте
# .insert(index, item) # Вставляет элемент по указанному индексу

product_list = ['молоко', 'хлеб', 'яйца', 'сыр', 'колбаса', 'сок', 'масло', 'молоко', 'сыр', 'сигары', 'виски', 'кола', 'виски']

# Список вредных продуктов
bad_product_list = ['сигары', 'виски', 'кола', 'виски']

clear_list = []

# Попробуйте пройтись циклом, и сформировать новый список без дубликатов
# if product not in clear_list

for product in product_list:
    if product not in clear_list:
        clear_list.append(product)

# Полная копия исходника
clear_list = [product for product in product_list]

# Копия без дубликаторв
# clear_list = list(set(product_list))

# Давайте обойдем product_list и сформируем новый список продуктов из тех кторые НЕ входят в список вредных продуктов
# clear_list = []
# for product in product_list:
#     if product not in bad_product_list:
#         clear_list.append(product)


# clear_list = [product for product in product_list if product not in bad_product_list]
# print(clear_list)

#####################################

# clear_list = []
# for product in product_list:
#     if product not in bad_product_list:
#         clear_list.append(product.upper())


# clear_list = [product.upper() for product in product_list if product not in bad_product_list]
# print(clear_list)


clear_list = []
for product in product_list:
    if product not in bad_product_list:
        if product.count('о') > 1:
            clear_list.append(product.upper())
        else:
            clear_list.append(product.lower())

# тут мы отфильтровали полезные продукты и сделали продукты с двумя буквами "о" заглавными
clear_list = [product.upper() if product.count('о') > 1 else product.lower() for product in product_list if product not in bad_product_list]
print(clear_list)


# Практика!

# Датасет: список фильмов с годом выпуска
movies = [
    "Титаник (1997)", 
    "Матрица (1999)",
    "Властелин колец (2001)",
    "Начало (2010)",
    "Зеленая миля (1999)",
    "Интерстеллар (2014)",
    "Гладиатор (2000)",
    "Король Лев (1994)",
    "Форрест Гамп (1994)",
    "Аватар (2009)"
]

# 1. Создайте список, содержащий только названия фильмов без года. Пример результата: ['Титаник', 'Матрица', ...]
# clear_films
# film .split() [Зеленая миля, (1999)] [0]

# 2. Создайте список фильмов 90-х годов (1990-1999). Подсказка: можно использовать срезы строк и проверку числа
# Как добыть год? split() [1]   (1994).replace('(', '').replace(')', '')
# Отинтовать. Проверить на диапазон

# 

# Вариант 1 на однострочнике
clear_films = [film.split()[0] for film in movies]
print(clear_films)

# Вариант 2 на однострочнике
min_year = 1990
max_year = 1999

clear_films = [film.split()[0] for film in movies if int(film.split()[-1].replace('(', '').replace(')', '')) in range(min_year, max_year + 1)]
print(clear_films)
# БЕЗ Range
clear_films = [film.split()[0] for film in movies if int(film.split()[-1].replace('(', '').replace(')', '')) >= min_year and int(film.split()[-1].replace('(', '').replace(')', '')) <= max_year]
print(clear_films)
# Range функция в Python которая возвращает последовательность чисел в заданном диапазоне.

# Вариант от Ивана
movies_90 = [movie for movie in movies if int(movie.split('(')[1][0:4]) in range(1990, 2000)]

print(range(1, 10)) # range(1, 10)
print(type(range(1, 10))) # <class 'range'>
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9] НЕ включая 10