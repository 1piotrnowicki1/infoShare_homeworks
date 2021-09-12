"""
Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny lub nieprawidłowy

"""
print('Podaj długości boków trójkąta a,b,c:')
a = int(input('Podaj długość boku a: '))
b = int(input('Podaj długość boku b: '))
c = int(input('Podaj długość boku c: '))


def prawidlowy_trojkat(a, b, c):
    if a+b >= c and b+c >= a and c+a >= b and a != 0 and b != 0 and c != 0:
        return True
    else:
        return False


def zbadaj_Trojkat(a, b, c):

    boki = [a, b, c]
    boki_sorted = sorted(boki)

    if (boki_sorted[2] ** 2) == (boki_sorted[0] ** 2) + (boki_sorted[1] ** 2):
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: prostokątnym')
    elif a == b or b == c or a == c:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: równoramienny')
    elif a != b and a != c and b != c and a != 0 and b != 0 and c != 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: różnoboczny')
    elif a == b and a == c and b == c and a != 0 and b != 0 and c != 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: równoboczny')


if prawidlowy_trojkat(a, b, c):
    zbadaj_Trojkat(a, b, c)
else:
    print('Trójkąt o podanych bokach a,b,c jest trójkątem: nieprawidłowym')


