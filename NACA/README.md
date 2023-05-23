# Programme de génération et de tracé des profils NACA

Ce programme permet de générer les coordonnées et de tracer les profils NACA symétriques à 4 chiffres. Les profils NACA sont des formes d'aile utilisées en aérodynamique, caractérisées par des équations mathématiques paramétrées.

## Fonctionnalités

Le programme offre les fonctionnalités suivantes :

1. Demande à l'utilisateur de fournir le numéro du profil NACA, la corde du profil, le nombre de points le long de la corde et le type de distribution des points.
2. Calcule les coordonnées (x, yup, ydown) du profil NACA en utilisant les équations spécifiées.
3. Calcule l'épaisseur maximale et la position du maximum le long de la corde.
4. Affiche les résultats de l'épaisseur maximale et de la position du maximum.
5. Trace le profil NACA généré à l'aide de Matplotlib, en affichant à la fois l'extrados et l'intrados.
6. Personnalise le graphique avec une légende, un quadrillage, des étiquettes sur les axes et un titre.

## Prérequis

Pour exécuter ce programme, vous devez disposer des bibliothèques suivantes :

1. NumPy
2. Matplotlib

## Utilisation

Exécutez le fichier profil_naca.py à l'aide de Python 3.

Suivez les instructions affichées pour fournir les paramètres requis : numéro du profil NACA, corde du profil, nombre de points le long de la corde et type de distribution des points.

Les coordonnées du profil NACA seront calculées et les résultats de l'épaisseur maximale et de la position du maximum seront affichés.
Un graphique représentant le profil NACA sera généré et affiché à l'écran.