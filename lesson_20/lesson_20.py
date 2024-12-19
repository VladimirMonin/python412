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
print(all(all_list)) # True
print(all(any_list)) # False

print(any(all_list))  # True
print(any(any_list))  # True

# Список строковых чисел
nums_list = ["1", "2", "3", "4", "5"]

# Проверим через all что все элементы проходят isdigit
all_nums = all(map(str.isdigit, nums_list)) # True

# Создание генераторного выражения
all_nums = all(num.isdigit() for num in nums_list)


from cities import cities_list

# Проверим, что в наборе есть город с населением более 10000000

result = any(map(lambda city: city["population"] > 10000000, cities_list))
print(result) # True

# 