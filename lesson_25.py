"""
Lesson 25
16.01.2025

ООП. 
- Методы и атрибуты классов
- Методы и атрибуты экземпляров
- self
- __call__
"""


class JpegImage:
    """
    Класс - муляж для демонстрации полиморфизма на примере работы с разными типами изображений
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

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


class PngImage:
    """
    Класс - муляж для демонстрации полиморфизма на примере работы с разными типами изображений
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

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


image_jpeg_1 = JpegImage("image_1.jpeg")
image_jpeg_2 = JpegImage("image_2.jpeg")
image_png_1 = PngImage("image_1.png")
image_png_2 = PngImage("image_2.png")


images = [image_jpeg_1, image_jpeg_2, image_png_1, image_png_2]

for image in images:
    image.open()
    image.crop(100, 100)
