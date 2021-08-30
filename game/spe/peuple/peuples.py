from spe.peuple import peuple
from spe.peuple import celtes_sud_france

class CollectionPeuples:

    def __init__(self):
        self.lPeuples_ = dict()

        celtesSudFrance = celtes_sud_france.CeltesSudFrance()
        self.SetPeuple(celtes_sud_france.CeltesSudFrance.NOM, celtesSudFrance)

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
