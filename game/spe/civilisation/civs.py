import random
from spe.civilisation import celtes
from spe.civilisation import civ

class CollectionCivs:

    def __init__(self):
        self.lCivs_ = dict()

        francais = civ.Francais()
        self.SetCiv(civ.Francais.NOM, francais)
        christianisme = civ.Christianisme()
        self.SetCiv(civ.Christianisme.NOM, christianisme)
        nordique = civ.Nordique()
        self.SetCiv(civ.Nordique.NOM, nordique)
        germanique = civ.Germanique()
        self.SetCiv(civ.Germanique.NOM, germanique)
        phenicien = civ.Phenicien()
        self.SetCiv(civ.Phenicien.NOM, phenicien)
        arabe = civ.Arabe()
        self.SetCiv(civ.Arabe.NOM, arabe)
        juive = civ.Juive()
        self.SetCiv(civ.Juive.NOM, juive)
        grecque = civ.Grecque()
        self.SetCiv(civ.Grecque.NOM, grecque)
        celteObj = celtes.Celte()
        self.SetCiv(celtes.Celte.NOM, celteObj)

    def __getitem__(self, idCiv):
        # assert not idPeuple in self.lPeuples_, u"Pas de peuple '{}'".format(idPeuple)
        return self.lCivs_[idCiv]

    def __setitem__(self, idCiv, civ):
        self.SetCiv(idCiv, civ)

    def SetCiv (self, idCiv, civ):
        self.lCivs_[idCiv] = civ

    def __len__(self):
        return len(self.lCivs_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lCivs_) == 0:
            return "Aucune civilisation."
        str = u"Liste de toutes les civilisations : "
        for civ in self.lCivs_:
            str = str + civ + ","
        return str
