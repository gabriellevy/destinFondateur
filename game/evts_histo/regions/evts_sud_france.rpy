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
    from spe.richesse import richesse

    # Massilia
    apprentissageEcritureParMassiliaPasFait = condition.Condition("apprentissageEcritureParMassilia", "1", condition.Condition.DIFFERENT)
    rencontreMassilaPasFait = condition.Condition("rencontreMassila", "1", condition.Condition.DIFFERENT)
    rencontreMassilaFait = condition.Condition("rencontreMassila", "1", condition.Condition.EGAL)
    mauvaisRapportAvecMassalia = condition.Condition(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5, condition.Condition.INFERIEUR)

    # temps
    anneeSupMoins600 = condition.Condition(temps.Date.DATE_ANNEES, "-600", condition.Condition.SUPERIEUR)
    anneeInf0 = condition.Condition(temps.Date.DATE_ANNEES, "0", condition.Condition.INFERIEUR)

    # science
    niveauEcritureNul = condition.Condition(science.Science.C_ECRITURE, "0.3", condition.Condition.INFERIEUR)

    # base
    siSudFrance = condition.Condition(region.Region.C_REGION, sud_france.SudFrance.NOM, condition.Condition.EGAL)
    def AjouterEvtsReligieuxH():
        global selecteur_

        apprentissageEcritureParMassilia = declencheur.Declencheur(proba.Proba(0.4, True), "apprentissageEcritureParMassilia")
        apprentissageEcritureParMassilia.AjouterConditions( [estEnModeHisto, anneeSupMoins600, anneeInf0, apprentissageEcritureParMassiliaPasFait,
            siSudFrance, rencontreMassilaFait, niveauEcritureNul])
        selecteur_.ajouterDeclencheur(apprentissageEcritureParMassilia)

        rencontreMassila = declencheur.Declencheur(proba.Proba(1.0, True), "rencontreMassila")
        rencontreMassila.AjouterConditions( [estEnModeHisto, anneeSupMoins600, anneeInf0, rencontreMassilaPasFait, siSudFrance])
        selecteur_.ajouterDeclencheur(rencontreMassila)

        attaqueParMassalia = declencheur.Declencheur(proba.Proba(0.05, True), "attaqueParMassalia")
        # peut arriver plusieurs fois
        attaqueParMassalia.AjouterConditions( [estEnModeHisto, anneeSupMoins600, anneeInf0, siSudFrance, mauvaisRapportAvecMassalia, rencontreMassilaFait])
        selecteur_.ajouterDeclencheur(attaqueParMassalia)

label attaqueParMassalia:
    menu:
        "attaque Par Massalia regarde bien la SUITE":
            pass
    "Vos rapports avec les phocéens de Massalia sont devenus très mauvais et ils décident de lancer un raid contre votre village pour vous chasser des environs."
    $ population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    if population > 4000 and violence > 0.3:
        "Les guerriers [nomPeuple] tiennent bon et parviennent à tendre une embuscade aux phocéens qui préfèrent négocier un traité que de prendre le risque de se battre."
        "Les [nomPeuple] conservent leurs terres et recevront un tribu régulier contre la promesse de respecter les commerçants phocéens."
        $ AjouterACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
        $ AjouterACarac(richesse.Richesse.C_TRIBUS, 0.5)
        $ RetirerAPopulationPourcent(2)
    else:
        "Vos [nomPeuple] sont vaincus et leur village détruit. Les phocéens ne tentent cependant pas de les exterlminer. Ils veulent juste s'étendre en volant leurs terres."
        "Les [nomPeuple] se réinstallent donc à bonne distance, affaiblis mais furieux et décidés à ne pas se laisser encore surprendre."
        $ AjouterACarac(peuple.Peuple.C_VIOLENCE, 0.1)
        $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.3)
        $ RetirerAPopulationPourcent(10)

    jump fin_cycle

label rencontreMassila:
    $ situation_.SetValCarac("rencontreMassila", "1")
    menu:
        "A FAIRE coucou massilia (texte d'ambiance etc)":
            pass
    jump fin_cycle

label apprentissageEcritureParMassilia:
    $ situation_.SetValCarac("apprentissageEcritureParMassilia", "1")
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
