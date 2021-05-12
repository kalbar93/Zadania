import pickle

class Firma:

    def __init__(self, nazwa, miejscowosc , rodzaj_firmy):
        self.__nazwa = nazwa
        self.__miejscowosc = miejscowosc
        self.__rodzaj_firmy = rodzaj_firmy
        self.ilePracownikow = 0

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def miejscowosc(self):
        return self.__miejscowosc

    @property
    def rodzaj_firmy(self):
        return self.__rodzaj_firmy

    @nazwa.setter
    def nazwa(self, nazwa):
        self.__nazwa = nazwa

    @miejscowosc.setter
    def miejscowosc(self, miejscowosc):
        self.__miejscowosc = miejscowosc

    @rodzaj_firmy.setter
    def rodzaj_firmy(self, rodzaj_firmy):
        self.__rodzaj_firmy = rodzaj_firmy


    def   __str__(self):
        return(f"Nazwa Firmy: {self.__nazwa} Miejscowość: {self.__miejscowosc} Rodzaj Firmy: {self.__rodzaj_firmy}")


class FirmaController:

    def __init__(self):
        self.listaFirm = []


    def dodajFirme(self, nazwa ,miejscowosc,rodzaj_firmy):
        plikFirmy = open("listaFirmy.dat", "ab")

        firma = Firma(nazwa,miejscowosc,rodzaj_firmy)
        self.listaFirm.append(firma)

        pickle.dump(self.listaFirm, plikFirmy)
        plikFirmy.close()

    def usunFirme(self,nazwa):
        plikFirmy = open("listaFirmy.dat", "ab")
        plikPracownicy = open("ilePracowników.dat" , "ab")

        for i in self.listaFirm:
            if (i.nazwa == nazwa):

                if(i.ilePracownikow == 0):
                    self.listaFirm.remove(i)
                    print("Firma zostałą usunieta")
                else:
                    print("Firma zawiera pracowników.Nie można usunąć.Upewnij się że firma nie ma pracowników żeby usunąć.")

                break

        pickle.dump(self.listaFirm, plikFirmy)
        plikFirmy.close()
        plikPracownicy.close()


    def pokazFirmy(self):
        plikFirmy = open("listaFirmy.dat", "ab")


        for i in self.listaFirm:
            print(i)

        pickle.dump(self.listaFirm, plikFirmy)
        plikFirmy.close()


class Pracownik:
    def __init__(self, imie ,nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.zatrudnienie = []

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @imie.setter
    def imie(self, imie):
        self.__imie = imie

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def   __str__(self):
        return(f"Imię: {self.__imie} Nazwisko: {self.__nazwisko} ")


class PracownikController(FirmaController): # Dlaczego nie Pracwonik

    def __init__(self):
        super().__init__()
        self.listaPracownikow = []

    def dodajPracownika(self,imie, nazwisko):
        plikPracownicy = open("listaPracownicy.dat" , "ab")

        pracownik = Pracownik(imie,nazwisko)
        self.listaPracownikow.append(pracownik)

        pickle.dump(self.listaPracownikow, plikPracownicy)
        plikPracownicy.close()


    def usunPracownika(self,nazwisko):
        plikPracownicy = open("listaPracownicy.dat", "ab")

        for i in self.listaPracownikow:
            if (i.nazwisko == nazwisko):
                self.listaPracownikow.remove(i)
                break

        pickle.dump(self.listaPracownikow, plikPracownicy)
        plikPracownicy.close()

    def pokazPracownikow(self):
        plikPracownicy = open("listaPracownicy.dat", "ab")

        for i in self.listaPracownikow:
            print(i)

        plikPracownicy.close()




class Zatrudnienie(PracownikController):

    def __init__(self):
        super().__init__() #?

    def przypiszFirme(self, nazwisko, nazwa):

        plikPracownicy = open("listaPracownicy.dat", "ab")
        plikFirmy = open("listaFirmy.dat", "ab")

        for i in self.listaPracownikow:
            if (i.nazwisko == nazwisko):

                for j in self.listaFirm:
                    if (j.nazwa == nazwa):
                        i.zatrudnienie.append(j)
                        j.ilePracownikow += 1
                        break

        pickle.dump(self.listaPracownikow, plikPracownicy)
        plikPracownicy.close()
        pickle.dump(self.listaFirm, plikFirmy)
        plikFirmy.close()




    def usunFirmePracownikowi(self, nazwisko, nazwa):

        plikPracownicy = open("listaPracownicy.dat", "ab")
        plikFirmy = open("listaFirmy.dat", "ab")

        for i in self.listaPracownikow:
            if (i.nazwisko == nazwisko):

                for j in self.listaFirm:
                    if (j.nazwa == nazwa):
                        i.zatrudnienie.remove(j)
                        j.ilePracownikow -= 1
                        break

        pickle.dump(self.listaPracownikow, plikPracownicy)
        plikPracownicy.close()
        pickle.dump(self.listaFirm, plikFirmy)
        plikFirmy.close()

    def wyswietlZatrudnieniePracownika(self, nazwisko):

        plikPracownicy = open("listaPracownicy.dat", "ab")

        for i in self.listaPracownikow:
            if (i.nazwisko == nazwisko):

                for j in i.zatrudnienie:
                    print(j)

        pickle.dump(self.listaPracownikow, plikPracownicy)
        plikPracownicy.close()

class App(Zatrudnienie):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):

        while True:
                modul = int(input("Wybierz moduł: 1 - Firmy, 2 - Pracownicy, 3 - Zatrudnienie, 4 - Koniec"))

                if(modul == 1):

                    while(True):
                        menu = int(input("1 - Dodaj firme, 2 - Usuń firmę, 3 - Pokaz firmy - 4 - Koniec"))

                        if menu == 1:
                            nazwa = input("Podaj nazwe firmy: ")
                            miejscowosc = input("Podaj miasto firmy: ")
                            rodzaj = input("Podaj rodzaj firmy: ")

                            self.dodajFirme(nazwa, miejscowosc, rodzaj)

                        elif menu==2:
                            nazwa = input("Podaj nazwe firmy do usunięcia: ")
                            self.usunFirme(nazwa)

                        elif menu==3:
                             self.pokazFirmy()

                        elif menu==4:
                             break

                elif (modul == 2):

                    while (True):
                        menu = int(input("1 - Dodaj pracownika, 2 - Usuń pracownika, 3 - Pokaz pracownikow - 4 - Koniec"))

                        if menu == 1:
                            imie = input("Podaj imie: ")
                            nazwisko = input("Podaj nazwisko: ")
                            self.dodajPracownika(imie, nazwisko)

                        elif menu == 2:
                            nazwisko = input("Podaj nazwisko pracownika do usunięcia: ")
                            self.usunPracownika(nazwisko)

                        elif menu == 3:
                            self.pokazPracownikow()

                        elif menu == 4:
                            break

                elif (modul == 3):

                    while (True):
                        menu = int(input("1 - Przypisz firmę do pracownika, 2 - Usuń firmę pracownikowi, 3 - Wyswietl zatrudnienie pracownika - 4 - Koniec"))

                        if menu == 1:
                            nazwisko = input("Podaj nazwisko: ")
                            nazwa = input("Podaj nazwe firmy: ")
                            self.przypiszFirme(nazwisko, nazwa)

                        elif menu == 2:
                            nazwisko = input("Podaj nazwisko: ")
                            nazwa = input("Podaj nazwe firmy: ")
                            self.usunFirmePracownikowi(nazwisko, nazwa)

                        elif menu == 3:
                            nazwisko = input("Podaj nazwisko: ")
                            self.wyswietlZatrudnieniePracownika(nazwisko)

                        elif menu == 4:
                            break

                elif (modul == 4):
                    break



firma = App()