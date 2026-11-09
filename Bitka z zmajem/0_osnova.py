# BITKA Z ZMAJEM — OSNOVA
# Ti in zmaj se izmenično napadata. Kdor prvi ostane brez življenj, izgubi.

# 1. Ustvari spremenljivki `igralec` in `zmaj`, ki bosta vsebovali začetno število življenj (100).

# 2. Ustvari zanko, ki se bo izvajala, dokler imata oba še življenja.


# 3. V zanki izpiši trenutno število življenj obeh.


# 4. Uporabniku ponudi izbiro: napad ali zdravljenje. Če izbere napad, naj se zmaju odšteje naključno število življenj med 10 in 20. Če izbere zdravljenje, naj se igralcu doda 15 življenj.


# 5. Če je zmaj še živ, naj se izvede njegova poteza: zmaj bruha ogenj in igralcu odšteje naključno število življenj med 5 in 15.


# 6. Ko eden od igralcev ostane brez življenj, izpiši, kdo je zmagal.


# 7. Za naključna števila uporabi funkcijo `randint` iz modula `random`.


import random


stevilo = random.randint(1, 2)




igralec = 100      # tvoja življenja
zmaj = 100         # zmajeva življenja

print("=== BITKA Z ZMAJEM ===")
print("Pred tabo stoji ogromen zmaj!")

while igralec > 0 and zmaj > 0:
    print()
    print("Ti:", igralec, "| Zmaj:", zmaj)
    izbira = input("1 = napad, 2 = zdravljenje: ")

    # TVOJA POTEZA
    if izbira == "1":
        udarec = random.randint(10, 20)
        zmaj = zmaj - udarec
        print("Udaril si zmaja za", udarec)
    elif izbira == "2":
        igralec = igralec + 15
        print("Pozdravil si se za 15.")

    # ZMAJEVA POTEZA (samo, če je še živ)
    if zmaj > 0:
        ogenj = random.randint(5, 15)
        igralec = igralec - ogenj
        print("Zmaj bruha ogenj! Izgubiš", ogenj)

print()
if igralec > 0:
    print("ZMAGA! Premagal si zmaja!")
else:
    print("Zmaj je zmagal ... Poskusi znova!")
