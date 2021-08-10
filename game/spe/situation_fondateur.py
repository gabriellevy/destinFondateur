from abs.religions import religion
from spe.peuple import peuple
from abs import situation
from abs.humanite import metier
from abs.univers import temps
from spe import portrait_fondateur
from abs.humanite import portrait
from spe.peuple import peuple

class SituationFondateur(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 435500)
        self.collectionPeuples = None

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_fondateur.PortraitFondateur()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    def AffichagePeuple(self):
        return u"{}".format(self.caracs_[peuple.Peuple.C_PEUPLE])
