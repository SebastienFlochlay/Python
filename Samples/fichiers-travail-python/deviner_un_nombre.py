
# import du module random, spécialisé dans la génération
# de nombres aléatoires
import random

# on créé un nombre au hasard en 0 et 100
chiffre_secret = random.randint(0, 100)
# chiffre_secret = random.randint(0, 5)

# on initilise la variable réponse avec None
reponse = None
historique = []

# tant que la réponse est différente du chiffre secret,
# la boucle va continuer de tourner
while reponse != chiffre_secret:

	# on demande à l'utilisateur de devenir le chiffre
	# (on oublie pas de convertir la réponse en entier)
    reponse = int(input('Entrez un chiffre entre 0 et 100\n'))
    historique.append(reponse)

    # si l'essai de l'utilisateur est plus petit ou plus
    # grand que la réponse à deviner, on lui donne un 
    # indice
    if reponse > chiffre_secret:
        print('Le chiffre secret est plus petit que ça')
    elif reponse < chiffre_secret:
        print('Le chiffre secret est plus grand que ça')
    
# sinon, le bon chiffre est deviné
print('Gagné !')

taille = len(historique)
print("Vous avez gagné en", taille, "coups :")

for coup in historique:
    print('- ', coup)