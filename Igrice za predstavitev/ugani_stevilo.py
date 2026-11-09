# 1. Računalnik si izmisli število
# 2. 












# UGANI ŠTEVILO
# Računalnik si izmisli skrito število, ti pa ga poskušaš uganiti.

import random

print("=== UGANI ŠTEVILO ===")
print("Izmislil sem si število od 1 do 100. Ali ga uganeš?")
print()

skrito = random.randint(1, 100)   # naključno število od 1 do 100
poskusi = 0
ugib = 0

# Zanka se ponavlja, dokler ugib ni enak skritemu številu
while ugib != skrito:
    vnos = input("Tvoje ugibanje: ")

    # Če nisi vpisal števila, te opozorimo in vprašamo znova
    if not vnos.isdigit():
        print("To ni število. Poskusi znova.")
        continue

    ugib = int(vnos)
    poskusi = poskusi + 1

    if ugib < skrito:
        print("Več!")
    elif ugib > skrito:
        print("Manj!")

print()
print("BRAVO! Skrito število je bilo", skrito)
print("Uganil si v", poskusi, "poskusih.")
