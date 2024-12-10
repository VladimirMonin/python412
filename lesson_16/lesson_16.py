"""
Урок 16
05.12.2024

Python функции: args, kwargs. Модули и файлы. Упаковка приложения. Урок: 16

1. Продвинутые аргументы функций:
    - *args для произвольного числа позиционных аргументов
    - **kwargs для произвольного числа именованных аргументов
    - Комбинирование разных типов аргументов

2. Модульность Python:
    - Конструкция if __name__ == '__main__'
    - Работа с несколькими модулями
    - Организация множественных точек входа
    - Импорты между модулями

3. Работа с файлами:
    - Чтение/запись текстовых файлов
    - Создание файла настроек
    - Форматы хранения настроек
    - Обработка ошибок при работе с файлами

4. Упаковка приложения:
    - Подготовка проекта к упаковке
    - Внешние конфигурационные файлы
    - Использование PyInstaller
    - Тестирование упакованного приложения

5. Практика:
    - Создание приложения с настройками
    - Разделение логики по модулям
    - Сохранение конфигурации
    - Финальная сборка в exe
"""

# **kwargs - произвольное число именованных аргументов

# pip install tabulate
from tabulate import tabulate

group = [
    ["Имя", "Возраст", "Рост"],
    ["Вася", 16, 180],
    ["Таня", 17, 165],
    ["Женя", 18, 175],
    ["Нина", 15, 160],
]

# Выводим на экран
print(tabulate(group, headers="firstrow", tablefmt="fancy_grid"))

# PRACTICE - функция для вывода таблицы
"""
Опишите функцию, которая будет принимать:
1. Аргументы:
    - data: list[list[str]] - список списков с данными
    - **params:
        - headers: list[str] - заголовки столбцов
        - tablefmt: str - стиль таблицы
2. Возвращает:
    - str - таблица в виде строки

Используйте внутри функции проверку на наличие ключей
headers и tablefmt в словаре params
если нет первого, укажите  headers='firstrow'
если нет второго, возьмите стиль 'grid'

Вызовите функцию с проверочным набором.

group = [
    ['Имя', 'Возраст', 'Рост'],
    ['Вася', 16, 180],
    ['Таня', 17, 165],
    ['Женя', 18, 175],
    ['Нина', 15, 160],
]

table_params = {
    'tablefmt': 'fancy_grid',
}
"""
table_params = {
    'tablefmt': 'html',
}


def get_table_by_list(data: list[list[str]], **params) -> str:
    """
    Функция для вывода таблицы из списка списков
    :param data: list[list[str]] - список списков с данными
    :param **params:
        - headers: list[str] - заголовки столбцов
        - tablefmt: str - стиль таблицы
    :return: str - таблица в виде строки
    """
    headers = params.get("headers", "firstrow")
    tablefmt = params.get("tablefmt", "grid")

    result = tabulate(data, headers=headers, tablefmt=tablefmt)

    return result


print(get_table_by_list(group, **table_params))