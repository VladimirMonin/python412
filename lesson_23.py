"""
Lesson 23
09.01.2025

Знакомство с асинхронностью в Python
- asyncio
- await
- async sleep
- aiohttp
- 
"""

# Импортируем модуль для работы с асинхронностью
import asyncio


# Напишем функцию, которая будет выполняться асинхронно
# принемает время выполнения в секундах и название задачи

async def task(time: int, name: str) -> str:
    # Выведем сообщение
    print(f"Начало задачи {name}")
    # await - позволит перейти к другим задачам
    # asyncio.sleep - имитация ожидания ввода - вывода
    await asyncio.sleep(time)
    # Выведем сообщение
    print(f"Задача {name} выполнена")
    return f'{name}: сделано!'


# Функция которая запустит все эти задачи
async def main():
    pizza = await task(5, "Пицца")
    film = await task(3, "Фильм")
    friends = await task(2, "Друзья")

    # Выведем результаты
    print(pizza, film, friends, "Поехали!")


asyncio.run(main())
