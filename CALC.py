from tkinter import *


def wynik():
    dzialanie = wynikEntry.get()
    wynik = None
    if("+" in dzialanie):
        #print(11)
        dzialanieList = dzialanie.split("+")
        wynik = int(dzialanieList[0])+int(dzialanieList[1])
    elif ("-" in dzialanie):
        dzialanieList = dzialanie.split("-")
        wynik = int(dzialanieList[0]) - int(dzialanieList[1])
    elif ("*" in dzialanie):
        dzialanieList = dzialanie.split("*")
        wynik = int(dzialanieList[0]) * int(dzialanieList[1])
    elif ("/" in dzialanie):
        dzialanieList = dzialanie.split("/")
        wynik = int(dzialanieList[0]) / int(dzialanieList[1])

    wynikEntry.delete(0, END)
    wynikEntry.insert(0, wynik)

def click(value):
    if(value == "="):
        wynik()
    else:
        wynikEntry.insert(END, value)


def wyczyscB():
    wynikEntry.delete(0, END)



root= Tk()

root.title("Kalkulator - Zadanie domowe")
root.geometry("400x320")


wynikRamka = Frame(root,width=312, height=50)
wynikEntry = Entry(wynikRamka, font=('arial', 18, 'bold'), width=30, bg="#eee", justify=RIGHT)
ramkaKlawiatura = Frame(root , width = 400, height = 300)

wynikEntry.grid(row = 0 , column = 0 )
wynikRamka.grid(row = 0 ,column = 0)
ramkaKlawiatura.grid(sticky =W)

# rzad 1
przyciskWyczysc = Button(ramkaKlawiatura,text="C", width=45, height=3,command=lambda: wyczyscB())
przyciskWyczysc.grid(row=0, column=0, columnspan=4, padx=1, pady=1)


podziel  = Button(ramkaKlawiatura, text= "/", width=10, height=3,command=lambda: click("/"))
podziel.grid(row=1, column=3, padx=1, pady=1)

#rzad 2

siedem = Button(ramkaKlawiatura , text= "7",width=10, height=3,command=lambda: click("7"))
siedem.grid(row=1, column=0, padx=1, pady=1)

osiem = Button(ramkaKlawiatura , text= "8",width=10, height=3,command=lambda: click("8"))
osiem.grid(row=1, column=1, padx=1, pady=1)

dziewiec = Button(ramkaKlawiatura , text= "9",width=10, height=3,command=lambda: click("9"))
dziewiec.grid(row = 1 , column= 2 , padx = 1 , pady= 1)

mnozenie = Button(ramkaKlawiatura , text= "*",width=10, height=3,command=lambda: click("*"))
mnozenie.grid(row =2 , column = 3 , padx =1, pady=1)

#rzad 3

cztery = Button(ramkaKlawiatura , text= "4",width=10, height=3,command=lambda: click("4"))
cztery.grid(row =2 ,column= 0 ,padx=1,pady=1)

piec = Button(ramkaKlawiatura , text= "5",width=10, height=3,command=lambda: click("5"))
piec.grid(row =2 , column = 1 ,padx = 1, pady=1)

szesc = Button(ramkaKlawiatura , text= "6",width=10, height=3,command=lambda: click("6"))
szesc.grid(row=2,column= 2, padx=1, pady=1)

minus = Button(ramkaKlawiatura , text= "-",width=10, height=3,command=lambda: click("-"))
minus.grid(row=3,column=3,padx=1,pady=1)

#rzad 4

jeden =Button(ramkaKlawiatura , text= "1",width=10, height=3,command=lambda: click("1"))
jeden.grid(row=3,column=0,padx=1,pady=1)

dwa =Button(ramkaKlawiatura , text= "2",width=10, height=3,command=lambda: click("2"))
dwa.grid(row=3,column = 1,padx=1,pady=1)

trzy= Button(ramkaKlawiatura , text= "3",width=10, height=3,command=lambda: click("3"))
trzy.grid(row=3,column=2,padx=1,pady=1)

plus = Button(ramkaKlawiatura , text= "+",width=10, height=3,command=lambda: click("+"))
plus.grid(row=4,column=3,padx=1,pady=1)

#rzad 5

zero =Button(ramkaKlawiatura , text= "0",width=10, height=3,command=lambda: click("0"))
zero.grid(row=4,column=0,padx=1,pady=0)

kropka = Button(ramkaKlawiatura , text= ".",width=10, height=3,command=lambda: click("."))
kropka.grid(row=4,column=1,padx=1 ,pady=1)

rownosc= Button(ramkaKlawiatura , text= "=",width=10, height=3,command=lambda: click("="))
rownosc.grid(row=4,column=2,padx=1,pady=1)


root.mainloop()