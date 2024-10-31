# Креативные задачи по Python

## Задачки

**1. Генератор никнеймов**
Пользователь вводит имя и год рождения. Создайте три варианта никнейма:
- Имя задом наперёд + год
- Первая и последняя буква имени + случайные 3 цифры
- Имя через нижнее подчёркивание

**2. Тайный шифр**
Замените все гласные буквы в строке на '*', а согласные на '#'.
Пример: "привет" → "#*#*#*#"

**3. Детектор повторов**
Найдите самый часто повторяющийся символ в строке.
Пример: "программирование" → "р"

**4. Текстовый светофор**
Программа получает строку и "зажигает" в ней все буквы определённого цвета:
- Красные буквы: а, о, у
- Жёлтые буквы: е, ё, и
- Зелёные буквы: остальные

**5. Числовой палиндром++**
Проверьте, является ли число палиндромом при записи в двоичной системе.
Пример: 9 → 1001 (да)

**6. Анализатор пароля**
Оцените сложность пароля по шкале от 1 до 5:
- Наличие цифр (+1)
- Наличие букв разного регистра (+1)
- Наличие спецсимволов (+1)
- Длина больше 8 (+1)
- Нет последовательностей типа 123, abc (+1)

**7. Текстовый калькулятор**
Преобразуйте текстовую запись числа в число:
"два плюс три" → 2 + 3 = 5

**8. Поиск слов**
В большом тексте найдите все слова, которые начинаются и заканчиваются на одну и ту же букву.

**9. Ритм стиха**
Проверьте, имеют ли строки одинаковое количество гласных букв (проверка ритма стиха).

**10. Цензор**
Замените все "плохие" слова из заданного списка на звёздочки той же длины.

**11. Музыкальный плейлист**
Создайте список песен, где каждая следующая песня начинается на ту букву, 
которой заканчивается предыдущая.

**12. Текстовый змей**
Преобразуйте строку так, чтобы каждое следующее слово начиналось 
с большей буквы:
"привет мир" → "привет Мир"
"как дела сегодня" → "как Дела СЕГОДНЯ"

**13. Шифр Цезаря в лексикографическом порядке**

Напишите программу для шифрования текста, где сдвиг происходит по кодам символов.

Правила:
- Вводим текст на русском или английском языке 
- Вводим число - на сколько позиций сдвигать символы
- Программа должна сдвинуть каждый символ на указанное количество позиций
- Пробелы оставляем без изменений

Пример:
Введите текст: Привет
Введите сдвиг: 1
Результат: Рсйгёу

Подсказка:
- Для получения кода символа используем ord()
- Для получения символа по коду используем chr()



## Наборы данных

```python
# Русские гласные буквы в разных регистрах
VOWELS_RU = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
             'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']

# Английские гласные буквы в разных регистрах
VOWELS_EN = ['a', 'e', 'i', 'o', 'u', 'y',
             'A', 'E', 'I', 'O', 'U', 'Y']

# Список "плохих" слов для цензуры
BAD_WORDS = ['пончик', 'пирожок', 'торт', 'конфета', 'мороженое']

# Поэма "Чебурек" для тестирования задач
POEM = """
Я съел чебурек, а потом и пирог,
Запил это дело стаканом компота.
А после пошёл я купить пирожок,
Ведь кушать конфеты была мне охота.

Зашёл в магазин, там стоял торт большой,
К нему мороженое просто манило.
Купил всё, что было, унёс к себе домой,
И съел, хоть уже даже есть не хотелось!
"""

# Числа текстом для калькулятора
NUMBERS_TEXT = {
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
    'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9
}

# Операции текстом
OPERATIONS = {
    'плюс': '+',
    'минус': '-',
    'умножить': '*',
    'разделить': '/'
}
```

---

## Решения


### 1. Генератор никнеймов

```python
name = input("Введите имя: ")
year = input("Введите год рождения: ")

# Вариант 1: имя задом наперед + год
nickname1 = name[::-1] + year

# Вариант 2: первая и последняя буква + 3 случайных цифры
from random import randint
nickname2 = name[0] + name[-1] + str(randint(100,999))

# Вариант 3: имя через подчеркивание
nickname3 = '_'.join(name)

print(f"Ваши никнеймы:\n{nickname1}\n{nickname2}\n{nickname3}")
```

### 2. Тайный шифр

```python
from lesson_5.data import VOWELS_RU

text = input("Введите текст: ")
result = ""

# Проходим по каждой букве и заменяем на символы
for letter in text:
    if letter.lower() in VOWELS_RU:
        result += '*'
    else:
        result += '#'

print(result)
```

### 3. Детектор повторов

```python
text = input("Введите текст: ")
max_count = 0
max_char = ''

# Проходим по каждому уникальному символу
for char in set(text):
    # Считаем количество его повторений
    current_count = text.count(char)
    if current_count > max_count:
        max_count = current_count
        max_char = char

print(f"Самый частый символ: {max_char} (встречается {max_count} раз)")
```

### 4. Текстовый светофор

```python
text = input("Введите текст: ")
result = ""

# Определяем цвета букв
red_letters = 'аоу'
yellow_letters = 'еёи'

for letter in text:
    if letter.lower() in red_letters:
        result += f"\033[91m{letter}\033[0m"  # Красный
    elif letter.lower() in yellow_letters:
        result += f"\033[93m{letter}\033[0m"  # Жёлтый
    else:
        result += f"\033[92m{letter}\033[0m"  # Зелёный

print(result)
```


### 5. Числовой палиндром++

```python
number = int(input("Введите число: "))
# Переводим в двоичную систему и убираем префикс '0b'
binary = bin(number)[2:]
# Проверяем, является ли палиндромом
is_palindrome = binary == binary[::-1]

print(f"Число {number} в двоичной системе: {binary}")
print(f"Это{'' if is_palindrome else ' не'} палиндром")
```

### 6. Анализатор пароля

```python
# Задача 6. Анализатор пароля
password = input("Введите пароль: ")
score = 0

# Проверяем наличие цифр
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break
if has_digit:
    score += 1

# Проверяем наличие букв разного регистра
has_upper = False
has_lower = False
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
if has_upper and has_lower:
    score += 1

# Проверяем наличие спецсимволов
has_special = False
for char in password:
    if not char.isalnum():
        has_special = True
        break
if has_special:
    score += 1

# Проверяем длину
if len(password) > 8:
    score += 1

# Проверяем отсутствие последовательностей
sequences = ['123', 'abc', 'password']
has_sequence = False
for seq in sequences:
    if seq in password.lower():
        has_sequence = True
        break
if not has_sequence:
    score += 1

print(f"Сложность пароля: {score}/5")
```

### 7. Текстовый калькулятор

```python
text = input("Введите выражение словами (например 'два плюс три'): ")
words = text.split()

# Получаем числа и операцию
num1 = NUMBERS_TEXT[words[0]]
operation = OPERATIONS[words[1]]
num2 = NUMBERS_TEXT[words[2]]

# Вычисляем результат
result = eval(f"{num1}{operation}{num2}")
print(f"Результат: {result}")
```

### 8. Поиск слов

```python
text = input("Введите текст: ").lower()
words = text.split()
same_letters = []

# Ищем слова с одинаковыми первой и последней буквами
for word in words:
    if word[0] == word[-1]:
        same_letters.append(word)

print("Слова с одинаковыми первой и последней буквами:", same_letters)
```

### 9. Ритм стиха

```python
# Задача 9. Ритм стиха
from lesson_5.data import VOWELS_RU

def count_vowels(line):
    count = 0
    for char in line:
        if char.lower() in VOWELS_RU:
            count += 1
    return count

lines = []
while True:
    line = input("Введите строку стиха (пустая строка для завершения): ")
    if not line:
        break
    lines.append(line)

# Проверяем количество гласных в каждой строке
vowels_count = count_vowels(lines[0])
has_rhythm = True

for line in lines:
    if count_vowels(line) != vowels_count:
        has_rhythm = False
        break

print(f"Стих {'имеет' if has_rhythm else 'не имеет'} ритм")
```


### 10. Цензор
```python
from lesson_5.data import BAD_WORDS, POEM

text = POEM

# Заменяем каждое плохое слово на звёздочки
for word in BAD_WORDS:
    text = text.replace(word, '*' * len(word))

print(text)

```
### 11. Музыкальный плейлист

```python
songs = [
    "Акула - Кислотный диджей",
    "Йода - Звёздные войны",
    "Антонов - Мечты",
    "Иванушки - Тополиный пух",
    "Хлеб - Чай сахар"
]

valid_playlist = []
for i in range(len(songs)):
    # Находим песню, которая начинается с последней буквы предыдущей
    for song in songs:
        if not song in valid_playlist:
            if not valid_playlist or song[0].lower() == valid_playlist[-1][-1].lower():
                valid_playlist.append(song)
                break

print("Плейлист с правильной последовательностью:")
for song in valid_playlist:
    print(song)

```

### 12. Текстовый змей

```python
text = input("Введите текст: ")
words = text.split()
result = []

# Увеличиваем регистр каждого следующего слова
for i, word in enumerate(words):
    if i == 0:
        result.append(word.lower())
    else:
        result.append(word.upper() if i > 1 else word.capitalize())

print(' '.join(result))
```
