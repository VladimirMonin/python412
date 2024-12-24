"""
24.12.2024
Урок 21. Области видимости. Замыкания. Декораторы
- 4 Области видимости в Python
"""

# Области видимости в Python

 
# 1. Глобальная область видимости
# 2. Локальная область видимости
# 3. Нелокальная область видимости

# Функция счётчик которая хранит состояние
from typing import Callable
"""
Callable - это аннотация типа, которая позволяет указать, что что возвращается является вызываемым объектом.
[[аргумент_a, аргумент_b], возвращаемый тип данных]
"""



def counter()-> Callable[[], int]:
    
    count = 0
    print(f"{id(count)=}")
    
    def inner() -> int:
        nonlocal count
        count += 1
        return count
    
    return inner

counter1 = counter()
print(id(counter1)) # 140707366366784
counter2 = counter()
print(id(counter2)) # 140707366366848
print(counter1()) # 1
print(counter1()) # 2
print(counter1()) # 3

print(counter2())  # 1
print(counter2())  # 2
