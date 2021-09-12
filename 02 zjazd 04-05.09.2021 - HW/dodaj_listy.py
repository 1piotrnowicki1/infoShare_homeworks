"""
Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy na tych samych indeksach.
Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis ‘Podane listy muszą być tej samej długości’

"""

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]


def dodaj_listy(lista1, lista2):
    if len(lista1) != len(lista2):
        print('Podane listy muszą być tej samej długości')
    else:
        lista_sum = []
        for i in range(len(lista1)):
            suma = lista1[i] + lista2[i]
            lista_sum.append(suma)
        print(lista_sum)
        return lista_sum


dodaj_listy(lista1, lista2)