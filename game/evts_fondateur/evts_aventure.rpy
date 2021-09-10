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
        aventurierDesMers.AjouterConditions([estEnModeFondateur, estDansRegionCotiere, aventurierDesMersPasFait])
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
        "Le vrai bonheur d'un homme est d'honorer ses ancêtres dans son pays, pas d'abandonner sa famille pour risquer la noyade pour des chimères.":
            $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.1)
            $ RetirerACaracPos(peuple.Peuple.C_AVENTURE, 0.3)
        "Va poursuivre l'aventure et la prospérité. C'est le meilleur moyen de servir ton peuple et ta famille.":
            $ RetirerACaracPos(peuple.Peuple.C_COHESION, 0.02)
            $ AjouterACaracIdentite(peuple.Peuple.C_AVENTURE, 0.5)
            $ AjouterAAffinite(civ.Nordique.NOM, 0.3)
            $ AjouterAAffinite(civ.Phenicien.NOM, 0.5)

    jump fin_cycle
