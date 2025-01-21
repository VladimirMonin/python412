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


employee = Employee("Спартак", 30, 300000)
print(employee)
employee.add_experience()
print(employee)
employee.add_experience()
print(employee)

employee.set_age(25)
print(employee.get_age())

employee.salary_index = 15
print(employee.salary_index)
