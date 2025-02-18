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
Пишем пример паттерна Command - Команда.
Простой торговый бот

Команды:
- Купить монету
- Продать монету
- Запросить цену монеты
- Выставить уведомление цены монеты
"""

from abc import ABC, abstractmethod

class BotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class BuyCommand(BotCommand):
    def execute(self):
        print("Покупаем монету")

class SellCommand(BotCommand):
    def execute(self):
        print("Продаем монету")

class GetPriceCommand(BotCommand):
    def execute(self):
        print("Запрашиваем цену монеты")

class SetPriceCommand(BotCommand):
    def execute(self):
        print("Выставляем уведомление цены монеты")

# РАБОТА С КОМАНДАМИ
# ДВА КЛАССА
"""
Эмуляция API биржи
и торгового бота
"""

class Bot:
    def __init__(self):
        self.history: list[BotCommand] = []

    def _add_to_history(self, command: BotCommand):
        self.history.append(command)

    def execute_commands(self, command: BotCommand):
        command.execute()
        self._add_to_history(command)


class ExchangeAPI:
    def __init__(self):
        self.bot = Bot()

    def buy(self):
        self.bot.execute_commands(BuyCommand())

    def sell(self):
        self.bot.execute_commands(SellCommand())

    def get_price(self):
        self.bot.execute_commands(GetPriceCommand())

    def set_price(self):
        self.bot.execute_commands(SetPriceCommand())

# ИСПОЛЬЗОВАНИЕ
if __name__ == "__main__":
    api = ExchangeAPI()
    api.buy()
    api.sell()
    api.get_price()
    api.set_price()

    print("История команд:")
    for command in api.bot.history:
        print(command)