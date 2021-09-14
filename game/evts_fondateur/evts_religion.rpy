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
    ameApresLaMortPasFait = condition.Condition("ameApresLaMort", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsReligieux():
        global selecteur_
        # création de religion
        creationReligion = declencheur.Declencheur(proba.Proba(0.5, True), "creationReligion")
        creationReligion.AjouterConditions([estEnModeFondateur, aPasDeReligion, creationReligionPasFait])
        selecteur_.ajouterDeclencheur(creationReligion)

        ameApresLaMort = declencheur.Declencheur(proba.Proba(0.1, True), "ameApresLaMort")
        ameApresLaMort.AjouterConditions([estEnModeFondateur, aUneReligion, estPasAthee, ameApresLaMortPasFait])
        selecteur_.ajouterDeclencheur(ameApresLaMort)

label ameApresLaMort:
    $ situation_.SetValCarac("ameApresLaMort", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "Le doute et la peur se répandent parmi les [nomPeuple]. Pitié [titreFondateur], dites nous ce qui arrive aux âmes des morts."
    menu:
        "L'âme n'existe pas. Tout est corporel et matériel.":
            $ RetirerACaracPos(peuple.Peuple.C_SPIRITUALITE, 0.2)
        "L'âme à la mort se réincarne dans le corps d'un nouvel être vivant en train de naître.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SPIRITUALITE, 0.5) # le plus haut pour moi car rapproche de tous les êtres vivants et d'un grand cycle mais bon, jsuis peut-être pas objectif...
        "À notre mort notre âme s'envole vers l'au delà.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SPIRITUALITE, 0.3)

    jump fin_cycle
    
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
