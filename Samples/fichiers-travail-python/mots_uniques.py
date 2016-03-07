
# ouverture du fichier contenant le texte en lecture
fichier = open('/home/elephorm/Bureau/chanson.txt')
# récupération du texte, et mise en minuscule
texte = fichier.read().lower()
 
# remplacement de tous les signes de ponctuations par une chaine
# vide
ponctuation = (";", ",", ".", ":", "«", "»", "'", "—", "?", "!", "-")
for signe in ponctuation:
	texte = texte.replace(signe, "")

# découpage du texte, au niveau des espaces pour obtenir une liste
# de mots que l'on passe à un set
mots = set(texte.split())

# affichage du contenu du set
for mot in mots:
	print(mot)