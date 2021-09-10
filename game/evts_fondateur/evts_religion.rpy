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

    creationReligionPasFait = condition.Condition("creationReligion", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsReligieux():
        global selecteur_
        # création de religion
        creationReligion = declencheur.Declencheur(proba.Proba(0.5, True), "creationReligion")
        creationReligion.AjouterConditions([estEnModeFondateur, aPasDeReligion, creationReligionPasFait])
        selecteur_.ajouterDeclencheur(creationReligion)

label creationReligion:
    $ situation_.SetValCarac("creationReligion", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ persoImg = civRef.GenererImagePerso(True, 30)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "Un jour [nomPerso] vient vous voir tandis que vous méditez dans une clairière."
    $ renpy.show(persoImg, [right])
    with moveinright
    $ std = Character(nomPerso)
    std "Mes excuses pour l'interruption [titreFondateur]. Mais de graves troubles secouent le peuple"
    std "Certains adorent des dieux sculptés, d'autres la nature, d'autres le destin, d'autres encore méprisent toutes les croyances et s'attirent la haine des fidèles."
    std "Dans votre sagesse la véritable nature de la divinité doit vous avoir été révélée. Quelle est-elle ?"
    menu:
        "Les dieux sont multiples et omniprésents.":
            $ situation_.SetValCarac( religion.Religion.C_RELIGION, religion.Polytheiste.NOM)
        "Il n'y a qu'un seul Dieu et nous sommes son peuple élu. Les autres ne sont que poussière.":
            $ situation_.SetValCarac( religion.Religion.C_RELIGION, religion.Monotheiste.NOM)
            $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.1)
            $ RetirerACaracPos(peuple.Peuple.C_COOPERATION, 0.3)
            $ AjouterAAffinite(civ.Juive.NOM, 0.5)
        "La divinité n'existe pas. Seuls règnent le hasard et la volonté.":
            $ situation_.SetValCarac( religion.Religion.C_RELIGION, religion.Atheisme.NOM)
            $ RetirerACaracPos(peuple.Peuple.C_COHESION, 0.02)

    jump fin_cycle
