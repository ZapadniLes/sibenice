import random
import sibenice
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovos = str(random.choice(slova))

delka= len(slovos)
print(delka)
chyba=0
odpovedi=""


print(slovos)
#print(hadanka)

while(chyba != 7):
    scan=0
    poprava=sibenice.obesenec[chyba]
    pismeno = input("Jaké písmeno hádáš: ")
    for i in slovos:
            
        if i in odpovedi:
           #scan= scan+1
           print(i, end="")
        else:
            print("_", end="")
            scan = scan+1

    if scan ==0:
        break

    odpovedi=odpovedi+pismeno

    if pismeno not in slovos:
        chyba=chyba+1



    """if (scan>0):
        chyba=chyba+1"""



    print("\n", "počet chyb: ", chyba)
    print(poprava)


