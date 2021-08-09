from abs.religions import religion
from chapitres.classes import fondateur
from abs import situation
from abs.humanite import metier
from abs.univers import temps
from spe import portrait_fondateur
from abs.humanite import portrait

class SituationFondateur(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 435500)

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_fondateur.PortraitFondateur()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)
