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
- __call__
- Пример полиморфизма на классах - болванках Image
"""

import json


class JsonFile:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            result = json.load(file)
            return result

    def write(self, data: list[dict]):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append(self, data: list[dict]):
        # 0. Проверка типов данных
        if not isinstance(data, list):
            raise TypeError("Метод append принимает только список")
        if not all(isinstance(item, dict) for item in data):
            raise TypeError("Все элементы должны быть словарями")
        # 1. Прочитать файл
        file = self.read()
        # 2. Добавить новые данные
        file.extend(data)
        # 3. Записать в файл
        self.write(file)


data = [
    {"name": "Владимир", "age": 25, "is_married": True},
    {"name": "Андрей", "age": 25, "is_married": True},
]

new_data= [
    {"name": "Алексей", "age": 25, "is_married": True},

]

json_file = JsonFile("data.json")
json_file.write(data)
json_file.append(new_data)
