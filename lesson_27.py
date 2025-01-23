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

    def __shift_indent(self, message: str, direction: bool):
        """
        Приватный метод для сдвига всего послания на __indent_index
        :param message: текст сообщения
        :param direction: True - кодируем, False - декодируем
        :return: Результат
        """

        result = ""

        for char in message:
            # chr - возвращает символ по коду в таблице UTF-8
            # ord - возвращает код символа в таблице UTF-8
            if direction:
                new_char = chr(ord(char) + self.__indent_index)
            else:
                new_char = chr(ord(char) - self.__indent_index)

            result += new_char

        return result
    
    def encode(self, message: str) -> str:
        """
        Публичный интерфейс для взаимодействия с классом
        Метод кодирования
        :param message: текст сообщения
        :return: Результат
        """
        return self.__shift_indent(message, True)
    
    def decode(self, message: str) -> str:
        """
        Публичный интерфейс для взаимодействия с классом
        Метод декодирования
        :param message: текст сообщения
        :return: Результат
        """
        return self.__shift_indent(message, False)



# Тестируем
if __name__ == "__main__":
    cipher = UtfCeasarCipher()
    
    while True:
        # Тут 2 потенциальных места для исключений
        # 1. Ввод индекса сдвига - int - ValueError
        # 2. Установка в Setter - ValueError
        try:
            indent = int(input("Введите индекс сдвига: "))
            try:
                cipher.indent_index = indent
            except ValueError as e:
                print(e)
                continue
        except ValueError as e:
            print(e)
            continue

        user_message = input("Введите сообщение: ")
        encoded_message = cipher.encode(user_message)
        decoded_message = cipher.decode(encoded_message)

        print(f"Закодированное сообщение: {encoded_message}")
        print(f"Декодированное сообщение: {decoded_message}")

