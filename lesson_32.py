"""
Тема ООП Ч9. SOLID и знакомство с паттернами ООП. Урок: 32

SOLID - принципы ООП
S - Single Responsibility Principle (Принцип единственной ответственности)
O - Open/Closed Principle (Принцип открытости/закрытости)
L - Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
I - Interface Segregation Principle (Принцип разделения интерфейса)
D - Dependency Inversion Principle (Принцип инверсии зависимостей)

Singletone - Одиночка. Экземпляр класса существует в единственном виде. Часто бывает нужно для соединений с БД, логгеров, соединений по сети и т.п.

Builder - Строитель. Позволяет создавать сложные объекты пошагово. Полезен когда есть необходимость делать объекты разных "конфигураций". 

"""

"""
Сделаем
- DodoManager - директор
- AbstractBuilder - абстрактный Додо Строитель
- DodoPizzaBuilder - строитель пиццы
- DodoDanvichBuilder - строитель строитель сендвичей
- Pizza - класс пиццы (классы конечных продуктов)
- Danvich - класс сендвича (классы конечных продуктов)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Product:
    name: str
    steps: List[str] = field(default_factory=list)
    
    def __str__(self) -> str:
        return f"{self.name}:\n" + "\n".join(self.steps)

class AbstractBuilder(ABC):
    def __init__(self, product: Product):
        self.product = product

    @abstractmethod
    def wash_hands(self):
        pass

    @abstractmethod
    def coock_hat(self):
        pass

    @abstractmethod
    def get_product_base(self):
        pass

    @abstractmethod
    def add_souse(self):
        pass

    @abstractmethod
    def add_products(self):
        pass

    @abstractmethod
    def pack(self):
        pass

class DodoPizzaBuilder(AbstractBuilder):
    def wash_hands(self):
        self.product.steps.append("Моем руки")
        print("Моем руки")

    def coock_hat(self):
        self.product.steps.append("Надеваем шапочку")
        print("Надеваем шапочку")

    def get_product_base(self):
        self.product.steps.append("Делаем основу для пиццы")
        print("Делаем основу для пиццы")

    def add_souse(self):
        self.product.steps.append("Добавляем соус")
        print("Добавляем соус")

    def add_products(self):
        self.product.steps.append("Добавляем продукты для пиццы")
        print("Добавляем продукты для пиццы")

    def pack(self):
        self.product.steps.append("Упаковываем пиццу")
        print("Упаковываем пиццу")

class DodoDanvichBuilder(AbstractBuilder):
    def wash_hands(self):
        self.product.steps.append("Моем руки")
        print("Моем руки")

    def coock_hat(self):
        self.product.steps.append("Надеваем шапочку")
        print("Надеваем шапочку")

    def get_product_base(self):
        self.product.steps.append("Делаем основу для сендвича")
        print("Делаем основу для сендвича")

    def add_souse(self):
        self.product.steps.append("Добавляем соус")
        print("Добавляем соус")

    def add_products(self):
        self.product.steps.append("Добавляем продукты для сендвича")
        print("Добавляем продукты для сендвича")

    def pack(self):
        self.product.steps.append("Упаковываем сендвич")
        print("Упаковываем сендвич")

class DodoManager:
    def __init__(self):
        self.builder: Optional[AbstractBuilder] = None

    def set_builder(self, builder: AbstractBuilder):
        self.builder = builder

    def make_product(self) -> Product:
        if self.builder is None:
            raise ValueError("Builder не установлен")
        self.builder.wash_hands()
        self.builder.coock_hat()
        self.builder.get_product_base()
        self.builder.add_souse()
        self.builder.add_products()
        self.builder.pack()
        return self.builder.product

if __name__ == '__main__':
    director = DodoManager()
    
    pizza_product = Product("Пицца")
    director.set_builder(DodoPizzaBuilder(pizza_product))
    print(director.make_product())
    print()
    
    danvich_product = Product("Сендвич")
    director.set_builder(DodoDanvichBuilder(danvich_product))
    print(director.make_product())
