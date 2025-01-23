"""
Lesson 27
23.01.2025

ООП. Инкапсуляция. Продолжение.
- Класс "Шифр Цезаря" основанный на сдвиге по таблице кодирования UTF-8
- ord() - возвращает код символа в таблице UTF-8
- chr() - возвращает символ по коду в таблице UTF-8
"""
class ManagerEmployee:
    def __init__(self, name: str, age: int, salary: int | float, position: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"Сотрудник: {self.name}, возраст: {self.age}, зарплата: {self.salary}, должность: {self.position}"

    def drink_coffee(self):
        print(f"{self.name} в должности {self.position} выпил кофе")

    def work(self):
        print(f"{self.name} поработал")

    def hit_coworker(self, coworker):
        print(f"{self.name} ударил {coworker.name}")


class Employee:
    def __init__(self, name: str, age: int, salary: int | float, position: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"Сотрудник: {self.name}, возраст: {self.age}, зарплата: {self.salary}, должность: {self.position}"

    def drink_coffee(self):
        print(f"{self.name} в должности {self.position} выпил кофе")

    def work(self):
        print(f"{self.name} поработал")


class Organisaton:
    def __init__(self, name: str, employees: list[Employee]):
        self.name = name
        self.employees = employees

    def create_employee(self, name: str, age: int, salary: int | float, position: str):
        employee = Employee(name, age, salary, position)
        self.employees.append(employee)

    def delete_employee(self, employee: Employee):
        self.employees.remove(employee)


# Тест
organisation = Organisaton("ООО Рога и Копыта", [])
organisation.create_employee("Владимир", 25, 100000, "Рядовой")
organisation.create_employee("Андрей", 25, 100000, "Рядовой")
organisation.create_employee("Сергей", 25, 100000, "Рядовой")

[print(employee) for employee in organisation.employees]

# Удалим сотрудника
organisation.delete_employee(organisation.employees[0])
[print(employee) for employee in organisation.employees]