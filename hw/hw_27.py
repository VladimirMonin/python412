import asyncio
from openai import AsyncOpenAI # pip install openai
from hw_27_data import DATA

API_KEY = "ключ"
BASE_URL = "https://api.vsegpt.ru/v1"
MAX_CHUNK_SIZE = 2000 # Максимальная длина текста для 1 запроса к API
SLEEP_TIME = 4 # Задержка между запросами
OUTPUT_FILE = "lecture_summary.md"
PROMPT_THEME = """
Привет!

Определи общую тему  текста. И постарайся максимально полно и точно описать её,
с использованием пунктов и подпунктов.

Не додумывай того, чего там небыло.
Исключи small talks.
"""

PROMPT_TIMESTAMPS = """
Привет!

Ты - ассистент по созданию таймкодов для видео.
Тебе будет предоставлен текст с таймкодами из видео.
Твоя задача - создать краткое описание каждого смыслового блока.
Ты не должен использовать полное цитирование. Создай краткое описание для блока.
Каждый блок должен начинаться с таймкода в формате чч:мм:сс.
Описание должно быть одним предложением, передающим суть начинающегося отрезка.
Игнорируй слишком короткие фрагменты или паузы.
Объединяй связанные по смыслу части в один большой блок.
Описания должны быть в стиле, как это обычно делают на youtube.



ВАЖНО.
СТРОГИЕ ПРАВИЛА:
1. Для видео длительностью:
   - до 30 минут: максимум 5 таймкодов
   - 30-60 минут: максимум 8 таймкодов
   - 1-2 часа: максимум 10 таймкодов
   - 2+ часа: максимум 15 таймкодов

2. Минимальный интервал между таймкодами:
   - для коротких видео (до 30 мин): 3-5 минут
   - для длинных видео: 10-15 минут

3. Объединяй близкие по смыслу темы в один таймкод

ВАЖНО: Если ты превысишь количество таймкодов - твой ответ будет отклонён!

В твоём ответе должны быть только таймкоды и описания.
Никаких других комментариев или пояснений.

КАК ПИСАТЬ?

Ты не пишешь описательные, длинные предложения. 
Вроде: "Пояснение адаптивного подхода к верстке на примере Visual Studio Code, где контент перестраивается в зависимости от размера экрана. "

Ты пишешь короткий, ёмкий вариант.
"Адаптивный подход к вёрстке. Пример в Visual Studio Code. Контент перестраивается в зависимости от размера экрана."
Или даже ещё немного короче.

Спасибо!
"""

PROMPT_CONSPECT_WRITER = """
Привет!
Ты опытный технический писатель. Ниже, я предоставляю тебе полный текст лекции а так же ту часть,
с которой ты будешь работать.

Ты великолепно знаешь русский язык и отлично владеешь этой темой.

Тема занятия: {topic}

Полный текст лекции:
{full_text}

Сейчас я дам тебе ту часть, с котороый ты будешь работать. Я попрошу тебя написать конспект лекции.
А так же блоки кода.

Ты пишешь в формате Markdown. Начни с заголовка 2го уровня.
В тексте используй заголовки 3го уровня.

Используй блоки кода по необходимости.

Отрезок текста с которым ты работаешь, с которого ты будешь работать:
{text_to_work}
"""

client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)

async def get_ai_request(prompt: str, model: str = "openai/gpt-4o-mini", max_tokens: int = 16000, temperature: float = 0.7) -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content

OUTPUT_FILE = "lecture_summary.md"

def split_text_to_chunks(data: list) -> list:
    """Разбивает текст на чанки не более MAX_CHUNK_SIZE символов"""
    chunks = []
    current_chunk = ""
    
    for item in data:
        text = item['text']
        if len(current_chunk) + len(text) <= MAX_CHUNK_SIZE:
            current_chunk += text
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = text
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def save_to_markdown(timestamps: str, theme: str, chunks: list):
    """Сохраняет результаты в markdown файл"""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Таймкоды\n\n")
        f.write(timestamps)
        f.write("\n\n---\n\n")
        
        f.write("# Краткое содержание\n\n")
        f.write(theme)
        f.write("\n\n---\n\n")
        
        f.write("# Конспект\n\n")
        for chunk in chunks:
            f.write(chunk)
            f.write("\n\n---\n\n")

async def main():
    # Получаем полный текст из DATA
    full_text = " ".join([item['text'] for item in DATA])
    
    # 1. Получаем таймкоды и тему
    tasks = [
        get_ai_request(PROMPT_TIMESTAMPS + full_text),
        get_ai_request(PROMPT_THEME + full_text)
    ]
    timestamps, theme = await asyncio.gather(*tasks)
    await asyncio.sleep(SLEEP_TIME)
    
    # 2. Разбиваем на чанки
    chunks = split_text_to_chunks(DATA)
    
    # 3. Отправляем чанки на обработку
    conspect_tasks = []
    for chunk in chunks:
        prompt = PROMPT_CONSPECT_WRITER.format(
            topic=theme,
            full_text=full_text,
            text_to_work=chunk
        )
        conspect_tasks.append(get_ai_request(prompt))
        await asyncio.sleep(SLEEP_TIME)
    
    chunk_results = await asyncio.gather(*conspect_tasks)
    
    # 4. Сохраняем результаты
    save_to_markdown(timestamps, theme, chunk_results)

if __name__ == "__main__":
    asyncio.run(main())
