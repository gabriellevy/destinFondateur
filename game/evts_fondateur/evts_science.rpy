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

    # simples marqueurs de fait/pas fait des événements
    inventionEcriturePasFait = condition.Condition("inventionEcriture", "1", condition.Condition.DIFFERENT)
    anneeInf100 = condition.Condition(temps.Date.DATE_ANNEES, "100", condition.Condition.INFERIEUR)
    def AjouterEvtsScience():
        global selecteur_

        inventionEcriture = declencheur.Declencheur(proba.Proba(0.2, True), "inventionEcriture")
        inventionEcriture.AjouterCondition(estEnModeFondateur)
        inventionEcriture.AjouterCondition(inventionEcriturePasFait)
        inventionEcriture.AjouterCondition(anneeInf100)
        selecteur_.ajouterDeclencheur(inventionEcriture)

label inventionEcriture:
    $ situation_.SetValCarac("inventionEcriture", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomPerso)
    $ plaignantImg = civRef.GenererImagePerso(True, 50)
    $ renpy.show(plaignantImg, [right])
    with moveinright
    std "[titreFondateur], j'ai personnellement vu des érudits étrangers qui dessinent des symboles sur des surfaces comme la pierre ou la cire et s'en servent pour mémoriser des choses et des chiffres."
    std "Je pense qu'adopter ce système et aller observer comment il fonctionne pourrait nous être très utile."
    menu:
        "Étonnante idée. Nous devons développer cette technique et l'utiliser autant que possible..":
            $ AjouterACarac(peuple.Peuple.C_INTEL, 0.5)
        "C'est intreéssant, nous devrions l'utiliser pour nous organiser et compter.":
            pass
        "Tout cela n'est que perte de temps et mépris de nos bonnes et solides mémoires qui nous ont toujours bien servi et continuerons de le faire.":
            $ RetirerACarac(peuple.Peuple.C_INTEL, 0.5)
            $ AjouterAAffinite(civ.Celte.NOM, 0.3)

    jump fin_cycle
