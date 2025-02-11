"""
Тема ООП Ч9. SOLID и знакомство с паттернами ООП. Урок: 32

SOLID - принципы ООП
S - Single Responsibility Principle (Принцип единственной ответственности)
O - Open/Closed Principle (Принцип открытости/закрытости)
L - Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
I - Interface Segregation Principle (Принцип разделения интерфейса)
D - Dependency Inversion Principle (Принцип инверсии зависимостей)

Singletone - Одиночка. Экземпляр класса существует в единственном виде. Часто бывает нужно для соединений с БД, логгеров, соединений по сети и т.п.
"""

class Singletone():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        self.data = data


st = Singletone(10)
st2 = Singletone(20)

print(st.data, st)
print(st2.data, st2)

# 20 <__main__.Singletone object at 0x0000017115137D70>
# 20 <__main__.Singletone object at 0x0000017115137D70>