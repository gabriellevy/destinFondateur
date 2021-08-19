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

    ruseEtForcePasFait = condition.Condition("ruseEtForce", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsJustice():
        global selecteur_
        # tenté par l'aventure marine ?
        ruseEtForce = declencheur.Declencheur(proba.Proba(0.1, True), "ruseEtForce")
        ruseEtForce.AjouterCondition(estEnModeFondateur)
        ruseEtForce.AjouterCondition(aventurierDesMersPasFait)
        selecteur_.ajouterDeclencheur(ruseEtForce)

label ruseEtForce:
    $ situation_.SetValCarac("ruseEtForce", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPersoTueur = civRef.GenererPatronyme(True)
    $ nomPersoJuge = civRef.GenererPatronyme(True)
    $ nomPersoVictime = civRef.GenererPatronyme(True)
    $ nomPersoTueurImg = civRef.GenererImagePerso(True, 30)
    $ nomPersoJugeImg = civRef.GenererImagePerso(True, 30)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "[nomPersoTueur] et [nomPersoJuge] débattent depuis des heures d'une grave affaire de morale."
    $ renpy.show(nomPersoJugeImg, [left])
    with moveinleft
    $ renpy.show(nomPersoTueurImg, [right])
    with moveinright
    $ std = Character(nomPersoJuge)
    $ std2 = Character(nomPersoTueur)
    std "D'accord, [nomPersoVictime] t'avais volé et offensé et tu étais en droit de te venger mais l'empoisonner est traître et déloyal. Un homme se doit de défier son ennemi en face."
    std2 "En plus d'être malhonnête et cruel [nomPersoVictime] était un puissant guerrier et m'aurait à coup sûr battu. Seule la ruse pouvait me permettre de restaurer mon honneur."
    std "Peu importe ton avis, [titreFondateur] décidera de ta punition."
    menu:
        "L'honneur réside dans la force et le courage. [nomPersoTueur] a eu tort et sera puni.":
            $ RetirerACarac(peuple.Peuple.C_VIOLENCE, 0.3)
            $ AjouterAAffinite(civ.Celte.NOM, 0.2)
            $ AjouterAAffinite(civ.Germanique.NOM, 0.2)
        "Seule la réussite compte. [nomPersoTueur] était dans son droit et a bien agi.":
            $ AjouterACarac(peuple.Peuple.C_INTEL, 0.3)
        "Nul ne doit se venger sans consulter un sage qui déterminera les fautes et les punitions. [nomPersoTueur] sera jugé pour son crime.":
            $ AjouterACarac(peuple.Peuple.C_LEGALISME, 0.3)

    jump fin_cycle
