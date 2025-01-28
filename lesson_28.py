"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
- Абстрактные классы и методы
- Иерархическое наследование (вертикальное) - на примере мопса
"""


class Animal(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, favorite_toy: str, name: str, age: int):
        super().__init__(name, age)
        self.favorite_toy = favorite_toy


class Mops(Dog):
    def __init__(self, noise: str,  favorite_toy: str,  name: str, age: int):
        super().__init__(favorite_toy, name, age)
        self.noise = noise


mops = Mops("храпит", "мяч", "Ворчун", 2)
# MRO - Method Resolution Order
print(Mops.__mro__)
# (<class '__main__.Mops'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)