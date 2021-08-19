import random
from spe.region import region
from spe.civilisation import civ

class Peuple:
    C_PEUPLE = u"Peuple"
    # caracs variables de peuple
    C_POP = u"Population"
    C_COHESION = u"Cohésion"
    # souveraineté
    C_SOUV = u"Souveraineté"
    # ------------- val de souveraineté
    TRIBUE = u"Tribu"
    # caracs principale d'identité de peuple
    C_VIOLENCE = u"Violence"
    C_CREATIVITE = u"Creativité"
    C_AVENTURE = u"Aventure" # peuple qui ne se satisfait aps de ce qu'il a mais cherche toujours à aller plus loin (inclut donc l'ambition)
    C_INTEL = u"Intellectualisme" # Les écrivains, intellectuels et philosophes sont respectés. La ruse est plus acceptée
    C_LEGALISME = u"Légalisme"
    C_SENSUALITE = u"Sensualité" # peuples où la recherche du plaisir des sens au sens large est un but avoué de la vie
    C_SPIRITUALITE = u"Spiritualité" # Appréciation des superstitions, religions, ésotérismes, la magie
    C_COOPERATION = u"Coopération" # Facilité à s'entendre avec les autres peuples et à coopérer avec eux (inclut tolérance)
    C_LIBERTE = u"Liberté" # Peuple qui sont fiers de leur liberté, de leurs droits. L'esclavagey est mal vu et moins brutal
    C_ARGENT = u"Argent" # La richesse est très valorisée et au coeur des coutumes
    C_SEXISME = u"Sexisme" # Niveau de différence de traitement entre les sexes

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
        situation.SetValCarac(Peuple.C_COHESION, 1)
        situation.SetValCarac(Peuple.C_SOUV, Peuple.TRIBUE)

class CeltesSudFrance(Peuple):

    NOM = u"Avatiques"

    def __init__(self):
        self.nom_ = CeltesSudFrance.NOM
        self.labelDepart_ = "choix_peuple_avatiques"

    def SelectionDePeuple(self, situation):
        """
        changements de caracs quand on sélectionne ce peuple
        """
        # début en -600:
        situation.AvanceDeXJours(400 * 365)
        Peuple.SelectionDePeuple(self, situation)
        civilisationDepart = civ.Celte()
        situation[civilisationDepart.nom_] = 1
        regionObj = situation.collectionRegions[region.SudFrance.NOM]
        regionObj.SelectionDeRegion(situation)
        situation[Peuple.C_PEUPLE] = civilisationDepart.GenererNomPeuple()

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
