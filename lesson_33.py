"""
Тема ООП Ч10. Паттерны ООП. Урок: 33
- Абстрактная фабрика
- Фасад
- Прототип
- Декоратор
- Посредник (Proxy)
- Адаптер (Apapter)
"""

from abc import ABC, abstractmethod

class AbstractRequest(ABC):
    
    @abstractmethod
    def make_request(self)-> str:
        pass


class RealRequest(AbstractRequest):
    
    def make_request(self)-> str:
        return "Реальный запрос"


class ProxyRequest(AbstractRequest):

    def __init__(self, real_request: AbstractRequest):
        self.real_request = real_request
        
    def make_request(self)-> str:
        self.__additional_logic()
        return self.real_request.make_request()

    def __additional_logic(self):
        print("Логика перед запросом")

# TEST
request = RealRequest()
proxy_request = ProxyRequest(request)
print(proxy_request.make_request())
