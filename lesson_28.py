"""
Тема: ООП Ч5. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 28
"""

"""Device (базовый: бренд, модель)
Phone (+ номер телефона)
Laptop (+ размер экрана)
Tablet (+ поддержка стилуса)
"""
# Absctract Base Class
from abc import ABC, abstractmethod

# 1. Наследование от  ABC
# 2. Декораторы абстрактных методов

class AbstractFile(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: list[dict]):
        pass

    @abstractmethod
    def append(self, data: list[dict]):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.file_path}"


class TxtFile(AbstractFile):
    
    def read(self):
        pass

    def write(self):
        pass

    def append(self):
        pass


txt_file = TxtFile("file.txt")
