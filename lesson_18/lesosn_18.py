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

# CSV
import csv

table_list = [
    ["first_name", "middle_name", "last_name"],
    ["Владимир", "Александрович", "Монин"],
    ["Семен", "Константинович", "Беляев"],
    ["Дмитрий", "Владимирович", "Бобов"],
    ["Иван", "Петрович", "Бунько"],
    ["Никита", "Федорович", "Вахрамеев"],
    ["Екатерина", "Александровна", "Голосняк"],
    ["Спартак", "Витальевич", "Добровольский"],
    ["Григорий", "Сергеевич", "Калинин"],
    ["Вадим", "Валерьевич", "Козлов"],
    ["Андрей", "Викторович", "Курочкин"],
    ["Размик", "Априкович", "Мнацаканян"],
    ["Алексей", "Николаевич", "Охонько"],
    ["Даниил", "Дмитриевич", "Рукавишников"],
    ["Алексей", "Владимирович", "Черноусов"],
    ["Павел", "Алексеевич", "Шарапов"],
    ["Кирилл", "Русланович", "Шарахудинов"],
    ["Дмитрий", "Вячеславович", "Юдин"],
]

# Список словарей
table_dict = [
    {"first_name": "Владимир", "middle_name": "Александрович", "last_name": "Монин"},
    {"first_name": "Семен", "middle_name": "Константинович", "last_name": "Беляев"},
    {"first_name": "Дмитрий", "middle_name": "Владимирович", "last_name": "Бобов"},
    {"first_name": "Иван", "middle_name": "Петрович", "last_name": "Бунько"},
    {"first_name": "Никита", "middle_name": "Федорович", "last_name": "Вахрамеев"},
    {"first_name": "Екатерина", "middle_name": "Александровна", "last_name": "Голосняк"},
    {"first_name": "Спартак", "middle_name": "Витальевич", "last_name": "Добровольский"},
    {"first_name": "Григорий", "middle_name": "Сергеевич", "last_name": "Калинин"},
    {"first_name": "Вадим", "middle_name": "Валерьевич", "last_name": "Козлов"},
    {"first_name": "Андрей", "middle_name": "Викторович", "last_name": "Курочкин"},
    {"first_name": "Размик", "middle_name": "Априкович", "last_name": "Мнацаканян"},
    {"first_name": "Алексей", "middle_name": "Николаевич", "last_name": "Охонько"},
    {"first_name": "Даниил", "middle_name": "Дмитриевич", "last_name": "Рукавишников"},
    {"first_name": "Алексей", "middle_name": "Владимирович", "last_name": "Черноусов"},
    {"first_name": "Павел", "middle_name": "Алексеевич", "last_name": "Шарапов"},
    {"first_name": "Кирилл", "middle_name": "Русланович", "last_name": "Шарахудинов"},
    {"first_name": "Дмитрий", "middle_name": "Вячеславович", "last_name": "Юдин"}
]

# # Запись в CSV файл списка списков для Excel
# with open("table_list.csv", "w", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";", lineterminator="\n")
#     writer.writerows(table_list)

# # utf-8-sig - специальный кодировочный формат для Excel и продуктов Microsoft

# # Чтение CSV файла
# with open("table_list.csv", "r", encoding="utf-8-sig") as file:
#     reader = csv.reader(file, delimiter=";")
#     table_list = list(reader)


# print(table_list)

# # Считаем как список словарей
# with open("table_list.csv", "r", encoding="utf-8-sig") as file:
#     reader = csv.DictReader(file, delimiter=";")
#     table_dict = list(reader)

# print(table_dict)

new_student = {
    "first_name": "Анатолий",
    "middle_name": "Андреевич",
    "last_name": "Андреев",
}

new_student_list = [
    "Анатолий",
    "Андреевич",
    "Андреев",
]

# # Дозапись в CSV файл списка
# with open("table_list.csv", "a", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";", lineterminator="\n")
#     writer.writerow(new_student_list)


# Дозапись в CSV файл словаря
# fildnames - список названий столбцов
with open("table_list.csv", "a", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file, fieldnames=new_student.keys(), delimiter=";", lineterminator="\n"
    )
    writer.writerow(new_student)

    
"""
CSV reader и writer
CSV Reader и Writer - это классы из модуля csv для работы с CSV файлами.

CSV Reader (csv.reader):
- Создает объект для чтения CSV файлов
- Основные параметры:
  * delimiter - разделитель полей (по умолчанию ',')
  * lineterminator - символ конца строки (по умолчанию '\r\n')
  * encoding - кодировка файла (utf-8, utf-8-sig для Excel)
- Методы:
  * next() - читает следующую строку
  * list(reader) - преобразует весь файл в список списков

CSV Writer (csv.writer): 
- Создает объект для записи в CSV файлы
- Основные параметры:
  * delimiter - разделитель полей
  * lineterminator - символ конца строки

- Методы:
  * writerow() - записывает одну строку
  * writerows() - записывает несколько строк

Работа со списками:
- Списки списков напрямую записываются через writerows()
- При чтении получаем список списков
- Каждая строка CSV = список значений

Работа со словарями:
- Для словарей используются DictReader и DictWriter
- DictReader создает словари с заголовками как ключами
- DictWriter требует указания fieldnames (заголовков столбцов)
- Позволяет работать с именованными полями вместо индексов

Пример с DictWriter:
writer = csv.DictWriter(file, fieldnames=['first_name', 'middle_name', 'last_name'])
writer.writeheader() # записывает заголовки
writer.writerows(table_dict) # записывает данные

Пример с DictReader:
reader = csv.DictReader(file)
for row in reader:
    print(row['first_name']) # обращение по имени поля

"""