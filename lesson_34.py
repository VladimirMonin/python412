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

# Паттерн Состояние на примере нескольких разных действий на кухне

from abc import ABC, abstractmethod

class Command(ABC):
    """Абстрактный класс команды"""
    @abstractmethod
    def execute(self):
        pass

class Dog:
    """
    Получатель команд (Receiver)
    Класс, который непосредственно выполняет действия
    """
    def sit(self):
        print("Собака села")
    
    def roll(self):
        print("Собака перекатилась")
    
    def bark(self):
        print("Гав-гав!")

class SitCommand(Command):
    """Конкретная команда для действия 'сидеть'"""
    def __init__(self, dog: Dog):
        self._dog = dog
    
    def execute(self):
        self._dog.sit()

class RollCommand(Command):
    """Конкретная команда для действия 'перекатиться'"""
    def __init__(self, dog: Dog):
        self._dog = dog
    
    def execute(self):
        self._dog.roll()

class BarkCommand(Command):
    """Конкретная команда для действия 'лаять'"""
    def __init__(self, dog: Dog):
        self._dog = dog
    
    def execute(self):
        self._dog.bark()

class Owner:
    """
    Инициатор (Invoker)
    Хозяин собаки, который отдает команды
    """
    def __init__(self):
        self._command = None
    
    def set_command(self, command: Command):
        self._command = command
    
    def execute_command(self):
        self._command.execute()

# Пример использования
if __name__ == "__main__":
    # Создаем получателя
    dog = Dog()
    
    # Создаем команды
    sit = SitCommand(dog)
    roll = RollCommand(dog)
    bark = BarkCommand(dog)
    
    # Создаем вызывающего
    owner = Owner()
    
    # Выполняем команды
    owner.set_command(sit)
    owner.execute_command()  # Собака села
    
    owner.set_command(roll)
    owner.execute_command()  # Собака перекатилась
    
    owner.set_command(bark)
    owner.execute_command()  # Гав-гав!