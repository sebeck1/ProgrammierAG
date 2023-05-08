import random
import string

die_adjektive = ["schläfrig", "lahm", "stinkend", "fett", "rot", "orange", "gelb", "grün", "blau", "lila", "flauschig", "weiß", "stolz", "tapfer"]

die_nomen = ["Apfel", "Dinosaurier", "Kugel", "Taoster", "Ziege", "Drachen", "Hammer", "Ente", "Panda"]

print("Willkommen im Passwort-Generator!")

adjektiv = random.choice(die_adjektive)
nomen = random.choice(die_nomen)
zahl = random.randrange(0,100)
sonderz = random.choice(string.punctuation)

passwort = adjektiv + nomen + str(zahl) + sonderz

print("Das neue Password ist: %s" % passwort)

