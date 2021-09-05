import random
from spe.region import region
from spe.region import sud_france
from spe.civilisation import civ
from spe.civilisation import celtes
from spe.science import science

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
    # C_VIOLENCE celtes 0.6 moins de 0.3 = non violent au point de facilement collaborer et payer des rançons
    C_VIOLENCE = u"Violence"
    C_CREATIVITE = u"Creativité"
    C_AVENTURE = u"Aventure" # peuple qui ne se satisfait pas de ce qu'il a mais cherche toujours à aller plus loin (inclut donc l'ambition et aussi la curiosité)
    # C_INTEL celtes 0.1
    C_INTEL = u"Intellectualisme" # Les écrivains, intellectuels et philosophes sont respectés. La ruse est plus acceptée aussi. => favorise la science
    C_LEGALISME = u"Légalisme"
    C_SENSUALITE = u"Sensualité" # peuples où la recherche du plaisir des sens au sens large est un but avoué de la vie
    C_SPIRITUALITE = u"Spiritualité" # Appréciation des superstitions, religions, ésotérismes, la magie
    C_COOPERATION = u"Coopération" # Facilité à s'entendre avec les autres peuples et à coopérer avec eux (inclut tolérance)
    C_LIBERTE = u"Liberté" # Peuple qui sont fiers de leur liberté, de leurs droits. L'esclavagey est mal vu et moins brutal
    C_ARGENT = u"Argent" # La richesse est très valorisée et au coeur des coutumes
    C_SEXISME = u"Sexisme" # Niveau de différence de traitement entre les sexes. Patriarcat très fort = 1.0

    # ------------ état militaire et diplomatique du peuple
    C_DIPLOMATIE = u"Diplomatie" # diplomacie "en général" c'est à dire passe en mode guerre si le peuple est en guerre même avec un seul ennemi
    # ------------- val de C_DIPLOMATIE
    PAIX = u"Paix"
    GUERRE = u"Guerre"

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
        situation.SetValCarac(Peuple.C_DIPLOMATIE, Peuple.PAIX)
        situation.SetValCarac(Peuple.C_SOUV, Peuple.TRIBUE)
