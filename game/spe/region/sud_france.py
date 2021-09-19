from spe.region import geo
from spe.region import region

class SudFrance(region.Region):
    """
    Ne correspond pas à l'aquitaine mais seulement à la côté méditérannéenne, le bord des pyrénnées
    et environ 200 km vers l'intérieur des terres
    """

    NOM = u"Gaule narbonnaise" # en théorie on pourrait faire varier le nom selon l'époque mais pas trop envie de me prendre la tête avec ça pour l'instant

    # caracs liées aux voisins :
    C_RAPPORT_MASSILIA = u"Rapports avec Massilia" # 0 = haîne, 1. = alliance
    C_RAPPORT_AVATIQUES = u"Rapports avec les Avatiques" # 0 = haîne, 1. = alliance
    C_RAPPORT_SALYENS = u"Rapports avec les Salyens" # 0 = haîne, 1. = alliance

    def __init__(self):
        self.nom_ = SudFrance.NOM

    def SelectionDeRegion(self, situation):
        region.Region.SelectionDeRegion(self, situation)
        situation.SetValCarac(geo.Geo.C_COTIERE, "1")
        situation.SetValCarac(SudFrance.C_RAPPORT_MASSILIA, 0.4) # valeur de base à la rencontre ??
        situation.SetValCarac(SudFrance.C_RAPPORT_AVATIQUES, 0.7) # valeur de base à la rencontre ??

    def GetForet(self):
        forets = ["Forêt des cèdres du Luberon", "Forêt des Dentelles de Montmirail", "Forêt de l'Esterel",
        "Forêt des Maures", "Forêt de Menton", "Forêt du Mont-Ventoux",
        "Forêt du Tanneron", "Forêt de la Sainte-Baume"]
        return random.choice(forets)
