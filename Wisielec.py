import Start
import LosowanieSlowa

Start.wiadomosc_startowa()
ile_prob = Start.wybor_trudnosci()
ukryte_slowo = LosowanieSlowa.losowanie_slowa()
#print(ukryte_slowo)
LosowanieSlowa.czy_zgadl(ukryte_slowo, ile_prob)