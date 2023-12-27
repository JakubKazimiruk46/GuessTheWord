#losowanie slowa
import random

slownik = open("slowa.txt", "r" ,encoding="utf-8")

def losowanie_slowa():
    caly_slownik = slownik.read()
    slowa = list(map(str, caly_slownik.split("\n")))
    return(random.choice(slowa))

def podpowiedz(ukryte_slowo, zgadywanka, dlugosc, ile_zgadl):
    aktualna_podpowiedz = ""

    for i in range(dlugosc):
       try:
            if ukryte_slowo[i] == zgadywanka[i] or ukryte_slowo[i] == ile_zgadl[i]:
                aktualna_podpowiedz += ukryte_slowo[i]
            else:
                aktualna_podpowiedz += "_"
            aktualna_podpowiedz += " "
       except:
           aktualna_podpowiedz += " _"
    return aktualna_podpowiedz


def czy_zgadl(ukryte_slowo, ile_prob):
    ile_zgadl = ""
    dlugosc_slowa = len(ukryte_slowo)
    print(f"Wylosowales {dlugosc_slowa} literowe slowo")

    i = 0
    while i < ile_prob:
        print(f"Prob: {ile_prob-i}")
        odpowiedz = input("Podaj swoja odpowiedz: ")
        print("")

        if odpowiedz == ukryte_slowo:
            print("Brawo!")
            print("")
            break

        else:
            print("Nie tym razem, ale lap podpowiedz ;)")
            ile_zgadl = podpowiedz(ukryte_slowo, odpowiedz, dlugosc_slowa, ile_zgadl)
            #print(podpowiedz(ukryte_slowo, odpowiedz, dlugosc_slowa, ile_zgadl))
            print(ile_zgadl)
            print("")
            i+=1
    print(f"Slowo ktore musiales odgadnac to: {ukryte_slowo}")