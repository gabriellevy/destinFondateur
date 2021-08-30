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
    from spe.region import region
    from spe.region import sud_france
    from spe.science import science

    apprentissageEcritureParMassiliaPasFait = condition.Condition("apprentissageEcritureParMassilia", "1", condition.Condition.DIFFERENT)
    rencontreMassilaPasFait = condition.Condition("rencontreMassila", "1", condition.Condition.DIFFERENT)
    rencontreMassilaFait = condition.Condition("rencontreMassila", "1", condition.Condition.EGAL)
    anneeSupMoins600 = condition.Condition(temps.Date.DATE_ANNEES, "-600", condition.Condition.SUPERIEUR)
    anneeInf0 = condition.Condition(temps.Date.DATE_ANNEES, "0", condition.Condition.INFERIEUR)
    niveauEcritureNul = condition.Condition(science.Science.C_ECRITURE, "0.3", condition.Condition.INFERIEUR)
    siSudFrance = condition.Condition(region.Region.C_REGION, sud_france.SudFrance.NOM, condition.Condition.EGAL)
    def AjouterEvtsReligieuxH():
        global selecteur_

        apprentissageEcritureParMassilia = declencheur.Declencheur(proba.Proba(0.4, True), "apprentissageEcritureParMassilia")
        apprentissageEcritureParMassilia.AjouterCondition(estEnModeHisto)
        apprentissageEcritureParMassilia.AjouterCondition(anneeSupMoins600)
        apprentissageEcritureParMassilia.AjouterCondition(anneeInf0)
        apprentissageEcritureParMassilia.AjouterCondition(apprentissageEcritureParMassiliaPasFait)
        apprentissageEcritureParMassilia.AjouterCondition(siSudFrance)
        apprentissageEcritureParMassilia.AjouterCondition(rencontreMassilaFait)
        apprentissageEcritureParMassilia.AjouterCondition(niveauEcritureNul)
        selecteur_.ajouterDeclencheur(apprentissageEcritureParMassilia)

        rencontreMassila = declencheur.Declencheur(proba.Proba(1.0, True), "rencontreMassila")
        rencontreMassila.AjouterCondition(estEnModeHisto)
        rencontreMassila.AjouterCondition(anneeSupMoins600)
        rencontreMassila.AjouterCondition(anneeInf0)
        rencontreMassila.AjouterCondition(rencontreMassilaPasFait)
        rencontreMassila.AjouterCondition(siSudFrance)
        selecteur_.ajouterDeclencheur(rencontreMassila)

label rencontreMassila:
    $ situation_.SetValCarac("rencontreMassila", "1")
    menu:
        "A FAIRE coucou massilia (texte d'ambiance etc)":
            pass
    jump fin_cycle

label apprentissageEcritureParMassilia:
    $ situation_.SetValCarac("apprentissageEcritureParMassilia", "1")
    menu:
        "l'écriture c'est trop cool":
            pass
    $ civRef = situation_.GetCivilisationDeReference()
    "Vos voisins phocéens de Massila parlent et surtout écrivent en grec. Comme vous commercez avec eux ils décident d'initier les [nomPeuple] car c'est un art très pratique pour tenir les comptes."
    $ intellectualisme = situation_.GetValCarac(peuple.Peuple.C_INTEL)
    $ curiosite = situation_.GetValCarac(peuple.Peuple.C_AVENTURE)
    if curiosite < 0.5 and intellectualisme < 0.2:
        "Mais les [nomPeuple] les repoussent. Ils ont toujours bien vécu sans se compliquer la vie avec ça et continueront."
        $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
    else:
        "Plusieurs commerçants [nomPeuple] s'y intéressent essentiellement pour tenir leurs comptes."
        $ AjouterACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
        $ AjouterACarac(civ.Grecque.NOM, 0.1)
        $ AjouterACarac(peuple.Peuple.C_INTEL, 0.1)
        $ AjouterACarac(science.Science.C_ECRITURE, 0.3)
    jump fin_cycle
