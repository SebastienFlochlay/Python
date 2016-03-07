# -*- coding: latin-1 -*-
#########################
# Juste Prix            #
# --------------------- #
# Créé : le 29/06/2010  #
# Auteur : Suzy         #
#########################

from random import randint

#Afficher l'interface :
print("-----------------\n" +
      "| Le Juste Prix |\n" +
      "-----------------\n" +
      "Choix de la difficulté :\n" +
      "1 - Entre 0 et 100\n" +
      "2 - Entre 0 et 1000\n" +
      "3 - Entre 0 et 10000\n" +
      "4 - Entre 0 et 100000")

#Laisser le choix de la difficulté à l'utilisateur :
difficulte = input()
while (difficulte != "1" and difficulte != "2" and
       difficulte != "3" and difficulte != "4") :
    print("Veuillez entrer quelque chose de correct !")
    difficulte = input()

#Initialiser les variables :
nbEssais = 0
reponse = -1
#Générer un nombre aléatoire :
if difficulte == "1" :
    aDeviner = randint(0, 100)
elif difficulte == "2" :
    aDeviner = randint(0, 1000)
elif difficulte == "3" :
    aDeviner = randint(0, 10000)
else :
    aDeviner = randint(0, 100000)

#Indiquer que le jeu à commencé :
print("Le jeu commence, alors combien ?")

#Boucle principale :
while reponse != aDeviner :
    nbEssais += 1
    #Vérifier qu'un nombre est bien donné :
    reponseEstUnNombre = False
    while not reponseEstUnNombre :
        reponse = input()
        try :
            reponse = eval(reponse)
            reponseEstUnNombre = True
        except :
            print("Vous devriez donner un nombre...")
    #Dire si c'est plus ou moins :
    if reponse < aDeviner :
        print("C'est plus !")
    elif reponse > aDeviner :
        print("C'est moins !")

#Terminer le jeu :
print("Bravo, vous avez trouvé la bonne réponse après",nbEssais, "essais !")
