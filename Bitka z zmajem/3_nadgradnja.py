# BITKA Z ZMAJEM — 3. NADGRADNJA  (★★★)
# NOVO: lastne funkcije, pošasti kot slovarji, izbira junaka,
#       točke in rekord, shranjen v datoteko rekord.txt

import random
import os

# NOVO: vsaka pošast je slovar — podatki so zbrani skupaj in imajo imena
posasti = [
    {"ime": "Goblin", "hp": 40,  "moc": 8,  "nagrada": 10},
    {"ime": "Ork",    "hp": 60,  "moc": 12, "nagrada": 20},
    {"ime": "Trol",   "hp": 90,  "moc": 16, "nagrada": 30},
    {"ime": "Zmaj",   "hp": 130, "moc": 22, "nagrada": 0},
]

# NOVO: junaki imajo različne lastnosti
junaki = {
    "1": {"ime": "Bojevnik", "hp": 120, "min": 10, "max": 18, "napoji": 2},
    "2": {"ime": "Čarovnik", "hp": 80,  "min": 14, "max": 26, "napoji": 3},
    "3": {"ime": "Lokostrelec", "hp": 100, "min": 8, "max": 22, "napoji": 2},
}


def izberi_junaka():
    """Vpraša igralca, katerega junaka želi, in vrne njegov slovar."""
    print("Izberi junaka:")
    for kljuc in junaki:
        j = junaki[kljuc]
        print(kljuc, "=", j["ime"], "(življenja", str(j["hp"]) + ", udarec",
              str(j["min"]) + "-" + str(j["max"]) + ")")
    while True:
        izbira = input("Izbira: ")
        if izbira in junaki:
            return dict(junaki[izbira])   # kopija, da ne spreminjamo izvirnika
        print("Vpiši 1, 2 ali 3!")


def napad(junak):
    """Izračuna, koliko škode naredi junak. Vrne število."""
    udarec = random.randint(junak["min"], junak["max"]) + junak["mec"]
    if random.randint(1, 10) == 1:
        print("KRITIČNI UDAREC!")
        udarec = udarec * 2
    return udarec


def bitka(junak, posast):
    """Ena bitka. Vrne True, če junak zmaga, in False, če izgubi."""
    hp = posast["hp"]
    while junak["zivljenja"] > 0 and hp > 0:
        print()
        print(junak["ime"] + ":", junak["zivljenja"], "|", posast["ime"] + ":", hp,
              "| Napoji:", junak["napoji"])
        izbira = input("1 = napad, 2 = napoj: ")
        if izbira == "1":
            udarec = napad(junak)
            hp = hp - udarec
            print("Udaril si za", udarec)
        elif izbira == "2":
            if junak["napoji"] > 0:
                junak["napoji"] -= 1
                junak["zivljenja"] = min(junak["zivljenja"] + 25, junak["hp"])
                print("Spil si napoj. Življenja:", junak["zivljenja"])
            else:
                print("Nimaš več napojev! Izgubil si potezo.")
        else:
            print("Vpiši 1 ali 2!")
            continue

        if hp > 0:
            skoda = random.randint(posast["moc"] // 2, posast["moc"])
            junak["zivljenja"] -= skoda
            print(posast["ime"], "te napade! Izgubiš", skoda)
    return junak["zivljenja"] > 0


def trgovina(junak):
    """Trgovina med bitkami. Spreminja slovar junaka."""
    while True:
        print()
        print("--- TRGOVINA --- (zlato:", str(junak["zlato"]) + ")")
        print("1 = napoj (15)   2 = meč +5 škode (25)   3 = naprej")
        nakup = input("Izbira: ")
        if nakup == "1" and junak["zlato"] >= 15:
            junak["zlato"] -= 15
            junak["napoji"] += 1
            print("Kupil si napoj. Napoji:", junak["napoji"])
        elif nakup == "2" and junak["zlato"] >= 25:
            junak["zlato"] -= 25
            junak["mec"] += 5
            print("Kupil si meč! Bonus škoda:", junak["mec"])
        elif nakup == "3":
            return
        else:
            print("Tega ne moreš kupiti (premalo zlata?).")


def preberi_rekord():
    """Prebere rekord iz datoteke. Če datoteke še ni, je rekord 0."""
    if os.path.exists("rekord.txt"):
        with open("rekord.txt") as f:
            return int(f.read())
    return 0


def shrani_rekord(tocke):
    with open("rekord.txt", "w") as f:
        f.write(str(tocke))


# ===================== GLAVNI PROGRAM =====================
print("=== BITKA Z ZMAJEM ===")
rekord = preberi_rekord()
print("Trenutni rekord:", rekord, "točk")
print()

junak = izberi_junaka()
junak["zivljenja"] = junak["hp"]
junak["zlato"] = 0
junak["mec"] = 0
tocke = 0

for i, posast in enumerate(posasti):
    print()
    print("========== Pred tabo je", posast["ime"].upper(), "==========")
    if not bitka(junak, posast):
        break
    print()
    print("Premagal si:", posast["ime"] + "!")
    tocke += posast["hp"]                 # točke = koliko življenj si odvzel
    junak["zlato"] += posast["nagrada"]
    if i < len(posasti) - 1:
        trgovina(junak)

print()
if junak["zivljenja"] > 0:
    print("ZMAGA! Premagal si vse pošasti in zmaja!")
    tocke += junak["zivljenja"] * 2       # bonus za preostala življenja
else:
    print("Padel si v boju ...")

print("Tvoje točke:", tocke)
if tocke > rekord:
    print("NOV REKORD!")
    shrani_rekord(tocke)
else:
    print("Rekord je še vedno", rekord)
