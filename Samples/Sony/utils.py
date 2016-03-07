"""
    Contain some usefull tools.
"""

def demo(a, b):
    """Demo function"""
    return (a + b)

def demo2(*nombres):
    """ Retourne la moyenne de tous les paramètres """
    if not nombres:
        raise ValueError("Vous devez passer au moins un paramètre")
    return sum(nombres) / len(nombres)
