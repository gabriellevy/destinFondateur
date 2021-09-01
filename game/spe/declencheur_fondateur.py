from abs import proba
from abs import modifProba
from abs import condition
from abs import declencheur
from spe import situation_fondateur
from abs.univers import temps

class DeclencheurFondateur(declencheur.Declencheur):

    def EvtHistoArriveEntreDateAetB(self, dateA, dateB):
        """
        ajouteur de condition multiple pour événements historiques qui contient
         - la condition d'être en mode historique
         - la date minimum de l'evt
         - la date maximum de l'evt
        """
        estEnModeHisto1 = condition.Condition(situation_fondateur.SituationFondateur.C_MODE, situation_fondateur.SituationFondateur.C_MODE_HISTORIQUE, condition.Condition.EGAL)
        self.conditions_.append(estEnModeHisto1)
        supADateA = condition.Condition(temps.Date.DATE_ANNEES, dateA, condition.Condition.SUPERIEUR)
        self.conditions_.append(supADateA)
        infADateB = condition.Condition(temps.Date.DATE_ANNEES, dateB, condition.Condition.INFERIEUR)
        self.conditions_.append(infADateB)
