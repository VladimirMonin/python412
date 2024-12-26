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


def say_name(name: str):
    # name - local в пространстве функции say_name
    def say_goodbye():
        print(f"{name}, настал твой час!")

    say_goodbye()


say_name("Валера")

# Замыкания


def say_name2(name: str):
    # name - local в пространстве функции say_name
    name = name.capitalize()

    def say_goodbye():
        print(f"{name}, настал твой час!")

    return say_goodbye


goodbye_v = say_name2("Валера")
goodbye_b = say_name2("Борис")

goodbye_v()
goodbye_b()


"""
Пока goodbye_v ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Валера останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к goodbye_v

goodbye_v -> say_name2 -> say_goodbye -> name = "Валера" 
"""

from typing import Callable

# Callable - что-то вызываемое (функция)- значит она сама вызываема
# [[аргумент1, аргумент2], возвращаемое значение]
# new_name: Callable[[int, int], int] = sum_a_b


def counter(start: int = 0) -> Callable[[], int]:
    # Данные переменной start лежат ТУТ

    def step():
        # При вызове мы переписываем start
        # Это возможно благодаря nonlocal (доступ наружу)
        nonlocal start
        start += 1
        return start

    return step


c1: Callable = counter()
c2: Callable = counter(10)

print(c1())
print(c1())

print(c2())
print(c2())

# Подобие декоратора - принт декоратор

def print_msg():
    print('Послали сообщение')

def print_decorator(func: Callable):
    func = func
    def wrapper():
        print('Декорируем функцию')
        func()
        print('Функция декорирована')

    return wrapper


# Как бы выглядела декорация если бы не было синатксического сахара в виде @

# decorated_func = print_decorator(print_msg)
# decorated_func()

# Декораторирование "с собачкой"

# @print_decorator
# def print_msg2():
#     print("Послали сообщение")


# print_msg2()


# @print_decorator
# def print_msg3(msg: str):
#     print(f"Послали сообщение: {msg}")


# print_msg3("Привет, мир!")


def print_decorator2(func: Callable):
    def wrapper(msg: str):
        print(f"Декорируем функцию с аргументом {msg}")
        func(msg)
        print("Функция декорирована")

    return wrapper

@print_decorator2
def print_msg4(msg: str):
    print(f"Послали сообщение: {msg}")

print_msg4("Привет, мир!")


def print_decorator3(func: Callable):
    def wrapper(*args, **kwargs):
        print(f"Декорируем функцию с аргументами {args} и {kwargs}")
        func(*args, **kwargs)
        print("Функция декорирована")

    return wrapper

@print_decorator3
def print_msg5(name: str, msg: str, age:   int = 18):
    print(f"Послали сообщение: {msg} для {name} {age} лет")

@print_decorator3
def get_msg(msg: str):
    return f'Получено сообщение: {msg}'

print_msg5("Валера", "Привет, мир!", 25)
result_get_msg = get_msg("Привет, мир!")
print(result_get_msg)

def print_decorator4(func: Callable):
    def wrapper(*args, **kwargs):
        print(f"Декорируем функцию с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print("Функция декорирована")
        
        return result

    return wrapper

@print_decorator4
def get_msg2(msg: str):
    return f'Получено сообщение: {msg}'


result_get_msg2 = get_msg2("Привет, мир!")
print(result_get_msg2)
