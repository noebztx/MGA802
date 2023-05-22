import numpy as np
import matplotlib.pyplot as plt


# Fonction pour calculer les coordonnées du profil NACA
def coordonnees_naca(naca, corde, nombre_points, distribution):
    t = int(naca[2:]) / 100

    if distribution == "linéaire" or distribution == "L":
        xc = np.linspace(0, corde, nombre_points)
    if distribution == "non-uniforme" or distribution == "U":
        xc = 0.5 * (1 - np.cos(np.linspace(0, np.pi, nombre_points)))

    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)

    x = xc * corde
    yup = yt * corde
    ydown = -yt * corde

    return x, yup, ydown


# Fonction pour calculer l'épaisseur maximale et sa position
def calculer_epaisseur_max(yup, ydown, corde):
    epaisseurs = yup - ydown
    indice_max = np.argmax(epaisseurs)
    position_max = corde * indice_max / len(yup)
    epaisseur_max = np.max(epaisseurs)
    return epaisseur_max, position_max


# Demande les entrées à l'utilisateur
naca = input("Numéro du profil NACA 4 chiffres symétrique : ")
corde = float(input("Corde du profil (en mètre) : "))
nombre_points = int(input("Nombre de points le long de la corde : "))
distribution = input("Type de distribution de points linéaire (L) ou non-uniforme (U) : ")

# Calcul les cordonnées suivant les paramètres entrés par l'utilisateur
x, yup, ydown = coordonnees_naca(naca, corde, nombre_points, distribution)

# Calcule l'épaisseur maximale et sa position
epaisseur_max, position_max = calculer_epaisseur_max(yup, ydown, corde)

# Affiche les résultats
print("Épaisseur maximale :", epaisseur_max)
print("Position du maximum :", position_max)

# Trace le profil NACA calculé
plt.plot(x, yup, label="Extrados")
plt.plot(x, ydown, label="Intrados")
plt.xlabel("Position le long de la corde (m)")
plt.ylabel("Déviation de la corde (m)")
plt.title("Profil NACA " + naca)
plt.grid(True)
plt.legend()
plt.show()
