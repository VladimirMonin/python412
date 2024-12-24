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

proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

variants = [
    "кот",
    "шеф",
    "мозг",
    "лес",
    "фолк",
    "код",
    "рот",
    "мёд",
    "лук",
    "лес",
    "год",
    "час",
    "друг",
    "муж",
    "айфон",
    "стол",
    "нос",
    "сыр",
    "хлеб",
    "мир",
    "свет",
    "рок",
    "дед",
    "дом",
    "сон",
    "глаз",
    "торт",
    "драйв",
    "байк",
    "джаз",
    "грим",
    "рэп",
    "старт",
    "пинг-понг",
    "каприз",
    "драйф",
    "размах",
    "панк",
    "размер",
    "перекус",
    "блеск",
    "накал",
    "размен",
    "кураж",
    "форсаж",
    "прорыв",
]

# PRACTICE - Функция генератор пословиц с кешированием

# Логика создания всех вариантов пословиц:

# result = []

# for proverb in proverbs:
#     for variant in variants:
#         new_proverb = proverb.lower().replace("ум", variant).capitalize()
#         result.append(new_proverb)

from random import shuffle


def cached_proverbs_generator(
    proverbs: List[str], variants: List[str]
) -> Callable[[], List[str]]:
    cache = []
    max_variant = 0

    def inner() -> List[str]:
        nonlocal cache, max_variant
        # Проверяем изменился ли список
        if max_variant == len(proverbs) * len(variants) and cache:
            print("Кеш")
            shuffle(cache)
            return cache

        # Если список изменился, обновляем кеш
        cache = []
        for proverb in proverbs:
            for variant in variants:
                new_proverb = proverb.lower().replace("ум", variant).capitalize()
                cache.append(new_proverb)
        max_variant = len(proverbs) * len(variants)
        print("Вычисление")
        shuffle(cache)
        return cache

    return inner


proverbs_generator = cached_proverbs_generator(proverbs, variants)
print(proverbs_generator()[:5])
print(proverbs_generator()[:5])
print(proverbs_generator()[:5])
print(proverbs_generator()[:5])


from random import choice, shuffle
from typing import Generator, Set


def random_proverb_generator(
    proverbs: list[str], variants: list[str]
) -> Generator[str, None, None]:
    # Храним использованные комбинации
    used_combinations: Set[tuple] = set()
    # Максимальное количество возможных комбинаций
    max_combinations = len(proverbs) * len(variants)

    while True:
        # Если использовали все комбинации - очищаем историю
        if len(used_combinations) >= max_combinations:
            used_combinations.clear()

        # Выбираем случайную пословицу и вариант замены
        current_proverb = choice(proverbs)
        current_variant = choice(variants)

        # Создаём уникальный ключ комбинации
        combination = (current_proverb, current_variant)

        # Если такой комбинации ещё не было
        if combination not in used_combinations:
            used_combinations.add(combination)
            # Генерируем и отдаём новую пословицу
            yield current_proverb.lower().replace("ум", current_variant).capitalize()


# Закажем 5 пословиц
proverb_gen = random_proverb_generator(proverbs, variants)
for _ in range(5):
    print(next(proverb_gen))


reuslt = []
for proverb in proverb_gen:
    reuslt.append(proverb)
    if len(reuslt) == 5:
        break

print(reuslt)
