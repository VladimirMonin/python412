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
# Импортируем time.perf_counter()
import time


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
    tasks = [task(3, "Пицца"), task(2, "Фильм"), task(1, "Друзья")]
    results = await asyncio.gather(*tasks)

    # Выведем результаты
    print(*results, "Поехали!")

# Засекаем старт
start_time = time.perf_counter()
asyncio.run(main())

# Финиш
finish_time = time.perf_counter()

print(f"Время выполнения программы: {finish_time - start_time:.2f} секунд")
