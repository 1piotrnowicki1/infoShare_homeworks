"""
Homework 4:
Stworzyć klasę użytkownika, która będzie dziedziczyć po klasie człowiek (imię, nazwisko, etc.)
oraz będzie miała atrybut wieku automatycznie obliczany na podstawie daty urodzenia.
(https://www.programiz.com/python-programming/property - getter)

*Zadanie z gwiazdką - dodać do daty urodzenia setter który sprawdzi czy podano prawidłowy format daty w dacie urodzenia, np. dd/mm/yyyy
https://www.programiz.com/python-programming/property
"""

class czlowiek:
    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia