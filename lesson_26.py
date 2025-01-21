"""
Lesson 26
21.01.2025

ООП. Инкапсуляция.
Инкапсуляция - возможность что-то сокрыть внутри-класса.
Атрибуты, методы. Т.е. мы можем спрятать логику и информацию, от воздействия извне.

И при желании, мы можем дать интерфейсы для работы с этим.
_ - защищённые атрибуты и методы
__ - приватные атрибуты и методы
"""
from dotenv import load_dotenv
import os
from openai import OpenAI    # pip install openai

load_dotenv()

VSE_GPT_KEY= os.getenv("VSE_GPT_KEY")
BASE_URL = "https://api.vsegpt.ru/v1"

class Employee:
    def __init__(self, name: str, age: int, salary: int | float):
        self.name = name
        self.__age = age
        self._salary = salary
        self.__experience: int = 0
        self.__salary_index: int = 10

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if not isinstance(age, int) and age > 18:
            raise ValueError("Возраст должен быть больше 18 лет")
        self.__age = age

    @property
    def salary_index(self):
        return self.__salary_index

    @salary_index.setter
    def salary_index(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Индекс должен быть числом")
        if value < 0:
            raise ValueError("Индекс должен быть больше 0")

        self.__salary_index = value

    def _get_dollars_salary(self, cource):
        result = round(self._salary / cource, 2)
        return result

    def __set_salary(self, value: int | float):
        self._salary = value

    def add_experience(self):
        self.__experience += 1
        new_salary = self._salary + (self._salary * self.__salary_index / 100)
        self.__set_salary(new_salary)

    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.__age}\nЗарплата: {self._salary}. Выслуга: {self.__experience} лет"


"""
.env - ЕГО НЕ ОТПРАВЛЯЮТ НА ГИТХАБ
VSE_GPT_KEY=sk-1234567890

.env.example - ЕГО ОТПРАВЛЯЮТ НА ГИТХАБ
VSE_GPT_KEY=КЛЮЧ_ОТ_ВСЕ_ГПТ


pip install python-dotenv
load_dotenv() - загружает переменные из .env
VSE_GPT_KEY = os.getenv("VSE_GPT_KEY")


"""

#PRACTICE - Сделаем класс запроса к AI
"""
ДОНОР:
client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)
async def get_ai_request(prompt: str, max_retries: int = 3, base_delay: float = 2.0):

    Отправляет запрос к API с механизмом повторных попыток
    base_delay - начальная задержка, которая будет увеличиваться экспоненциально
    :param prompt: текст запроса
    :param max_retries: максимальное количество попыток
    :param base_delay: начальная задержка между попытками
    :return: ответ от API

    for attempt in range(max_retries):
        try:
            response = await client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=16000,
                temperature=0.7,
            )
            return response.choices[0].message.content

        except openai.RateLimitError:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2**attempt)  # Экспоненциальное увеличение задержки
            await asyncio.sleep(delay)

"""

class AiRequest():
    def __init__(self, api_key: str, model: str, base_url: str):
        self.__models = ["openai/gpt-4o-mini", "anthropic/claude-3-5-haiku", "deepseek/deepseek-chat"]
        self.api_key = api_key
        self.__model = model if model in self.__models else "openai/gpt-4o-mini"
        self.__temperature = 0.7
        self.__max_tokens = 8000
        self.__base_url = base_url
        self.__client = OpenAI(api_key=self.api_key, base_url=self.__base_url)
       

    @property
    def model(self, model: str):
        return self.__model
    
    @model.setter
    def model(self, model: str):
        if model not in self.__models:
            raise ValueError("Модель не найдена")
        self.__model = model

    def get_ai_request(self, prompt: str):
        
        response = self.__client.chat.completions.create(
            model=self.__model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.__max_tokens,
            temperature=self.__temperature,
        )
        return response.choices[0].message.content

ai_request = AiRequest(model="openai/gpt-4o-mini", api_key=VSE_GPT_KEY, base_url="https://api.vsegpt.ru/v1")
task = "Шутка про обезъянку"

result = ai_request.get_ai_request(task)
print(result)

ai_request.model = "anthropic/claude-3-5-haiku"
result = ai_request.get_ai_request(task)

print(result)





