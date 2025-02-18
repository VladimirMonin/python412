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
    def __init__(self, coin_name: str):
        self.coin_name = coin_name

    @abstractmethod
    def execute(self):
        pass

class BuyCommand(BotCommand):
    def execute(self):
        print(f"Покупаем монету {self.coin_name}")

class SellCommand(BotCommand):
    def execute(self):
        print(f"Продаем монету {self.coin_name}")

class GetPriceCommand(BotCommand):
    def execute(self):
        print(f"Запрашиваем цену монеты {self.coin_name}")

class SetPriceCommand(BotCommand):
    def execute(self):
        print(f"Выставляем уведомление цены монеты {self.coin_name}")

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

    def buy(self, coin_name: str):
        self.bot.execute_commands(BuyCommand(coin_name))

    def sell(self, coin_name: str):
        self.bot.execute_commands(SellCommand(coin_name))

    def get_price(self, coin_name: str):
        self.bot.execute_commands(GetPriceCommand(coin_name))

    def set_price(self, coin_name: str):
        self.bot.execute_commands(SetPriceCommand(coin_name))

# ИСПОЛЬЗОВАНИЕ
if __name__ == "__main__":
    api = ExchangeAPI()
    api.buy("BTC")
    api.sell("ETH")
    api.get_price("DOGE")
    api.set_price("XRP")

    print("\nИстория команд:")
    for command in api.bot.history:
        print(f"{command.__class__.__name__}: {command.coin_name}")