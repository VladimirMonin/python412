"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
- Абстрактные классы и методы
- Иерархическое наследование (вертикальное) - на примере мопса
- Матрешки
"""

# Множественное наследование

class Animal():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Swim:
    def __init__(self, deep: int):
        self.deep = deep

    def swim(self):
        return f"Ныряет на глубину {self.deep} метров"
    


class Fly:
    def __init__(self, speed: int, height: int):
        self.speed = speed
        self.height = height

    def fly(self):
        return f"Летает со скоростью {self.speed} км/ч на высоту {self.height} метров"
    

class Duck(Animal, Swim, Fly):
    def __init__(
        self, name: str, age: int, deep: int, speed: int, height: int, color: str
    ):
        Animal.__init__(self, name, age)
        Swim.__init__(self, deep)
        Fly.__init__(self, speed, height)
        self.color = color


print(Duck.__mro__)
duck = Duck("Дональд", 2, 5, 100, 1000, "белый")
print(duck.swim())
print(duck.fly())
# (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Swim'>, <class '__main__.Fly'>, <class 'object'>)