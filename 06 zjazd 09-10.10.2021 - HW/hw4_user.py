"""
Homework 4:
Stworzyć klasę użytkownika, która będzie dziedziczyć po klasie człowiek (imię, nazwisko, etc.)
oraz będzie miała atrybut wieku automatycznie obliczany na podstawie daty urodzenia.
(https://www.programiz.com/python-programming/property - getter)

*Zadanie z gwiazdką - dodać do daty urodzenia setter który sprawdzi czy podano prawidłowy format daty w dacie urodzenia, np. dd/mm/yyyy
https://www.programiz.com/python-programming/property
"""

from datetime import date, datetime

from hw4_czlowiek import czlowiek

class user(czlowiek):
    def __init__(self, imie, nazwisko, data_urodzenia):
        super().__init__(imie, nazwisko, data_urodzenia)

    @property
    def wiek(self):
        today = date.today()
        urodziny = datetime.strptime(self.data_urodzenia, '%d-%m-%Y')
        return today.year - urodziny.year


czlowiek1 = user('Piotr', 'Nowicki', '30-03-1992')

print((czlowiek1.imie) + " ma " + str(czlowiek1.wiek) + " lat")