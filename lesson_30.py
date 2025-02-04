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
# Собственное исключение GameSroceOperationError - для обработки ошибок при работе с математическими операторами

class GameScoreMathError(Exception):
    pass


# Класс GameScore (игровые очки) - для демонстрации работы математических операторов

class GameScore:
    MIN_SCORE = 0
    MAX_SCORE = 1000

    def __init__(self, score):
        self.score = self._validate_score_limit(score)

    def __str__(self):
        return f'Ваши очки: {self.score}'

    def __repr__(self):
        return f'GameScore(score="{self.score}")'

    def _validate_other_type(self, other):
        if not isinstance(other, GameScore):
            raise TypeError(f"Нельзя сложить GameScore и {type(other)}")

    def _validate_score_limit(self, score):
        if not self.MIN_SCORE <= score <= self.MAX_SCORE:
            raise GameScoreMathError(f"Нельзя установить очки вне диапазона от {self.MIN_SCORE} до {self.MAX_SCORE}")
        else:
            return score

    def __iadd__(self, other: "GameScore"):
        self._validate_other_type(other)
        new_score = self.score + other.score
        self.score = self._validate_score_limit(new_score)
        return self

    def __isub__(self, other: "GameScore"):
        self._validate_other_type(other)
        new_score = self.score - other.score
        self.score = self._validate_score_limit(new_score)
        return self

    def __add__(self, other: "GameScore"):
        return self.__iadd__(other)

    def __sub__(self, other: "GameScore"):
        return self.__isub__(other)

my_score = GameScore(100)
print(my_score)

new_score = GameScore(50)

my_score -= new_score
print(my_score)
