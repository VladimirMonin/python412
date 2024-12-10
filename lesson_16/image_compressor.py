"""
Программа для сжатия изображений
Работает на pillow и сжимает то что дают на входе в webp
pip install pillow
"""

# Импорт
from PIL import Image  # pip install pillow
import os  # встроенный в пайтон модуль для работы с ОС

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]
COMPRESS_PERCENT = 50


def get_path_to_file():
    """
    Функция для получения пути к файлу
    """
    user_file = input("Введите путь к файлу: ").strip().strip('"').strip("'")
    os_path = os.path.abspath(user_file)
    return os_path


def get_file_extension(file_path):
    """
    Функция для получения расширения файла
    """
    file_extension = file_path.split(".")[-1]
    return file_extension


def get_file_name(file_path):
    """
    Функция для получения названия файла
    """
    file_name = os.path.basename(file_path)
    no_extension_name = file_name.split(".")[0]
    return no_extension_name


def compress_image(file_path, compress_percent):
    """
    Функция для сжатия изображения
    """
    image = Image.open(file_path)
    # Получаем директорию исходного файла
    source_dir = os.path.dirname(file_path)
    # Формируем полный путь для нового файла
    new_file_name = os.path.join(
        source_dir, f"{get_file_name(file_path)}_compressed.webp"
    )
    image.save(new_file_name, "webp", quality=compress_percent)


def compress_images_in_dir(dir_path):
    """
    Функция для сжатия изображений в директории
    """
    # os.listdir(dir_path) - возвращает список файлов в директории
    for file_name in os.listdir(dir_path):
        # os.path.join(dir_path, file_name) - возвращает полный путь к файлу
        file_path = os.path.join(dir_path, file_name)
        # os.path.isfile(file_path) - проверяет является ли объект файлом
        if os.path.isfile(file_path):
            file_extension = get_file_extension(file_path)
            if file_extension in ALLOWED_EXTENSIONS:
                compress_image(file_path, COMPRESS_PERCENT)


def main():
    print("Выберите действие:")
    print("1. Сжать изображение")
    print("2. Сжать изображения в директории")
    user_choice = input("Введите номер действия: ")

    if user_choice == "1":
        file_path = get_path_to_file()
        file_extension = get_file_extension(file_path)

        if file_extension not in ALLOWED_EXTENSIONS:
            raise ValueError("Недопустимое расширение файла")
        compress_image(file_path, COMPRESS_PERCENT)

    elif user_choice == "2":
        dir_path = get_path_to_file()
        compress_images_in_dir(dir_path)

    else:
        print("Неизвестное действие")


if __name__ == "__main__":
    main()
