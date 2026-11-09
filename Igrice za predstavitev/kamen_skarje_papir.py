# KAMEN, ŠKARJE, PAPIR
# Igraš proti računalniku. Kdor prvi zbere 3 točke, zmaga.

import random

moznosti = ["kamen", "škarje", "papir"]
moje_tocke = 0
racunalnik_tocke = 0

print("=== KAMEN, ŠKARJE, PAPIR ===")
print("Kamen zdrobi škarje, škarje prerežejo papir, papir zavije kamen.")
print("Kdor prvi zbere 3 točke, zmaga!")

while moje_tocke < 3 and racunalnik_tocke < 3:
    print()
    jaz = input("Izberi (kamen / škarje / papir): ").lower().strip()

    # Preverimo, ali je izbira pravilna
    if jaz not in moznosti:
        print("Tega ne poznam. Napiši kamen, škarje ali papir.")
        continue

    racunalnik = random.choice(moznosti)
    print("Računalnik je izbral:", racunalnik)

    if jaz == racunalnik:
        print("Neodločeno!")
    elif (jaz == "kamen" and racunalnik == "škarje") or \
         (jaz == "škarje" and racunalnik == "papir") or \
         (jaz == "papir" and racunalnik == "kamen"):
        print("Zmagal si krog!")
        moje_tocke = moje_tocke + 1
    else:
        print("Računalnik je zmagal krog.")
        racunalnik_tocke = racunalnik_tocke + 1

    print("Rezultat — ti:", moje_tocke, " računalnik:", racunalnik_tocke)

print()
if moje_tocke == 3:
    print("ČESTITAM, ZMAGAL SI IGRO!")
else:
    print("Tokrat je zmagal računalnik. Poskusi znova!")
