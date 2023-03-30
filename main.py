import random
  
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovo = random.choice(slova)

pismeno = input("Jaké písmeno hádáš: ")


