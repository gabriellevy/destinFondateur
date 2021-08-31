import random
from spe.region import region
from spe.region import sud_france
from spe.civilisation import civ
from spe.civilisation import celtes

class Richesse:
    """
    liste des caracs de science (niveau approximatif de la civilisation en divers domaine)
    """
    # caracs liées à la richesse du peuple
    C_TRIBUS = u"Tribus" # rançons soutirées aux peuples voisins. SOuvent score élevé après des batailles gagnées mais diminue rapidement tous les ans
