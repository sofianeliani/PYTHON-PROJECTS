import math

a = int(input("Saisissez a : "))
b = int(input("Saisissez b : "))
c = int(input("Saisissez c : "))
racineDeDelta = 0
retour = 0
delta = b**2 - 4*a*c

print(delta)

if delta > 0:
    racineDeDelta=math.sqrt(delta)
    retour = [(-b-racineDeDelta)/(2*a),(-b+racineDeDelta)/(2*a)]
    print(retour)
elif delta < 0:
    retour = []  #liste vide
    print("Pas de racine")
else:
    retour = [-b/(2*a)] #liste d'un seul élément
    print(retour)
