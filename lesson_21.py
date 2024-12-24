"""
24.12.2024
Урок 21. Области видимости. Замыкания. Декораторы
- 4 Области видимости в Python
"""

# Области видимости в Python


# 1. Глобальная область видимости
# 2. Локальная область видимости
# 3. Нелокальная область видимости

# Функция счётчик которая хранит состояние
from typing import Callable, List

"""
Callable - это аннотация типа, которая позволяет указать, что что возвращается является вызываемым объектом.
[[аргумент_a, аргумент_b], возвращаемый тип данных]
"""


def counter() -> Callable[[], int]:

    count = 0
    print(f"{id(count)=}")

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner


counter1 = counter()
print(id(counter1))  # 140707366366784
counter2 = counter()
print(id(counter2))  # 140707366366848
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print(counter2())  # 1
print(counter2())  # 2

# Функция с кешем
"""
Функция которая принемает список
Проверяет, есть ли что-то в сохранённых данных и является ли это тот же список, что и предыдущий
Если да, то возвращает результат предыдущего вызова
Если нет, то вызывает функцию и сортирует список
Сохраняет в переменную результат и возвращает его
"""

participants = [
    "Моннин Владимир Александрович",
    "Беляв Семен Константинович",
    "Бобов Дмитрий Владимирович",
    "Вахрамеев Никита Федорович",
    "Голосняк Екатерина Александровна",
    "Добровольский Спартак Виталиевич",
    "Завалин Артём Андреевич",
    "Калинин Григорий Сергеевич",
    "Козлов Вадим Валерьевич",
    "Мнацаканян Размик Априкович",
    "Охонько Алексей Николаевич",
    "Рукавишников Даниил Дмитриевич",
    "Шарапов Павел Алексеевич",
    "Шарахудинов Кирилл Русланович",
    "Юдин Дмитрий Вячеславович",
]

# Функция сортировки
# def sort_participants(participants: list[str]) -> list[str]:
#     return sorted(participants)

# print(sort_participants(participants))


def cahed_sorter(participants: List[str]) -> Callable[[], list[str]]:
    cache = []
    last_length = 0

    def inner() -> List[str]:
        nonlocal cache, last_length
        # Проверяем изменился ли список
        if last_length == len(participants) and cache:
            return cache

        # Если список изменился, обновляем кеш
        cache = sorted(participants)
        last_length = len(participants)
        return cache

    return inner


sorter = cahed_sorter(participants)
print(sorter())
print(sorter())
participants.append("Киркоров Филлип Бедросович")
print(sorter())
