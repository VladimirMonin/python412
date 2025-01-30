"""
Тема: ООП Ч6. Миксины на примерах. Урок: 29
- Псевдокод Django и добавление MenuMixin в классы
- Специальные методы, магические методы double underscope methods
    - __init__ - Иницилизатор
    - __str__ - Строковое представление объекта
    - __len__ - Длина объекта
    - __bool__ - Преобразование объекта в булево значение
    - __call__ - Вызов объекта как функции
    - __iter__ - Итератор
"""

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self._index = 0

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        # тут может быть сложная логика, но мы отдаем наружу int
        return len(self.songs)
    
    def __str__(self):
        # тут может быть сложная логика, но мы отдаем наружу str
        return f'Плейлист "{self.name}, кол-во треков: {len(self.songs)}"'
    
    def __bool__(self):
        # тут может быть сложная логика, но мы отдаем наружу bool
        return bool(self.songs)
    
    def __call__(self, vibe: str):
        # тут может быть сложная логика, мы можем и принимать и отдавать
        return(f'Начал проигрывание {self.name} с настроением: {vibe}')

    def __iter__(self):
        # Работает при помещении экземпляра в for
        self._index = 0  # Сбрасываем индекс при начале итерации
        return self  # Возвращаем сам объект как итератор

    def __next__(self):
        # Работает при вызове next() - Т.е. при каждой итерации
        try:
            song = self.songs[self._index]
            self._index += 1
            return f"Сейчас играет: {song}"
        except IndexError:
            self._index = 0  # Сбрасываем индекс
            # Если закончились песни, выбрасываем спец. исключение котороые обрабатывает FOR автоматом`
            raise StopIteration("Плейлист закончился!")

playlist = Playlist("Рок хиты")
playlist.add_song("Queen - We Will Rock You")
playlist.add_song("AC/DC - Highway to Hell")
playlist.add_song("Nirvana - Smells Like Teen Spirit")

# Вариант 1: через for
for song in playlist:
    print(song)

# Вариант 2: через next()
playlist_iter = iter(playlist)
print(next(playlist_iter))
print(next(playlist_iter))
print(next(playlist_iter))
# Тут будет StopIteration