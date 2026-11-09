# BITKA Z ZMAJEM — 2. NADGRADNJA  (★★)
# NOVO: več pošasti zapored (seznami + zanka for), zlato za vsako zmago,
#       trgovina med bitkami (meč in napoji).



napoj = 5


while:

    if izbira = ZDRAVLJENJE:
        if napoj > 0:
            napoj = napoj - 1






















import random

# NOVO: seznami — na istem mestu (indeksu) so podatki iste pošasti
imena = ["Goblin", "Ork", "Trol", "Zmaj"]
zivljenja = [40, 60, 90, 130]
moc = [8, 12, 16, 22]          # največja škoda, ki jo naredi pošast
nagrade = [10, 20, 30, 0]      # zlato za zmago

igralec = 100
napoji = 2
zlato = 0
mec = 0                        # NOVO: bonus škoda, ki jo kupiš v trgovini

print("=== BITKA Z ZMAJEM ===")
print("Da prideš do zmaja, moraš premagati vse njegove služabnike!")

for i in range(len(imena)):
    posast = imena[i]
    hp = zivljenja[i]
    print()
    print("========== Pred tabo je", posast.upper(), "==========")

    # --- BITKA ---
    while igralec > 0 and hp > 0:
        print()
        print("Ti:", igralec, "|", posast + ":", hp, "| Napoji:", napoji)
        izbira = input("1 = napad, 2 = napoj: ")

        if izbira == "1":
            udarec = random.randint(10, 20) + mec
            if random.randint(1, 10) == 1:
                udarec = udarec * 2
                print("KRITIČNI UDAREC!")
            hp = hp - udarec
            print("Udaril si za", udarec)
        elif izbira == "2":
            if napoji > 0:
                napoji = napoji - 1
                igralec = min(igralec + 25, 100)
                print("Spil si napoj. Življenja:", igralec)
            else:
                print("Nimaš več napojev! Izgubil si potezo.")
        else:
            print("Vpiši 1 ali 2!")
            continue

        if hp > 0:
            skoda = random.randint(moc[i] // 2, moc[i])
            igralec = igralec - skoda
            print(posast, "te napade! Izgubiš", skoda)

    # --- PO BITKI ---
    if igralec <= 0:
        break                      # NOVO: izgubil si -> ne gremo naprej

    print()
    print("Premagal si:", posast + "!")
    zlato = zlato + nagrade[i]

    # NOVO: trgovina (ne po zadnji pošasti)
    if i < len(imena) - 1:
        print("Dobiš", nagrade[i], "zlatnikov. Imaš jih", zlato)
        while True:
            print()
            print("--- TRGOVINA --- (zlato:", str(zlato) + ")")
            print("1 = napoj (15 zlatnikov)")
            print("2 = boljši meč, +5 škode (25 zlatnikov)")
            print("3 = naprej v boj")
            nakup = input("Izbira: ")
            if nakup == "1" and zlato >= 15:
                zlato = zlato - 15
                napoji = napoji + 1
                print("Kupil si napoj. Napoji:", napoji)
            elif nakup == "2" and zlato >= 25:
                zlato = zlato - 25
                mec = mec + 5
                print("Kupil si meč! Bonus škoda:", mec)
            elif nakup == "3":
                break
            else:
                print("Tega ne moreš kupiti (premalo zlata?).")

print()
if igralec > 0:
    print("ZMAGA! Premagal si vse pošasti in zmaja!")
else:
    print("Padel si v boju ... Poskusi znova!")
