"""
Тема ООП Ч10. Паттерны ООП. Урок: 33
- Абстрактная фабрика
"""

from abc import ABC, abstractmethod

# АБСТРАКТНЫЕ ПРОДУКТЫ
class AbstractGenerator(ABC):
    def __call__(self):
        print(f"{self.__class__.__name__} работает!")


class AbstractWriter(ABC):
    def __call__(self):
        print(f"{self.__class__.__name__} работает!")


class AbstractFormatter(ABC):
    def __call__(self):
        print(f"{self.__class__.__name__} работает!")


class AbstractPublicator(ABC):
    def __call__(self):
        print(f"{self.__class__.__name__} работает!")


# КОНКРЕТНЫЕ ПРОДУКТЫ
class YouTubeGenerator(AbstractGenerator):
    pass

class YouTubeWriter(AbstractWriter):
    pass

class YouTubeFormatter(AbstractFormatter):
    pass

class YouTubePublicator(AbstractPublicator):
    pass


class TelegramGenerator(AbstractGenerator):
    pass

class TelegramWriter(AbstractWriter):
    pass

class TelegramFormatter(AbstractFormatter):
    pass

class TelegramPublicator(AbstractPublicator):
    pass




# АБСТРАКТНАЯ ФАБРИКА
class AbstractContentFactory(ABC):

    @abstractmethod
    def create_generator(self):
        pass

    @abstractmethod
    def create_writer(self):
        pass

    @abstractmethod
    def create_formatter(self):
        pass

    @abstractmethod
    def create_publicator(self):
        pass

# КОНКРЕТНЫЕ ФАБРИКИ
class YouTubeContentFactory(AbstractContentFactory):

    def create_generator(self):
        return YouTubeGenerator()

    def create_writer(self):
        return YouTubeWriter()

    def create_formatter(self):
        return YouTubeFormatter()

    def create_publicator(self):
        return YouTubePublicator()


class TelegramContentFactory(AbstractContentFactory):

    def create_generator(self):
        return TelegramGenerator()

    def create_writer(self):
        return TelegramWriter()

    def create_formatter(self):
        return TelegramFormatter()

    def create_publicator(self):
        return TelegramPublicator()


# FACADE для работы

class FacadeCreator:
    def __init__(self, factory: AbstractContentFactory):
        self.factory = factory

    def create_content(self):
        generator = self.factory.create_generator()
        writer = self.factory.create_writer()
        formatter = self.factory.create_formatter()
        publicator = self.factory.create_publicator()

        generator()
        writer()
        formatter()
        publicator()


# Тесты
yt_factory = YouTubeContentFactory()
tg_factory = TelegramContentFactory()

yt_facade = FacadeCreator(yt_factory)
yt_facade.create_content()

tg_facade = FacadeCreator(tg_factory)
tg_facade.create_content()
