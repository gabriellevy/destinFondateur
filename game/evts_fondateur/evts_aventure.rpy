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
    from spe.region import geo

    estDansRegionCotiere = condition.Condition(geo.Geo.C_COTIERE, "1", condition.Condition.EGAL)
    aventurierDesMersPasFait = condition.Condition("aventurierDesMers", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsAventure():
        global selecteur_
        # tenté par l'aventure marine ?
        aventurierDesMers = declencheur.Declencheur(proba.Proba(0.3, True), "aventurierDesMers")
        aventurierDesMers.AjouterCondition(estEnModeFondateur)
        aventurierDesMers.AjouterCondition(estDansRegionCotiere)
        aventurierDesMers.AjouterCondition(aventurierDesMersPasFait)
        selecteur_.ajouterDeclencheur(aventurierDesMers)

label aventurierDesMers:
    $ situation_.SetValCarac("aventurierDesMers", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ persoImg = civRef.GenererImagePerso(True, 20)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "[nomPerso], un jeune homme turbulent de bonne famille, a demandé humblement à profiter de vos sages conseils."
    $ renpy.show(persoImg, [right])
    with moveinright
    $ std = Character(nomPerso)
    std "[titreFondateur], je sais que notre terre est douce et hospitalière et que la place d'un homme est auprès de sa famille."
    std "Mais ces marins et commerçants ne cessent de me parler de terres lointaines fascinantes, où un homme décidé peut faire des fortunes."
    std "J'aimerais ouvrir notre peuple au commerce en affrétant un navire mais je n'ose me décider."
    menu:
        "Le vrai bonheur d'un homme est d'honorer ses ancêtres dans son pays, pas d'abandonner sa famille pour risquer la noyage pour des chimères.":
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.1)
            $ RetirerACarac(peuple.Peuple.C_AVENTURE, 0.3)
        "Va poursuivre l'aventure et la prospérité. C'est le meilleur moyen de servir ton peuple et ta famille.":
            $ AjouterACarac(peuple.Peuple.C_COHESION, -0.02)
            $ AjouterACarac(peuple.Peuple.C_AVENTURE, 0.5)
            $ AjouterAAffinite(civ.Nordique.NOM, 0.3)
            $ AjouterAAffinite(civ.Phenicien.NOM, 0.5)

    jump fin_cycle
