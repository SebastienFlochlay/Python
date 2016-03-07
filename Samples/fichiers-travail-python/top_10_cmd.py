
"""
    Top 10 des sites visités, version ligne de commande
"""

import sys
import pathlib
import sqlite3
import collections

# Récupération du chemin vers le dossier de profile
try:
    dossier_de_profile = pathlib.Path(sys.argv[1])
except IndexError:
    sys.exit("Vous devez passer un dossier de profile en paramètre")

historique = dossier_de_profile / "places.sqlite"

# Vérifier que le fichier d'historique existe
if not historique.is_file():
    sys.exit("Impossible de trouver ce fichier : " + str(historique))

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
    print("-", site, ":", compte)