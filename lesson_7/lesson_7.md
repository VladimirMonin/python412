# Креативные задачи по Python: Множества (Set)

## Задачки

**1. Анализатор общих интересов**
Есть два списка интересов двух пользователей. Найдите:
- Общие интересы
- Уникальные интересы каждого пользователя
- Все интересы обоих пользователей
- Процент совпадения интересов

**2. Фильтр уникальных посетителей**
Создайте систему учета уникальных посетителей сайта:
- Добавляйте IP-адреса в множество
- Считайте общее количество посещений
- Выведите статистику по часам
- Определите самый активный час

**3. Генератор тегов 2.0**
Усовершенствуйте генератор тегов:
- Создайте множество уникальных тегов из текста
- Удалите теги короче 3 символов
- Приведите к нижнему регистру
- Удалите дубликаты с разным регистром
- Выведите топ-5 самых длинных тегов

**4. Проверка уникальности паролей**
Создайте валидатор паролей:
- Проверяйте уникальность символов в пароле
- Считайте процент уникальных символов
- Отмечайте повторяющиеся символы
- Предлагайте замену повторяющихся символов

**5. Словарный анализатор**
Сравните два текста:
- Найдите общие слова
- Уникальные слова каждого текста
- Процент совпадения словарного запаса
- Самые длинные уникальные слова

**6. Музыкальный плейлист**
Работа с музыкальными жанрами:
- Объедините жанры из разных плейлистов
- Найдите общие жанры
- Уникальные жанры каждого плейлиста
- Создайте рекомендации на основе пересечений

**7. Проверка расписания**
Найдите конфликты в расписании встреч:
- Проверьте пересечение временных слотов
- Найдите свободные окна
- Предложите оптимальное время для новой встречи
- Учитывайте длительность встреч

**8. Анализатор покупок**
Работа со списками покупок:
- Найдите общие товары в списках
- Уникальные товары каждого списка
- Создайте общий список покупок
- Удалите дубликаты с разным написанием

**9. Валидатор email-адресов**
Проверьте список email-адресов:
- Удалите дубликаты с разным регистром
- Проверьте уникальность доменов
- Создайте статистику по доменам
- Найдите похожие адреса

**10. Игра "Множества слов"**
Создайте игру:
- Игрок составляет слова из заданных букв
- Проверяйте уникальность слов
- Считайте очки за длину слов
- Храните рекорды в множестве

## Наборы данных

```python
# Интересы пользователей
USER1_INTERESTS = {'Python', 'JavaScript', 'Gaming', 'Music', 'AI'}
USER2_INTERESTS = {'JavaScript', 'Music', 'Sports', 'Movies', 'AI'}

# IP-адреса с временем посещения
VISITS = [
    ('192.168.1.1', '10:00'),
    ('192.168.1.2', '10:30'),
    ('192.168.1.1', '11:00'),
    ('192.168.1.3', '11:30')
]

# Музыкальные жанры
PLAYLIST1 = {'Rock', 'Pop', 'Jazz', 'Blues'}
PLAYLIST2 = {'Pop', 'Hip-Hop', 'Rock', 'Electronic'}

# Расписание встреч
MEETINGS = {
    ('09:00', '10:00', 'Встреча 1'),
    ('10:30', '11:30', 'Встреча 2'),
    ('11:00', '12:00', 'Встреча 3')
}

# Списки покупок
SHOPPING_LIST1 = {'Хлеб', 'Молоко', 'Яйца', 'Сыр'}
SHOPPING_LIST2 = {'молоко', 'Творог', 'сыр', 'Йогурт'}

# Email адреса
EMAILS = {
    'user@gmail.com',
    'User@Gmail.com',
    'another@yahoo.com',
    'test@gmail.com'
}

# Буквы для игры в слова
GAME_LETTERS = {'а', 'к', 'т', 'о', 'м', 'р', 'с', 'л', 'в', 'п'}
```

**1. Анализатор общих интересов**

```python
user1 = {'Python', 'JavaScript', 'Gaming', 'Music', 'AI'}
user2 = {'JavaScript', 'Music', 'Sports', 'Movies', 'AI'}

common = user1 & user2
unique1 = user1 - user2
unique2 = user2 - user1
all_interests = user1 | user2

match_percent = (len(common) / len(all_interests)) * 100

print("Общие интересы:", common)
print("Уникальные интересы 1:", unique1)
print("Уникальные интересы 2:", unique2)
print(f"Процент совпадений: {match_percent:.1f}%")

```

**2. Фильтр уникальных посетителей**

```python
visits = [('192.168.1.1', '10:00'), ('192.168.1.2', '10:30')]
unique_ips = set()
total_visits = 0

for ip, time in visits:
    unique_ips.add(ip)
    total_visits += 1

print("Уникальных посетителей:", len(unique_ips))
print("Всего визитов:", total_visits)

```

**3. Генератор тегов 2.0**

```python
password = "hello123hello"
unique_chars = set(password)
total_chars = len(password)

unique_percent = (len(unique_chars) / total_chars) * 100

print(f"Уникальность символов: {unique_percent:.1f}%")
print("Уникальные символы:", unique_chars)

```

**4. Проверка уникальности паролей**

```python
password = "hello123hello"
unique_chars = set(password)
total_chars = len(password)

unique_percent = (len(unique_chars) / total_chars) * 100

print(f"Уникальность символов: {unique_percent:.1f}%")
print("Уникальные символы:", unique_chars)

```

**5. Словарный анализатор**

```python
text1 = "кошка собака птица"
text2 = "собака рыбка птица"

words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

common_words = words1 & words2
unique_words1 = words1 - words2
unique_words2 = words2 - words1

print("Общие слова:", common_words)
print("Уникальные слова 1:", unique_words1)
print("Уникальные слова 2:", unique_words2)

```

**6. Музыкальный плейлист**

```python
playlist1 = {'Rock', 'Pop', 'Jazz'}
playlist2 = {'Pop', 'Hip-Hop', 'Rock'}

common_genres = playlist1 & playlist2
all_genres = playlist1 | playlist2
unique_genres1 = playlist1 - playlist2

print("Общие жанры:", common_genres)
print("Все жанры:", all_genres)
print("Уникальные жанры 1:", unique_genres1)

```

**7. Проверка расписания**

```python
list1 = {'Хлеб', 'Молоко', 'Яйца'}
list2 = {'молоко', 'Творог', 'яйца'}

list1_lower = {item.lower() for item in list1}
list2_lower = {item.lower() for item in list2}

common_items = list1_lower & list2_lower
all_items = list1_lower | list2_lower

print("Общие товары:", common_items)
print("Все товары:", all_items)

```

**8. Анализатор покупок**

```python
emails = {'User@gmail.com', 'user@gmail.com', 'test@mail.ru'}
unique_emails = {email.lower() for email in emails}

print("Уникальные email:", unique_emails)
print("Всего уникальных:", len(unique_emails))

```

**9. Валидатор email-адресов**

```python
letters = {'а', 'к', 'т', 'о', 'м'}
used_words = set()

word = "кот"
if set(word) <= letters and word not in used_words:
    used_words.add(word)
    print("Слово засчитано!")

print("Использованные слова:", used_words)

```

**10. Игра "Множества слов"**

```python
items = ['кот', 'КОТ', 'собака', 'СОБАКА', 'пес']
unique_items = {item.lower() for item in items}

print("Уникальные элементы:", unique_items)
print("Количество уникальных:", len(unique_items))

```
