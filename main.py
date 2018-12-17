def main():
    generator_kodow_pocztowych()
    brakujace_elementy()
    lista_liczb()


def generator_kodow_pocztowych():
    kod_1 = "79-900"
    kod_2 = "80-155"
    lista_kodow = []

    okreg_kodowy_1 = int(kod_1[:2])
    strefa_kodowa_1 = int(kod_1[3:]) + 1
    okreg_kodowy_2 = int(kod_2[:2]) + 1
    strefa_kodowa_2 = 1000

    for i in range(okreg_kodowy_1, okreg_kodowy_2):
        for j in range(strefa_kodowa_1, strefa_kodowa_2):
            while len(str(j)) < 3:
                j = "0" + str(j)
            lista_kodow.append(str(i) + "-" + str(j))
        strefa_kodowa_1 = 0
        strefa_kodowa_2 = int(kod_2[3:])

    print(lista_kodow)


def brakujace_elementy():
    wejscie = [2, 3, 7, 4, 9], 10
    lista_jeden_minus_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_wejscie, roznica = wejscie

    roznica = list(set(lista_jeden_minus_n) - set(lista_wejscie))

    print(roznica)


def lista_liczb():
    wygenerowana_lista = [i / 10.0 for i in range(20, 60, 5)]

    print(wygenerowana_lista)


if __name__ == "__main__":
    main()
