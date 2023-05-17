from math import *

a = float(input("Entrez le coefficient a: "))
b = float(input("Entrez le coefficient b: "))
c = float(input("Entrez le coefficient c: "))

delta_x = b**2 - 4*a*c

if delta_x > 0:
    x1 = (-b + sqrt(delta_x)) / (2*a)
    x2 = (-b - sqrt(delta_x)) / (2*a)
    print("Les racines réelles de l'équation sont:", x1, "et", x2)
elif delta_x == 0:
    x = -b / (2*a)
    print("La racine réelle de l'équation est:", x)
else:
    print("L'équation n'a pas de racines réelles.")
