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
"""
Dunder underscope методы, дандер методы, или магические методы
__init__ - инициализатор
"""

class SimpleCar:
    mark = "Lada"

simple_car_1 = SimpleCar()
simple_car_2 = SimpleCar()

simple_car_1.mark = "BMW"
simple_car_1.color = "red"

print(simple_car_1.mark)
print(simple_car_1.color)

class Car:
    def __init__(self, mark: str, color: str):
        self.mark = mark
        self.color = color
        print(self)

    def drive(self):
        print(f"Машина {self.mark} едет")


# car1 = Car() # TypeError: Car.__init__() missing 1 required positional argument: 'mark'

car1 = Car("BMW", "чёрный")
car2 = Car("Audi", "зелёная")

print(car1.mark)
print(car2.mark)

car1.drive()
car2.drive()
