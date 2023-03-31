import random
import sibenice
hadanka=[]
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovos = random.choice(slova)

for letter in slovos:
    hadanka.append(letter)

delka= len(slovos)
print(delka)
chyba=0
scan=0

while(chyba!= delka):
    scan=0
    poprava=sibenice.obesenec[chyba]
    pismeno = input("Jaké písmeno hádáš: ")
    for i in hadanka:
            
        if (i != pismeno):
           scan=scan+1

    if (scan>0):
        chyba=chyba+1
    print(chyba)
    print(poprava)
            
    




