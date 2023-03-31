import random
import sibenice
import os
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovos = str(random.choice(slova))

delka= len(slovos)
print("Slovo má tolik písmen: ", delka)
chyba=0
odpovedi=""


#print(slovos)
#print(hadanka)

while(chyba != 8):
    scan=0
    poprava=sibenice.obesenec[chyba]
    pismeno = input("Jaké písmeno hádáš: ")
    for i in slovos:

        odpovedi=odpovedi+pismeno        
        if i in odpovedi:
           #scan= scan+1
           print(i, end="")
        else:
            print("_", end="")
            scan = scan+1

    if scan == 0:
        print("\n", "Gratuluji uhádl jsi dané slovo (" + slovos + ") a vyhrál jsi.")
        break


    if pismeno not in slovos:
        chyba=chyba+1




    print("\n", "počet chyb: ", chyba)
    print(poprava)