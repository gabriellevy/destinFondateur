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

label changementCivRef:
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomCiv = civRef.nom_
    "La civilisation [nomCiv] est devenu dominante parmi les [nomPeuple]."
    $ renpy.run(gui.SetPreference("font", civRef.GetPolice(), True))
    $ RetirerACaracPos(peuple.Peuple.C_COHESION, 0.5)

    jump fin_cycle
