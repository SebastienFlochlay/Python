
"""
    Contient des outils pour gérer des classes
    d'école.
"""


def moyenne(*nombres):
    """ Retourne la moyenne de tous les paramètres """
    if not nombres:
        raise ValueError("Vous devez passer au moins un paramètre")
    return sum(nombres) / len(nombres)


def moyenne(a, b=0, *args, c=True, **nombres):
    print(a, b, args, c, nombres)


def censure(entree, sortie, **substitutions):
    """ Censure les mots d'un fichier texte. """

    # ouverture des fichiers
    with open(entree) as source, open(sortie, 'w') as dest:
        # lecture du fichier d'origine ligne à ligne
        for ligne in source:
            # remplacement des mots pour chaque ligne
            for mot, remplacement in substitutions.items():
                ligne = ligne.replace(mot, remplacement)

            # ecriture du fichier de destination
            dest.write(ligne)


def listing(iterable, *, bullet="- "):
    """ Retourne une chaine représentant un listing.

        Le listing affiche les elements de l'itérable
        un par un, ligne par ligne, annotés par des
        tirets
    """
    items = []
    # parcours de tous les éléments de l'itérable
    for element in iterable:
        # formatage des éléments via un template
        # puis ajout dans la liste
        items.append("%s%s" % (bullet, element))

    # fusion de toutes les chaines de la liste
    # avec des sauts de ligne
    return "\n".join(items)


def mots(*fichiers):
    """ Génère les mots contenus dans ces fichiers """

    # déclaration d'un tuple contenant la ponctuation 
    # à retirer
    ponctuation = (";", ",", ".", ":", "«", "»", 
                   "'", "—", "?", "!", "-", "'")

    # pour chaque chemin de fichier
    for chemin in fichiers:
        # ouverture du fichier
        with open(chemin) as f:
            # parcours du fichier ligne à ligne
            for ligne in f:
                # retrait de la poncturation et mise en 
                # minuscule
                for signe in ponctuation:
                    ligne = ligne.lower().replace(signe, "")
                    # récupération des mots et sortie de chaque
                    # mot un par un
                    for mot in ligne.split():
                        yield mot
                    