"""
Урок 19
17.12.2024

Python: Функции высшего порядка и анонимные функции

1. Функции высшего порядка:
    - Концепция функций как объектов первого класса
    - Передача функций как аргументов
    - Возврат функций из функций
    - Практические примеры применения

2. Встроенные функции высшего порядка:
    - map() - преобразование элементов
    - filter() - фильтрация по условию
    - sorted() с key функцией
    - all() и any() для проверки условий

3. Анонимные функции (lambda):
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
