from spe.region import region
from spe.region import sud_france

class CollectionRegions:

    def __init__(self):
        self.lRegions_ = dict()

        sudFrance = sud_france.SudFrance()
        self.SetRegion(sud_france.SudFrance.NOM, sudFrance)

    def __getitem__(self, idRegion):
        # assert not idPeuple in self.lPeuples_, u"Pas de peuple '{}'".format(idPeuple)
        return self.lRegions_[idRegion]

    def __setitem__(self, idRegion, region):
        self.SetRegion(idRegion, region)

    def SetRegion (self, idRegion, region):
        self.lRegions_[idRegion] = region

    def __len__(self):
        return len(self.lRegions_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lRegions_) == 0:
            return "Aucune Région."
        str = u"Liste de toutes les régions : "
        for region in self.lRegions_:
            str = str + region + ","
        return str
