import random
from spe.civilisation import civ

class Grecque(civ.Civ):
    """
    NOTE a faire : pourrait être divisé entre plusieurs cultures assez différentes (sparte, athêne, byzance, grecs actuel...)
    """
    NOM = u"Grecque"

    def __init__(self):
        self.nom_ = Grecque.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin grec PAS FAIT"
        return u"prénom féminin grec PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple grec PAS FAIT"

    def GenererNom(self):
        return u"nom grec PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Sage {}".format(nom)
