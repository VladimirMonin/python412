"""
18.02.2025
Тема ООП Ч11. Паттерны ООП. Урок: 34
- Поведенческие паттерны ООП
- Паттерн Strategy - Стратегия - способ реализации алгоритма разными вариантами (одно действие - разные реализации)

- Паттерн State - Состояние - способ организации кода при переходе от одного состояния к другому
- Паттерн Observer - Наблюдатель - способ организации кода, когда один объект наблюдает за другим объектом

- Паттерн Command - Команда - способ организации кода, когда один объект передает команду другому объекту

- Паттерн Chain of Responsibility - Цепочка обязанностей - способ организации кода, когда один объект передает обязанности другому объекту

"""
"""
Описание примера.
Пишем пример паттерна Наблюдатель.

Классы:
Хозяин - Owner
Кот - Cat
Пес - Dog
Хомяк - Hamster

Хозяин режет мясо, рыбу и орехи. Каждый наблюдатель (кот, пес, хомяк) реагирует на это по-своему.
Есть список наблюдателей, которые реагируют на действия хозяина.
"""

from abc import ABC, abstractmethod

class  AbstractPet(ABC):
    def __init__(self, name):
        self.name = name
        self.favorite_food = [""]
        self.current_food = ""

    @abstractmethod
    def update(self, message):
        pass

    @abstractmethod
    def reaction(self):
        pass

class Cat(AbstractPet):
    def update(self, message):
        print(f"Кот получил сообщение: {message}")
        self.current_food = message.lower()
        self.reaction()

    def reaction(self):
        if any(food.lower() in self.current_food for food in self.favorite_food):
            print(f"{self.name} мурлычет")
        else:
            print(f"{self.name} игнорирует")

class Dog(AbstractPet):
    def update(self, message):
        print(f"Пёс получил сообщение: {message}")
        self.current_food = message.lower()
        self.reaction()

    def reaction(self):
        if any(food.lower() in self.current_food for food in self.favorite_food):
            print(f"{self.name} виляет хвостом")
        else:
            print(f"{self.name} всё равно заинтересованно смотрит")

class Hamster(AbstractPet):
    def update(self, message):
        print(f"Хомяк получил сообщение: {message}")
        self.current_food = message.lower()
        self.reaction()

    def reaction(self):
        if any(food.lower() in self.current_food for food in self.favorite_food):
            print(f"{self.name} смотрит прожигающим душу взглядом")
        else:
            print(f"{self.name} ему пофиг")

class Owner:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet: AbstractPet):
        self.pets.append(pet)

    def remove_pet(self, pet: AbstractPet):
        self.pets.remove(pet)

    def notify_pets(self, message):
        for pet in self.pets:
            pet.update(message)

    def cut_fish(self):
        self.notify_pets("рыба")

    def cut_meat(self):
        self.notify_pets("мясо")

    def cut_nuts(self):
        self.notify_pets("орехи")

if __name__ == "__main__":
    owner = Owner()
    cat = Cat("Барсик")
    dog = Dog("Тузик")
    hamster = Hamster("Хомяк")
    owner.add_pet(cat)
    owner.add_pet(dog)
    owner.add_pet(hamster)
    cat.favorite_food = ["рыба", "мясо"]
    dog.favorite_food = ["мясо"]
    hamster.favorite_food = ["орехи"]
    owner.cut_fish()
    owner.cut_meat()
    owner.cut_nuts()