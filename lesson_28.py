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

    def test(self):
        print(f"Тестовый метод из класса Animal")
        


class Swim:
    def swim(self):
        return f"плавает"
    
    def test(self):
        print(f"Тестовый метод из класса Swim")


class Fly:
    def fly(self):
        return f"летает"
    
    def test(self):
        print(f"Тестовый метод из класса Fly")


class Duck(Swim, Fly, Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

print(Duck.__mro__)
duck = Duck("Дональд", 2)
duck.test()
# (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Swim'>, <class '__main__.Fly'>, <class 'object'>)