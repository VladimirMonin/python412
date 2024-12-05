"""
Программа для сжатия изображений
Работает на pillow и сжимает то что дают на входе в webp
pip install pillow
"""
# Импорт 
from PIL import Image # pip install pillow
import os # встроенный в пайтон модуль для работы с ОС

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']
COMPRESS_PERCENT = 50

# Получаем путь к файлу
user_file = input('Введите путь к файлу: ').strip().strip('"').strip("'")

# Получаем абсолютный путь к файлу с помощью модуля os
file_path = os.path.abspath(user_file)

# Получаем рассширение файла
file_extension = file_path.split('.')[-1]

# Проверяем расширение файла
if file_extension not in ALLOWED_EXTENSIONS:
    raise ValueError('Недопустимое расширение файла')

# Открываем файл
image = Image.open(file_path)

# Определяем новое имя файла
new_file_name = f'{file_path.split(".")[0]}_compressed.webp'

# Сжимаем изображение и сохраняем
image.save(new_file_name, 'webp', quality=COMPRESS_PERCENT)