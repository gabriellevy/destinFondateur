# génération du personnage principal et de ce qui le concerne en début de partie comme ses parents

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import testDeCarac
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from spe.peuple import peuple
    from abs.religions import religion

    def genererDateNaissance(situation, ageActuel=15):
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
        situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererFondateur(situation, tousLesTraits):
        """
        A FAIRE : profil spécifique au Fondateur
        """
        # situation[trait.Violence.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Opportunisme.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Assurance.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Observation.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Cupidite.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Courage.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Ambition.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Rancune.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Franchise.NOM] = trait.Trait.SEUIL_A_PAS

        # compétences professionnelles
        # situation[metier.Politique.NOM] = trait.Trait.SEUIL_A
        # situation[metier.Guerrier.NOM] = trait.Trait.SEUIL_A
        # situation[metier.Chasseur.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques peuple
        situation[peuple.Peuple.C_VIOLENCE] = 0

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        situation[identite.Identite.C_NOM] = "Fondateur" # A FAIRE : générer nom selon culture
        return

label choix_peuple:
    $ genererDateNaissance(situation_, 13)
    $ genererFondateur(situation_, traits_)
    jump fin_cycle
