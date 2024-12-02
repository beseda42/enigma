class Reflector:
    """
    Класс - рефлектор

    Attributes:
        __alphabet(list[str]): алфавит
        __code(dict[str, str]): словарь замен букв
    """
    def __init__(self, alphabet, code):
        """
        Конструктор класса

        Args:
            alphabet(str): Алфавит в виде непрерывной последовательности символов. Пример: АБВГ
            code(str): Параметры рефлектора в виде "буква-буква" через пробел. Пример: "А-Б Б-А В-Г Г-В"

        Raises:
            ValueError: Если количество символов в рефлекторе неравно количеству символов в алфавите
        """
        self.__alphabet = list(alphabet)
        self.__code = dict(elem.split("-") for elem in code.split(" "))
        if len(self.__alphabet) != len(self.__code):
            raise ValueError("Количество символов в рефлекторе должно быть равно количеству символов в алфавите")

    def reflect(self, letter, prev_position):
        """
        Имитирует прохождение сигнала через рефлектор
        Заменяет букву на её пару в рефлекторе

        Args:
            letter(str): Буква
            prev_position(int): Положение третьего ротора

        Returns:
            str: Зашифрованная буква
        """
        return self.__code.get(self.__alphabet[(self.__alphabet.index(letter) - prev_position + len(self.__alphabet)) % len(self.__alphabet)])

