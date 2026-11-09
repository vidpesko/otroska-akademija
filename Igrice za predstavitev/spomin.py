# SPOMIN
# Na mizi je 12 obrnjenih kart, ki tvorijo 6 parov.
# Vsakič obrneš dve karti. Če sta enaki, ostaneta odprti.
# Cilj: odpreti vse pare v čim manj potezah.

import random
import time

# 6 parov črk -> 12 kart
karte = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"]
random.shuffle(karte)                  # premešamo karte

odprte = [False] * 12                  # na začetku so vse karte zaprte
poteze = 0
najdeni_pari = 0


def pokazi_mizo(prva=-1, druga=-1):
    """Izpiše mizo: odprte karte pokaže, zaprte so označene s številko."""
    print()
    for i in range(12):
        if odprte[i] or i == prva or i == druga:
            print("[ " + karte[i] + " ]", end=" ")
        else:
            print("[" + str(i + 1).rjust(2) + " ]", end=" ")
        if (i + 1) % 4 == 0:           # po 4 karte v vrsti
            print()
    print()


def izberi_karto(besedilo):
    """Vpraša za številko karte, dokler ne dobi pravilne."""
    while True:
        vnos = input(besedilo)
        if not vnos.isdigit():
            print("Vpiši številko od 1 do 12.")
            continue
        st = int(vnos) - 1
        if st < 0 or st > 11:
            print("Vpiši številko od 1 do 12.")
        elif odprte[st]:
            print("Ta karta je že odprta. Izberi drugo.")
        else:
            return st


print("=== SPOMIN ===")
print("Izberi dve karti s številko. Najdi vseh 6 parov!")

while najdeni_pari < 6:
    pokazi_mizo()
    prva = izberi_karto("Prva karta: ")
    druga = izberi_karto("Druga karta: ")
    while druga == prva:
        print("To karto si že izbral. Izberi drugo.")
        druga = izberi_karto("Druga karta: ")

    poteze = poteze + 1
    pokazi_mizo(prva, druga)

    if karte[prva] == karte[druga]:
        print("PAR! Odlično!")
        odprte[prva] = True
        odprte[druga] = True
        najdeni_pari = najdeni_pari + 1
    else:
        print("Ni par. Zapomni si, kje sta bili ...")
        time.sleep(3)
        print("\n" * 40)               # "pobrišemo" zaslon, da kart ne vidiš več

pokazi_mizo()
print("BRAVO! Našel si vse pare v", poteze, "potezah.")
