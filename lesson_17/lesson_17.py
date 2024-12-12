"""
Урок 17

10.12.2024

Python: Работа с файлами TXT JSON конфигурация приложений. Урок: 17

1. Основы работы с файлами: +
    - Кодировки файлов (UTF-8, ASCII, CP1251)
    - Функция open() и её параметры
    - Функция close()
    - Режимы работы с файлами (r, w, a, b)
    - Контекстный менеджер with
    - Методы read(), write(), readlines()

2. Работа с различными форматами:
    - Текстовые файлы (txt) +
    - JSON файлы и модуль json +
    - YAML файлы и модуль PyYAML -
    - CSV файлы и модуль csv -
    - Сравнение форматов для хранения конфигурации

3. Создание конфигурации приложения:
    - Структура конфигурационного файла
    - Реализация конфига в YAML
    - Валидация конфигурации
    - Обработка ошибок при чтении конфига

4. Упаковка приложения с внешней конфигурацией: -
    - Структура проекта с внешним конфигом
    - Настройка PyInstaller
    - Размещение конфига рядом с exe
    - Относительные пути в приложении

5. Практика: -
    - Создание приложения с внешним YAML-конфигом
    - Реализация чтения/записи всех изученных форматов
    - Обработка различных кодировок
    - Сборка финального приложения с внешней конфигурацией
"""


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    Читает содержимое текстового файла и возвращает его в виде строки.
    Args:
        file_path (str): Путь к файлу для чтения
        encoding (str, optional): Кодировка файла. По умолчанию 'utf-8'
    """
    with open(file_path, "r", encoding=encoding) as file:
        text = file.read()
    return text


def write_file(
    file_path: str, text: str, encoding: str = "utf-8", mode: str = "w"
) -> None:
    """
    Записывает текст в файл. Автоматически добавляет перенос строки в конце.
    Флаг по умолчанию - 'w'
    Args:
        file_path (str): Путь к файлу для записи
        text (str): Текст для записи в файл
        encoding (str, optional): Кодировка файла. По умолчанию 'utf-8'
        mode (str, optional): Режим открытия файла ('w' - перезапись, 'a' - дозапись). По умолчанию 'w'
    """
    with open(file_path, mode, encoding=encoding) as file:
        file.write(text + "\n")


# Тестируем
# Запись в файл
TXT_FILE = r"./lesson_17/lesson_17_test.txt"
# write_file(TXT_FILE, 'Тест функции', mode='a')
# Чтение из файла
# text = read_file(TXT_FILE)
# print(text)


# Контекстный менеджер  with
with open(TXT_FILE, "r", encoding="utf-8") as file:
    text = file.read()


print(text)


JSON_STRING = """

{"coord":{"lon":30.2642,"lat":59.8944},"weather":[{"id":804,"main":"Clouds","description":"пасмурно","icon":"04n"}],"base":"stations","main":{"temp":3.36,"feels_like":-1.6,"temp_min":2.08,"temp_max":3.36,"pressure":1020,"humidity":90,"sea_level":1020,"grnd_level":1018},"visibility":10000,"wind":{"speed":7,"deg":260},"clouds":{"all":100},"dt":1733851619,"sys":{"type":2,"id":197864,"country":"RU","sunrise":1733813355,"sunset":1733835282},"timezone":10800,"id":498817,"name":"Санкт-Петербург","cod":200}

"""

import json

python_data = json.loads(JSON_STRING)
print(type(python_data))
print(python_data)

json_string = json.dumps(python_data, indent=4, ensure_ascii=False)
print(json_string)

# "\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433",

# """
# ensure_ascii
# Это хитрый способ представить кириллицу (и любые другие не-ASCII символы) используя только ASCII-совместимые символы, где:

# \u говорит "внимание, дальше идет Unicode символ"
# Следующие 4 цифры - это шестнадцатеричный код символа из таблицы UTF-8
# Это как если бы мы сказали: "Не могу написать букву 'а', но могу написать инструкцию 'возьми символ номер 0430 из Unicode таблицы'".

# Такой подход позволяет:

# Использовать только ASCII символы (0-127)
# При этом кодировать любые Unicode символы
# Сохранять полную обратную совместимость
# Гарантировать корректную передачу данных через любые системы
# Это действительно умное техническое решение, которое помогло решить проблему совместимости между разными системами и кодировками!
# """

# В Python 4 метода для работы с JSON
# 1. json.loads() - преобразует строку в объект Python
# 2. json.dumps() - преобразует объект Python в строку JSON
# 3. json.load() - читает файл JSON и преобразует его в объект Python
# 4. json.dump() - записывает объект Python в файл JSON


# JSON файлы
# Load - загрузка
# Dump - выгрузка

# Сохраним данные в JSON файл
with open("lesson_17/test.json", "w", encoding="utf-8") as file:
    json.dump(python_data, file, indent=4, ensure_ascii=False)


# Загрузка данных из JSON файла
with open("lesson_17/test.json", "r", encoding="utf-8") as file:
    data = json.load(file)


from pprint import pprint

pprint(data, sort_dicts=False, indent=2)
