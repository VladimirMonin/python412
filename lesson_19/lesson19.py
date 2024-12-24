"""
Урок 19
17.12.2024

Python: Функции высшего порядка и анонимные функции

1. Функции высшего порядка: +
    - Концепция функций как объектов первого класса
    - Передача функций как аргументов
    - Возврат функций из функций
    - Практические примеры применения

2. Встроенные функции высшего порядка:
    - map() - преобразование элементов +
    - filter() - фильтрация по условию +
    - sorted() с key функцией +
    - all() и any() для проверки условий -

3. Анонимные функции (lambda): +
    - Синтаксис lambda выражений
    - Применение с map() и filter()
    - Ограничения lambda функций
    - Сравнение с обычными функциями

4. Практика:
    - Обработка списков данных
    - Фильтрация и сортировка объектов
    - Цепочки преобразований
    - Комбинирование функций высшего порядка
"""

nums_list = [1, 2, 3, 4, 5]

new_nums_list = [num + 1 for num in nums_list]  # 2, 3, 4, 5, 6


def add_one(num):
    return num + 1


new_nums_list = [add_one(num) for num in nums_list]

nums_list = [1, 2, 3, 4, 5]


def my_map(func, nums_list: list) -> list:

    result = []

    for num in nums_list:
        result.append(func(num))

    return result


my_print = print
my_print("Hello", "World", sep=" ")

new_nums_list = my_map(add_one, nums_list)
print(new_nums_list)

some_str = "компьютер"
# some_str()  # TypeError: 'str' object is not callable

# map, filter, sorted

names_list = names = [
    "Владимир",
    "Семен",
    "Дмитрий",
    "Иван",
    "Никита",
    "Спартак",
    "Артём",
    "Рашид",
    "Григорий",
    "Вадим",
    "Андрей",
    "Размик",
    "Алексей",
    "Даниил",
    "Павел",
    "Кирилл",
    "Дмитрий",
    "Екатерина",
]

list_lenght_names = [len(name) for name in names_list]
list_lenght_names = list(map(len, names_list))
print(list_lenght_names)


# users_nums = list(map(int, input("Введите числа через пробел: ").split()))
# print(users_nums)


list_upper_names = list(map(str.upper, names_list))


def upper_name(name: str):
    """
    Функция принимает имя и возвращает его в верхнем регистре
    :param name: Строка с именем
    """
    return name.upper()


list_upper_names = list(map(upper_name, names_list))
print(list_upper_names)

"""
lambda - анонимная функция
lambda а, б: а + б

1. Нет имени
2. Нет def
3. Нет return (происходит автоматически)
4. Нет возможности дать сложный цикл или ветвление, в связи с однострочностью.
"""


def my_sum(a, b):
    return a + b


my_sum = lambda a, b: a + b


nums_list = [1, 2, 3, 4, 5]
# Обойдем через map и умножим на 2
new_nums_list = list(map(lambda num: num * 2, nums_list))

from data.cities import cities_list

populations_list = list(map(lambda city: city["population"], cities_list))

populations_list = list(map(lambda city: round(city["population"], -3), cities_list))

# Получим список цифр популяции городов, и округлим числа  до тысяч
populations_list = list(map(lambda city: round(city["population"], -3), cities_list))

# Тернарный if.  Утверждение ЕСЛИ условие, ИНАЧЕ альтернатива

# Получим список цифр популяции городов, и округлим числа  до тысяч ЕСЛИ это число, иначе оставим None
populations_list = list(
    map(
        lambda city: (
            round(city["population"], -3)
            if isinstance(city["population"], int)
            else None
        ),
        cities_list,
    )
)

print(populations_list)

"""
Хочу получить список таких словарей
{ "name": "Абакан",
    "population": 18000,}  Популяция округлена
"""

populations_list = list(
    map(
        lambda city: {
            "name": city["name"],
            "population": round(city["population"]),
        },
        cities_list,
    )
)

from pprint import pprint

# pprint(populations_list[:50])

# sort и sorted
"""
sort - метод списка, который сортирует список по возрастанию
sorted - функция, которая возвращает новый отсортированный список


[{'name': 'Абаза', 'population': 15000},
 {'name': 'Абакан', 'population': 187000},
 {'name': 'Абдулино', 'population': 18000},
 {'name': 'Абинск', 'population': 39000},

Попробуем это сортировать 2 способами
"""

# Используем метод sort
# populations_list.sort(key=lambda city: city["population"])

# Используем функцию sorted
populations_list = sorted(
    populations_list, key=lambda city: city["population"])

pprint(populations_list[:-6:-1])
pprint(populations_list[:5])


# Сортировка по 2м признакам
# Будем сортировать исходный cities_list по 
#  "subject": 
# "population": 

sorted_cities_list = sorted(
    cities_list,
    key=lambda city: (
        city["subject"],
        city["population"],
    ))

pprint(sorted_cities_list[:50])


# Filter
# filter(func, iterable)

# Найдем города которые более 1000000 человек
big_cities = list(filter(lambda city: city["population"] > 1000000, cities_list))
pprint(big_cities[:5])

# Списковое выражение
big_cities = [city for city in cities_list if city["population"] > 1000000]

pprint(big_cities[:5])

# PRACTICE Поисковик городов по субъекту
"""
1. Пользователь вводит субъект РФ
2. Мы проверяем что он есть в коллекции
3. Мы фильтруем коллекцию через filter или list comprehension
4. Выводим все города субьекта
* Можете отсортировать их по населению (по убыванию)
"""

print("Поисковик городов по субъекту")

user_subject = input("Введите субъект РФ: ")

if user_subject in {city["subject"] for city in cities_list}:
    
    filtered_cities = [city for city in cities_list if city["subject"] == user_subject]
    
    sorted_cities = sorted(
        filtered_cities, key=lambda city: city["population"], reverse=True
    )
    pprint(sorted_cities)

else:
    print("Такого субъекта нет")
