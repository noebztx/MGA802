import random

# Ouvrir le fichier en mode lecture
with open("mots_pendu.txt", 'r') as f:
    # Lire le contenu du fichier
    mots = f.read().split()


# Fonction pour choisir un mot au hasard
def choisir_mot(mots):
    return random.choice(mots)


def affichage(mot_aleatoire, lettres_proposees):
    affichage = ''
    for lettre in mot_aleatoire:
        if lettre in lettres_proposees:
            affichage += lettre + ' '
        else:
            affichage += '_ '
    return affichage


def lettre_input():
    lettre = input("Entrez une lettre : ")
    return lettre.lower()


def play_game(file_name):
    mot_aleatoire = choisir_mot(mots)
    lettres_proposees = set()
    chances = 6

    while chances > 0:
        print("Mot actuel :", affichage(mot_aleatoire, lettres_proposees))

        lettre = lettre_input()

        if lettre not in mot_aleatoire:
            chances -= 1
        else:
            lettres_proposees.add(lettre)

        if set(mot_aleatoire) == lettres_proposees:
            print("Félicitations ! Vous avez deviné le mot :", mot_aleatoire)
            break

        print("Chances restantes :", chances)

    if chances == 0:
        print("Dommage ! Vous avez épuisé toutes vos chances. Le mot était :", mot_aleatoire)


# Exécution du jeu
play_game('mots_pendu.txt')
