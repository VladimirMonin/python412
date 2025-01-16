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
        print(f"Обрабатываем в __init__ экземпляр класса {self}")
        self.color = color

    # Посмотрим на полный конструктор. __new__
    def __new__(cls, *args, **kwargs):
        print(f"Создаём экземпляр класса {cls}")
        instance = super().__new__(cls)
        print(f'Это уже созданная собака {instance}')
        return instance

"""
Первый экземпляр
Создаём экземпляр класса <class '__main__.Dog'>
Это уже созданная собака <__main__.Dog object at 0x0000015BC7596B40>
Обрабатываем в __init__ экземпляр класса <__main__.Dog object at 0x0000015BC7596B40>

Второй
Создаём экземпляр класса <class '__main__.Dog'>
Это уже созданная собака <__main__.Dog object at 0x0000015BC7596B70>
Обрабатываем в __init__ экземпляр класса <__main__.Dog object at 0x0000015BC7596B70>
"""

dog = Dog("черный")
dog1 = Dog("белая")
dog1.name = "Стрелка"

Dog.name = "Шарик"

print(dog.name, dog.color)
print(dog1.name, dog1.color)

print(dog1.__class__.name) # Но Шарик мы можем достать - если таки обратиться к классу этого экземпляра

# __dict__ - коллекция которая даст нам все атрибуты экземпляра
print(dog.__dict__) # {'color': 'черный'}
print(dog1.__dict__) # {'color': 'белая', 'name': 'Стрелка'}

print(dir(dog1))  # атрибуты и методы экземпляра

"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'name']
"""