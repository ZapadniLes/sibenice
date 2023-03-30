import random

  
with open("./slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovo = print(random.choice(slova))

