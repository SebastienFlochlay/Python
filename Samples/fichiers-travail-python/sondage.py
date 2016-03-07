
# creation du dictionnaire
stats = {}
# initialisation de la reponse à None
reponse = None

# tant que la réponse n'est pas une chaîne vide
while reponse != "":

	# demander aux utilisateurs leurs couleurs préférées
	reponse = input('Quelle est votre couleur préférée ?\n')

	# si la dernière réponse n'est pas vide
	if reponse:

		# si la réponse existe dans le dico
		if reponse in stats:
			# incrément le score existant
			stats[reponse] = stats[reponse] + 1
		
		# si la réponse n'existe pas
		else:
			# mettre un score de 1
			stats[reponse] = 1

# afficher la liste des votes en itérant
# sur les paires clé/valeur du dictionnaire
print('Vote pour les couleurs :')
for couleur, score in stats.items():
	print("-", couleur, ":", score)