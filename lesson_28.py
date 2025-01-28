"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
- Абстрактные классы и методы
- Иерархическое наследование (вертикальное) - на примере мопса
- Матрешки
"""

# Множественное наследование

class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)  # pop удаляет использованные ключи
        self.age = kwargs.pop('age', None)
        super().__init__(**kwargs)

class Swim:
    def __init__(self, **kwargs):
        self.deep = kwargs.pop('deep', None)
        super().__init__(**kwargs)

    def swim(self):
        print(f"{self.name} плавает и ныряет на глубину {self.deep} метров")

class Fly:
    def __init__(self, **kwargs):
        self.speed = kwargs.pop('speed', None)
        self.height = kwargs.pop('height', None)
        super().__init__(**kwargs)

    def fly(self):
        print(
            f"{self.name} летит со скоростью {self.speed} км/ч на высоте {self.height} метров"
        )


class Duck(Animal, Swim, Fly):
    def __init__(self, **kwargs):
        self.color = kwargs.pop('color', None)
        super().__init__(**kwargs)




print(Duck.__mro__)
duck = Duck(name="Дональд", age=10, deep=10, speed=100, height=1000, color="белый")

# (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Swim'>, <class '__main__.Fly'>, <class 'object'>)