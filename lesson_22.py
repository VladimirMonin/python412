"""
Lesson 22
Повторение:
  -Области видимости
  -Замыкания
  -Принт декоратор

Декоратор с возвратом значения
Декоратор замеряющий скорость работы функции
"""

# Области видимости

# Built-in scope - встроенная область видимости (служебная)
# Global scope - глобальная область видимости
# Local scope - локальная область видимости
# Nonlocal scope - не локальная область видимости

my_print = print
my_print("Hello, world!")
print(type(my_print))

a = 2  # global


def one():
    a = 1  # local
    print(a)


print(a)  # global 2
one()  # local 1
print(a)  # global 2


def two():
    global a
    a = 1  # local
    print(a)


print("С директивой global")  # global 2
print(a)  # global 2
two()  # global 1
print(a)  # global 1


def three():
    a = 1  # local
    print(f"Функция three a: {a}")

    def inner():
        nonlocal a
        a = 2  # nonlocal
        print(f"Функция inner a: {a}")

    inner()
    print(f"Функция three a: {a}")
    print(a)


three()
