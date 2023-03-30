import random
import sibenice
hadanka=[]
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovos = random.choice(slova)

for letter in slovos:
    hadanka.append(letter)

delka= len(slovos)
chyba=0
scan=0
poprava=sibenice.obesenec[chyba]

while(chyba!= delka):

    pismeno = input("Jaké písmeno hádáš: ")
    for i in hadanka:
            
        if (i != pismeno):
           scan=scan+1
           if (scan>delka):
               chyba=chyba+1
        print(chyba)
    print(poprava)
            
    




