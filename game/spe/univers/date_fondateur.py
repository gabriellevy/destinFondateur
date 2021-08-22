import random
from abs.univers import temps

class DateFondateur(temps.Date):
    """
    commence en -1000 d'où un décalage d'années
    """

    def __init__(self, nbJours = None):
        if nbJours is None:
            self.nbJours_ = 40000 + random.randint(0, 40000) # nombre de jours semi aléatoire pour destin extermis
        else:
            self.nbJours_ = nbJours # nombre de jours depuis
        self.numJourGregorien = -1
        self.numMoisGregorien = -1
        self.dateDepartAvantJC_ = -1000 # début du calendrier en -1000
        self.CalculerJourEtMoisGregorien()

    def GetNbAnnees(self):
        return self.nbJours_/365 + self.dateDepartAvantJC_
