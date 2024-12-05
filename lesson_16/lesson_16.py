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

# *args - произвольное число позиционных аргументов
products = ['яблоко', 'банан', 'апельсин']

apple, *_ = products
print(apple)# яблоко
print(_) # ['банан', 'апельсин']


def get_products(*args):
    print(args)
    print(type(args))
    [print(item) for item in args]

get_products('яблоко')
get_products(*products)
get_products(products[0], products[1], products[2])

# Проверка на палиндром
def is_palindrome(*words:str) -> dict:
    """
    Функция проверки слова на палиндром
    :param word: str - слово для проверки
    """
    result = {}
    for word in words:
        raw_word = word.lower().replace(' ', '')
        result[word] = raw_word == raw_word[::-1]

    return result

result = is_palindrome("шалаш", "топот", "дед", "мадам", "а роза упала на лапу азора")

print(result)

words = ["шалаш", "топот", "дед", "мадам", "а роза упала на лапу азора"]

print(is_palindrome(*words))

# **kwargs - произвольное число именованных аргументов

message_dict = {
    "name": "Вася",
    "message": "привет!",
}

def get_message(name, message):
    return f'Твоё имя:{name}\nСообщение для тебя:{message}!'

print(get_message(name="Вася", message="привет!"))
print(get_message(**message_dict))


message = 'привет!'
print_config = {
    'sep': '---',
    'end': '\n\n',
}

print(message, **print_config)
