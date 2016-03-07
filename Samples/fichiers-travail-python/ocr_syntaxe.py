# -*- coding: latin-1 -*-
##########################
# Création d'une syntaxe #
# ---------------------- #
# Auteur : Suzy          #
# Crée le : 02/07/2010   #
##########################

# Utile pour vérifier l'existence d'un fichier :
import os

# Petite interface textuelle :
print("*******************************\n" +
      "* Exemple de syntaxe simple : *\n" +
      "*******************************")

# Demander le nom du projet :
nomProjet = input("Donnez un nom à votre projet : ")

# Demander le nom du fichier à utiliser :
nomFichier = input("Quel fichier voulez-vous utiliser ? ")
while not os.path.exists(nomFichier) :
    print("Ce fichier n'existe pas !")
    nomFichier = input("Quel fichier voulez-vous utiliser ? ")

# Ouvrir le fichier :
fichier = open(nomFichier,"r")
numeroLigne = 1
# Lire le fichier :
for ligne in fichier :
    # On retire le caractère de fin de ligne :
    ligne = ligne.replace("\n","")
    #On retire les commentaires de la lignes :
    ligne = ligne.split("#")[0]
    # On ne considère pas les lignes vides :
    if ligne != "" :
        if numeroLigne == 1 :
            # On retire tous les espaces :
            ligne = ligne.replace(' ','')
            # On sépare les opérations :
            operations = ligne.split(',')
        elif numeroLigne == 2 :
            # On sépare les nombres :
            premiersNombres = ligne.split(' ')
            # On retire tous les espaces de trop :
            while '' in premiersNombres :
                premiersNombres.remove('')
        elif numeroLigne == 3 :
            # On retire les crochets et les espaces et on sépare les nombres : 
            deuxiemesNombres = ligne.replace(' ','').replace("[","").replace("]","").split(',')
        numeroLigne += 1

#Fermer le fichier :
fichier.close()

# Pour chaque opération :
for operation in operations :
    # Associer un nom à chaque opération et ne pas faire la suite
    # si l'opération n'existe pas :
    if operation == '+' :
        nomOperation = 'addition'
    elif operation == '-' :
        nomOperation = 'soustraction'
    elif operation == '*' :
        nomOperation = 'multiplication'
    elif operation == '/' :
        nomOperation = 'division'
    elif operation == '%' :
        nomOperation = 'modulo'
    elif operation == '**' :
        nomOperation = 'puissance'
    elif operation == '//' :
        nomOperation = 'divisionEntiere'
    else :
        print("L'opération %s n'est pas reconnue : les fichiers ne seront pas générés !" % (operation))
        continue
    print("Génération des fichiers pour l'opération %s." % (operation))
    # Pour chacune des valeurs :
    for valeur in premiersNombres :
        # Création du fichier :  
        fichier = open('%s-%s-%s.txt' % (nomProjet,nomOperation,valeur), 'w')
        # Ecrire dans le fichier :
        for nombre in range(eval(deuxiemesNombres[0]),eval(deuxiemesNombres[1]),eval(deuxiemesNombres[2])) :
            if (operation == '/' or operation == '//' or operation == '%') and nombre == 0 :
                fichier.write("%s %s %s = impossible !\n" % (valeur.center(10), operation, str(nombre).center(10))) 
            else :
                fichier.write("%s %s %s = %f\n" % (valeur.center(10), operation, str(nombre).center(10), \
                                                                      eval(valeur+operation+str(nombre))))                
        # Fermer le fichier :
        fichier.close()
