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
    def __init__(self, name: str, employees: list[Employee | ManagerEmployee]):
        self.name = name
        self.employees = employees

    def add_employee(self, employee: Employee | ManagerEmployee):
        self.employees.append(employee)

    def delete_employee(self, employee: Employee | ManagerEmployee):
        self.employees.remove(employee)


# Тест
organisation = Organisaton("ООО Рога и Копыта", [])
# Создадим сотрудников
employee_1 = Employee("Вася", 25, 100000, "Программист")
employee_2 = Employee("Петя", 25, 100000, "Программист")
manager_employee = ManagerEmployee("Ваня", 25, 500000, "Менеджер")

# Добавим сотрудников в организацию
organisation.add_employee(employee_1)
organisation.add_employee(employee_2)
organisation.add_employee(manager_employee)

# Выдадим мотивационный пендаль!
manager_employee.hit_coworker(employee_1)
