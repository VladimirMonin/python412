"""
Урок 18

12.12.2024

Python: CSV и YAML форматы. Конфигурация приложений. Урок: 18


1. YAML конфигурация:
    - Установка и импорт PyYAML
    - pip install py
    - Синтаксис YAML файлов
    - Методы load() и dump()
    - Преимущества над JSON


2. Работа с CSV файлами:
    - Модуль csv и его основные классы
    - DictReader и DictWriter
    - Диалекты CSV
    - Практика с табличными данными

    
3. Создание конфигурации приложения:
    - Структура конфигурационного файла
    - Реализация конфига в YAML
    - Валидация конфигурации
    - Обработка ошибок при чтении

4. Упаковка приложения:
    - Структура проекта с внешним конфигом
    - Настройка PyInstaller
    - Размещение конфига рядом с exe
    - Относительные пути в приложении

5. Практика:
    - Доработка приложения с внешней конфигурацией
    - Реализация чтения/записи CSV
    - Создание YAML конфига
    - Сборка финального приложения
"""

# PyYAML - библиотека для работы c YAML
# pip install pyyaml

import yaml

# Список покупок
shopping_list = [
    {
        "name": "Молоко",
        "quantity": 2,
        "unit": "литра",
        "category": "Молочные продукты",
        "priority": "высокая",
    },
    {
        "name": "Хлеб",
        "quantity": 1,
        "unit": "буханка",
        "category": "Хлебобулочные изделия",
        "priority": "средняя",
    },
    {
        "name": "Яблоки",
        "quantity": 1.5,
        "unit": "кг",
        "category": "Фрукты",
        "priority": "низкая",
    },
]

shop_list = ["молоко", "кефир", "бананы"]

# Методы yaml

# yaml.dump() - запись данных в YAML файл
# yaml.load() - чтение данных из YAML файла

yaml_string = yaml.dump(shop_list, allow_unicode=True)
print(yaml_string)

# Читаем config.yaml и печатаем его
with open("lesson_18\config.yaml", "r", encoding="utf-8") as file:
    yaml_data = yaml.load(file, Loader=yaml.Loader)
    print(yaml_data)


CITY = yaml_data["city"]
TIMEOUT = yaml_data["timeout"]

print(CITY, TIMEOUT)
