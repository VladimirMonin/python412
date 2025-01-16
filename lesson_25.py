"""
Lesson 25
16.01.2025

ООП. 
- Методы и атрибуты классов
- Методы и атрибуты экземпляров
- self
- __call__
"""

class Dog:
    name = "Бобик"

    def __init__(self, color: str):
        self.color = color


dog = Dog("черный")
dog1 = Dog("белая")
dog1.name = "Стрелка"

Dog.name = "Шарик"

print(dog.name, dog.color)
print(dog1.name, dog1.color)
