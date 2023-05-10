# Ouvrir le fichier en mode lecture
with open("message. txt", ' r') as f:
    # Lire le contenu du fichier
    contenu = f.read()


a = input("Entrez la clé :")

# On crée un fichier txt et on écrit dedans
with open("message_encrypte.txt", "w") as fichier:
    fichier.write()