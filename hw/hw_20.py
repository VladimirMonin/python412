from marvel import small_dict as sd
from pprint import pprint


small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,

    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

# ### Задача 1: Поиск фильмов по названию
# 1. Запросите у пользователя ввести название фильма или его часть.
# 2. Найдите фильмы в словаре `small_dict` (не забудьте про регистр).
#    - Обойдите циклом ключи словаря, и если ключ содержит введенную строку или равен ей, выведите его.
#    - Опционально: добавьте найденные фильмы в список и затем выведите этот список.

# ### Задача 2: Фильтрация фильмов по году выхода
# 1. Найдите фильмы, которые вышли после 2024 года.
#    - Обойдите проблему с ошибкой (невозможно сравнить None с числом).
#    - Используйте проверку типов данных, чтобы избежать ошибок при сравнении.
   
# 2. Выполните следующие действия:
#    1. Попробуйте просто распечатать названия фильмов.
#    2. Попробуйте собрать список названий фильмов.
#    3. Попробуйте собрать словарь (как исходный, но фильтрованный по году).
#    4. Попробуйте собрать список словарей в формате `[{‘Человек-хрюк’: 2024}, ...]`.


new_sd = {}
for key, value in sd.items():
    new_sd[key] = value


# 1. Это же в одну строку.
new_sd = {key:value for key, value in sd.items()}
# print(new_sd)

# 2. Просим у пользователя название или часть, ищем в словаре по вхождению

user_film = input('Введите название фильма или его часть: ')
# 2.1. Выводим все фильмы, которые содержат вхождение
user_films_dict = {key:value for key, value in sd.items() if user_film.lower() in key.lower()}
# pprint(user_films_dict, sort_dicts=False)

# 3. Фильтрованные фильмы по году.
user_year = 2024

# Попробуйте собрать похожий однострочник фильтрующий фильмы по году.
film_by_year = {key:value for key, value in sd.items() if value == user_year}
# print(film_by_year)

# 4. Собрать фильмы вышедшие ДО 2024 года. Попробуйте обойти ошибку с None.
# тернарный оператор  утверждение if условие else другое
# type(value) == int
# isinstance(value, int)
film_by_year = {key:value for key, value in sd.items() if isinstance(value, int) and value < user_year}
print(film_by_year)

# 5. Список словарей
films_list = [{key:value} for key, value in sd.items()]

films_list = [{key.lower().replace(" ", "_"):value} for key, value in sd.items()]

films_list = [{key.lower().replace(" ", "_"):value if value is not None else 0} for key, value in sd.items()]

print(films_list)