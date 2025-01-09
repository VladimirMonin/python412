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


# ЗАВТРАК!
async def main():
    # Включаем чайник IO bound - оно будет идти конкурентно
    pot = asyncio.create_task(task(5, "Чайник"))

    # Достаем колбасу и сыр из холодильника и нарезаем хлеб
    # CPU bound - оно будет идти последовательно
    cheese = await task(2, "Сыр и колбаса")
    bread = await task(2, "Хлеб")

    # Дождемся чайника
    hot_water = await pot

    # Заварить чай
    # CPU bound - оно будет идти последовательно
    black_tea = await task(3, "Чай")



    

# Засекаем старт
start_time = time.perf_counter()
asyncio.run(main())

# Финиш
finish_time = time.perf_counter()

print(f"Время выполнения программы: {finish_time - start_time:.2f} секунд")
