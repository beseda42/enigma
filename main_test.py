from main import check_positions, check_plugboard_input, check_text
from rotor import Rotor
from enigma import Enigma
from plugboard import Plugboard
from reflector import Reflector

def main_test(positions, plugboard_input, text):
    """
    Полная имитация main.py для проверки тестами
    Args:
        positions: Начальное положение роторов
        plugboard_input: Соединительная панель
        text: Текст для шифровки

    Returns: Зашифрованный текст

    """
    input_data = []
    file_path = "settings.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line[0] != "#":
                input_data.append(line)

    alphabet = input_data[0]
    reflector = Reflector(alphabet, input_data[4])

    check_positions(alphabet, positions)
    check_plugboard_input(alphabet, plugboard_input)
    plugboard = Plugboard(plugboard_input)
    check_text(alphabet, text)

    rotor1 = Rotor(alphabet, input_data[1], positions[0])
    rotor2 = Rotor(alphabet, input_data[2], positions[1])
    rotor3 = Rotor(alphabet, input_data[3], positions[2])
    enigma = Enigma(plugboard, rotor1, rotor2, rotor3, reflector)

    return enigma.encode_str(text)
