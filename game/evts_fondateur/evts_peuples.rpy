init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from spe import situation_fondateur
    from spe.peuple import peuple
    from spe.civilisation import civ
    from spe.civilisation import romains

    # simples marqueurs de fait/pas fait des événements
    toleranceAuMelangePasFait = condition.Condition("toleranceAuMelange", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsPeuples():
        global selecteur_

        toleranceAuMelange = declencheur.Declencheur(proba.Proba(0.1, True), "toleranceAuMelange")
        toleranceAuMelange.AjouterConditions([estEnModeFondateur, toleranceAuMelangePasFait])
        selecteur_.ajouterDeclencheur(toleranceAuMelange)

label toleranceAuMelange:
    $ situation_.SetValCarac("toleranceAuMelange", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomPerso)
    $ plaignantImg = civRef.GenererImagePerso(False, 50, [])
    # $ annee = situation_.GetAnnee() A FAIRE : ces fonctions
    # $ peupleVoisin = situation_.GetRegion().GetVoisinAleatoire(annee) A FAIRE : ces fonctions
    $ peupleVoisin = civRef.GenererNomPeuple() # TMP à remplacer par ce qui est dessus
    $ renpy.show(plaignantImg, [right])
    with moveinright
    std "[titreFondateur], les [peupleVoisin] sont de plus en plus nombreus parmi nous. Ils vendent leurs marchandises étranges, parlent de leurs dieux à nos jeunes gens et même les séduisent et partagent leurs amusements. Nous craignons que nos jeunes s'éloignent de nous et de nos traditions."
    menu:
        "Ne vous mélangez pas aux étrangers et ne suivez pas leurs dieux et leurs coutumes inférieurs. Le commerce seul est acceptable.":
            $ RetirerACaracPos(peuple.Peuple.C_COOPERATION, 0.4)
            $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.5)
        "Acceptez les échanges et même les mariages car c'est du mélange que ressort le meilleur.":
            $ AjouterACaracIdentite(peuple.Peuple.C_COOPERATION, 1.0)
            $ AjouterACaracIdentite(peuple.Peuple.C_CREATIVITE, 0.1)
            $ RetirerACaracPos(peuple.Peuple.C_COHESION, 0.5)
        "Soyez prudents. Les étrangers amènent parfois de bonnes choses mais ils sont tout aussi souvent trompeurs et corrupteurs.":
            $ AjouterACaracIdentite(peuple.Peuple.C_COOPERATION, 0.1)
        "Dominez les étrangers. Et quand vous vous êtes assurés de votre supériorité, vous pouvez vous mélanger avec eux et les intégrer à votre groupe.":
            $ AjouterACaracIdentite(peuple.Peuple.C_COOPERATION, 0.3)
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.3)

    jump fin_cycle
