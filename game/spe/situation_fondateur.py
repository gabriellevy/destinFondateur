from abs.religions import religion
from spe.peuple import peuple
from abs import situation
from abs.humanite import metier
from abs.univers import temps
from spe import portrait_fondateur
from abs.humanite import portrait
from spe.peuple import peuple
from spe.region import region
from spe.civilisation import civ
from spe.region import geo

class SituationFondateur(situation.Situation):

    # Mode de jeu actuel (fondateur ou historique)
    C_MODE = u"Mode"
    C_MODE_HISTORIQUE = u"Mode historique"
    C_MODE_FONDATEUR = u"Mode fondateur"

    def __init__(self):
        # date de départ = -1000 => l'affichage est trafiqué en fonction de ça (cf formatGregorienAvantJC)
        situation.Situation.__init__(self, 0)
        self.collectionPeuples = None
        self.collectionRegions = None
        self.collectionCivs = None
        self.SetValCarac(SituationFondateur.C_MODE, SituationFondateur.C_MODE_FONDATEUR)

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_fondateur.PortraitFondateur()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    def GetCivilisationDeReference(self):
        civPlusHaute = None
        valPlusHaute = 0
        for civK in self.collectionCivs.lCivs_.keys():
            valCiv = self.GetValCarac(civK)
            if valCiv != "" and valCiv > valPlusHaute:
                valPlusHaute = valCiv
                civPlusHaute = civK

        self.caracs_[civ.Civ.C_CIV] = civPlusHaute
        return self.collectionCivs.lCivs_[civPlusHaute]

    def DescriptionCivilisation(self):
        str=u""
        str = u"{}Influence de civilisation :".format(str)
        # niveau de civilisation :
        for civK in self.collectionCivs.lCivs_.keys():
            valCiv = self.GetValCarac(civK)
            if valCiv != "":
                str = u"{}\n{}({})".format(str, civK, valCiv)

        str = u"{}\n\nAffinités de civilisation :".format(str)
        # niveau d'affinité de civilisation :
        for civK in self.collectionCivs.lCivs_.keys():
            valCiv = self.GetValCarac(u"affinite{}".format(civK))
            if valCiv != "":
                str = u"{}\n{}({})".format(str, civK, valCiv)
        return str


    def AffichagePeuple(self):
        return u"{}".format(self.caracs_[peuple.Peuple.C_PEUPLE])

    def AffichageRegion(self):
        return u"{}".format(self.caracs_[region.Region.C_REGION])

    def AffichageReligion(self):
        return u"{}".format(self.caracs_[religion.Religion.C_RELIGION])

    def AffichagePopulation(self):
        return u"Population : {}".format(self.caracs_[peuple.Peuple.C_POP])

    def AfficherDebug(self):
        str = u"{} : {}".format(peuple.Peuple.C_COHESION, self.caracs_[peuple.Peuple.C_COHESION])
        str = u"{}\n\nIdentité de peuple : \n{} : {}".format(str, peuple.Peuple.C_VIOLENCE, self.caracs_[peuple.Peuple.C_VIOLENCE])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_CREATIVITE, self.caracs_[peuple.Peuple.C_CREATIVITE])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_INTEL, self.caracs_[peuple.Peuple.C_INTEL])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_LEGALISME, self.caracs_[peuple.Peuple.C_LEGALISME])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_SENSUALITE, self.caracs_[peuple.Peuple.C_SENSUALITE])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_SPIRITUALITE, self.caracs_[peuple.Peuple.C_SPIRITUALITE])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_COOPERATION, self.caracs_[peuple.Peuple.C_COOPERATION])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_LIBERTE, self.caracs_[peuple.Peuple.C_LIBERTE])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_ARGENT, self.caracs_[peuple.Peuple.C_ARGENT])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_SEXISME, self.caracs_[peuple.Peuple.C_SEXISME])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_AVENTURE, self.caracs_[peuple.Peuple.C_AVENTURE])

        str = u"{}\n{}".format(str, self.caracs_[peuple.Peuple.C_SOUV])
        return str

    def AfficherGeographie(self):
        str = u"{}".format(self.AffichageRegion())
        if self.GetValCarac(geo.Geo.C_COTIERE) == "1":
            str = u"{}\nCôtière".format(str)
        return str

    # DATES ET TEMPS QUI PASSE-----------------------------------------------------------------------------------------------------------
    def AffichageDate(self):
        nbJours = self.caracs_[temps.Date.DATE]
        dateDuJour = temps.Date(nbJours)
        dateStr = u"{}".format(dateDuJour.formatGregorienAvantJC(1000))
        return dateStr
