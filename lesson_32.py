"""
Тема ООП Ч9. SOLID и знакомство с паттернами ООП. Урок: 32

SOLID - принципы ООП
S - Single Responsibility Principle (Принцип единственной ответственности)
O - Open/Closed Principle (Принцип открытости/закрытости)
L - Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
I - Interface Segregation Principle (Принцип разделения интерфейса)
D - Dependency Inversion Principle (Принцип инверсии зависимостей)
"""

from abc import ABC, abstractmethod


class AbstractDocumentReader(ABC):
    """
    Интерфейс для чтения документов
    """

    @abstractmethod
    def read(self, file_path: str):
        """
        Абстрактный метод для чтения документа
        """
        pass


class AbstractDocumentWriter(ABC):
    """
    Интерфейс для записи документов
    """
    # Single Responsibility Principle (Принцип единственной ответственности)
    # Один класс - одна ответственность
    # Interface Segregation Principle (Принцип разделения интерфейса)
    # Не надо заставлять всех клиентов реализовывать методы, которые они не будут использовать
    @abstractmethod
    def write(self, file_path: str):
        """
        Абстрактный метод для записи документа
        """
        pass


class AbstractDocumentAppender(ABC):
    """
    Интерфейс для дозаписи документов
    """

    @abstractmethod
    def append(self, file_path: str):
        """
        Абстрактный метод для дозаписи документа
        """
        pass


class TxtDocument(AbstractDocumentReader, AbstractDocumentWriter, AbstractDocumentAppender):
    """
    Класс для работы с текстовыми файлами
    """
    # Single Responsibility Principle (Принцип единственной ответственности)
    # Один класс - одна ответственность
    # Interface Segregation Principle (Принцип разделения интерфейса)
    # Не надо заставлять всех клиентов реализовывать методы, которые они не будут использовать
    def read(self, file_path: str):
        """
        Чтение текстового файла
        """
        print(f'Чтение текстового файла {file_path} классом {self.__class__.__name__}')
    
    def write(self, file_path: str):
        """
        Запись текстового файла
        """
        print(f'Запись текстового файла {file_path} классом {self.__class__.__name__}')
    
    def append(self, file_path: str):
        """
        Дозапись текстового файла
        """
        print(f'Дозапись текстового файла {file_path} классом {self.__class__.__name__}')


class PdfDocument(AbstractDocumentReader):
    """
    Класс для работы с pdf файлами
    """
    def read(self, file_path: str):
        """
        Чтение pdf файла
        """
        print(f'Чтение pdf файла {file_path} классом {self.__class__.__name__}')


class FileWorkerFacade:
    # Dependency Inversion Principle (Принцип инверсии зависимостей)
    # Работает с абстрактным классом, а не с конкретным классом

    # Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
    # Можно использовать любой класс, который наследуется от AbstractDocumentReader
    def __init__(self, document: AbstractDocumentReader):
        self.document = document
    
    def read(self, file_path: str):
        self.document.read(file_path)


document = TxtDocument()
file_worker = FileWorkerFacade(document)
file_worker.read("file.txt")
