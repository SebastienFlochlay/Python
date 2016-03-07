
# on import le module pathlib
import pathlib

# on créé un objet Path à partir du chemin du dossier
# qu'on souhaite parcourir
dossier = pathlib.Path("/home/elephorm/Bureau")

# on créé un dictionnaire qui va contenir le compte
# de chaque mot que nous allons rencontrer
stats = {}

# on itère sur tous les fichiers présents dans ce dossier
for chemin in dossier.iterdir():

	# on ouvre chaque fichier
	fichier = open(str(chemin))

	# on lit son contenu, et on le met en minuscule
	texte = fichier.read().lower()

	# on retire toute la ponctuation
	ponctuation = (";", ",", ".", ":", "«", "»", "'", "—", "?", "!", "-")
	for signe in ponctuation:
		texte = texte.replace(signe, "")

	# on sépare les mots les uns des autres et on parcour
	# les mots un par un
	for mot in texte.split():

		# ignorer les mots trop petits
		if len(mot) >= 2:

			# on incrémente des compteurs des mots au fur
			# et à mesure qu'on les rencontre
			if mot in stats:
				stats[mot] = stats[mot] + 1
			else:
				stats[mot] = 1


# on initilise les variables qui vont être attachés
# au mot le plus utilisé
mot_le_plus_utilise = None
score_max = 0

# on itère sur notre dictionnaire
for mot, score in stats.items():

	# si jamais le mot de ce tour de boucle
	# a un score plus grand que tous les mots
	# précédement rencontrés
	if score > score_max:
		score_max = score
		mot_le_plus_utilise = mot

# on affiche le gagnant
print(mot_le_plus_utilise, "est le mot le plus utilisé avec un score de :", score_max)

