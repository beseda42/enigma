from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

class Enigma:
    """
    Класс - энигма

    Attributes:
        __plugboard(Plugboard): Соединительная панель
        __rotors(list[Rotor]): Роторы
        __reflector(Reflector): Рефлектор
    """

    def __init__(self, plugboard, rotor1, rotor2, rotor3, reflector):
        """
        Конструктор класса

        Args:
            plugboard(Plugboard): Соединительная панель
            rotor1(Rotor): Первый ротор
            rotor2(Rotor): Второй ротор
            rotor3(Rotor): Третий ротор
            reflector(Reflector): Рефлектор
        """
        self.__plugboard = plugboard
        self.__rotors = [rotor1, rotor2, rotor3]
        self.__reflector = reflector

    def encode_letter(self, letter):
        """
        Шифрует 1 букву

        Args:
            letter(str): Буква
        Returns:
            str: Зашифрованная буква
        """
        encode_letter = self.__plugboard.change(letter)

        prev_position = 0
        for rotor in self.__rotors:
            encode_letter = rotor.change_forward(encode_letter, prev_position)
            prev_position = rotor.get_position()

        encode_letter = self.__reflector.reflect(encode_letter, prev_position)

        prev_position = 0
        for rotor in reversed(self.__rotors):
            encode_letter = rotor.change_back(encode_letter, prev_position)
            prev_position = rotor.get_position()

        encode_letter = self.__rotors[0].end_return(encode_letter)

        encode_letter = self.__plugboard.change(encode_letter)
        self.__rotors[0].turn()
        if self.__rotors[0].check_full_turn():
            self.__rotors[1].turn()

        return encode_letter

    def encode_str(self, str):
        """
        Шифрует строку

        Args:
            str(str): Строка
        Returns:
            str: Зашифрованная строка
        """
        encode_str = ""
        for elem in str:
            encode_str += self.encode_letter(elem)
        return encode_str