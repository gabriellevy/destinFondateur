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
    def AjouterEvtsFamilleF():
        global selecteur_
        # mariage
        mariageFondateur = declencheur.Declencheur(proba.Proba(0.5, True), "mariageFondateur")
        mariageFondateur.AjouterCondition(estEnModeFondateur)
        mariageFondateur.AjouterCondition(mariageFondateurPasFait)
        mariageFondateur.AjouterCondition(siTribue)
        selecteur_.ajouterDeclencheur(mariageFondateur)

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
        "Le cortps et le coeur doivent se soumettre à la raison et au bien de la tribu. Vous acceptez le marriage avec [nomFianceeArgent]":
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.3)
        "Le plaisir des sens est indigne du sage ascète que vous êtes. Vous choisissez le célibat.":
            $ AjouterAAffinite(civ.Christianisme.NOM, 0.4)
            $ RetirerACarac(peuple.Peuple.C_SENSUALITE, 0.3)
        "Pourquoi choisir ? En tant que figure morale des [nomPeuple] vous a^pprouvez la polygamie et épousez [nomFianceeAmour] et [nomFianceeArgent]":
            $ AjouterACarac(peuple.Peuple.C_SENSUALITE, 0.3)

    jump fin_cycle
