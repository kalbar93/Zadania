import pymysql


try:
    conn = pymysql.connect(host="127.0.0.1" ,user="root" , password="Sqlpass11", database="DB93",charset="utf8" )
    c= conn.cursor()

    print("Połączenie z bazą danych poprawne")

except:
    print("Błąd połączenia")


def dodaj(imie,nazwisko,pensja):

    c.execute(f"insert into pracownicy(Imie, Nazwisko, Pensja) values ('{imie}','{nazwisko}',{pensja})")

    decyzja = input("Czy wykonać operację: T/N").upper()

    if decyzja == "T":
        conn.commit()
        print("Dane zostały dodane!")
    else:
        conn.rollback()
        print("Dane anulowane")

def wyswietl():
    c.execute("select * from Pracownicy")
    dane = c.fetchall()

    for  i in dane:
        print(f"ID:{i[0]}  Imię:{i[1]} Nazwisko: {i[2]}, Pensja: {i[3]}" )



def usun(nazwisko):
    c.execute(f"select * from Pracownicy where nazwisko = '{nazwisko}'")
    dane = c.fetchall()
    print(dane)
    id = dane[0][0]

    c.execute(f"DELETE FROM Pracownicy WHERE idPracownicy = {id}")

    decyzja = input("Czy wykonać operację: T/N").upper()

    if decyzja == "T":
        conn.commit()
        print("Dane zostały usunięte!")
    else:
        conn.rollback()
        print("Dane anulowane")


def zmien(nazwisko,noweImie,noweNazwisko,nowaPensja):
    c.execute(f"SELECT * FROM Pracownicy WHERE Nazwisko='{nazwisko}'")
    dane = c.fetchall()
    id = dane[0][0]
    c.execute(f"UPDATE Pracownicy SET Imie ='{noweImie}' , Nazwisko='{noweNazwisko}' , Pensja={nowaPensja} WHERE idPracownicy={id}")


    decyzja = input("Czy wykonać operację: T/N").upper()

    if decyzja == "T":
        conn.commit()
        print("Dane zostały zmienione!")
    else:
        conn.rollback()
        print("Dane anulowane")

def wyszkaj(fraza):
    c.execute(f"SELECT * FROM Pracownicy WHERE imie LIKE'%{fraza}%' OR nazwisko LIKE '%{fraza}%' ")
    dane = c.fetchall()
    for i in dane:
        print(f"ID: {i[0]} Imię: {i[1]} Nazwisko {i[2]} Pensja {i[3]}")

while (True):

    menu = int(input("1-dodaj, 2-wyswietl, 3-usun, 4-zmien, 5-wyszukaj, 6-koniec"))

    if (menu == 1):
        # imie, nazwisko, pensja

        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        pensja = int(input("Podaj pensję: "))

        dodaj(imie, nazwisko,pensja)

    elif (menu == 2):

        wyswietl()


    elif (menu == 3):
        # nazwisko
        nazwisko = input("Podaj nazwisko pracownika do usunięcia: ")
        usun(nazwisko)

    elif (menu == 4):
        # nazwisko, noweImie, nopweNazwisko, nowaPensja

        nazwisko = input("Podaj nazwisko osoby której dane chcesz zmienic: ")
        noweImie = input("Podaj nowe imię: ")
        noweNazwisko =input("Podaj nowe nazwisko: ")
        nowaPensja = int(input("Podaj nową pensje: "))

        zmien(nazwisko,noweImie,noweNazwisko,nowaPensja)

    elif (menu == 5):
        # fraza szukania (imie oraz nazwisko)
        fraza= input("Szukana fraza: ")

        wyszkaj(fraza)
    elif (menu == 6):
        conn.close()
        print("Koniec programu")
        break
    else:
        print("Błedna opcja menu")



