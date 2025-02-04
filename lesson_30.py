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


В Python сравнительные операторы (==, !=, <, <=, >, >=) работают через специальные методы. Если вы хотите обеспечить работу ВСЕХ операторов сравнения для объектов (например, игроков), достаточно явно определить три метода:

• eq: для проверки равенства (==);
• lt: для проверки «меньше чем» (<);
• gt: для проверки «больше чем» (>).
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

    def __bool__(self):
        return bool(self.score)

# Композиция. В таком варианте очки - неотделимы от игрока. Живут и умирают с ним.
# class Player2:
#     def __init__(self):
#         self.scores = GameScore(0)


# Добавим класс Игрок - у которого на инициализации будет создаваться баланс
# Агрегация. В таком варианте Очки - могут иметь самостоятельность и в какой то момент "попасть" в игрока
class Player:
    def __init__(self, scores: GameScore, nickname: str):
        self.scores = scores
        self.nickname = nickname

    def __str__(self):
        return f'Игрок {self.nickname}: {self.scores}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: "Player"):
        return self.scores.score == other.scores.score

    def __lt__(self, other: "Player"):
        return self.scores.score < other.scores.score

    def __gt__(self, other: "Player"):
        return self.scores.score > other.scores.score

    # МАТЕМАТИКА. Будет 4 метода. Такие же как в GameScore.
    # Мы опишем эти же 4 метода, левый операнд self.socres, правый - other: GameScore

    def __iadd__(self, other: "GameScore"):
        self.scores += other
        return self

    def __isub__(self, other: "GameScore"):
        self.scores -= other
        return self

    def __add__(self, other: "GameScore"):
        return self.__iadd__(other)

    def __sub__(self, other: "GameScore"):
        return self.__isub__(other)

    def __bool__(self):
        return bool(self.scores)


p1 = Player(scores=GameScore(200), nickname="Фил")
p2 = Player(scores=GameScore(190), nickname="Боб")
p3 = Player(scores=GameScore(320), nickname="Ник")
p4 = Player(scores=GameScore(530), nickname="Саманта")

print(p1 == p2) # False
print(p1 < p2) # True
print(p1 > p2) # False

# Не красиво, но технически будет работать
print(p1.scores.score > p2.scores.score)

players = [p1, p2, p3, p4]

# == от is?

players.sort(reverse=True)
print(players[:3]) # ТОП3 игроков

players.sort(key=lambda player: player.nickname)
print(players)

# Создам баланс
gs = GameScore(500)

# Добавлю Бобу
p2 += gs

# Сортирую игроков и вывожу ТОП3 игроков
players.sort(reverse=True)
print(players[:3]) # ТОП3 игроков

if p2:
    # Сюда попаду ЕСЛИ баланс игрока НЕ 0
    pass

active_players = [player for player in players if player]