"""
Тема ООП Ч8. Погружение в Dataclasses. Урок: 31
- @dataclass
- (order=True)
- field
    - default factory
    - ...

"""

from dataclasses import dataclass, field

# field
"""
field - позволяет настроить отдельное поле класса
comparare=False - отключает сравнение по этому полю
"""

@dataclass
class Employee:
    # Автоматически генерируемый __init__
    first_name: str = "Сергей"
    last_name: str = "Сергеев"
    hobbies: list[str] = field(default_factory=list)
    age: int = field(default=18, compare=False)
    work_week: tuple= ("понедельник", "вторник", "среда", "четверг", "пятница")

employee = Employee("Николай", "Соболев", ["футбол", "программирование"], 35)
employee2 = Employee(first_name="Елена", last_name="Петрова", age=28, hobbies=["чтение", "SQL"])
employee3 = Employee("Петр", "Петров")

# Автоматически генерируемый __repr__
print(employee)
print(employee2)
print(employee3)

employee3.work_week = ["хлебушек"]
# Employee(first_name='Николай', last_name='Соболев', age=35, hobbies=['футбол', 'программирование'])
serialize_employee = repr(employee)
print(serialize_employee)
deserialize_employee = eval(serialize_employee)

# Автоматически генерируемый __eq__ - сравнение на равенство по всем полям
print(f'{employee == employee2 = }')