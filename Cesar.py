import string
alphabet = string.ascii_lowercase

# Ouvrir le fichier en mode lecture
#with open("message.txt", 'r') as f:
    # Lire le contenu du fichier
    # contenu = f.read()
contenu = f.read()
a = int(input("Entrez la clé :"))
encrypte = ""

for k in [contenu]:
    encrypte.append = alphabet[alphabet.find(k)+a]

# On crée un fichier txt et on écrit dedans
with open("message_encrypte.txt", "w") as fichier:
    fichier.write(encrypte)
