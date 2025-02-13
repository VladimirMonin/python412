"""
Тема ООП Ч10. Паттерны ООП. Урок: 33
- Абстрактная фабрика
- Фасад
- Прототип
- Декоратор
- Посредник (Proxy)
- Адаптер (Apapter)
"""

from abc import ABC, abstractmethod

class OnlineShop:
    def __init__(self, payment_system: "PaymentSystem"):
        self.payment_system = payment_system

    def buy(self, amount: int) -> None:
        self.payment_system.pay(amount)

    def get_document(self, id_payment: int) -> None:
         self.payment_system.get_document(id_payment)
    
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

    @abstractmethod
    def get_document(self, id_payment: int) -> None:
        pass


class YandexPayAdapter(PaymentSystem):
    def pay(self, amount: int) -> None:
        print(f"Оплата {amount} рублей через Яндекс.Кошелек")

    def get_document(self, id_payment: int) -> None:
        print(f"Документ оплаты {id_payment}")


class RoboPayAdapter(PaymentSystem):
    def pay(self, amount: int) -> None:
        print(f"Оплата {amount} рублей через Робокасса")

    def get_document(self, id_payment: int) -> None:
        print(f"Документ оплаты {id_payment}")


# TEST
shop = OnlineShop(YandexPayAdapter())
shop.buy(100)
shop.get_document(1)

shop = OnlineShop(RoboPayAdapter())
shop.buy(100)
shop.get_document(1)
