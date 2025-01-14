"""
Lesson 24
14.01.2025
Знакомство с ООП в Python
"""

# Классы
# Класс - это шаблон для создания объектов
# Объект - это экземпляр класса

# Нейминг
"""
UpperCamelCase - для классов
Используем существительные и прилагательные
"""

class Car:
    mark = "Ёмобиль" # Поле или атрибут класса

car = Car()
car_1 = Car()
print(car)
print(type(car))

print(car_1)

print(car.mark)
print(car_1.mark)
