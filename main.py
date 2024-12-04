from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
import sys

def check_positions(alphabet, input_str):
    """
    Проверка введенных данных: положение роторов

    Args:
        alphabet(str): Алфавит
        input_str(str): Положение роторов

    Raises:
        ValueError: Некорректное положение роторов
    """
    if len(input_str) != 3:
        raise ValueError ("Положение 3 роторов должно быть представлено в виде трех букв, написанных слитно")
    for elem in input_str:
        if elem not in alphabet:
            raise ValueError("Положение ротора должно быть задано буквой из алфавита")

def check_plugboard_input(alphabet, plugboard_input):
    """
    Проверка введенных данных: положение роторов

    Args:
        alphabet(str): Алфавит
        plugboard_input(str): Положение роторов

    Raises:
        ValueError: Некорректная соединительная панель
    """
    if len((plugboard_input.replace(" ", "")).replace("-", "")) % 2 != 0:
        raise ValueError ("В соединительной панели должны быть пары букв")
    for elem in (plugboard_input.replace(" ", "")).replace("-", ""):
        if elem not in alphabet:
            raise ValueError (f"Неизвестный символ в соединительной панели: {elem} нет в алфавите")
        if plugboard_input.count(elem) > 1:
            raise ValueError(f"Символ в соединительной панели может быть использован только один раз: {elem} появляется несколько раз")

def check_text(alphabet, text):
    """
    Проверка введенных данных: текст

    Args:
        alphabet(str): Алфавит
        text(str): Текст для шифрования

    Raises:
        ValueError: Некорректный текст
    """
    for elem in text:
        if elem not in alphabet:
            raise ValueError(f"Неизвестный символ в тексте: {elem} нет в алфавите")

def print_help(args):
    """
    Вывод данных о программе

    Args:
        args(int): len(sys.argv)
    """
    print("Шифровальная машина Enigma\n")
    print("Алфавит, конфигурация роторов и рефлектора задается через settings.txt в указанном формате:")
    print("Алфавит\nРотор1\nРотор2\nРотор3\nРефлектор\n")
    print("Пример:")
    print("АБВГ\nБВАГ\nГАБВ\nАГВБ\nА-Б Б-А В-Г Г-В\n")
    if args > 1:
        print("Запуск через консоль осуществляется следующим образом:\n")
        print("main.py _положение роторов_ _соединительная панель_ _текст_\n")
        print("Пример:\nmain.py ААА БВ ГАВ\n")
    else:
        print("Запуск через текстовый интерфейс осуществляется следующим образом:\n")
        print("_положение роторов_ _соединительная панель_ _текст_\n")
        print("Пример:\nААА БВ ГАВ\n")
    print("Положение роторов: 3 буквы, написанные слитно, например: ААА")
    print("Соединительная панель: пары букв, написанные слитно. Количество: от нуля до половины алфавита")
    print("Текст для шифрования: любой текст, включающий в себя только символы алфавита")

if __name__ == "__main__":
    #Считывание настроек энигмы из текстового файла
    input_data = []
    file_path = "settings.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line[0] != "#":
                input_data.append(line)

    alphabet = input_data[0]
    reflector = Reflector(alphabet, input_data[4])

    #Если осуществляется консольный запуск с передачей параметров:
    if len(sys.argv) > 1:

        if sys.argv[1] == "help":
            print_help(len(sys.argv))
            sys.exit(0)

        elif len(sys.argv) - 1 < 2:
            print(sys.argv)
            print ("Некорректное количество аргументов. Для помощи воспользуйтесь help")
            sys.exit(0)

        #Считывание положения роторов
        positions = sys.argv[1]
        check_positions(alphabet, positions)

        #Считывание соединительной панели
        if len(sys.argv) - 1 > 2:
            args = sys.argv[2:-1]
            plugboard_input = " ".join(args)
            check_plugboard_input(alphabet, plugboard_input)
            plugboard = Plugboard(plugboard_input)
        else:
            plugboard = Plugboard("")

        #Считывание текста
        text = sys.argv[-1]
        check_text(alphabet, text)

    #Если осуществляется запуск через текстовый интерфейс/через консоль без передачи данных
    else:
        '''
        print("Для начала работы введите start. Для получения справки введите help")
        user_input = ""
        while user_input != "start":
            user_input = input()
            if user_input == "help":
                print_help(len(sys.argv))
        '''
        #Считывание положения роторов
        positions = input("Введите положение 3 роторов (3 буквы, слитно):")
        check_positions(alphabet, positions)

        #Считывание соединительной панели
        plugboard_input = input("Введите настройки соединительной панели в виде пар букв, написанных слитно:")
        check_plugboard_input(alphabet, plugboard_input)
        plugboard = Plugboard(plugboard_input)

        #Считывание текста
        text = input("Введите текст, который нужно зашифровать:")

    check_text(alphabet, text)

    #Инициализация роторов и энигмы
    rotor1 = Rotor(alphabet, input_data[1], positions[0])
    rotor2 = Rotor(alphabet, input_data[2], positions[1])
    rotor3 = Rotor(alphabet, input_data[3], positions[2])
    enigma = Enigma(plugboard, rotor1, rotor2, rotor3, reflector)

    #Вывод зашифрованного сообщения
    print(enigma.encode_str(text))