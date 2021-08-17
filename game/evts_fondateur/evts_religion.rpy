

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
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "Un jour [nomPerso] vient vous voir tandis que vous méditez dans une clairière."
    $ std = Character(nomPerso)
    std "Mes excuses pour l'interruption [titreFondateur]. Mais de graves troubles secouent le peuple"
    std "Certains adorent des dieux sculptés, d'autres la nature, d'autres le destin, d'autres encore méprisent toutes les croyances et s'attirent la haine des fidèles."
    std "Dans votre sagesse la véritable nature de la divinité doit vous avoir été révélée. Quelle est-elle ?"
    menu:
        "Les dieux sont multiples et omniprésents.":
            $ situation_.SetValCarac( religion.Religion.C_RELIGION, religion.Polytheiste.NOM)
        "Il n'y a qu'un seul Dieu et nous sommes son peuple élu. Les autres ne sont que poussière.":
            $ situation_.SetValCarac( religion.Religion.C_RELIGION, religion.Monotheiste.NOM)
            $ AjouterACarac(peuple.Peuple.C_COHESION, 0.1)
        "La divinité n'existe pas. Seuls règnent le hasard et la volonté.":
            $ situation_.SetValCarac( religion.Religion.C_RELIGION, religion.Atheisme.NOM)
            $ RetirerACarac(peuple.Peuple.C_COHESION, 0.02)

    jump fin_cycle
