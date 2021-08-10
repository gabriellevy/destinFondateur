import random
from spe.peuple import region

class Peuple:
    C_PEUPLE = u"Peuple"
    # caracs principale d'identité de peuple
    C_VIOLENCE = u"Violence"

    def __init__(self):
        self.nom_ = u"pas de nom de peuple, doit être overridé"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return u"Peuple : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{}".format(self.nom_)

    def SelectionDePeuple(self, situation):
        """
        changements de caracs quand on sélectionne ce peuple
        """
        situation[Peuple.C_PEUPLE] = self.nom_

class CeltesSudFrance(Peuple):

    NOM = u"Celtes du sud de la France"

    def __init__(self):
        self.nom_ = CeltesSudFrance.NOM

    def SelectionDePeuple(self, situation):
        """
        changements de caracs quand on sélectionne ce peuple
        """
        Peuple.SelectionDePeuple(self, situation)
        situation[region.Region.C_REGION] = region.SudFrance.NOM

class CollectionPeuples:

    def __init__(self):
        self.lPeuples_ = dict()

        celtesSudFrance = CeltesSudFrance()
        self.SetPeuple(CeltesSudFrance.NOM, celtesSudFrance)

    def __getitem__(self, idPeuple):
        # assert not idPeuple in self.lPeuples_, u"Pas de peuple '{}'".format(idPeuple)
        return self.lPeuples_[idPeuple]

    def __setitem__(self, idPeuple, peuple):
        self.SetPeuple(idPeuple, peuple)

    def SetPeuple (self, idPeuple, peuple):
        self.lPeuples_[idPeuple] = peuple

    def __len__(self):
        return len(self.lPeuples_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lPeuples_) == 0:
            return "Aucun Peuple."
        str = u"Liste de toutes les peuples : "
        for peuple in self.lPeuples_:
            str = str + peuple + ","
        return str
