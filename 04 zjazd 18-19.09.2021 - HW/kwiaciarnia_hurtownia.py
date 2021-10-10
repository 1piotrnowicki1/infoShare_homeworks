from klient_member import Member
from kwiaty import Kwiaty
from logi import Operation

class KwiaciarniaHurtownia:

    members = []
    flowers = []
    logi_historia = []

    def __init__(self):
        self.main()

    def add_logi(self, operation: str) -> None:
        """
        Creates an Operation object, then adds it to KwiaciarniaHurtownia.logi_historia

        Args:
        operation (str): name of the operation
        """
        new_operation = Operation(operation)
        KwiaciarniaHurtownia.logi_historia.append(new_operation)

    def show_logs_actions(self):
        for operatin in KwiaciarniaHurtownia.logi_historia:
            print(vars(operatin))

    def add_member(self):
        Imie = input('Podaj imie: ')
        Nazwisko = input('Podaj nazwisko: ')
        Password = input('Podaj haslo: ')
        member = Member(Imie, Nazwisko, Password)
        KwiaciarniaHurtownia.members.append(member)

        self.add_logi('Został stworzony nowy klient')

    def members_list(self):
        for member_list in KwiaciarniaHurtownia.members:
            member_list.klients_list()

        #for member in KwiaciarniaHurtownia.members:
        #    print(vars(member))

        self.add_logi('Została wyświetlona lista klientów')

    def add_flower(self):
        kwiat = input('Podaj nazwe kwiata: ')
        kolor = input('Podaj kolor kwiata: ')
        ilosc = int(input('Podaj ilosc: '))
        flower = Kwiaty(kwiat, kolor, ilosc)
        KwiaciarniaHurtownia.flowers.append(flower)

        self.add_logi('Dodany został nowy kwiat')

    def show_flowers_list(self):

        for flower_list in KwiaciarniaHurtownia.flowers:
            flower_list.print_flowers_ilosc()

        self.add_logi('Została wyświetlona lista kwiatów')

    def sell_flowers(self):
        def check_if_flower_exists(kwiat_lp):
            for kwiat in KwiaciarniaHurtownia.flowers:
                if kwiat.lp == kwiat_lp:
                    return kwiat
                else:
                    continue
            return False

        kwiat_lp = int(input('Podaj ID kwiata który chcesz sprzedać: '))
        flower = check_if_flower_exists(kwiat_lp)
        if flower:
            zamowienie = int(input('Podaj ile kwiatów klient chce kupic: '))
            if flower.ilosc >= zamowienie:
                flower.ilosc -= zamowienie
                print(f'Zostało sprzedanych {zamowienie} kwiatów')
            else:
                print('Niewystarczająca ilość kwiatów do sprzedaży')
        else:
            print('wybrany klient nie istnieje')

        self.add_logi('Kwiat został sprzedany klientowi')

    def restock_flowers(self):
        def check_if_flower_exists(kwiat_lp):
            for kwiat in KwiaciarniaHurtownia.flowers:
                if kwiat.lp == kwiat_lp:
                    return kwiat
                else:
                    continue
            return False

        kwiat_lp = int(input('Podaj ID kwiata który chcesz dokupić: '))
        flower = check_if_flower_exists(kwiat_lp)
        if flower:
            szt = int(input('Podaj ile kwiatów chcesz dokupić: '))
            nowe_kwiaty = flower.ilosc + szt
            flower.dokup_kwiaty(nowe_kwiaty)
        else:
            print('Wybrany kwiat nie istnieje')

        self.add_logi('Kwiat zostały dokupione')

    def print_menu(self):
        print('Wybierz opcje: ')
        print(10 * '*')
        print('1. Dodaj klienta ')
        print('2. Lista klientow')
        print('3. Dodaj kwiata')
        print('4. Lista dostępnych kwiatow')
        print('5. Sprzedaj kwiata')
        print('6. Uzupełnij braki magazynowe')
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
            elif option == '5':
                self.sell_flowers()
            elif option == '6':
                self.restock_flowers()
            elif option == '7':
                self.show_logs_actions()


KwiaciarniaHurtownia()