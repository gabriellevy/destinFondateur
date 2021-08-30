import random
from spe.region import geo

class Region:
    """
    approximations d'emplacement dans le monde, très simplificatrices
    """
    C_REGION = u"Région" # région principale du peuple

    def __init__(self):
        self.nom_ = u"pas de nom de région, doit être overridé"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return u"Région : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{}".format(self.nom_)

    def SelectionDeRegion(self, situation):
        """
        changements de caracs quand on sélectionne ce peuple
        """
        situation[Region.C_REGION] = self.nom_
