import random

list_pis = []
  
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovo = print(random.choice(slova))



pismeno = input("Jaké písmeno hádáš: ")