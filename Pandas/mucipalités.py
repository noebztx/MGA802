import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement du fichier traité
data = pd.read_csv('fichier_traité.csv')

# Filtrage des divisions de recensement correspondant aux municipalités
municipalites = data[data['Type'] == 'MÉ'].copy()  # créer une copie du DataFrame afin de résoudre l'erreur
# "SettingWithCopyWarning"

# Affichage du nombre de municipalités
nombre_municipalites = len(municipalites)  # le nombre de municipalités est égale à la taille de la variable
print("Nombre de municipalités :", nombre_municipalites)

population_moyenne_2016 = municipalites['Pop16'].mean()  # Calcul de la population moyenne en 2016
population_moyenne_2021 = municipalites['Pop21'].mean()  # Calcul de la population moyenne en 2021
print("Population moyenne en 2016 :", population_moyenne_2016)
print("Population moyenne en 2021 :", population_moyenne_2021)

municipalites.loc[:, 'accroissement'] = 100 * (municipalites['Pop21'] - municipalites['Pop16']) / municipalites[
    'Pop16']  # calcul de l'accroissement en %
# Le résultat est assigné à une nouvelle colonne appelée 'accroissement' dans le DataFrame 'municipalites'.

# Nuage de points : pourcentage d'accroissement de la population en fonction de la population en 2021
plt.scatter(municipalites['Pop21'], municipalites['accroissement'])
plt.xlabel('Population en 2021')
plt.ylabel('Accroissement de la population en %')
plt.title('Accroissement de la population en 2021 par rapport à 2016')
plt.show()

# Classification des municipalités en 5 catégories selon leur population en 2021
bins = [0, 2000, 10000, 25000, 100000, np.inf]  # Intervalle de population pour chaque catégorie
labels = ['<2000', '2000-9999', '10000-24999', '25000-99999', '100000+']  # Étiquettes des catégories
municipalites.loc[:, 'Population_categorie'] = pd.cut(municipalites['Pop21'], bins=bins, labels=labels)  # Le résultat
# est assigné à une nouvelle colonne appelée 'Population_categorie' dans le DataFrame 'municipalites'.

# Diagramme en barres horizontales du nombre de municipalités dans chaque catégorie
municipalites['Population_categorie'].value_counts().sort_index().plot(kind='barh')
plt.xlabel('Nombre de municipalités')
plt.ylabel('Catégorie de population')
plt.title('Répartition des municipalités par catégorie de population en 2021')
plt.show()
