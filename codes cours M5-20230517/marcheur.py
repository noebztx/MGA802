# Fonction pour obtenir le chemin d'un marcheur aleatoire
# Python de base

from random import randint


def avance_marcheur(pos0):
    """
    Ajoute un pas aleatoire au marcheur
    :param pos0: position du marcheur
    :return: nouvelle position du marcheur
    """
    return pos0 + randint(-1,1)


def marcheur_aleatoire(nb_pas):
    """
    :param nb_pas: Nombre de pas que le marcheur parcourt
    :return: L'ensemble des positions qu'il a parcouru
    """
    # initialisation
    position = 0
    chemin = []

    for i in range(nb_pas):
        position = avance_marcheur(position)
        chemin.append(position)

    return chemin