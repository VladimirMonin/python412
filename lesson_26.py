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
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.__age = age
        self._salary = salary

    def _get_dollars_salary(self, cource):
        result = round(self._salary / cource, 2)
        return result
    
    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.__age}\nЗарплата: {self._salary}"


employee = Employee("Спартак", 30, 300000)
print(employee.name)
# print(employee.age) # AttributeError: 'Employee' object has no attribute 'age'
# Как добыть всё же приватный атрибут возраст? Пайтон искажает к ним путь.
print(employee._Employee__age) # переменная._НазваниеКласса__название_атрибута
employee.age = 25
print(employee)
print(employee.age)
print(employee._salary)
print(employee._get_dollars_salary(105))

# Вызовем dict на объекте
print(employee.__dict__)
