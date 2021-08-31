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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:

    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(f'%  {bcolors.FAIL}1: {bcolors.OKBLUE}Oblicz średnią arytmetyczną{bcolors.ENDC}')
    print(f'%  {bcolors.FAIL}2: {bcolors.OKBLUE}Podnieść do potęgi{bcolors.ENDC}')
    print(f'%  {bcolors.FAIL}3: {bcolors.OKBLUE}Porównaj liczby{bcolors.ENDC}')
    print(f'%  {bcolors.FAIL}4: {bcolors.OKBLUE}Wyjdź{bcolors.ENDC}')
    print('%')
    decyzja = input(f'%  {bcolors.WARNING}{bcolors.BOLD}Podaj opcje którą chcesz wybrać:{bcolors.ENDC}             ')

    if decyzja == '1':
        liczba_1 = int(input("%  Podaj pierwszą liczbę:                       "))
        liczba_2 = int(input("%  Podaj drugą liczbę:                          "))
        średnia = ((liczba_1 + liczba_2) / 2)
        print(f'%  {bcolors.UNDERLINE}{bcolors.OKGREEN}Średnia arytmetyczna z liczb {liczba_1} i {liczba_2} wynosi:{bcolors.ENDC}  {średnia}')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
    elif decyzja == '2':
        liczba_1 = int(input("%  Podaj pierwszą liczbę:                       "))
        liczba_2 = int(input("%  Podaj drugą liczbę:                          "))
        potęga = (liczba_1 ** liczba_2)
        print(f'%  {bcolors.UNDERLINE}{bcolors.OKGREEN}Liczba {liczba_1} podniesiona do potęgi {liczba_2} wynosi:{bcolors.ENDC}     {potęga}')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')

    elif decyzja == '3':
        liczba_1 = int(input("%  Podaj pierwszą liczbę:                       "))
        liczba_2 = int(input("%  Podaj drugą liczbę:                          "))
        if liczba_1 > liczba_2:
            print(f'%  {bcolors.UNDERLINE}{bcolors.OKGREEN}Większą liczbą od {liczba_2} jest liczba{bcolors.ENDC}              {liczba_1}')
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')
        else:
            print(f'%  {bcolors.UNDERLINE}{bcolors.OKGREEN}Większą liczbą od {liczba_1} jest liczba{bcolors.ENDC}              {liczba_2}')
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n')

    elif decyzja == '4':
        quit()
