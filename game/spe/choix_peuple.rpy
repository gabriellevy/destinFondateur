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

    def genererFondateur(situation):
        """
        A FAIRE : profil spécifique au Fondateur
        """
        civRef = situation.GetCivilisationDeReference()
        # situation[trait.Violence.NOM] = trait.Trait.SEUIL_A_EXTREME

        # compétences professionnelles
        # situation[metier.Politique.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques peuple
        situation[peuple.Peuple.C_VIOLENCE] = 0

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        if civRef is not None:
            situation[identite.Identite.C_NOM] = civRef.GenererPatronyme(True)

    def SelectionPeuple(peup, situation):
        peup.SelectionDePeuple(situation)
        renpy.jump(peup.labelDepart_)

label choix_peuple:
    $ index_peuple = 0

    python:
        menu_items = [(cle, valeur) for cle, valeur in situation_.collectionPeuples.lPeuples_.items()]
        # menu_items.append(("Never mind", Pass))
        peupleChoisi = menu(menu_items)
        SelectionPeuple(peupleChoisi, situation_)
    "fin choix"
    jump fin_cycle

label choix_peuple_avatiques:
    scene bg village_celte
    $ nomPeuple = situation_.GetValCarac(peuple.Peuple.C_PEUPLE)
    "Vous êtes un noble fortuné et influent du peuple des avatiques."
    "Vous avez été éloigné du pouvoir à cause de vos divergences avec les autres nobles et de vos idées impopulaires."
    "Beaucoup de vos suivants ont décidé de rester avec vous et vous avez construit un village pour vous regrouper et prendre le contrôle des terres environnantes. Vous avez décide de vous nommer [nomPeuple]"
    "L'environnement est idéal. Vous êtes proche du Rhône et de l'étang d'eau salée de Berre. De plus le riche port grec de Massilia est toute proche et est un très bon partenaire de commerce."
    $ genererDateNaissance(situation_, 30)
    $ genererFondateur(situation_)
    $ situation_.SetValCarac(peuple.Peuple.C_POP, 2214)
    jump fin_cycle
