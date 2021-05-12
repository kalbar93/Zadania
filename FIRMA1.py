""""
Zaprojektuj aplikację dla firmy szkoleniowej, która będzie umożliwiała:
 Zdefiniowanie listy kursów
 Dodanie na wybrany kurs uczestnika
Kursy i kursanci powinny być obiektami.
Pola dla kursu: nazwa, miasto, termin
Pola dla uczestnika: imie, nazwisko, telefon, email
Menu: dodaj kurs, lista kursów, usuń kurs, dodaj uczestnika do kursu, usuń uczestnika z
kursu, lista uczestników na danym kursie
W programie ustalamy, że nazwy kursów oraz nazwiska uczestników się nie powtarzają i
stanowią element identyfikacyjny.
"""

class Kurs():

    def __init__(self, nazwa, miasto, termin):
        self.__nazwa = nazwa
        self.__miasto = miasto
        self.__termin = termin
        self.listaUczestnikow = []

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def miasto(self):
        return self.__miasto

    @property
    def termin(self):
        return self.__termin

    @nazwa.setter
    def nazwa(self,nazwa):
        self.__nazwa = nazwa

    @miasto.setter
    def miasto(self,miasto):
        self.__miasto = miasto

    @termin.setter
    def termin(self,termin):
        self.__termin = termin

    def __str__(self):
        return(f"Nazwa: {self.nazwa} Miasto: {self.miasto} itd...")

class Uczestnik():

    def __init__(self, imie, nazwisko, telefon, email):

        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__telefon = telefon
        self.__email = email

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def telefon(self):
        return self.__telefon

    @property
    def email(self):
        return self.__email

    @imie.setter
    def imie(self,imie):
        self.__imie = imie

    @nazwisko.setter
    def nazwisko(self,nazwisko):
        self._nazwisko = nazwisko

    @telefon.setter
    def telefon(self,telefon):
        self.__telefon = telefon

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return(f"Imię: {self.imie} Nazwisko: {self.nazwisko} itd...")

class HR():
    def __init__(self):
        self.listaKursow =[]

    def dodajKurs(self, nazwa, miasto, termin):

        kurs = Kurs(nazwa, miasto, termin)
        self.listaKursow.append(kurs)

    def usunKurs(self, nazwaKursu):

        for i in self.listaKursow:
            if i.nazwaKursu == nazwaKursu:
                self.listaKursow.remove(i)
                break

    def wyswietlListeKursow(self):

        for i in self.listaKursow:
            print(i)

    def dodajUczestnika(self, nazwaKursu, imie, nazwisko, telefon, email):

        for i in self.listaKursow:
            if i.nazwa == nazwaKursu:
                uczestnik = Uczestnik(imie, nazwisko, telefon, email)
                i.listaUczestnikow.append(uczestnik)


    def usunUczestnika(self,nazwaKursu, nazwisko):

        for i in self.listaKursow:
            if i.nazwa == nazwaKursu:
                for j in i.listaUczestnikow:
                    if j.nazwisko == nazwisko:
                        i.listaUczestnikow.remove(j)
                        break


    def listaUczestnikow(self, nazwaKursu):

        for i in self.listaKursow:
            if i.nazwa == nazwaKursu:
                for j in i.listaUczestnikow:
                    print(j)



class Firma(HR):

    def __init__(self, nazwaFirmy):
        super().__init__()
        self.nazwaFirmy = nazwaFirmy
        self.menu()

    def menu(self):

        print(f"Witaj w {self.nazwaFirmy}")
        while True:
            menu = input("D-dodaj Kurs, P-pokaz liste kursow, U-usun kurs,DU- dodaj uczestnika do kursu, UU- usun uczestnika z kursu,LU - listna uczestnikow na kursie , K-koniec").upper()

            if menu == "D":

                nazwaKursu = input("Podaj nazwe kursu: ")
                miasto = input("Podaj miejsce kursu(miasto): ")
                termin = input("Podaj termin kursu: ")
                self.dodajKurs(nazwaKursu, miasto, termin)

            elif menu == "P":

                self.wyswietlListeKursow()

            elif menu == "U":

                nazwaKursu = input("Podaj nazwe kursu do usunięcia: ")

                self.usunKurs(nazwaKursu)


            elif menu == "DU":

                nazwaKursu = input("Podaj nazwe kursu")
                imie = input("Podaj imie uczestnika: ")
                nazwisko = input("Podaj nazwisko uczestnika: ")
                telefon = int(input("Podaj telefon uczesnika: "))
                emial = input("Podaj email uczesnika: ")

                self.dodajUczestnika(nazwaKursu, imie, nazwisko, telefon, emial)

            elif menu == "UU":
                nazwaKursu = input("Podaj nazwe kursu: ")
                nazwisko = input("Podaj nazwiwsko do usuniecia z tego kursu: ")

                self.usunUczestnika(nazwaKursu, nazwisko)

            elif menu == "LU":
                nazwaKursu = input("Podaj nazwe kursu: ")

                self.listaUczestnikow(nazwaKursu)

            elif menu == "K":
                print("Koniec programu")
                break

            else:
                print("Nierozpoznana opcja !!!")
                print("Sprobuj jeszcze raz")


firma = Firma("Firma Szkoleniowa")
