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

# СОСТОЯНИЯ

class KitchenState(ABC):
    @abstractmethod
    def run(self):
        pass

class Cooking(KitchenState):
    def run(self):
        print("Приготовление блюда")

class Washing(KitchenState):
    def run(self):
        print("Мытье посуды")

class LookingRefrigerator(KitchenState):
    def run(self):
        print("Задумчиво смотрим в холодильник")

# КОНТЕКСТ

class Kitchen:
    def __init__(self):
        self.state: KitchenState = LookingRefrigerator()

    def set_state(self, state: KitchenState):
        if not isinstance(state, KitchenState):
            raise TypeError("Передано неверное состояние")
        self.state = state

    def run(self):
        self.state.run()

# ИСПОЛЬЗОВАНИЕ

if __name__ == "__main__":
    kitchen = Kitchen()
    kitchen.run() # Задумчиво смотрим в холодильник
    kitchen.set_state(Cooking())
    kitchen.run() # Приготовление блюда
    kitchen.set_state(Washing())
    kitchen.run() # Мытье посуды
    kitchen.set_state(LookingRefrigerator())
    kitchen.run() # Задумчиво смотрим в холодильник
