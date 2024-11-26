"""
Урок 8
07.11.2024

1. Завершение темы множеств:
    - Операции над множествами (union |, intersection &, difference -, symmetric_difference ^)
    - Методы issubset(), issuperset(), isdisjoint()
    - Практический пример с множествами

2. Словари (dict):
    - Концепция словарей (ключ-значение)
    - Создание словарей
    - Доступ к элементам
    - Изменение значений
    
3. Работа со словарями:
    - Простая итерация по словарю
    - Метод .keys()
    - Метод .values()
    - Метод .items()

4. Распаковка в Python:
    - Базовая распаковка последовательностей
    - Распаковка кортежей
    - Применение распаковки к .items()

5. Практика:
    - Создание простого словаря
    - Обход словаря разными способами
    - Работа с данными через распаковку
    - Объединенный пример с множествами и словарями
"""

# union - объединение множеств. Оператор |.
# intersection - пересечение множеств. Оператор &.
# difference - разность множеств. Оператор -.
# symmetric_difference - симметрическая разность множеств. Оператор ^.
# issubset - является ли множество подмножеством другого множества.
# issuperset - является ли множество
# isdisjoint - не пересекаются ли множества.

films_1 = {'Брат', 'Брат 2', 'Зеленая миля', 'Побег из Шоушенка', 'Форрест Гамп', 'Титаник'}
films_2 = {'Титаник', 'Аватар', 'Терминатор', 'Брат', 'Зеленая миля', 'Матрица'}

# Объединение множеств (union |) - какие фильмы смотрели оба человека
print("Объединение:", films_1 | films_2) # films_1.union(films_2)

# Пересечение множеств (intersection &) - какие фильмы смотрели оба человека
print("Пересечение:", films_1 & films_2) # films_1.intersection(films_2)

# Разность множеств (difference -) - какие фильмы смотрел первый человек, но не смотрел второй
print("Разность films_1 - films_2:", films_1 - films_2) # films_1.difference(films_2)
print("Разность films_2 - films_1:", films_2 - films_1)

# Симметрическая разность (symmetric_difference ^)
print("Симметрическая разность:", films_1 ^ films_2) # films_1.symmetric_difference(films_2)

# Проверка на подмножество (issubset)
subset = {'Брат', 'Титаник'}
print("subset является подмножеством films_1:", subset.issubset(films_1))

# Проверка на надмножество (issuperset)
print("films_1 является надмножеством subset:", films_1.issuperset(subset))

# Проверка на непересечение (isdisjoint)
disjoint_set = {'Властелин колец', 'Хоббит'}
print("disjoint_set не пересекается с films_1:", disjoint_set.isdisjoint(films_1))


####################### Словари #######################

# Словарь - упорядоченная коллекция элементов, где у каждого элемента есть ключ.
# Ключ - это уникальный идентификатор элемента.
# Значение - это данные, которые хранятся в элементе.

person_dict ={
    'name': 'Сёма',
    'age': 18,
    'city': 'Москва',
}

# Доступ к элементам
name = person_dict['name']
age = person_dict['age']
city = person_dict['city']

# Изменение значений
person_dict['age'] = 20

# Удаление элемента
del person_dict['city']

# Новая запись
person_dict['city'] = 'Санкт-Петербург'

# Добавим хобби
person_dict['hobbies'] = ['Дота', 'Футбол', 'Чтение']

print(person_dict)

from pprint import pprint

pprint(person_dict, sort_dicts=False)

person_dict ={
    'name': 'Сёма',
    'age': 18,
    'city': 'Москва',
}
# Перебор циклом for по словарю без методов - по ключам
[print(x) for x in person_dict] # печатаем ключи словаря
print(len(person_dict)) # Количество ключей

# keys - возвращает "список" ключей словаря
dict_k = person_dict.keys()
print(dict_k)
print(list(dict_k))
print(type(dict_k))
# Dict_keys - спископодобная структура данных, которая хранит в себе ключи словаря и может быть приведена к списку.

# values - возвращает "список" значений словаря
dict_v = person_dict.values()
print(dict_v)
# items - возвращает "список" пар ключ-значение
dict_items = person_dict.items()
print(dict_items)
###############################
for key in person_dict.keys():
    print(key)

for value in person_dict.values():
    print(value)

for key, value in person_dict.items():
    print(key, value)

# Распаковка словаря
some_list = ['Имя', 'Возраст', 'Город']

name, age, city = some_list
print(name, age, city)
name, *other = some_list
print(name, other)

dict_items = [['name', 'Сёма'], ['age', 18], ['city', 'Москва']]

key, value = dict_items[0]
key, value = dict_items[1]
key, value = dict_items[2]
# key, value = dict_items[3] # IndexError: list index out of range

for key, value in dict_items:
    print(key, value)

print(list(person_dict.items()))
for key, value in person_dict.items():
    print(key, value)


from marvel import small_dict


"""
Практика!
Задача №1
1. Запросите у пользователя названия фильма или его часть
2. Найдите эти фильмы в small_dict (не забудьте про регистр)

Для этого обойдите циклом ключи словаря, и если ключ содержит введенную строку или равен ей - выведите его.

Опционально: можете добавить это в список и потом вывести его.


Задача №2
Найдите фильмы, с годом выхода после 2024 года.
Обойдите проблему с ошибкой (невозможно сравнить None с числом)

2.1 Попробуйте их просто распечатать
2.2 Попробуйте собрать список названий
2.3 Попробуйте собрать словарь (как исходный, но фильтрованный по году)
2.4 Попробуйте собрать список словарей [{'Человек-хрюк': 2024}, ...]
----

Проверка типов данных чтобы не было ошибок при сравнении
if year is None:
    continue
"""

# 1.

user_input = 'Человек-паук: Нет пути домой'

for title in small_dict:
    if user_input.lower() in title.lower():
        print(title)


result = [title for title in small_dict if user_input.lower() in title.lower()]
print(result)