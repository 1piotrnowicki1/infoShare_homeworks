class Kwiaty:
    pozycja = 1

    def __init__(self, kwiat, kolor, ilosc):
        self.lp = self.pozycja
        self.kwiat = kwiat
        self.kolor = kolor
        self.ilosc = ilosc
        Kwiaty.pozycja += 1

    def print_flowers_ilosc(self):
        for key, value in vars(self).items():
            print(key, value)


    def dokup_kwiaty(self, nowe_kwiaty):
        if isinstance(nowe_kwiaty, (int, float)):
            self.ilosc = nowe_kwiaty
        else:
            print('Nowy balans musi byc intem')