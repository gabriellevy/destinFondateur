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
    from spe.civilisation import celtes

    # simples marqueurs de fait/pas fait des événements
    traitementEnnemisMortsPasFait = condition.Condition("traitementEnnemisMorts", "1", condition.Condition.DIFFERENT)
    femmesEtGuerrePasFait = condition.Condition("femmesEtGuerre", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsGuerreF():
        global selecteur_

        traitementEnnemisMorts = declencheur.Declencheur(proba.Proba(0.1, True), "traitementEnnemisMorts")
        traitementEnnemisMorts.AjouterConditions([estEnModeFondateur, traitementEnnemisMortsPasFait])
        selecteur_.ajouterDeclencheur(traitementEnnemisMorts)

        femmesEtGuerre = declencheur.Declencheur(proba.Proba(0.1, True), "femmesEtGuerre")
        femmesEtGuerre.AjouterConditions([estEnModeFondateur, femmesEtGuerrePasFait])
        selecteur_.ajouterDeclencheur(femmesEtGuerre)

label femmesEtGuerre:
    $ situation_.SetValCarac("femmesEtGuerre", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "[titreFondateur], que doivent faire leurs femmes quand les [nomPeuple] partent à la guerre ?"
    menu:
        "Les femmes doivent défendre leur peuple de la même manière que les hommes.":
            $ RetirerACaracPos(peuple.Peuple.C_SEXISME, 0.3)
            # représenter d'une manière quelconque le fait que cela provoque des pertes plus forts (et moins de fécondité post guerre)
        "Emmenez les femmes aux combats. Elles encourageront les hommes depuis les arrières et panseront leurs blessures":
            $ AjouterAAffinite(celtes.Celte.NOM, 0.3)
            $ AjouterAAffinite(civ.Germanique.NOM, 0.3)
            # représenter d'une manière quelconque le fait que les défaites provoquent un massacre parmi les femmes
        "Aucune femme ne doit approcher du champs de bataille.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SEXISME, 0.3)

    jump fin_cycle

label traitementEnnemisMorts:
    $ situation_.SetValCarac("traitementEnnemisMorts", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomPerso)
    $ plaignantImg = civRef.GenererImageGuerrier(True, 25, [])
    $ renpy.show(plaignantImg, [right])
    with moveinright
    std "[titreFondateur], nous avons tué des pillards qui tentaient de voler notre réserve. Ce devrait être jour de fête mais nos guerriers se disputent sur ce qu'e l'on doit faire des corps des ennemis tués."
    menu:
        "Rien. Laissez les aux bêtes sauvages.":
            pass
        "Traitez-les comme vous traiteriez les corps des nôtres.":
            $ RetirerACaracPos(peuple.Peuple.C_COHESION, 0.3)
            $ AjouterACaracIdentite(peuple.Peuple.C_COOPERATION, 0.5)
        "Que les guerriers se fassent des trophées si ils le souhaitent.":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.3)
            if civRef.nom_ == celtes.Celte.NOM:
                "Les guerriers [nomPeuple] s'empressent de décapiter leurs ennemis morts à la manière celte et les exposent dans leurs huttes."

    jump fin_cycle
