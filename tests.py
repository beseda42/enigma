import random
import pytest
from main_test import main_test
from enigma import Enigma
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

@pytest.fixture
def random_str():
    """
    Returns: Десять случайных слов
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = []
    for i in range(10):
        str = ''
        for j in range(random.randint(1,10)):
            str += alphabet[random.randint(0, len(alphabet) - 1)]
        words.append(str)
    return words

@pytest.fixture
def dif_positions_enigmas():
    """
    Returns: Две энигмы, в которых отличаются только начальные позиции роторов
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    enigmas = []
    plugboard = Plugboard('FG LK')
    pos1 = 'B'
    pos2 = 'C'
    rotor_same1 = 'PLOKMIJNBHUYGVCFTRDXZSEWAQ'
    rotor_same2 = 'LKJHGFDSAQZWXECRVTBYNUMIOP'
    rotor_same3 = 'MLPKONJIBHUVGYCFTXDRZSEWAQ'
    ref = Reflector(alphabet, 'Q-W W-Q E-R R-E T-Y Y-T U-I I-U O-P P-O A-S S-A D-F F-D G-H H-G J-K K-J L-Z Z-L X-C C-X V-B B-V N-M M-N')
    enigmas.append(Enigma(plugboard, Rotor(alphabet, rotor_same1, pos1), Rotor(alphabet, rotor_same2, pos1), Rotor(alphabet, rotor_same3, pos1), ref))
    enigmas.append(Enigma(plugboard, Rotor(alphabet, rotor_same1, pos2), Rotor(alphabet, rotor_same2, pos2), Rotor(alphabet, rotor_same3, pos2), ref))
    return enigmas

#Создание машины
@pytest.fixture
def dif_rotors_enigmas():
    """
    Returns: Две энигмы, в которых отличаются только роторы
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    enigmas = []
    plugboard = Plugboard('FG LK')
    def_pos = 'A'
    rotor_same1 = Rotor(alphabet, 'PLOKMIJNBHUYGVCFTRDXZSEWAQ', def_pos)
    rotor_same2 = Rotor(alphabet, 'LKJHGFDSAQZWXECRVTBYNUMIOP', def_pos)
    rotor1 = Rotor(alphabet, 'MLPKONJIBHUVGYCFTXDRZSEWAQ', def_pos)
    rotor2 = Rotor(alphabet, 'ZXCVBNMPOIUYTREWQASDFGHJKL', def_pos)
    ref = Reflector(alphabet, 'Q-W W-Q E-R R-E T-Y Y-T U-I I-U O-P P-O A-S S-A D-F F-D G-H H-G J-K K-J L-Z Z-L X-C C-X V-B B-V N-M M-N')
    enigmas.append(Enigma(plugboard, rotor_same1, rotor_same2, rotor1, ref))
    enigmas.append(Enigma(plugboard, rotor_same1, rotor_same2, rotor2, ref))
    return enigmas

@pytest.fixture
def dif_reflector_enigmas():
    """
    Returns: Две энигмы, в которых отличаются только рефлекторы
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    enigmas = []
    plugboard = Plugboard('FG LK')
    def_pos = 'B'
    rotor_same1 = Rotor(alphabet, 'PLOKMIJNBHUYGVCFTRDXZSEWAQ', def_pos)
    rotor_same2 = Rotor(alphabet, 'LKJHGFDSAQZWXECRVTBYNUMIOP', def_pos)
    rotor_same3 = Rotor(alphabet, 'MLPKONJIBHUVGYCFTXDRZSEWAQ', def_pos)
    ref1 = Reflector(alphabet, 'Q-W W-Q E-R R-E T-Y Y-T U-I I-U O-P P-O A-S S-A D-F F-D G-H H-G J-K K-J L-Z Z-L X-C C-X V-B B-V N-M M-N')
    ref2 =Reflector(alphabet, 'A-B B-A C-D D-C E-F F-E G-H H-G I-J J-I K-L L-K M-N N-M O-P P-O Q-R R-Q S-T T-S U-V V-U W-X X-W Y-Z Z-Y')
    enigmas.append(Enigma(plugboard, rotor_same1, rotor_same2, rotor_same3, ref1))
    enigmas.append(Enigma(plugboard, rotor_same1, rotor_same2, rotor_same3, ref2))
    return enigmas

# Возможность выставления различных начальных положений роторов
@pytest.mark.parametrize('input_case, expected_output', [('AAA', 'YKGQRX'), ('AAB', 'GGWXXJ'), ('KKK', 'PSGRRJ')])
def test_positions(input_case, expected_output):
    assert main_test(input_case, 'AB', 'KITTEN') == expected_output

# Возможность выставления различных начальных положений соединительной панели
@pytest.mark.parametrize('input_case, expected_output', [('', 'PKBWNX'), ('ER', 'PKBWZX'), ('TE KI NY', 'RKIXAQ')])
def test_plugboard(input_case, expected_output):
    assert main_test('ABC', input_case, 'KITTEN') == expected_output

# Корректность расшифровки сообщений
def test_decoding(random_str):
    decoding = []
    cases = random_str
    for elem in cases:
        code = main_test('ABC', 'AO', elem)
        decoding.append(main_test('ABC', 'AO', code))
    assert cases == decoding

# Невозможность расшифровки при другом начальном положении роторов
def test_position_decoding(dif_positions_enigmas):
    cases = dif_positions_enigmas
    output = []
    for elem in cases:
        output.append(elem.encode_str('ENIGMA'))
    assert output[0] != output[1]

# Невозможность расшифровки при другом положении роторов
def test_rotor_decoding(dif_rotors_enigmas):
    cases = dif_rotors_enigmas
    output = []
    for elem in cases:
        output.append(elem.encode_str('ENIGMA'))
    assert output[0] != output[1]

# Невозможность расшифровки при другом рефлекторе
def test_reflector_decoding(dif_reflector_enigmas):
    cases = dif_reflector_enigmas
    output = []
    for elem in cases:
        output.append(elem.encode_str('ENIGMA'))
    assert output[0] != output[1]

#Отработка некорректного ввода
@pytest.mark.parametrize('position, plugboard, text',
                         [('F', 'AB', 'TEST'),
                          ('РУС', 'AB', 'TEST'),
                          ('AAA', 'РУ', 'TEST'),
                          ('AAA', 'ERB', 'TEST'),
                          ('AAA', 'AA', 'TEST'),
                          ('AAA', 'AB', 'ТЕСТ')])
def test_error(position, plugboard, text):
    with pytest.raises(ValueError):
        main_test(position, plugboard, text)
