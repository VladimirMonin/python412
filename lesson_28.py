"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
- Абстрактные классы и методы
- Иерархическое наследование (вертикальное) - на примере мопса
"""

#PRACTICE
"""
класс - большая матрешка
- атрибут класса - счетчик выпущенных экземпляров
- атрибут экземпляра - ID экземпляра

класс - средняя матрешка
- атрибут класса - счетчик выпущенных экземпляров
- атрибут экземпляра - Большая матрешка

класс - маленькая матрешка
- атрибут экземпляра - ID экземпляра
- атрибут экземпляра - средняя матрешка

Иерархическое наследование

создавая маленькую матрешку, мы создаем весь комплект


возможно создадим миксины 
Чтобы можно было делать матрешки из разных материлов и разных коллекций
"""

class BigMattreshka:
    id = 0
    def __init__(self):
        self.id = self.__class__.id
        self.__class__.id += 1

    def __str__(self):
        return f"Матрешка размера {self.__class__.__name__} с id {self.id}"
    
    @classmethod
    def get_id(cls):
        return cls.id


class MediumMattreshka(BigMattreshka):
    id = 0
    def __init__(self):
        self.id = self.__class__.id
        self.__class__.id += 1
        self.big_mattreshka = BigMattreshka()


class SmallMattreshka(MediumMattreshka):
    id = 0
    def __init__(self):
        self.id = self.__class__.id
        self.__class__.id += 1
        self.medium_mattreshka = MediumMattreshka()


sm = SmallMattreshka()
big = BigMattreshka()
big2 = BigMattreshka()
big3 = BigMattreshka()

print(sm.id)
print(sm.medium_mattreshka.big_mattreshka.id)
print(big.id)
print(big2.id)
print(big3.id)
print(big.get_id(), big3.get_id())
print(SmallMattreshka.id)
print(sm.get_id())