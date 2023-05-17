# Ce code met en place un jeu de pendu où l'utilisateur doit deviner un mot en proposant des lettres.
# Il a 6 chances pour deviner correctement toutes les lettres du mot.
# importe le module random utilisé pour générer des nombres aléatoires
import random

# Ouvrir le fichier en mode lecture
with open("mots_pendu.txt", 'r') as f:
    # Lit le contenu du fichier
    mots = f.read().split()


# Fonction pour choisir un mot au hasard
def choisir_mot(mots):
    # renvoie un mot choisi au hasard parmi la liste lue
    return random.choice(mots)

# Fonction pour afficher les lettres trouvées
def affichage(mot_aleatoire, lettres_proposees):
    affichage = ''
    # parcourt chaque lettre du mot
    for lettre in mot_aleatoire:
        # si la lettre du mot fait partie des lettres proposées, elle est affichée
        if lettre in lettres_proposees:
            affichage += lettre + ' '
        else:
            # les lettres non trouvées sont affichées par des underscores
            affichage += '_ '
    return affichage

# Fonction pour entrer une lettre
def lettre_input():
    lettre = input("Entrez une lettre : ")
    # renvoie la lettre en minuscules
    return lettre.lower()

# Fonction qui lance le jeu
def play_game(file_name):
    # choisi un mot aléatoire
    mot_aleatoire = choisir_mot(mots)
    # initialise un ensemble vide pour stocker les lettres proposées
    lettres_proposees = set()
    # nombre de chances
    chances = 6

    # tant que chances est supérieure à 0, while s'exécute
    while chances > 0:
        print("Mot actuel :", affichage(mot_aleatoire, lettres_proposees))

        lettre = lettre_input()

        # Si la lettre entrée n'est pas dans le mot choisi chances est décrémentée de 1
        if lettre not in mot_aleatoire:
            chances -= 1
        # sinon la lettre est ajoutée à l'ensemble lettres_proposees
        else:
            lettres_proposees.add(lettre)

        # si toutes les lettres sont trouvées le jeu est gagné
        if set(mot_aleatoire) == lettres_proposees:
            print("Félicitations ! Vous avez deviné le mot :", mot_aleatoire)
            break

        print("Chances restantes :", chances)

    # si toutes chances sont épuisées le jeu est perdu
    if chances == 0:
        print("Dommage ! Vous avez épuisé toutes vos chances. Le mot était :", mot_aleatoire)


# Exécution du jeu
play_game('mots_pendu.txt')
