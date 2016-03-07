#! /usr/bin/env python3.4

"""
    Top 10 des sites visités, version graphique
"""

import sys
import pathlib
import sqlite3
import collections

from tkinter import Tk, Frame, Text, filedialog, messagebox, END

# création de l'application
app = Tk()
app.title('10 sites les plus visités')

# création de la fenêtre et de son champ texte
fenetre = Frame(app)
zone_de_texte = Text(fenetre, height=20, width=40)
zone_de_texte.pack()
fenetre.pack()

# ouverture d'une invite à choisir un dossier
dossier_de_profile = filedialog.askdirectory()
if not dossier_de_profile:
    sys.exit(0)

historique = pathlib.Path(dossier_de_profile) / "places.sqlite"

# Vérifier que le fichier d'historique existe
if not historique.is_file():
    messagebox.showwarning(
        "Erreur", 
        "Impossible de trouver le fichier de l'historique"
    ) 
    sys.exit(0)

# Connection à la base de données
connexion = sqlite3.connect(str(historique))
curseur = connexion.cursor()

# requête pour récupérer, pour chaque visite, 
# le site visité
requete = """
SELECT moz_places.rev_host 
  FROM moz_historyvisits, moz_places 
 WHERE moz_places.id == moz_historyvisits.place_id
"""

resultat = curseur.execute(requete)

# on remet le nom du site dans le bon ordre, et
# on retire les "." et "www" superflux
g = (l[0][-2::-1].replace('www.', '') for l in resultat)

# le compteur compteur chaque visite pour nous
compteur = collections.Counter(g)

for site, compte in compteur.most_common(10):
    ligne = site + " : " + str(compte) + " visites \n"

    # insertin des visites dans la zone de texte
    zone_de_texte.insert(END, ligne)

# lancement de la partie graphique
app.mainloop()