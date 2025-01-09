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
    # Условия вечеринки поменялись. Мы приглашаем гостей, когда пицца и фильм есть.
    # Create task - запустит задачу но дождаться её можно в другом месте
    pizza = asyncio.create_task(task(3, "Пицца"))
    film = asyncio.create_task(task(2, "Фильм"))
    
    # Пока запущены задачи, мы можем выполнять другую логику
    print("Пицца и фильм в процессе. Как только, так зовем друзей")
    
    # Но в какой-то момент нам нужно получить результаты ранее запущенных задач
    # wait - дождется выполнения задачи
    pizza = await pizza
    film = await film

    # Мы дождались 2 задачи и можем пригласить друзей (тоже асинхронно приглашаем 3х друзей
    # это можно сравнить с whatsap рассылкой :) )
    print("Приглашаем друзей")
    friends = await asyncio.gather(
        task(1, "Друг 1"), task(1, "Друг 2"), task(1, "Друг 3")
    )

    print(f"Приглашены друзья: {friends}")
    print("Вечеринка завершена")


    

# Засекаем старт
start_time = time.perf_counter()
asyncio.run(main())

# Финиш
finish_time = time.perf_counter()

print(f"Время выполнения программы: {finish_time - start_time:.2f} секунд")
