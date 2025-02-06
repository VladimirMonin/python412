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


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    lat: float
    lon: float
    is_used: bool = field(default=False, compare=False)
    is_million: bool = field(default=False, compare=False, repr=False)

    def __post_init__(self):
        if self.population >= 1_000_000:
            self.is_million = True

    def __str__(self):
        return f'Город: {self.name}. Население: {self.population} человек. Миллионник: {'Да' if self.is_million else 'Нет'}'
    
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
