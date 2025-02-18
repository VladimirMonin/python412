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

from abc import ABC, abstractmethod
import random

class FigthingStrategy(ABC):

    @abstractmethod
    def fight(self):
        pass

# Критический пинок
class CriticalPunch(FigthingStrategy):
    def fight(self):
        print(f'Критический пинок лапой с уроном {random.randint(20, 50)}')


# Слабый удар
class WeakPunch(FigthingStrategy):
    def fight(self):
        print(f'Слабый удар лапой с уроном {random.randint(1, 10)}')

# Боевой мяу
class BattleMeow(FigthingStrategy):
    def fight(self):
        print(f'Боевой мяу без урона. Но очень страшно!')

# Кот
class Cat:
    def __init__(self, name):
        self.name = name
        self.strategy: FigthingStrategy = BattleMeow()

    def fight(self):
        print(f'{self.name} атакует:')
        self.strategy.fight()

    def set_strategy(self, strategy: FigthingStrategy):
        if not isinstance(strategy, FigthingStrategy):
            raise ValueError('Коты себя так не ведут!')
        self.strategy = strategy

if __name__ == '__main__':
    cat = Cat('Барсик')
    cat.fight()
    test = "Помурчать"
    # cat.set_strategy(test)
    cat.set_strategy(WeakPunch())
    cat.fight()

