from abs.humanite import portrait
import random

class PortraitFondateur(portrait.Portrait):

    def DeterminerPortraits(self, situation, ageAnnees):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        portraits = []
        portraitCourant = situation.GetValCarac(portrait.Portrait.C_PORTRAIT)

        # if ageAnnees >= 30 and ageAnnees <= 40:
        #     portraits.append("images/portraits/clovis30_40.png")
        # elif ageAnnees > 40:
        #     portraits.append("images/portraits/clovis40+.png")
        # else:
        #     portraits.append("images/portraits/clovis15_30.png")
        portraits.append("images/portraits/celte20-40.png")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
