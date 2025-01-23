"""
Lesson 27
23.01.2025

ООП. Инкапсуляция. Продолжение.
- Класс "Шифр Цезаря" основанный на сдвиге по таблице кодирования UTF-8
- ord() - возвращает код символа в таблице UTF-8
- chr() - возвращает символ по коду в таблице UTF-8

Employee и  Organisaton как пример взаимодействия классов
Класс ManagerEmployee и потребность в наследовании при незначительных вариациях логики и атрибутов
Базовый пример наследования в коде. DRY - избегаем повторения кода (а так же сложных аннотаций типов)
"""
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


class ManagerEmployee(Employee):
        def hit_coworker(self, coworker):
            print(f"{self.name} ударил {coworker.name}")

        def work(self):
            print(f"{self.name} мотивирует коллег")


class Accountant(Employee):
    def work(self):
        print(f"{self.name} считает деньги")


class Organisaton:
    def __init__(self, name: str, employees: list[Employee]):
        self.name = name
        self.employees = employees

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def delete_employee(self, employee: Employee):
        self.employees.remove(employee)


# Тест
organisation = Organisaton("ООО Рога и Копыта", [])
# Создадим сотрудников
base_employee = Employee("Андрей", 25, 100000, "Программист")
manager_employee = ManagerEmployee("Владимир", 30, 150000, "Менеджер")
accountant = Accountant("Алексей", 35, 120000, "Бухгалтер")

# Добавим сотрудников в организацию
organisation.add_employee(base_employee)
organisation.add_employee(manager_employee)
organisation.add_employee(accountant)

# Вызов метода работа
[employee.work() for employee in organisation.employees]
