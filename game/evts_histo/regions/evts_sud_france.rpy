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
    from spe import declencheur_fondateur

    # Massilia
    apprentissageEcritureParMassiliaPasFait = condition.Condition("apprentissageEcritureParMassilia", "1", condition.Condition.DIFFERENT)
    rencontreMassilaPasFait = condition.Condition("rencontreMassila", "1", condition.Condition.DIFFERENT)
    guerreAvatiquesPhoceensPasFait = condition.Condition("guerreAvatiquesPhoceens", "1", condition.Condition.DIFFERENT)
    rencontreMassilaFait = condition.Condition("rencontreMassila", "1", condition.Condition.EGAL)
    mauvaisRapportAvecMassalia = condition.Condition(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5, condition.Condition.INFERIEUR)
    mauvaisRapportAvecAvatiques = condition.Condition(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.5, condition.Condition.INFERIEUR)

    # science
    niveauEcritureNul = condition.Condition(science.Science.C_ECRITURE, "0.3", condition.Condition.INFERIEUR)

    # base
    siSudFrance = condition.Condition(region.Region.C_REGION, sud_france.SudFrance.NOM, condition.Condition.EGAL)
    def AjouterEvtsSudFranceH():
        global selecteur_

        apprentissageEcritureParMassilia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.4, True), "apprentissageEcritureParMassilia")
        apprentissageEcritureParMassilia.AjouterConditions( [apprentissageEcritureParMassiliaPasFait,
            siSudFrance, rencontreMassilaFait, niveauEcritureNul])
        apprentissageEcritureParMassilia.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(apprentissageEcritureParMassilia)

        rencontreMassila = declencheur_fondateur.DeclencheurFondateur(proba.Proba(1.0, True), "rencontreMassila")
        rencontreMassila.AjouterConditions( [ rencontreMassilaPasFait, siSudFrance])
        rencontreMassila.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(rencontreMassila)

        guerreAvatiquesPhoceens = declencheur_fondateur.DeclencheurFondateur(proba.Proba(1.0, True), "guerreAvatiquesPhoceens")
        # ENVIRON -200 AVANT jc
        guerreAvatiquesPhoceens.AjouterConditions( [guerreAvatiquesPhoceensPasFait, siSudFrance, rencontreMassilaFait])
        guerreAvatiquesPhoceens.EvtHistoArriveEntreDateAetB(-210, -190)
        selecteur_.ajouterDeclencheur(guerreAvatiquesPhoceens)

        attaqueParMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "attaqueParMassalia")
        # peut arriver plusieurs fois
        attaqueParMassalia.AjouterConditions( [siSudFrance, mauvaisRapportAvecMassalia, rencontreMassilaFait])
        attaqueParMassalia.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(attaqueParMassalia)

label guerreAvatiquesPhoceens:
    menu:
        "guerreAvatiquesPhoceens regarde bien la SUITE":
            pass
    $ situation_.SetValCarac("guerreAvatiquesPhoceens", "1")
    "L'expansion des phocéens de Massalia se heurte de plus en plus souvent aux peuples celtes des environs."
    "De leur côté les celtes avatiques sont de plus en plus tentés par le pillage de la riche Massalia. Cela va dégénérer en guerre ouverte."
    $ population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    $ rapport_massalia = situation_.GetValCaracInt(sud_france.SudFrance.C_RAPPORT_MASSILIA)
    $ rapport_avatiques = situation_.GetValCaracInt(sud_france.SudFrance.C_RAPPORT_AVATIQUES)

    if rapport_massalia > 0.6 and rapport_avatiques > 0.6:
        "Les [nomPeuple] ont de très bons rapports avec les deux camps et refusent de participer à la guerre dans quelque camps que ce soit."
        "Ils parviennent avec difficulté à le faire. Mais phocéens comme celtes attendaient leur aide et prennent très mal cette attitude."
        jump guerreAvatiquesPhoceens_neutralite
    elif rapport_massalia < 0.2:
        label guerreAvatiquesPhoceens_allies_avatiques:
            # allié aux avatiques
            "Le mépris des [nomPeuple] pour les grecs leur fait rejoindre leur frères celtes avatiques dans la guerre contre Massalia."
            "Malheureusement ces grecs ci sont disciplinés et bien armés et se cachent derrières des armures et des boucliers."
            "Les [nomPeuple] sont contraints de rester sur la défensive et voient leur village incendié par les envahisseurs."
            $ RetirerAPopulationPourcent(7)
            $ AjouterACarac(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.2)
            $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.2)
            $ RetirerACarac(richesse.Richesse.C_TRIBUS, 0.1)
            jump guerreAvatiquesPhoceens_fin
    elif rapport_avatiques < 0.2:
        label guerreAvatiquesPhoceens_allies_massalia:
            # allié à Massalia
            "C'est l'occasion pour les [nomPeuple] de se venger de leurs frères avatiques détestés en s'alliant aux puissants marins grecs en armure."
            "Ils parviennent ainsi à participer à quelques pillages juteux."
            $ RetirerAPopulationPourcent(3)
            $ AjouterACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.2)
            $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.2)
            $ AjouterACarac(richesse.Richesse.C_TRIBUS, 0.3)
            jump guerreAvatiquesPhoceens_fin
    elif violence < 0.2:
        "Les [nomPeuple] sont aussi pacifiques qu'on peut l'être et fuient les combats, quitte à fuir leur village temporairement."
        "Les avatiques et les phocéens ne font que les mépriser encore plus et pillent leurs terres."
        jump guerreAvatiquesPhoceens_neutralite
    elif rapport_avatiques > rapport_massalia:
        jump guerreAvatiquesPhoceens_allies_avatiques
    else:
        jump guerreAvatiquesPhoceens_allies_massalia

    label guerreAvatiquesPhoceens_neutralite:
        $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.1)
        $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.1)
        jump guerreAvatiquesPhoceens_fin

    label guerreAvatiquesPhoceens_fin:
        "Après plusieurs mois de traque et d'escarmouches les phocéens de Massalia sortent vainqueurs mais ne sont pas arrivés à grand chose."
        "Ils ont brûlé le village de l'île des avatiques, tué des guerriers, pris des esclaves et montré leur supériorité mais les avatiques se sont réinstallés aussitôt après."
        $ RetirerAPopulationPourcent(2)

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

label attaqueParMassalia:
    menu:
        "attaque Par Massalia regarde bien la SUITE":
            pass
    "Les rapports des [nomPeuple] avec les phocéens de Massalia sont devenus très mauvais et ceux-ci décident de lancer un raid contre leur village pour les chasser des environs."
    $ population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    if population > 4000 and violence > 0.3:
        "Les guerriers [nomPeuple] tiennent bon et parviennent à tendre une embuscade aux phocéens qui préfèrent négocier un traité que de prendre le risque de se battre."
        "Les [nomPeuple] conservent leurs terres et recevront un tribu régulier contre la promesse de respecter les commerçants phocéens."
        $ AjouterACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
        $ AjouterACarac(richesse.Richesse.C_TRIBUS, 0.5)
        $ RetirerAPopulationPourcent(2)
    else:
        "Les [nomPeuple] sont vaincus et leur village détruit. Les phocéens ne tentent cependant pas de les exterlminer. Ils veulent juste s'étendre en volant leurs terres."
        "Les [nomPeuple] se réinstallent donc à bonne distance, affaiblis mais furieux et décidés à ne pas se laisser encore surprendre."
        $ AjouterACarac(peuple.Peuple.C_VIOLENCE, 0.1)
        $ RetirerACarac(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.3)
        $ RetirerAPopulationPourcent(10)

    jump fin_cycle
