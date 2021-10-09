class Member:
    klient = 1

    def __init__(self, Imie, Nazwisko, Password):
        self.Lp = self.klient
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.Password = Password
        Member.klient += 1

    def klients_list(self):
        for key, value in vars(self).items():
            print(key, value)