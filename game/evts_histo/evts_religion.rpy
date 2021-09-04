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

    arriveeChristianismePasFait = condition.Condition("arriveeChristianisme", "1", condition.Condition.DIFFERENT)
    anneeSup100 = condition.Condition(temps.Date.DATE_ANNEES, "100", condition.Condition.SUPERIEUR)
    def AjouterEvtsReligieuxH():
        global selecteur_
        # création de religion
        arriveeChristianisme = declencheur.Declencheur(proba.Proba(0.1, True), "arriveeChristianisme")
        arriveeChristianisme.AjouterConditions([estEnModeHisto, anneeSup100, arriveeChristianismePasFait, estPasChretien])
        selecteur_.ajouterDeclencheur(arriveeChristianisme)

label arriveeChristianisme:
    $ situation_.SetValCarac("arriveeChristianisme", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    "La religion chrétienne se propage partout. Elle devient un sujet récurrent dans le peuple des [nomPeuple]."
    $ spiritualite = situation_.GetValCarac(peuple.Peuple.C_SPIRITUALITE) # AFAIRE : au lieu de juste la spiritualité ce serazit logique de tester aussi l'afinité avec christianisme
    $ violence = situation_.GetValCarac(peuple.Peuple.C_VIOLENCE)
    if spiritualite < 0.1:
        "Mais les [nomPeuple] ont la tête bien sur les épaules et bien peu prennent au sérieux cette étrange religion."
    elif spiritualite < 0.7:
        "Les missionnaires chrétiens font de nombreuses conversions parmi les vôtres. Les classes supérieures sont perplexes sur la conduite à adopter."
        $ AjouterACaracCiv(civ.Christianisme.NOM, 0.3)
        if violence > 0.5:
            "Devant le refus des chrétiens d'honorer les vrais dieux, des [nomPeuple] perdent patience et des émeutes éclatent."
            "Beaucoup de chrétiens et plusieurs de leurs missionnaires sont massacrés. Cela semble néanmoins avoir peut d'effet sur leur ferveur"
            $ RetirerACarac(civ.Christianisme.NOM, 0.3)
            $ RetirerAPopulationPourcent(1)
    else:
        "Les [nomPeuple] embrasse avec ferveur la nouvelle religion et a tôt fait de mélanger ss anciennes croyances avec la nouvelle bien plus parfaite foi."
        $ AjouterACaracCiv(civ.Christianisme.NOM, 0.6)


    jump fin_cycle
