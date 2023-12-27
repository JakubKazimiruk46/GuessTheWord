#Tutaj bêdzie sekwencja startowa
#TODO powtarzanie, podpowiedzi jesli pare pod rzad zle, poziom trudnosci z podzialem na dlugosc slow

from ast import Try
import random

def wiadomosc_startowa():
    print("""Czesc!

Masz przed soba gre polegajaca na zgadywaniu slowa, wybranego losowo przez komputer.
Wybierz poziom trudnosci:
1. Latwy (15 prob)
2. Sredni (10 prob)
3. Trudny (5 prob)

Powodzenia!
    """
    )

def wybor_trudnosci():
    try: 

        poziom_trudnosci = int(input("> "))
        
        if poziom_trudnosci == 1:
            return 15
        elif poziom_trudnosci == 2:
            return 10
        elif poziom_trudnosci == 3:
            return 5
        else:
            print("Nie rozumiem!")
    except:
        return 15