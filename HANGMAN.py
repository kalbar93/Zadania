
litery= set()
haslo = input("Podaj haslo do odgadnięcia: ")

liczba_prob =5

while True:
    koniec = True

    for i in haslo:
        if i in litery:
            print(i , end=" ")
        else:
            print("-", end=" ")
            koniec = False

    if koniec == True:
        print("Koniec gry")
        break


    zgadywana_litera=input("Podaj litere: ")
    litery.add(zgadywana_litera)

    if (zgadywana_litera not in haslo):
        liczba_prob = liczba_prob - 1

    if liczba_prob == 0:
        print("Koniec gry")
        print("GAME OVER")
        break

