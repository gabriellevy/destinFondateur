import random

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

    def SelectionDePeuple(self, situation):
        """
        changements de caracs quand on sélectionne ce peuple
        """
        situation[Region.C_REGION] = self.nom_

class SudFrance(Region):

    NOM = u"Sud de la France"

    def __init__(self):
        self.nom_ = SudFrance.NOM

class CollectionRegions:

    def __init__(self):
        self.lRegions_ = dict()

        sudFrance = SudFrance()
        self.SetRegion(SudFrance.NOM, sudFrance)

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
