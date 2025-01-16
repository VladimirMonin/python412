"""
Lesson 25
16.01.2025

ООП. 
- Методы и атрибуты классов
- Методы и атрибуты экземпляров
- self
- __call__
- @classmethod
- @staticmethod
"""


class JpegImage:
    """
    Класс - муляж для демонстрации полиморфизма на примере работы с разными типами изображений
    """

    extensions = ["jpg", "jpeg"]

    def __init__(self, file_path: str):
        self.file_path = file_path

    @classmethod
    def get_available_extensions(cls):
        """
        Метод возвращает список доступных расширений
        """
        return cls.extensions
    
    @classmethod
    def is_valid_extension(cls, extension: str) -> bool:
        """
        Метод проверяет расширение на валидность
        :param extension: Расширение файла
        :return: True/
        """
        return extension in cls.extensions
    
    def open(self):
        """
        Метод имитирующий открытие файла
        """
        print(f"Открываем {self.file_path}")

    def crop(self, heigth, width):
        """
        Метод имитирующий обрезку файла
        :param heigth: Выоста
        :param width: ширина
        """
        print(f"Обрезаем файл {self.file_path} до ширины: {width} и высоты {heigth}")

    @staticmethod
    def image_analys(file_path: str):
        """
        Анализ файла
        """
        print(f'{file_path} - это файл')

    


image = JpegImage("image.jpg")
image.image_analys("банан.jpg")
