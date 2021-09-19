init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from spe import declencheur_fondateur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from spe import situation_fondateur
    from spe.peuple import peuple
    from spe.civilisation import civ
    from spe.civilisation import celtes

    spiritualitePlusQueQuatre = condition.Condition(peuple.Peuple.C_SPIRITUALITE, 0.4, condition.Condition.SUPERIEUR)
    creativiteAuMoinsCorrecte = condition.Condition(peuple.Peuple.C_CREATIVITE, 0.3, condition.Condition.SUPERIEUR)
    creativiteMoinsQueHuit = condition.Condition(peuple.Peuple.C_CREATIVITE, 0.8, condition.Condition.INFERIEUR)
    violenceMoinsQueCinq = condition.Condition(peuple.Peuple.C_VIOLENCE, 0.5, condition.Condition.INFERIEUR)
    estCelte = condition.Condition(civ.Civ.C_CIV, celtes.Celte.NOM, condition.Condition.EGAL)
    def AjouterEvtsCeltesH():
        global selecteur_

        nouveauBarde = declencheur.Declencheur(proba.Proba(0.02, True), "nouveauBarde")
        nouveauBarde.AjouterConditions([estCelte, estEnModeHisto, creativiteAuMoinsCorrecte])
        selecteur_.ajouterDeclencheur(nouveauBarde)

        bonsArtisans = declencheur.Declencheur(proba.Proba(0.02, True), "bonsArtisans")
        bonsArtisans.AjouterConditions([estCelte, estEnModeHisto, creativiteMoinsQueHuit])
        selecteur_.ajouterDeclencheur(bonsArtisans)

        bonsSculpteurs = declencheur.Declencheur(proba.Proba(0.02, True), "bonsArtisans")
        bonsSculpteurs.AjouterConditions([estCelte, estEnModeHisto, creativiteMoinsQueHuit])
        selecteur_.ajouterDeclencheur(bonsSculpteurs)

        festinCelte = declencheur.Declencheur(proba.Proba(0.02, True), "festinCelte")
        festinCelte.AjouterConditions([estCelte, estEnModeHisto])
        selecteur_.ajouterDeclencheur(festinCelte)

        raidePourBetail = declencheur.Declencheur(proba.Proba(0.004, True), "raidePourBetail")
        raidePourBetail.AjouterConditions([estCelte, estEnModeHisto, violenceMoinsQueCinq])
        selecteur_.ajouterDeclencheur(raidePourBetail)

        consecrationDunBois = declencheur.Declencheur(proba.Proba(0.05, True), "consecrationDunBois")
        consecrationDunBois.AjouterConditions([estCelte, estEnModeHisto, spiritualitePlusQueQuatre])
        selecteur_.ajouterDeclencheur(consecrationDunBois)

label consecrationDunBois:
    "Les druides ont déterminé avec l'aide des oracles que la forêt de [nomForet] était sacrée. On ne pourra y pénétrer que sous al direction de son grand prêtre les jours de sacrifice."
    $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.05)
    $ AjouterACarac(celte.Celte.BOIS_SACRE, 1)
    jump fin_cycle

label raidePourBetail:
    "Un clan rival a volé beaucoup des vaches des [nomPeuple]. Il va falloir être plus vigilant... ou plus agressif."
    $ RetirerACaracPos(richesse.Richesse.C_TRIBUS, 0.05)
    jump fin_cycle

label festinCelte:
    $ nomRoi = civRef.GenererPatronyme(True)
    $ nomFille = civRef.GenererPatronyme(False)
    "Le roi [nomRoi] a donné un grand festin pour les fiançailles de sa fille [nomFille]."
    $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.1)
    "L'hydromel coule à flot et pour l'occasion le roi a même servi du vin à tous ses invités."
    "Un énorme chaudron ouvragé est au cen tre de la pièce et les invités sont allongés sur des lits tout autour. Plus ou moins proches du roi selon leur rang."
    $ creativite = situation_.GetValCarac(peuple.Peuple.C_CREATIVITE)
    if creativite > 0.3:
        "Le grand barde [nomBarde] a été convié et si bien honoré qu'il a composé un gand poème de compliment en l'honneur du roi [nomRoi]."
        $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.05)
    else:
        "Malheureusement al cour manque de poètes et le spectacle laisse à désirer mais la nourriture compense."

    jump fin_cycle

label bonsSculpteurs:
    menu:
        "hop bonsSculpteurs"
        "youpi bonsSculpteurs":
            pass
    $ bonsSculpteurs = situation_.GetValCaracInt("bonsSculpteurs")
    if bonsSculpteurs == 1:
        scene bg statue2
        $ situation_.SetValCarac("bonsSculpteurs", "2")
    elif bonsSculpteurs == 2:
        scene bg statue3
        $ situation_.SetValCarac("bonsSculpteurs", "3")
    else:
        scene bg statue1
        $ situation_.SetValCarac("bonsSculpteurs", "1")
    "Les artisans [nomPeuple] font des progrès remarquables dans la sculpture en bronze."
    $ AjouterACaracIdentite(peuple.Peuple.C_CREATIVITE, 0.1)

    jump fin_cycle

label bonsArtisans:
    "Les artisans [nomPeuple] font des progrès remarquables dans la création de torques et de bracelets d'argents."
    $ AjouterACaracIdentite(peuple.Peuple.C_CREATIVITE, 0.1)

    jump fin_cycle

label nouveauBarde:
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomBarde = civRef.GenererPatronyme(True)
    "Après 12 ans d'études, de voyages et de travail acharné, [nomBarde] est devenu un grand barde qui honorela grandeur des [nomPeuple]."
    $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.2)

    jump fin_cycle
