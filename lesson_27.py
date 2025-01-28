"""
Lesson 27
23.01.2025

ООП. Инкапсуляция. Продолжение.
- Класс "Шифр Цезаря" основанный на сдвиге по таблице кодирования UTF-8
- ord() - возвращает код символа в таблице UTF-8
- chr() - возвращает символ по коду в таблице UTF-8

Employee и  Organisaton как пример взаимодействия классов
Класс ManagerEmployee и потребность в наследовании при незначительных вариациях логики и атрибутов
Базовый пример наследования в коде. DRY - избегаем повторения кода (а так же сложных аннотаций типов)
Animal и Dog базовый вариант наследования
self.__class__.__name__
"""

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def voise(self):
        # self. - экземпляр
        # __class__ обращение к своему классу
        # __name__ получение имени класса в виде строки
        return f"{self.__class__.__name__} подаёт голос"
    
    def movie(self):
        return f"{self.name} двигается"


class Dog(Animal):
    
    def movie(self):
        return f"{self.name} бегает"
    
    def voise(self):
        # voise = Animal.voise(self)
        voise = super().voise()
        voise += " гав-гав"
        return voise


dog = Dog("Белка", 2)
animal = Animal("Стрелка", 3)
dog.voise() # Dog подает голос
animal.voise() # Animal подает голос
