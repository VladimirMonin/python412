"""
18.02.2025
Тема ООП Ч11. Паттерны ООП. Урок: 34
- Поведенческие паттерны ООП
- Паттерн Strategy - Стратегия - способ реализации алгоритма разными вариантами (одно действие - разные реализации)

- Паттерн State - Состояние - способ организации кода при переходе от одного состояния к другому
- Паттерн Observer - Наблюдатель - способ организации кода, когда один объект наблюдает за другим объектом

- Паттерн Command - Команда - способ организации кода, когда один объект передает команду другому объекту

- Паттерн Chain of Responsibility - Цепочка обязанностей - способ организации кода, когда один объект передает обязанности другому объекту

"""

# Паттерн Состояние на примере музыкального плеера.

from abc import ABC, abstractmethod


# Абстрактное состояние

class PlayerState(ABC):
    @abstractmethod
    def play(self) -> "PlayerState":
        pass

    @abstractmethod
    def stop(self) -> "PlayerState":
        pass

    @abstractmethod
    def pause(self) -> "PlayerState":
        pass


# Конкретные состояния
class PlayState(PlayerState):
    def play(self):
        print(f'{self.__class__.__name__} - Проигрывание музыки')
        return self

    def stop(self):
        print(f'{self.__class__.__name__} - Остановка музыки. Переход в состояние StopState')
        return StopState()

    def pause(self):
        print(f'{self.__class__.__name__} - Пауза. Переход в состояние PauseState')
        return PauseState()


class StopState(PlayerState):
    def play(self):
        print(f'{self.__class__.__name__} - Проигрывание музыки. Переход в состояние PlayState')
        return PlayState()

    def stop(self):
        print(f'{self.__class__.__name__} - Музыка уже остановлена')
        return self

    def pause(self):
        print(f'{self.__class__.__name__} - Музыка остановлена. Переход в состояние PauseState')
        return StopState()
    
class PauseState(PlayerState):
    def play(self):
        print(f'{self.__class__.__name__} - Проигрывание музыки. Переход в состояние PlayState')
        return PlayState()

    def stop(self):
        print(f'{self.__class__.__name__} - Остановка музыки. Переход в состояние StopState')
        return StopState()

    def pause(self):
        print(f'{self.__class__.__name__} - Музыка на паузе')
        return self


# Контекст
class Player:
    def __init__(self):
        self.state: PlayerState = StopState()

    def change_state(self, state: PlayerState):
        self.state = state

    def play(self) -> None:
        self.change_state(self.state.play())

    def stop(self) -> None:
        self.change_state(self.state.stop())

    def pause(self) -> None:
        self.change_state(self.state.pause())


if __name__ == "__main__":
    player = Player() 
    player.play() #  StopState - Проигрывание музыки. Переход в состояние PlayState
    player.pause() #  PlayState - Пауза. Переход в состояние PauseState
    player.play() # PauseState - Проигрывание музыки. Переход в состояние PlayState
    player.stop() # PlayState - Остановка музыки. Переход в состояние StopState
    player.stop() #  StopState - Музыка уже остановлена
    player.pause() # StopState - Музыка остановлена. Переход в состояние PauseState
    player.play() #  StopState - Проигрывание музыки. Переход в состояние PlayState
    player.stop() # PlayState - Остановка музыки. Переход в состояние StopState
    player.play() #  StopState - Проигрывание музыки. Переход в состояние PlayState
    player.play() #  PlayState - Проигрывание музыки
    player.stop() # PlayState - Остановка музыки. Переход в состояние StopState
