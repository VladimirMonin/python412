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


class AbstractBuilder(ABC):

    def __init__(self, product: str):
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
        self.product += "Моем руки\n"
        print("Моем руки")

    def coock_hat(self):
        self.product += "Надеваем шапочку\n"
        print("Надеваем шапочку")

    def get_product_base(self):
        self.product += "Делаем основу для пиццы\n"
        print("Делаем основу для пиццы")

    def add_souse(self):
        self.product += "Добавляем соус\n"
        print("Добавляем соус")

    def add_products(self):
        self.product += "Добавляем продукты для пиццы\n"
        print("Добавляем продукты для пиццы")

    def pack(self):
        self.product += "Упаковываем пиццу\n"
        print("Упаковываем пиццу")



class DodoDanvichBuilder(AbstractBuilder):
    
    def wash_hands(self):
        self.product += "Моем руки\n"
        print("Моем руки")

    def coock_hat(self):
        self.product += "Надеваем шапочку\n"
        print("Надеваем шапочку")

    def get_product_base(self):
        self.product += "Делаем основу для денвича\n"
        print("Делаем основу для денвича")

    def add_souse(self):
        self.product += "Добавляем соус\n"
        print("Добавляем соус")

    def add_products(self):
        self.product += "Добавляем продукты для денвича\n"
        print("Добавляем продукты для денвича")

    def pack(self):
        self.product += "Упаковываем денвич\n"
        print("Упаковываем денвич")


class DodoManager:
    def __init__(self):
        self.builder: AbstractBuilder = None

    def set_builder(self, builder: AbstractBuilder):
        self.builder = builder

    def make_product(self) -> str:
        self.builder.wash_hands()
        self.builder.coock_hat()
        self.builder.get_product_base()
        self.builder.add_souse()
        self.builder.add_products()
        self.builder.pack()
        return self.builder.product


director = DodoManager()
director.set_builder(DodoPizzaBuilder("Пицца: "))
print(director.make_product())

director.set_builder(DodoDanvichBuilder("Сендвич: "))
print(director.make_product())
