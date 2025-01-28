"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
"""

"""Device (базовый: бренд, модель)
Phone (+ номер телефона)
Laptop (+ размер экрана)
Tablet (+ поддержка стилуса)
"""


class Device:
    avalible_brands = ["Apple", "Samsung", "Xiaomi", "Huawei", "Nokia"]

    def __init__(self, brand: str, model: str):
        self.brand = self.__validate_brand(brand)
        self.model = model

    def __str__(self):
        return f"Тип девайса:{self.__class__.__name__}\n{self.brand} {self.model}"
    
    def __validate_brand(self, brand):
        if brand not in self.__class__.avalible_brands:
            raise ValueError(f"Бренд {brand} не поддерживается")
        return brand
    
    def turn_on(self):
        return f"Включаем {self.brand} {self.model}"
    
    def turn_off(self):
        return f"Выключаем {self.brand} {self.model}"
    

class Iphone(Device):
    def __init__(self, brand: str, model: str, memory: int, color: str):
        super().__init__(brand, model)
        self.memory = memory
        self.color = color

    def turn_light(self):
        return f"Включаем подсветку яблочка"


phone = Iphone("Apple", "Iphone 17 Pro Max", 2048, "Black")
phone.turn_on()
