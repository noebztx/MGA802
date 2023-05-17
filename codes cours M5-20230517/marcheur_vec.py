# Fonction pour obtenir le chemin d'un marcheur aleatoire
# Avec Numpy

import numpy as np
from numpy.random import default_rng


def marcheur_aleatoire(nb_pas):
    """
    :param nb_pas: Nombre de pas que le marcheur parcourt
    :return: L'ensemble des positions qu'il a parcouru
    """
    # initialisation
    pos0 = 0

    # generateur de nombres aleatoires
    rng = default_rng() 
    
    # generation des pas aleatoires
    pas = rng.integers(-1,2,size=nb_pas)

    chemin = pos0 + np.cumsum(pas)

    return chemin