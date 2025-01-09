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

import asyncio
import time
# pip install aiohttp
import aiohttp


# Функция для асинхронного GET запроса, принемает URL и возвращает ответ
async def get_url(url: str):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.json()
    await session.close()
    await asyncio.sleep(0.2) # Асинхронный сон в 0.2 секунды. Выходит, что не более 5 запросов в секунду.
    return result

# Так как мы будем делать запросы к погодному АПИ (Сразу по разным городам)
# Нам нужна функция которая на вход возьмет город и отдаст URL для запроса
# url = r'https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'

def get_url_by_city(city: str) -> str:
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'
    return url

# Москва Питер Екатеринбург Краснодар Омск

async def main():
    # print(f'Москва', await get_url(get_url_by_city('Москва')))
    # print(f'Санкт-Петербург', await get_url(get_url_by_city('Санкт-Петербург')))
    # print(f'Екатеринбург', await get_url(get_url_by_city('Екатеринбург')))
    # print(f'Краснодар', await get_url(get_url_by_city('Краснодар')))
    # print(f'Омск', await get_url(get_url_by_city('Омск')))

    # cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Краснодар', 'Омск']
    # results = await asyncio.gather(*[get_url(get_url_by_city(city)) for city in cities])

    # Используем geather
    cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Краснодар', 'Омск']
    tasks = [asyncio.create_task(get_url(get_url_by_city(city))) for city in cities]
    results = await asyncio.gather(*tasks)
    print(results)

# Засекаем старт
start_time = time.perf_counter()
asyncio.run(main())

# Финиш
finish_time = time.perf_counter()

print(f"Время выполнения программы: {finish_time - start_time:.2f} секунд")
