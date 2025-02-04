"""
04.02.2025

Тема ООП Ч7. Магические методы. Математика. Сравнение. Знакомство с Dataclasses. Урок: 30

МАТЕМАТИКА

Basic Math / Базовая математика:
- __add__(self, other)    # Addition (+) / Сложение
- __sub__(self, other)    # Subtraction (-) / Вычитание
- __mul__(self, other)    # Multiplication (*) / Умножение
- __truediv__(self, other)    # True Division (/) / Истинное деление
- __floordiv__(self, other)   # Floor Division (//) / Целочисленное деление
- __mod__(self, other)    # Modulo/Remainder (%) / Остаток от деления
- __pow__(self, other)    # Power (**) / Возведение в степень

INPLACE Operations / Операции с присваиванием:
- __iadd__(self, other)   # In-place Addition (+=) / Сложение с присваиванием
- __isub__(self, other)   # In-place Subtraction (-=) / Вычитание с присваиванием
- __imul__(self, other)   # In-place Multiplication (*=) / Умножение с присваиванием
- __itruediv__(self, other)   # In-place True Division (/=) / Деление с присваиванием
- __ifloordiv__(self, other)  # In-place Floor Division (//=) / Целочисленное деление с присваиванием
- __imod__(self, other)   # In-place Modulo (%=) / Остаток от деления с присваиванием
- __ipow__(self, other)   # In-place Power (**=) / Возведение в степень с присваиванием

COMPARISON Operations / Операции сравнения:
- __eq__(self, other)     # Equal to (==) / Равно
- __ne__(self, other)     # Not Equal to (!=) / Не равно
- __lt__(self, other)     # Less Than (<) / Меньше
- __gt__(self, other)     # Greater Than (>) / Больше
- __le__(self, other)     # Less Than or Equal to (<=) / Меньше или равно
- __ge__(self, other)     # Greater Than or Equal to (>=) / Больше или равно
"""


# Класс GameScore (игровые очки) - для демонстрации работы математических операторов

class GameScore:
    def __init__(self, score):
        self.score = score

    def __str__(self):
        return f'Ваши очки: {self.score}'

    def __repr__(self):
        return f'GameScore(score="{self.score}")'

    def __iadd__(self, other):
        self.score += other.score
        return self

    def __add__(self, other):
        return self.__iadd__(other)

    def __sub__(self, other):
        return self.__isub__(other)

    def __isub__(self, other):
        self.score -= other.score
        return self

my_score = GameScore(100)
print(my_score)

new_score = GameScore(50)

my_score += new_score
print(my_score)
