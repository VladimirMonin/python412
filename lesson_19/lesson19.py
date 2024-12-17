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
    "Екатерина"
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
