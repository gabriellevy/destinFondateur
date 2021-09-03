import random
from spe.civilisation import civ

class Romain(civ.Civ):
    NOM = u"Romain"

    # caracs de liens avec cette civilisation par d'autres peuples
    C_RAPPORT_ROME = u"Rapports avec Rome" # 0 = haîne, 1. = alliance
    C_GUERRE = u"En guerre avec Rome"

    def __init__(self):
        self.nom_ = Romain.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin romain PAS FAIT"
        return u"prénom féminin romain PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple romain PAS FAIT"

    def GenererNom(self):
        return u"nom romain PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Pater {}".format(nom)
