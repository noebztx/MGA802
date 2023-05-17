from time import perf_counter
from marcheur import *

nb_pas = 500
tic = perf_counter()
marcheur_aleatoire(nb_pas)

toc = perf_counter()
print(f"Temps d'execution: {toc-tic} [s]")
