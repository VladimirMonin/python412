"""
Урок 20
19.12.2024

Python: Генераторы и функции all(), any(), yield

1. Функции all() и any():
    - Принцип работы all()
    - Принцип работы any()
    - Практические примеры использования
    - Комбинирование с другими функциями

2. Генераторы в Python:
    - Концепция генераторов
    - Отличие от списков
    - Преимущества использования
    - Генераторные выражения

3. Ключевое слово yield:
    - Синтаксис и принцип работы
    - Отличие от return
    - Создание генераторных функций
    - Экономия памяти

4. Практика:
    - Создание собственных генераторов
    - Обработка больших наборов данных
    - Валидация данных через all()/any()
    - Цепочки генераторов
    - Работа с файлами через генераторы
"""

all_list = [True, True, True]
any_list = [True, False, False]

# Как будет работать all и any
print(all(all_list))  # True
print(all(any_list))  # False

print(any(all_list))  # True
print(any(any_list))  # True

# Список строковых чисел
nums_list = ["1", "2", "3", "4", "5"]

# Проверим через all что все элементы проходят isdigit
all_nums = all(map(str.isdigit, nums_list))  # True

# Создание генераторного выражения
all_nums = all(num.isdigit() for num in nums_list)


from math import pi
from cities import cities_list

# Проверим, что в наборе есть город с населением более 10000000

result = any(map(lambda city: city["population"] > 10000000, cities_list))
print(result)  # True

# Генераторы - функции которые возвращают по одному элементу
# Генератор пирожков


def pie_generator(n):
    for i in range(n):
        yield f"Пирожок {i}"


# Объект - генератор
five_pies = pie_generator(5)
print(type(five_pies))  # <class 'generator'>
print(five_pies)  # <generator object pie_generator at 0x000001E714C7A9B0>

print(next(five_pies))  # Пирожок 0
print(next(five_pies))  # Пирожок 1
print(next(five_pies))  # Пирожок 2
# print(next(five_pies))  # Пирожок 3
# print(next(five_pies))  # Пирожок 4
# print(next(five_pies))  # Пирожок 5
# print(next(five_pies))  # StopIteration Exception

for pie in five_pies:
    print(f"Пирожок из цикла: {pie}")

ten_pies = pie_generator(10)

pies_list = list(ten_pies)
print(pies_list) 
# print(next(ten_pies))  # StopIteration Exception


# Функция, создающая огромный список в памяти
def get_huge_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Генератор, выдающий значения по одному
def get_huge_generator(n):
    for i in range(n):
        yield i ** 2

# Демонстрация разницы
# Функция попытается создать огромный список в памяти
# print("Начинаем работу с функцией...")
# huge_list = get_huge_list(100_000_000)  # Это займет много памяти и времени

# Генератор будет выдавать значения по одному
# print("Начинаем работу с генератором...")
# for i, value in enumerate(get_huge_generator(100_000_000)):
#     if i % 1_000_000 == 0:
#         print(f"Сгенерировано {i:,} значений. Текущее значение: {value}")





def cities_by_population(min_population: int):
    for city in cities_list:
        if city["population"] > min_population:
            yield f'Город: {city["name"]}, население: {city["population"]}'


# user_num = int(input("Введите минимальное население: "))

# for city in cities_by_population(user_num):
#     print(city)
#     user_answer = input("Хотите продолжить? (y/n): ")
#     if user_answer.lower() == "n":
#         print("До свидания!")
#         break


# Вспомним какие у нас есть однострочники?

# Выражение списка (list comprehension)
cities_names = [city["name"] for city in cities_list]
print(cities_names)
# Выражение множества (set comprehension)
cities_names = {city["name"] for city in cities_list}
print(cities_names)
# Выражение словаря (dict comprehension)
cities_names = {city["name"]: city["population"] for city in cities_list}
print(cities_names)

# Генераторное выражение (generator expression)
cities_names = (city["name"] for city in cities_list)



min_population = 1_000_000
# Генераторное выражение
cities_generator = (city["name"] for city in cities_list if city["population"] > min_population)

cities_generator = (f'Город: {city["name"]}, население: {city["population"]}' for city in cities_list if city["population"] > min_population)



for city in cities_generator:
    print(city)
    user_answer = input("Хотите продолжить? (y/n): ")
    if user_answer.lower() == "n":
        print("До свидания!")
        break
