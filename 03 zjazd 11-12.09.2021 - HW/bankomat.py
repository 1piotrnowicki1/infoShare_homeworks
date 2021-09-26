"""
Napisać program bankomat który:
 - W słowniku karty przechowa informacje pod postacią ‘numer konta’ : {‘pin’: 1234, ‘saldo’: 1234}
 - Poprosi użytkownika o numer konta, a następnie gdy dany numer konta istnieje poprosi o numer pin.
 - Pozwoli użytkownikowi na dane opcje: odczytaj saldo, wpłać pieniądze, wypłać pieniądze, zmień kod PIN
 - Wyzwanie: zastanów się i zaimplementuj, w jaki sposób można przechowywać historię operacji. Zaimplementuj swoje rozwiązanie.

"""

karty = {'0000': {'pin': 1234, 'saldo': 10000}}

def authenticate_user():
    nr_konta = input('Podaj numer konta: ')
    if karty.get(nr_konta):
        pin = int(input('Podaj pin karty: '))
        if karty[nr_konta]['pin'] == pin:
            print('ok pin')
            return nr_konta
        else:
            print('Nok pin')
            return False
    else:
        return False

def options_user():
    print('1. Odczytaj saldo: ')
    print('2. Wpłać pieniądze: ')
    print('3. Zmień kod pin: ')
    print('4. Wyświetl historię: ')
    print('0. Wyjdz z programu: ')
    option = input('Podaj number opcji: ')
    return option

def main():
    zalogowany = False
    while not zalogowany:
        zalogowany = authenticate_user()
        print(f'Karta o numerze {zalogowany} zastala zalogowana')

    while True:
        choice = options_user()
        if choice == '1':
            print(f"Saldo: {karty['0000']['saldo']}")
            input('Nacisnij enter, aby wrocic do glownego menu')

        elif choice == '2':
            wplata = int(input('Suma wpłaty: '))
            karty['0000']['saldo'] += wplata
            print(f"Saldo: {karty['0000']['saldo']}")
            input('Nacisnij enter, aby wrocic do glownego menu')

        elif choice == '3':
            nowy_pin = int(input('Podaj nowy pin: '))
            karty['0000']['pin'] = nowy_pin
            print(f"Nowy pin: {karty['0000']['pin']}")
            input('Nacisnij enter, aby wrocic do glownego menu')

        elif choice == '4':
            pass

        elif choice == '0':
            break

if __name__ == "__main__":
    main()


