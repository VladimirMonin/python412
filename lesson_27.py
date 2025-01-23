"""
Lesson 27
23.01.2025

ООП. Инкапсуляция. Продолжение.
- Класс "Шифр Цезаря" основанный на сдвиге по таблице кодирования UTF-8
- ord() - возвращает код символа в таблице UTF-8
- chr() - возвращает символ по коду в таблице UTF-8
"""

print(ord("A"))  # 65
print(chr(65))  # A


class UtfCeasarCipher:
    max_indent = 10

    def __init__(self):
        self.__indent_index = 1

    @property
    def indent_index(self):
        return self.__indent_index
    
    @indent_index.setter
    def indent_index(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Индекс должен быть числом")
        
        if abs(value) > self.max_indent:
            raise ValueError(f"Индекс сдвига должен быть меньше {self.max_indent}")
        
        self.__indent_index = value

# Тестируем геттер и сеттер
cipher = UtfCeasarCipher()
print(cipher.indent_index)
cipher.indent_index = 5
print(cipher.indent_index)
# cipher.indent_index = 50
# cipher.indent_index = "банан"

while True:
    try:
        indent = input("Введите индекс сдвига: ")
        cipher.indent_index = int(indent)
        break
    
    except ValueError as e:
        print(e)
        print("Попробуйте снова")
