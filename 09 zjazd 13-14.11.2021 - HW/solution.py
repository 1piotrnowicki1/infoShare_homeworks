import math


def trojkat(bok1, bok2):
    try:
        bok3 = math.sqrt(bok1 ** 2 + bok2 ** 2)
        return bok3
    except TypeError:
        raise TypeError('Nie wpisałeś liczby. Podaj ponownie długość boku trójkąta.')


if __name__ == '__main__':
    trojkat(4, 5)


