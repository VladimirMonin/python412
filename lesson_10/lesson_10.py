"""
Урок 10
14.11.2023

1. Методы словарей (продолжение):
    - .pop(key)
    - .setdefault(key, default=None)
    - .popitem()
    - .fromkeys(sequence, value=None)
    - .zip()

2. Кортежи (tuple):
    - Что такое кортежи и зачем они нужны
    - Создание кортежей
    - Отличия от списков
    - Неизменяемость кортежей
    
3. Работа с кортежами:
    - Доступ к элементам
    - Методы кортежей (.count(), .index())
    - Распаковка кортежей
    - Кортежи как ключи словарей

4. Практика:
    - Создание и использование кортежей
    - Совместное использование словарей и кортежей
    - Решение задач с применением изученных структур данных
"""

person = {
    'first_name': 'Николай',
    'last_name': 'Соболев',
    'age': 30,
    'city': 'Москва',
    'phone': '+7(999)123-45-67',
    'occupation': 'Программист',
    'citizenship': 'РФ',
    'passport': '4510 123456',
    'gender': 'мужской'
}


# pop - удаляет элемент по ключу и возвращает его значение

first_name = person.pop('first_name')
print(first_name)
print(person)

# - .setdefault(key, default=None) - получить значение по ключу, если ключ не найден, то добавить его в словарь со значением по умолчанию
# Вариант 1. Пытаемся по ключу получить группу
# print(person['group']) # KeyError: 'group'

# Вариант 2. Пытаемся по ключу получить группу - get()
print(person.get('group')) # None - ключ не создается
print(person)
# Вариант 3. Пытаемся по ключу получить группу - setdefault()
print(person.setdefault('group')) # None - ключ не создается
print(person)
 
 
# - .popitem() - удаляет последний элемент словаря и возвращает его в виде кортежа
print(person.popitem())
print(person)

# - .fromkeys(sequence, value=None) - создает новый словарь на основе последовательности ключей и значения по умолчанию
# Создадим на базе предыдущего словаря новый

new_person = dict().fromkeys(person.keys(), None)
print(new_person)

# zip() - создает словарь на основе двух последовательностей - не является методом словаря, это встроенная функция
keys = ['name', 'age', 'city']
values = ['Сёма', 18, 'Москва']

# # Как бы это было в цикле?
# person = {}
# for key in keys:
#     person[key] = values[keys.index(key)]


# Как через zip() [('name', 'Сёма'), ('age', 18), ('city', 'Москва')]
# Важный момент, он учтет возможность разной длины в коллекциях - выведет только те, которые совпали (остальное отбросит)
person = dict(zip(keys, values))
print(person)

# Кортежи. 
# Кортеж - упорядоченная коллекция элементов, где у каждого элемента есть индекс. Не изменяемый тип данных.
# Кортеж - неизменяемый список.

# Пустой кортеж
empty_tuple = ()
print(empty_tuple)

# Кортеж из одного элемента
single_tuple = 1, # или (1,)
print(single_tuple)

# Кортеж месяцев
months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
# months[0] = 'Усабрь'

# Методы кортежей

# .count() - подсчитывает количество элементов в кортеже
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))  # 3

# .index() - возвращает индекс первого вхождения элемента
print(numbers.index(2))  # 1

# len() - возвращает длину кортежа (не метод, а встроенная функция)
print(len(numbers))  # 7

# Срезы работают так же, как и в списках
print(numbers[1:4])  # (2, 3, 2)

# Конкатенация кортежей
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# Умножение кортежа на число
print(tuple1 * 2)  # (1, 2, 3, 1, 2, 3)


# Frozen set - неизменяемое множество
# frozenset() - создает неизменяемое множество

# Создание frozenset из списка
frozen1 = frozenset([1, 2, 3, 4, 5])
print(frozen1)  # frozenset({1, 2, 3, 4, 5})

# Создание frozenset из строки
frozen2 = frozenset('hello')
print(frozen2)  # frozenset({'h', 'e', 'l', 'o'})

# Методы frozenset
# .copy() - создает копию множества
frozen3 = frozen1.copy()
print(frozen3)  # frozenset({1, 2, 3, 4, 5})

# .intersection() - пересечение множеств
frozen4 = frozenset([4, 5, 6, 7])
print(frozen1.intersection(frozen4))  # frozenset({4, 5})

# .union() - объединение множеств
print(frozen1.union(frozen4))  # frozenset({1, 2, 3, 4, 5, 6, 7})

# .difference() - разность множеств
print(frozen1.difference(frozen4))  # frozenset({1, 2, 3})

# .issubset() - является ли подмножеством
frozen5 = frozenset([1, 2])
print(frozen5.issubset(frozen1))  # True

# .issuperset() - является ли надмножеством
print(frozen1.issuperset(frozen5))  # True

# .isdisjoint() - не пересекаются ли множества
frozen6 = frozenset([8, 9])
print(frozen1.isdisjoint(frozen6))  # True

# len() - количество элементов
print(len(frozen1))  # 5


from marvel import full_dict as fd

# print(fd)

"""
1. Задача перепаковать это. Из словаря словарей
в список словарей. Переместить ключи, внутрь словаря 
и дать им ключ id

 УБИРАЕМ: {
        'id': 0, # ДОБАВЛЯЕМ
        'title': 'Железный человек',
        'year': 2008,
        'director': 'Джон Фавро',
        'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
        'producer': 'Ави Арад и Кевин Файги',
        'stage': 'Первая фаза'

"""
from pprint import pprint

full_dict_list = []

for ids, film in fd.items():
    film['id'] = ids
    full_dict_list.append(film)

# for ids, film in fd.items():
#     new_dict = {
#         'id': ids,
#         'year': film['year'],
#         'director': film['director'],
#         'screenwriter': film['screenwriter'],
#         'producer': film['producer'],
#         'stage': film['stage'],
#     }
#     full_dict_list.append(new_dict)


# for ids, film in fd.items():
#     new_dict = {
#         'id': ids,
#         **film
        
#     }
#     full_dict_list.append(new_dict)



# full_dict_list = [{'id': key, **value} for key, value in fd.items()]

# pprint(full_dict_list, sort_dicts=False)


# person = {
#     'first_name': 'Николай',
#     'last_name': 'Соболев',
#     'age': 30}

# keys = ['first_name', 'last_name', 'age']
# values = ['Николай', 'Соболев', 30]
# items = [('first_name', 'Николай'), ('last_name', 'Соболев'), ('age', 30)]

# Цикл по items
# for key, value in person.items():
# ('first_name', 'Николай') # Первая итерация
# ('last_name', 'Соболев') # Вторая итерация
# ('age', 30) # Третья итерация

# РАСПАКОВКА
# key, value = ('first_name', 'Николай')
# key - 'first_name'
# value - 'Николай'

# 2. Задача. Сделайте цикл по списку словарей. Выведите только названия фильмов. (Можно просто распечатать)

# for film in full_dict_list:
#     print(film['title'])




# [print(film['title']) for film in full_dict_list]

# 3. Задача. Напишите поиск по фильмам по названию. (частичное вхождение и независимо от регистра)
print('*' * 100)
# film_title = 'человек'
# for film in full_dict_list:
#     # Проверка на то, что по ключу лежит не None (None - вернет False)
#     if not film['title']:
#         continue
    
#     # Если название фильма есть попадаем сюда
#     if film_title.lower() in film['title'].lower():
#         print(film['title'])
    



# film_title = 'человек'
# result = [film for film in full_dict_list if film['title'] is not None and film_title.lower() in film['title'].lower()]

# print(result)
# 4. Поисковик по фазам. Для этого нам понадобится маленький словарь с расшифровкой фаз. Мы спрашиваем у человека введите фазу, а потом выводим фильмы, которые входят в эту фазу. (человек вводит 1, 2, или 3....) А мы из словаря берем соответсвтующее название фазы в строковом виде.

# Выдаем либо список словарей либо список названий фильмов.

stages = {
    '1': 'Первая фаза',
    '2': 'Вторая фаза',
    '3': 'Третья фаза',
    '4': 'Четвертая фаза',
    '5': 'Пятая фаза',
    '6': 'Шестая фаза',
}

user_input = '2'

if user_input not in stages:
    raise ValueError('Такой фазы нет')

stage_choise = stages[user_input] # 'Вторая фаза'

for film in full_dict_list:
    if film['stage'] == stage_choise:
        print(film['title'])


user_input = '2'

result = [film['title'] for film in full_dict_list if film['stage'] == stages[user_input]]

print(result)

# 5. Сделать словарь, где ключами будут годы, а значениями, списки словарей по этим годам.
"""
1. Пройдите по ключам "годы".
2. Соберите список лет. Получите уникальные значения (можно прогнать через сет)
3. Создайте новый словарь.
3. Пройдите по списку лет, и создавайте записи в новом словаре. Ключ - год, значение - список словарей с фильмами по этому году.
"""

# 1 и 2
years = {film['year'] if film['year'] != 'TBA' else 3000 for film in full_dict_list}
year_list = list(years)
sorted_year_list = sorted(year_list)

print(sorted_year_list)

# 3
new_dict = {}

for film in full_dict_list:
    # Проверяем, что год не является 'TBA' (неизвестным)
    if film['year'] != 'TBA':  
        # Если такого года еще нет в словаре - создаем для него пустой список
        if film['year'] not in new_dict:  
            year = film['year']
            new_dict[year] = []
        # Если такой год уже есть в словаре - добавляем фильм в список
        new_dict[film['year']].append(film)  
    
    # Если год не указан - ложим по ключу 
pprint(new_dict, sort_dicts=False)



# Вариант от Ивана
year_set = set(film['year'] for film in film_list)
films_dict = dict()
for year in year_set:
    films_by_year = list()
    for film in film_list:
        if film['year'] == year:
            films_by_year.append(film)
    films_dict[year] = films_by_year
pprint(films_dict, sort_dicts=False)
 