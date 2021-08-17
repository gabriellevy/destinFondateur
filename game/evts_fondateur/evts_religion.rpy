

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

    estEnModeFondateur = condition.Condition(situation_fondateur.SituationFondateur.C_MODE, situation_fondateur.SituationFondateur.C_MODE_FONDATEUR, condition.Condition.EGAL)
    creationReligionPasFait = condition.Condition("creationReligion", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsReligieux():
        global selecteur_
        # création de religion
        creationReligion = declencheur.Declencheur(proba.Proba(0.5, True), "creationReligion")
        creationReligion.AjouterCondition(estEnModeFondateur)
        creationReligion.AjouterCondition(aPasDeReligion)
        creationReligion.AjouterCondition(creationReligionPasFait)
        selecteur_.ajouterDeclencheur(creationReligion)

label creationReligion:
    # s'entraîne au combat
    $ situation_.SetValCarac("creationReligion", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    " ------------------------------> création de religion"
    "Un jour [nomPerso] vient vous voir tandis que vous méditez dans une clairière."
    $ std = Character(nomPerso)
    std "Mes excuses pour l'interruption"



    $ AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle
