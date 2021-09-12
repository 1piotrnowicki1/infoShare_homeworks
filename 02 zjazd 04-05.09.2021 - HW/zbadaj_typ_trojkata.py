"""
Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny lub nieprawidłowy

"""

def zbadaj_Trojkat():

    print('Podaj długości boków trójkąta a,b,c:')
    a = int(input('Podaj długość boku a: '))
    b = int(input('Podaj długość boku b: '))
    c = int(input('Podaj długość boku c: '))

    boki = [a, b, c]
    boki_sorted = sorted(boki)
    rownoramienny = len(set(boki_sorted))

    if (boki_sorted[2] ** 2) == (boki_sorted[0] ** 2) + (boki_sorted[1] ** 2) and a != 0 and b != 0 and c != 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: prostokątnym')
    elif len(boki) != rownoramienny and rownoramienny == 2 and a != 0 and b != 0 and c != 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: równoramienny')
    elif a != b and a != c and b != c and a != 0 and b != 0 and c != 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: różnoboczny')
    elif a == b and a == c and b == c and a != 0 and b != 0 and c != 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: równoboczny')
    elif a == 0 or b == 0 or c == 0:
        print('Trójkąt o podanych bokach a,b,c jest trójkątem: nieprawidłowym')

zbadaj_Trojkat()