"""
Тема ООП Ч8. Погружение в Dataclasses. Урок: 31
- @dataclass
- (order=True)
- field
    - default factory
    - ...

"""

from dataclasses import dataclass, field


# field
"""
field - позволяет настроить отдельное поле класса
comparare=False - отключает сравнение по этому полю
"""

"""
  {
    "coords": {
      "lat": "50.38333",
      "lon": "103.28333"
    },
    "district": "Сибирский",
    "name": "Закаменск",
    "population": 11191,
    "subject": "Бурятия"
  },
"""
# 1. Импорт городов и создание датакласса

from data.cities import cities_list


@dataclass(order=True)
class City:
    name: str = field(compare=False)
    population: int
    subject: str = field(compare=False)
    district: str = field(compare=False)
    lat: float = field(compare=False)
    lon: float = field(compare=False)
    is_used: bool = field(default=False, compare=False)
    is_million: bool = field(default=False, compare=False, repr=False)

    def __post_init__(self):
        if self.population >= 1_000_000:
            self.is_million = True

    def __str__(self):
        return f'Город: {self.name}. Население: {self.population} человек. Миллионник: {'Да' if self.is_million else 'Нет'}'
    
    def get_dict(self):
        return {
            "name": self.name,
            "population": self.population,
            "subject": self.subject,
            "district": self.district,
            "lat": self.lat,
            "lon": self.lon,
        }
    
# 2. Создание списка экземпляров

cities = []

for city in cities_list:
    # Если бы у нас была подходящая структура данных... Но они разные)
    # cities.append(City(**city))

    instance = City(
        name=city["name"],
        population=city["population"],
        subject=city["subject"],
        district=city["district"],
        lat=city["coords"]["lat"],
        lon=city["coords"]["lon"],
    )
    cities.append(instance)

print(cities[0])

print(list(filter(lambda city: city.is_million, cities)))
millions_city = [city for city in cities if city.is_million]

print(list(filter(lambda city: city.population > 1000000, cities)))

# Сортируем список городов
cities.sort(reverse=True)
print(cities[:10])

# 4. Список словарей из экземпляров City
cities_list_dicts = [city.get_dict() for city in cities]

# 5. Скинем это в JSON
import json

# 6. Запишем в файл
with open('cities.json', 'w', encoding="utf-8") as f:
    json.dump(cities_list_dicts, f, ensure_ascii=False, indent=4)

# 7. Прочитаем из файла
with open('cities.json', 'r', encoding="utf-8") as f:
    cities_from_json = json.load(f)

# 8. Производим десериализацию 
cities_obj = [City(**city) for city in cities_from_json]
# Что происходит в распаковке **
# City(
#         name = "Высоцк",
#         population = 1074,
#         subject = "Ленинградская область",
#         district = "Северо-Западный",
#         lat = 60.625604,
#         lon = 28.568277 
# )