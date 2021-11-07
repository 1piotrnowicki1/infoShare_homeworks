"""
Homework 3:
Przygotować skrypt który pyta użytkownika o dane personalne osoby (np imię, nazwisko, nr tel) i zapisuje je do JSONa.
Obsłużyć wyjątek (try/except) gdy podany nr tel nie jest prawdziwym nr tel.

Przykłady nr tel:
123-403-129
438 123 398
123456789

Zróbmy bez kierunkowego dla uproszczenia.

"""

import json

user_data = {}

def user_data_phone_number():

    name = input('Podaj imię: ')
    surname = input('Podaj nazwisko: ')
    while True:
        try:
            number = input('Podaj numer tel (9-cyfrowy): ')
            user_data['Name'] = name
            user_data['Surname'] = surname
            user_data['Phone_no'] = number
            number = number.replace(" ", "").replace("-", "")

            if len(str(number)) == 9:
                print('Dane użytkownika zostały zapisane')
                break
            else:
                raise ValueError

        except ValueError:
            print('Numer telefonu jest nieprawidłowy')

        finally:
            with open('user_data.json', 'w') as database_file:
                json.dump(user_data, database_file)

user_data_phone_number()