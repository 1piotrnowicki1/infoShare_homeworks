from klient_member import Member
from kwiaty import Kwiaty

class KwiaciarniaHurtownia:

    members = []
    flowers = []

    def __init__(self):
        self.main()

    def add_member(self):
        Imie = input('Podaj imie: ')
        Nazwisko = input('Podaj nazwisko: ')
        Password = input('Podaj haslo: ')
        member = Member(Imie, Nazwisko, Password)
        KwiaciarniaHurtownia.members.append(member)

    def members_list(self):
        for member_list in KwiaciarniaHurtownia.members:
            member_list.klients_list()

        #for member in KwiaciarniaHurtownia.members:
        #    print(vars(member))

    def add_flower(self):
        kwiat = input('Podaj nazwe kwiata: ')
        kolor = input('Podaj kolor kwiata: ')
        ilosc = input('Podaj ilosc: ')
        flower = Kwiaty(kwiat, kolor, ilosc)
        KwiaciarniaHurtownia.flowers.append(flower)

    def show_flowers_list(self):

        for flower_list in KwiaciarniaHurtownia.flowers:
            flower_list.print_flowers_ilosc()


    def print_menu(self):
        print('Wybierz opcje: ')
        print(10 * '*')
        print('1. Dodaj klienta ')
        print('2. Lista klientow')
        print('3. Dodaj kwiata')
        print('4. Lista dostępnych kwiatow')
        print('5. Sprzedaj kwiata')
        print('6. Dokup kwiaty')
        print('7. Historia transakcji')


    def main(self):
        while True:
            self.print_menu()
            option = input('Podaj opcję: ')
            if option == '1':
                self.add_member()
            elif option == '2':
                self.members_list()
            elif option == '3':
                self.add_flower()
            elif option == '4':
                self.show_flowers_list()

KwiaciarniaHurtownia()