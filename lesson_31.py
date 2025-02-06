"""
Тема ООП Ч8. Погружение в Dataclasses. Урок: 31
- @dataclass
- (order=True)
- field
    - default factory
    - ...


Напишем Класс - итератор, который будет настраиваться и возвращать
чанки длиной CHUNK_LENTH из LESSON_FILE

Который является массивом объектов JSON:

[
    {
        "timestamp": [
            65.58,
            66.18
        ],
        "text": " you Итак, давайте начнем с домашнего задания. Домашнее задание, я думаю, что кто-то из вас, наверное, уже заглянул, посмотрел. Вообще, это серия, целая серия, но вам досталась последняя. С другими группами мы пишем игру в города. Она пишет, что сначала в виде скрипта на Python, потом ребята рефакторят ее на функции, а потом ребята ее рефакторят на OOP."
    }.....


Каждый чанк будет экземпляром датакласса LessonChunk
- start_time: int
- finish_time: int
- text: str
"""

from dataclasses import dataclass, field
import json

LESSON_FILE = "lesson_30_data.json"
CHUNK_LENTH = 5000


@dataclass(order=True)
class LessonChunk:
    start_time: int
    finish_time: int = field(compare=False)
    text: str = field(compare=False)

    def format_time(self, seconds):
        if seconds is None:
            return "конец записи"
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class LessonReader:
    def __init__(self, file_path: str, chunk_length: int = CHUNK_LENTH):
        self.file_path = file_path
        self.chunk_length = chunk_length
        self.file_data = self.__read_json()

    def __read_json(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def __prepare_chunk(self):
        if not self.file_data:
            return None

        start_time = self.file_data[0]["timestamp"][0]
        current_text = ""
        finish_time = None

        while self.file_data and len(current_text) < self.chunk_length:
            chunk_data = self.file_data.pop(0)
            current_text += chunk_data["text"]
            finish_time = chunk_data["timestamp"][1]

        return LessonChunk(
            start_time=start_time, finish_time=finish_time, text=current_text
        )

    def __iter__(self):
        return self

    def __next__(self):
        chunk = self.__prepare_chunk()
        if chunk is None:
            raise StopIteration
        return chunk


# Тесты
if __name__ == "__main__":
    reader = LessonReader(LESSON_FILE)

    for i, chunk in enumerate(reader, 1):
        print(f"Чанк {i}:")
        print(f"Начало: {chunk.format_time(chunk.start_time)}")
        print(f"Конец: {chunk.format_time(chunk.finish_time)}")
        print(f"Длина текста: {len(chunk.text)}")
        print(f"Первые 50 символов: {chunk.text[:50]}")
        print("-" * 50)
