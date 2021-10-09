class Kwiaty:
    pozycja = 1

    def __init__(self, kwiat, kolor, ilosc):
        self.number = self.pozycja
        self.kwiat = kwiat
        self.kolor = kolor
        self.ilosc = ilosc
        Kwiaty.pozycja += 1

    def print_flowers_ilosc(self):
        for key, value in vars(self).items():
            print(key, value)

