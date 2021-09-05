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

    siTribue = condition.Condition(peuple.Peuple.C_SOUV, peuple.Peuple.TRIBUE, condition.Condition.EGAL)
    mariageFondateurPasFait = condition.Condition("mariageFondateur", "1", condition.Condition.DIFFERENT)
    fetesMariagePasFait = condition.Condition("fetesMariage", "1", condition.Condition.DIFFERENT)
    mariageEtAccouplementPasFait = condition.Condition("mariageEtAccouplement", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsFamilleF():
        global selecteur_
        # mariage du fondateur
        mariageFondateur = declencheur.Declencheur(proba.Proba(0.3, True), "mariageFondateur")
        mariageFondateur.AjouterConditions([estEnModeFondateur, mariageFondateurPasFait, siTribue])
        selecteur_.ajouterDeclencheur(mariageFondateur)
        # fêtes et mariage
        fetesMariage = declencheur.Declencheur(proba.Proba(0.1, True), "fetesMariage")
        fetesMariage.AjouterConditions([estEnModeFondateur, fetesMariagePasFait])
        selecteur_.ajouterDeclencheur(fetesMariage)

        mariageEtAccouplement = declencheur.Declencheur(proba.Proba(0.1, True), "mariageEtAccouplement")
        mariageEtAccouplement.AjouterConditions([estEnModeFondateur, mariageEtAccouplementPasFait])
        selecteur_.ajouterDeclencheur(mariageEtAccouplement)

label mariageEtAccouplement:
    $ situation_.SetValCarac("mariageEtAccouplement", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomChefFamille = civRef.GenererPatronyme(True)
    $ nomChefFamilleImg = civRef.GenererImagePerso(True, 50)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomChefFamille)
    $ renpy.show(nomChefFamilleImg, [right])
    with moveinright
    std "[titreFondateur], les dieux sont les témoins des mariages depuis toujours et les formes se perdent."
    std "Mariage et accouplement sont une seule et même chose pour beaucoup tandis que d'autres pensent que les jeunes doivent se déouvrir et choisir eux-mêmes leur conjoint."
    std "Ces deux vues sont irréconciliables. Récemment un homme en a tué un autre qui avait séduit et engrossé sa fille et refusait de l'épouser. Quelle voie devons nous suivre ?"
    menu:
        "C'est le père et seulement lui qui doit choisir le fiancé de sa fille. Toute copulation hors mariage est un crime.":
            $ AjouterACarac(peuple.Peuple.C_SEXISME, 0.3)
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.2)
        "Si une femme et un homme se jugent dignes l'un de l'autre, ils peuvent se marier. Après seulement ils pourront s'accoupler":
            $ RetirerACarac(peuple.Peuple.C_SEXISME, 0.2)
            $ AjouterACarac(peuple.Peuple.C_LIBERTE, 0.2)
            $ RetirerACarac(peuple.Peuple.C_COHESION, 0.1)
        "L'amour est le plus important, le mariage est accessoire. Laissez les jeunes gens se découvrir et s'épouser à leur gré.":
            $ AjouterACarac(peuple.Peuple.C_SENSUALITE, 0.2)
            $ AjouterACarac(peuple.Peuple.C_LIBERTE, 0.5)
            $ RetirerACarac(peuple.Peuple.C_SEXISME, 0.2)
            $ RetirerACarac(peuple.Peuple.C_COHESION, 0.1)

    jump fin_cycle

label fetesMariage:
    $ situation_.SetValCarac("fetesMariage", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomChefFamille = civRef.GenererPatronyme(True)
    $ nomChefFamilleImg = civRef.GenererImagePerso(True, 50)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomChefFamille)
    $ renpy.show(nomChefFamilleImg, [right])
    with moveinright
    "[nomChefFamille] est un homme noble et riche, un des plus importants de la tribue."
    std "[titreFondateur], j'ai besoin de vos sages conseils. Mon fils se marie aujourd'hui et je suis partagé entre l'envie de donner une très grande fête et la peur qu'elle dégénère."
    std "Car ce jour est sacré et je trouve que les beuveries et les farces déshonoreraient ma famille."
    menu:
        "Les fêtes sont les grands moments de relâchement des tensions et de fraternisation. Invitez tout le monde et festoyez. On se souviendra de votre générosité et de ce grand jour.":
            $ AjouterACarac(peuple.Peuple.C_SENSUALITE, 0.5)
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.1)
            $ AjouterACarac(peuple.Peuple.C_ARGENT, 0.1)
        "Les festins sont dégradants et vulgaires. Les mariages sont sacrés et doivent rester dignes.":
            $ RetirerACarac(peuple.Peuple.C_SENSUALITE, 0.3)
            $ AjouterACarac(peuple.Peuple.C_SPIRITUALITE, 0.1)
            $ AjouterACarac(peuple.Peuple.C_LEGALISME, 0.1)
        "Donnez de la dignité au mariage en invitant poètes et musiciens. En remplaçant la débauche par l'art votre prestige sera au plus haut.":
            $ AjouterACarac(peuple.Peuple.C_CREATIVITE, 0.2)
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.1)

    jump fin_cycle

label mariageFondateur:
    $ situation_.SetValCarac("mariageFondateur", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomChefFamille = civRef.GenererPatronyme(True)
    $ nomFianceeAmour = civRef.GenererPatronyme(False)
    $ nomFianceeArgent = civRef.GenererPatronyme(False)
    $ fianceeAmourImg = civRef.GenererImagePerso(False, 20)
    "Vous êtes l'homme le plus respecté de la tribu et vous n'êtes donc pas réellement surpris quand [nomChefFamille] vient vous proposer sa fille [nomFianceeArgent] en mariage."
    "C'est tout de même un grand honneur et une occasion à saisir. Leur famille est très riche et puissante. Une union entre eux et vous serait à n'en pas douter l'occasion de renforcer votre position à tous et de garantor l'avenir du village."
    "Seulement ces calculs ne suivent pas le désir réel de votre coeur. Vous étiez en effet sur le point d'avouer vos sentiments et votre désir de mariage à la belle [nomFianceeAmour]."
    $ renpy.show(fianceeAmourImg, [right])
    with moveinright
    menu:
        "Toujours les nobles élans du coeur doivent prendre le pas sur le froid calcul. Vous faites votre déclaration à [nomFianceeAmour].":
            "Elle accepte et vous vous mariez heureux. Au pris du ressentiment des nobles de la tribu."
            $ AjouterACarac(peuple.Peuple.C_SENSUALITE, 0.1)
            $ AjouterAAffinite(civ.Francais.NOM, 0.3)
            $ RetirerACarac(peuple.Peuple.C_COHESION, 0.1)
        "Le corps et le coeur doivent se soumettre à la raison et au bien de la tribu. Vous acceptez le marriage avec [nomFianceeArgent]":
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.3)
        "Le plaisir des sens est indigne du sage ascète que vous êtes. Vous choisissez le célibat.":
            $ AjouterAAffinite(civ.Christianisme.NOM, 0.4)
            $ RetirerACarac(peuple.Peuple.C_SENSUALITE, 0.3)
        "Pourquoi choisir ? En tant que figure morale des [nomPeuple] vous a^pprouvez la polygamie et épousez [nomFianceeAmour] et [nomFianceeArgent]":
            $ AjouterACarac(peuple.Peuple.C_SENSUALITE, 0.3)

    jump fin_cycle
