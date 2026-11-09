# BITKA Z ZMAJEM — 1. NADGRADNJA  (★)
# NOVO: kritični udarec, omejeno število napojev, opozorilo pri napačnem vnosu,
#       življenja ne morejo preseči 100.

import random

igralec = 100
zmaj = 100
napoji = 3         # NOVO: zdraviš se lahko samo 3-krat

print("=== BITKA Z ZMAJEM ===")
print("Pred tabo stoji ogromen zmaj!")

while igralec > 0 and zmaj > 0:
    print()
    print("Ti:", igralec, "| Zmaj:", zmaj, "| Napoji:", napoji)
    izbira = input("1 = napad, 2 = napoj: ")

    if izbira == "1":
        udarec = random.randint(10, 20)
        # NOVO: 1 proti 10 možnosti za kritični udarec (dvojna škoda)
        if random.randint(1, 10) == 1:
            udarec = udarec * 2
            print("KRITIČNI UDAREC!")
        zmaj = zmaj - udarec
        print("Udaril si zmaja za", udarec)

    elif izbira == "2":
        if napoji > 0:
            napoji = napoji - 1
            igralec = igralec + 25
            if igralec > 100:          # NOVO: več kot 100 ne gre
                igralec = 100
            print("Spil si napoj. Življenja:", igralec)
        else:
            print("Nimaš več napojev! Izgubil si potezo.")

    else:
        # NOVO: napačen vnos -> vprašamo znova, zmaj ne napade
        print("Vpiši 1 ali 2!")
        continue

    if zmaj > 0:
        ogenj = random.randint(5, 15)
        igralec = igralec - ogenj
        print("Zmaj bruha ogenj! Izgubiš", ogenj)

print()
if igralec > 0:
    print("ZMAGA! Premagal si zmaja!")
else:
    print("Zmaj je zmagal ... Poskusi znova!")
