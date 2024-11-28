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