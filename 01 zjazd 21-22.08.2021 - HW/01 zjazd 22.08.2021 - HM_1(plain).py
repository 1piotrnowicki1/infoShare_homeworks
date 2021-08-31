"""
Wydrukuje menu z następującymi opcjami:
- Oblicz średnią arytmetyczną
- Podnieś do potęgi
- Porównaj liczby

Użytkownik może wybrać dowolną opcję, a te powinny:
- Oblicz średnią arytmetyczną: przyjmij dwie liczby od użytkownika, następnie oblicz ich średnią arytmetyczną oraz wydrukuj ją na ekranie
- Podnieś do potęgi: przyjmij dwie liczby od użytkownika, podnieś pierwszą podaną liczbę do potęgi podanej jako druga liczba
  (przykładowo, jeśli podałem liczby 2 oraz 3, to wynik powinien wynosić 8. Przydatnym operatorem arytmetycznym będzie tu **)
- Porównaj liczby: przyjmij dwie liczby od użytkownika, a następnie wydrukuj na ekranie tę, która jest większa

Po zakończeniu którejkolwiek operacji, program powinien zacząć egzekucję od początku ( przydatna będzie tutaj pętla while )
"""

while True:
    print('1: Oblicz średnią arytmetyczną')
    print('2: Podnieść do potęgi')
    print('3: Porównaj liczby')
    print('4: Wyjdź')
    decyzja = input('Podaj opcje którą chcesz wybrać: ')

    if decyzja == '1':
        liczba_1 = int(input("Podaj pierwszą liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        print((liczba_1 + liczba_2) / 2)
    elif decyzja == '2':
        liczba_1 = int(input("Podaj pierwszą liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        print(liczba_1 ** liczba_2)

    elif decyzja == '3':
        liczba_1 = int(input("Podaj pierwszą liczbę: "))
        liczba_2 = int(input("Podaj drugą liczbę: "))
        if liczba_1 > liczba_2:
            print(liczba_1)
        else:
            print(liczba_2)

    elif decyzja == '4':
        quit()