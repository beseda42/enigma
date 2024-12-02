class Rotor:
    """
    Класс - ротор

    Attributes:
        __alphabet(list[str]): Алфавит
        __code(list[str]): Конфигурация ротора
        __position(int): Положение ротора
    """
    def __init__(self, alphabet, code, position):
        """
        Конструктор класса

        Args:
            alphabet(str): Алфавит
            code(str): Конфигурация ротора в виде непрерывной последовательности букв. Например, АБВГ
            position(str): Положение ротора (Буква из алфавита)

        Raises:
            ValueError: Некорректный аргумент
        """
        if len(alphabet) != len(code):
            raise ValueError("Количество букв в роторе должно быть равно мощности алфавита")
        for elem in code:
            if elem not in alphabet:
                raise ValueError(f"Неизвестный символ в роторе: {elem} нет в алфавите")
        if position not in alphabet:
            raise ValueError("Положение ротора должно быть задано буквой из алфавита")

        self.__alphabet = list(alphabet)
        self.__code = list(code)
        self.__position = self.__alphabet.index(position)
        self.__first_position = self.__code[0]

    def turn(self):
        """
        Имитирует поворот ротора
        Сдвиг конфигурации на 1
        """
        self.__code = self.__code[1:] + self.__code[:1]

    def check_full_turn(self):
        """
        Проверка на полный оборот ротора

        Returns
            boolean: Полный оборот был совершен?
        """
        if self.__code[0] == self.__first_position:
            return True
        return False

    def get_position(self):
        """
        Returns
            int: Положение ротора
        """
        return self.__position

    def change_forward(self, letter, prev_position):
        """
        Имитирует шифровку ротором до рефлектора

        Args:
            letter(str): Буква
            prev_position(int): Положение предыдущего ротора
        Returns:
            str: Зашифрованная буква
        """
        return self.__code[(self.__alphabet.index(letter) + self.__position - prev_position + len(self.__alphabet)) % len(self.__alphabet)]

    def change_back(self, letter, prev_position):
        """
        Имитирует шифровку ротором после рефлектора

        Args:
            letter(str): Буква
            prev_position(int): Положение предыдущего ротора
        Returns:
            str: Зашифрованная буква
        """
        return self.__alphabet[self.__code.index(self.__alphabet[(self.__alphabet.index(letter) + self.__position - prev_position + len(self.__alphabet)) % len(self.__alphabet)])]

    def end_return(self, letter):
        """
        Завершает шифровку роторами (Для 1 ротора после change_back)
        Args:
            letter(str): Буква
        Returns:
            str: Зашифрованная буква
        """
        return self.__alphabet[(self.__alphabet.index(letter) - self.__position + len(self.__alphabet)) % len(self.__alphabet)]