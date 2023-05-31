import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""Ce script demontre l'usage de pandas pour du nettoyage de donnees, des traces et des statistiques"""

filename = 'meteo_YUL_DLY_1972_2022.csv'

df_meteo = pd.read_csv(filename,index_col=0)
print(df_meteo.head())
print(df_meteo.shape)
print('Liste des champs:\n',list(df_meteo.columns))
print('\n')

# L,argument inplace permet de modifier la dataframe courante. 
# Sinon par defaut c'est la dataframe de sortie de la methode qui porte la modification

# On renomme les colonnes pour faciliter les appels
df_meteo.rename(columns={'Date/Time':'time','Mean Temp (°C)':'mean_temp',
                         'Min Temp (°C)':'min_temp','Max Temp (°C)':'max_temp',
                         'Total Precip (mm)': 'precip'},inplace=True)
# On ne garde que les colonnes qui nous interessent (celles avec des valeurs numeriques)
# On cherche donc les noms de colonnes qui ne sont pas dans notre short-list
columns_to_drop = df_meteo.columns[~np.in1d(df_meteo.columns,['time','mean_temp','min_temp','max_temp','precip'])]
# On supprime les colonnes identifiees 
df_meteo.drop(columns=columns_to_drop,inplace=True)
# On supprime les colonnes qui ne contiendraient que des NaN (argument all comme pour les fonctions numpy)
df_meteo.dropna(axis=1,how='all',inplace=True)
# On supprime les lignes dont les valeurs de temperatures sont des NaN (par exemple pour les mois dans le futur)
df_meteo.dropna(subset='mean_temp',axis=0,how='any',inplace=True)


# On convertit la date (chaine de caractere) en timestamp 
df_meteo.time = pd.to_datetime(df_meteo.time.values)
# On utilise cette colonne comme indice cela va permettre les manipulations suivantes.
df_meteo.set_index('time',inplace=True)
print('Liste des champs:\n',list(df_meteo.columns))
print('\n')

# Ici le trace des temperatures journalieres
df_meteo.plot(y=['min_temp','mean_temp','max_temp'])
plt.show()

# On peut realiser des reechantillonnages temporels tres facilement
df_year = df_meteo.resample('Y').mean()  # Moyenne annuelle
df_month = df_meteo.resample('M').mean() # Moyenne mensuelle
df_week = df_meteo.resample('7D').mean() # Moyenne hebdomadaire
# Pour tracer des donnees de plusieurs dataframe il faut 
ax = df_meteo.plot(y=['min_temp','mean_temp','max_temp'])
df_month.plot(ax=ax,y=['min_temp','mean_temp','max_temp'])
df_year.plot(ax=ax,y=['min_temp','mean_temp','max_temp'])
plt.show()

# On peut faire une moyenne glissante
# Cela conserve le meme echantillonnage que les donnes de debut
# Mais c'est consistant avec la moyenne hebdomadaire vue precedemment
# Mais il y a un delai
df_7days = df_meteo.rolling(7).mean()
df_week['time_shift'] = df_week.index + pd.Timedelta("7 day")
ax = df_7days.plot(y=['min_temp','mean_temp','max_temp'])
df_week.plot(ax=ax, x='time_shift',y=['min_temp','mean_temp','max_temp'])
plt.show()

# On peut sauvegarder en format binare la base de donne traitee
df_week.to_pickle('meteo_YUL_WKY_1972_2022.pkl')