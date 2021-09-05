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

    creativiteAuMoinsCorrecte = condition.Condition(peuple.Peuple.C_CREATIVITE, 0.3, condition.Condition.SUPERIEUR)
    creativiteMoinsQueHuit = condition.Condition(peuple.Peuple.C_CREATIVITE, 0.8, condition.Condition.INFERIEUR)
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
    $ AjouterACarac(peuple.Peuple.C_CREATIVITE, 0.1)

    jump fin_cycle

label bonsArtisans:
    "Les artisans [nomPeuple] font des progrès remarquables dans la création de torques et de bracelets d'argents."
    $ AjouterACarac(peuple.Peuple.C_CREATIVITE, 0.1)

    jump fin_cycle

label nouveauBarde:
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomBarde = civRef.GenererPatronyme(True)
    "Après 12 ans d'études, de voyages et de travail acharné, [nomBarde] est devenu un grand barde qui honorela grandeur des [nomPeuple]."
    $ AjouterACarac(peuple.Peuple.C_COHESION, 0.2)

    jump fin_cycle
