"""
Lesson 14
28.11.2024

Знакомство с функциями
DRY - Don't repeat yourself
SRP - Single Responsibility Principle
def - Ключевое слово языка - команда объявляющая функцию
Нейминг. Используем глаголы для описания происходящего внутри функции.
"""

def hello():
    print('Hello world!')

# print() len() int() str() - уже знакомые нам
# так же методы, где тоже () - вызов функции или метода

# нужно вызвать нашу функцию
hello
hello()

a = hello
b = hello()

print(a)
print(b)

a()
# b() # TypeError: 'NoneType' object is not callable

# Аргументы функции и возврат значения
def get_message(name, message, age=18):
    # Проверка на типы данных
    if not isinstance(name, str):
        raise TypeError('Имя должно быть строкой')
    if not isinstance(message, str):
        raise TypeError('Сообщение должно быть строкой')
    if not isinstance(age, int):
        raise TypeError('Возраст должен быть числом')

    if age < 18:
        message += ' (несовершеннолетний)'
    else:
        message += ' (совершеннолетний)'
    
    
    name = name.capitalize()
    message = message.lower()
    return f'Твоё имя:{name}\nСообщение для тебя:{message}!'

print(get_message('Вася', 'привет!'))
print(get_message('Таня', 'привет!'))
print(get_message('Боб', 'Пока!', 16))
# print(get_message('Пока')) # TypeError: get_message() missing 1 required positional argument: 'message'
# print(get_message('Пока', 'Боб!', 'Таня')) # TypeError: get_message() takes 2 positional arguments but 3 were given