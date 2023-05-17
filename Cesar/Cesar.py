import string
alphabet = string.ascii_lowercase

# Ouvrir le fichier en mode lecture
with open("message.txt", 'r') as f:
    # Lire le contenu du fichier
    contenu = f.read()

a = int(input("Entrez la clé :"))
encrypte = ""

for k in contenu:
    if k in alphabet:
        encrypte += alphabet[(alphabet.find(k)+a) % 26]
    else:
        encrypte += k

print(encrypte)
# On crée un fichier txt et on écrit dedans
with open("message_encrypte.txt", "w") as fichier:
    fichier.write(encrypte)
