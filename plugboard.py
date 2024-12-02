class Plugboard:
    """
    Класс - соединительная панель

    Attributes:
        __position (dict[str, str]): Словарь замен
    """
    def __init__(self, position = ""):
        """
        Конструктор класса

        Args:
            position(str): Строка вида "буква-буква буква-буква". Например, "Б-В А-Г"
        """
        if position == "":
            self.__position = None
        else:
            self.__position = {}
            pairs = (position.replace('-', '').split(' '))
            for pair in pairs:
                self.__position[pair[0]] = pair[1]
                self.__position[pair[1]] = pair[0]

    def change(self, letter):
        """
        Имитирует прохождение сигнала через соединительную панель
        В случае, если буква присутствует в соединительной панели - заменяет её.

        Args:
            letter(str): Буква

        Returns:
            str: Зашифрованная буква
        """
        if self.__position is not None:
            if letter in self.__position:
                return self.__position[letter]
        return letter
