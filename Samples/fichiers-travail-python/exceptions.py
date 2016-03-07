
chemin = "chanson.txt"

# fragile
fichier = open(chemin)
print(fichier.read())
fichier.close()


# robuste mais verbeux
try:
    fichier = open(chemin)
except EnvironmentError as e:
    print("Impossible d'ouvrir le fichier :", e)
else:
	print(fichier.read())
finally:
	try:
		fichier.close()
	except NameError:
		pass

# robuste est plus court
try:
	with open(chemin) as fichier:
		print(fichier.read())
except EnvironmentError as e:
    print("Impossible d'ouvrir le fichier :", e)
