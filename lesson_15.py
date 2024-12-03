"""
Урок 15
03.12.2024

Python функции. Аргументы и модули. Библиотеки plyer и requests. Урок: 15


1. Повторение функций:
    - DRY и SRP принципы
    - Объявление функций (def)
    - Вызов функций
    - Возврат значений (return)
    - Базовые проверки типов (isinstance)

2. Типы аргументов функций:
    - Позиционные аргументы
    - Именованные аргументы  
    - Аргументы по умолчанию
    - Обязательные и необязательные аргументы

3. Работа с внешними библиотеками:
    - Установка через pip
    - Импорт модулей
    - Библиотека plyer для уведомлений
    - Библиотека requests для HTTP запросов

4. Создание модулей:
    - Разделение кода на модули
    - Импорт собственных модулей
    - Относительные и абсолютные импорты
    - __name__ == '__main__'

5. Практика:
    - Создание функций для работы с API
    - Отправка уведомлений через plyer
    - Получение данных через requests
    - Структурирование кода в модули
"""

# Позиционные VS именованные аргументы

# def get_message(name, message, age=18):
#     # Проверка на типы данных
#     if not isinstance(name, str):
#         raise TypeError('Имя должно быть строкой')
#     if not isinstance(message, str):
#         raise TypeError('Сообщение должно быть строкой')
#     if not isinstance(age, int):
#         raise TypeError('Возраст должен быть числом')

#     if age < 18:
#         message += ' (несовершеннолетний)'
#     else:
#         message += ' (совершеннолетний)'
    
    
#     name = name.capitalize()
#     message = message.lower()
#     return f'Твоё имя:{name}\nСообщение для тебя:{message}!'

# print(get_message('Вася', 'привет!'))
# print(get_message('Таня', 'привет!'))
# print(get_message('Боб', 'Пока!', 16))
# print(get_message('Пока')) # TypeError: get_message() missing 1 required positional argument: 'message'
# print(get_message('Пока', 'Боб!', 'Таня')) # TypeError: get_message() takes 2 positional arguments but 3 were given

# result = get_message('Вася', 'привет!', 16)
# result = get_message(age=16, name='Вася', message='привет!')
# result = get_message(message='привет!', name='Вася')


#PRACTICE - функция проверки на палиндром одного слова
"""
Напишите функцию проверки на палиндром (слово читается в обе стороны) для одного слова или фразы
Учтите регистр и пробелы

Напишите блок проверки с пользовательским вводом и вызовом функции
Возврат булева значения
"""
# type hints - аннотация типов
def is_palindrome(word:str) -> bool:
    """
    Функция проверки слова на палиндром
    :param word: str - слово для проверки
    """
    word = word.replace(' ', '').lower()
    return word == word[::-1]

# Базовая аннотация типов
"""
str
int
float
bool
list
dict
tuple
set
list[str]
dict[str, int]
"""

# user_word = input('Введите слово: ')

# if is_palindrome(user_word):
#     print('Это палиндром')
# else:
#     print('Это не палиндром')


def check_palindrome(word:str) -> str:
    """
    Функция проверки на палиндром от Спартака.
    Возвращает строку с отчётом
    """
    raw_word = word.lower().replace(' ', '')
    if raw_word == raw_word[::-1]:
        return f'{word} - это палиндром'
    else:
        return f'{word} - не палиндром'


# print(check_palindrome(input('Введите слово: ')))


words = ["хлеб", "кот", "дед", "мама"]

# def check_many_palindromes(words:list[str]) -> str:
#     for word in words:
#         if is_palindrome(word):
#             return f'{word} - это палиндром'
    
#     return 'Нет палиндромов'
   
        
# # Протестируем как это будет работать
# print(check_many_palindromes(words))


def check_many_palindromes(words:list[str]) -> dict[str, bool]:
    result = {}
    for word in words:
        if is_palindrome(word):
            result[word] = True
        else:
            result[word] = False
    
    return result

# Тест
print(check_many_palindromes(words))