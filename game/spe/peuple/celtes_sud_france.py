from spe.peuple import peuple
from spe.region import region
from spe.region import sud_france
from spe.civilisation import civ
from spe.civilisation import celtes
from spe.science import science

class CeltesSudFrance(peuple.Peuple):

    NOM = u"Celtes de la Gaule Narbonaise" # des Avatiques

    def __init__(self):
        self.nom_ = CeltesSudFrance.NOM
        self.labelDepart_ = "choix_peuple_avatiques"

    def SelectionDePeuple(self, situation):
        """
        changements de caracs quand on sélectionne ce peuple
        """
        # début en -600:
        situation.AvanceDeXJours(400 * 365)
        peuple.Peuple.SelectionDePeuple(self, situation)
        civilisationDepart = celtes.Celte()
        situation[civilisationDepart.nom_] = 1
        regionObj = situation.collectionRegions[sud_france.SudFrance.NOM]
        regionObj.SelectionDeRegion(situation)
        situation[peuple.Peuple.C_PEUPLE] = civilisationDepart.GenererNomPeuple()
        situation[science.Science.C_ECRITURE] = 0

        # caracs d'identité
        situation[peuple.Peuple.C_VIOLENCE] = 0.6
        situation[peuple.Peuple.C_CREATIVITE] = 0.3
        situation[peuple.Peuple.C_AVENTURE] = 0.3
        situation[peuple.Peuple.C_INTEL] = 0.1
        situation[peuple.Peuple.C_LEGALISME] = 0.1
        situation[peuple.Peuple.C_SENSUALITE] = 0.3
        situation[peuple.Peuple.C_SPIRITUALITE] = 0.5
        situation[peuple.Peuple.C_COOPERATION] = 0.2
        situation[peuple.Peuple.C_LIBERTE] = 0.3
        situation[peuple.Peuple.C_ARGENT] = 0.1
        situation[peuple.Peuple.C_SEXISME] = 0.3
        situation[peuple.Peuple.C_ENDURANCE] = 0.3
