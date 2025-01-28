"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
"""

"""Device (базовый: бренд, модель)
Phone (+ номер телефона)
Laptop (+ размер экрана)
Tablet (+ поддержка стилуса)
"""


class Device:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Тип девайса:{self.__class__.__name__}\n{self.brand} {self.model}"
    
    def turn_on(self):
        return f"Включаем {self.brand} {self.model}"
    
    def turn_off(self):
        return f"Выключаем {self.brand} {self.model}"
    

class Iphone(Device):
    def __init__(self, memory: int, color: str):
        self.memory = memory
        self.color = color


phone = Iphone(128, "Black")
phone.turn_on()
