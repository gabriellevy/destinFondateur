from abs.religions import religion
from spe.peuple import peuple
from abs import situation
from abs.humanite import metier
from abs.univers import temps
from spe import portrait_fondateur
from abs.humanite import portrait
from spe.peuple import peuple
from spe.region import region
from spe.science import science
from spe.civilisation import civ
from spe.region import geo
from spe.univers import date_fondateur
import random
import logging

class SituationFondateur(situation.Situation):

    # Mode de jeu actuel (fondateur ou historique)
    C_MODE = u"Mode"
    C_MODE_HISTORIQUE = u"Mode historique"
    C_MODE_FONDATEUR = u"Mode fondateur"

    def __init__(self):
        situation.Situation.__init__(self, 0)
        date = date_fondateur.DateFondateur(0)
        self.caracs_[temps.Date.DATE] = date.nbJours_
        self.collectionPeuples = None
        self.collectionRegions = None
        self.collectionCivs = None
        self.listeCaracsIdentite_ = [peuple.Peuple.C_VIOLENCE, peuple.Peuple.C_CREATIVITE, peuple.Peuple.C_AVENTURE,
            peuple.Peuple.C_INTEL, peuple.Peuple.C_LEGALISME, peuple.Peuple.C_SENSUALITE, peuple.Peuple.C_SPIRITUALITE,
            peuple.Peuple.C_COOPERATION, peuple.Peuple.C_LIBERTE, peuple.Peuple.C_ARGENT, peuple.Peuple.C_SEXISME,
            peuple.Peuple.C_ENDURANCE]
        self.listeCaracsStructurePolitique_ = [ peuple.Peuple.C_CLASSE, peuple.Peuple.C_INDIVIDUALISME, peuple.Peuple.C_CLANIQUE,
            peuple.Peuple.C_FEODALE, peuple.Peuple.C_NATIONALITE, peuple.Peuple.C_THEOCRATIE ]
        self.SetValCarac(SituationFondateur.C_MODE, SituationFondateur.C_MODE_FONDATEUR)

    ############################ affichage ###########################
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
        """
        recalcule la civilisation de référence du peuple
        """
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

    def AffichageScience(self):
        str=u""
        # écriture :
        valEcriture = self.GetValCaracInt(science.Science.C_ECRITURE)
        if valEcriture < 0.2:
            str = u"{}\nAnalphabêtes".format(str)
        elif valEcriture < 0.5:
            str = u"{}\nAlphabêtisés".format(str)
        elif valEcriture < 0.5:
            str = u"{}\Litéraires".format(str)

        return str

    def AffichagePeuple(self):
        return u"{}".format(self.caracs_[peuple.Peuple.C_PEUPLE])

    def AffichageRegion(self):
        return u"{}".format(self.caracs_[region.Region.C_REGION])

    def AffichageReligion(self):
        return u"{}".format(self.caracs_[religion.Religion.C_RELIGION])

    def AffichagePopulation(self):
        return u"Population : {}".format(int(self.caracs_[peuple.Peuple.C_POP]))

    def AfficherDebug(self):
        str = u"{} : {}".format(peuple.Peuple.C_COHESION, self.caracs_[peuple.Peuple.C_COHESION])
        str = u"{}\n\nIdentité de peuple :".format(str)
        for carac in self.listeCaracsIdentite_:
            str = u"{}\n - {} : {}".format(str, carac, self.caracs_[carac])

        """
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_VIOLENCE, self.caracs_[peuple.Peuple.C_VIOLENCE])
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
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_ENDURANCE, self.caracs_[peuple.Peuple.C_ENDURANCE])
        str = u"{}\n - {} : {}".format(str, peuple.Peuple.C_CLASSE, self.caracs_[peuple.Peuple.C_CLASSE])
        str = u"{}\n{}".format(str, self.caracs_[peuple.Peuple.C_SOUV])
        """
        return str

    def AfficherGeographie(self):
        str = u"{}".format(self.AffichageRegion())
        if self.GetValCarac(geo.Geo.C_COTIERE) == "1":
            str = u"{}\nCôtière".format(str)
        return str

    # DATES ET TEMPS QUI PASSE-----------------------------------------------------------------------------------------------------------
    def GetDateDuJour(self):
        nbJours = self.caracs_[temps.Date.DATE]
        return date_fondateur.DateFondateur(nbJours)

    def GetDate(self, dateEnJours):
        """
        à overrider si la date du jeu destin a été overridée
        """
        return date_fondateur.DateFondateur(dateEnJours)

    def AvanceDeXJours(self, nbJoursPasses):
        situation.Situation.AvanceDeXJours(self, nbJoursPasses)

        # progression de la population :
        population = self.GetValCaracInt(peuple.Peuple.C_POP)
        popGagnee = (population * nbJoursPasses) / (365 * 100) # formule pour 1% par an

        # petit bonus pour les peuples sexistes (femmes moins éduquées et quasi obligées de procréer)
        sexisme = self.GetValCaracInt(peuple.Peuple.C_SEXISME)
        popGagnee = popGagnee * (0.75 + sexisme/2)

        # petit random :
        sexisme = self.GetValCaracInt(peuple.Peuple.C_SEXISME)
        popGagnee = popGagnee * (0.75 + random.uniform(0, 1.0)/2)

        popGagnee = int(popGagnee)
        self.AjouterACarac(peuple.Peuple.C_POP, popGagnee)

    def TourSuivant(self):
        """
        Passage au "tour" suivant dans un destin c'est à dire grosso modo
         - en mode fondateur : un mois un peu randomisé
         - en mode historique : un an un peu randomisé
        """
        nbJoursPasses = 200 + random.randint(0, 380)
        if self.EstEnModeFondateur():
            nbJoursPasses = 20 + random.randint(0, 20)
        self.AvanceDeXJours(nbJoursPasses)

    #--------------
    def EstEnModeFondateur(self):
        return self.GetValCarac(SituationFondateur.C_MODE) == SituationFondateur.C_MODE_FONDATEUR

    def GetRegion(self):
        return self.caracs_[region.Region.C_REGION]
