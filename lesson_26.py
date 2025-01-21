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
    def __init__(self, name: str, age: int, salary: int|float):
        self.name = name
        self.__age = age
        self._salary = salary
        self.__experience: int = 0
        self.__salary_index: int = 10

    def _get_dollars_salary(self, cource):
        result = round(self._salary / cource, 2)
        return result
    
    def __set_salary(self, value: int|float):
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
