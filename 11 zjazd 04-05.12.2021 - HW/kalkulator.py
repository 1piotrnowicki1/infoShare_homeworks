"""
HW11:
Napisać kalkulator który dodaje i odejmuje i podpiąć do niego loggera:

    - W przypadku gdy podamy wartość string wyrzuci błąd i zapisze go do loggera (poziom WARN lub ERROR)
    - Jeśli podane dane były poprawne to zapisze dane wejściowe i wynik do loggera (poziom INFO)
"""
import logging

def dodawanie(x=None, y=None):
    try:
        if not x: x = int(input('wpisz x '))
        if not y: y = int(input('wpisz y '))
        wynik_dodawania = (x + y)
        logger.info(f"Po dodaniu dwóch liczb {x} i {y} wynik będzie równy: {wynik_dodawania} ")
        return wynik_dodawania
    except (TypeError, ValueError):
        logger.error("Wpisałeś litere. podaj liczbe")
        raise TypeError('Nie wpisałeś liczby. Podaj ponownie liczbę.')


def odejmowanie(x=None, y=None):
    try:
        if not x: x = int(input('wpisz x '))
        if not y: y = int(input('wpisz y '))
        wynik_odejmowania = (x - y)
        logger.info(f"Po odjęciu liczby {y} od {y} wynik będzie równy: {wynik_odejmowania} ")
        return wynik_odejmowania
    except (TypeError, ValueError):
        logger.error("Wpisałeś litere. podaj liczbe")
        raise TypeError('Nie wpisałeś liczby. Podaj ponownie liczbę.')


if __name__ == '__main__':
    formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s')
    file_handler = logging.FileHandler("logfile.log")
    file_handler.setFormatter(formatter)
    # file_handler.setLevel(logging.INFO)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    while True:
        print('1: Dodawanie')
        print('2: Odejmowanie')
        print('3: Wyjdź')
        decyzja = input('Podaj opcje którą chcesz wybrać: ')
        if decyzja == '1':
            print(dodawanie(None, None))
        elif decyzja == '2':
            print(odejmowanie(None, None))
        elif decyzja == '3':
            quit()


