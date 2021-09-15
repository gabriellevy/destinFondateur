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

    siNonSouverain = condition.Condition(peuple.Peuple.C_SOUV, peuple.Peuple.MINORITE, condition.Condition.DIFFERENT)
    # simples marqueurs de fait/pas fait des événements
    choixRoiPasFait = condition.Condition("choixRoi", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsPouvoirF():
        global selecteur_

        choixRoi = declencheur.Declencheur(proba.Proba(0.1, True), "choixRoi")
        choixRoi.AjouterConditions([estEnModeFondateur, choixRoiPasFait, siNonSouverain])
        selecteur_.ajouterDeclencheur(choixRoi)

label choixRoi:
    $ situation_.SetValCarac("choixRoi", "1")
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ civRef = situation_.GetCivilisationDeReference()
    $ estMale = random.uniform(0, 1.0) > 0.5
    $ nomPerso = civRef.GenererPatronyme(estMale)
    $ imgPerso = civRef.GenererImagePerso(estMale, 50) # homme de 50 ans
    $ std = Character(nomPerso)
    $ renpy.show(imgPerso, [right])
    with moveinright
    std "[titreFondateur], vous êtes notre Guide et nous suivons vos commandements, mais nous avons aussi besoin de l'autorité d'un roi qui nous mènera à la guerre et rendra la justice."
    std "Comment choisir qui sera digne de cet honneur ? Quel est le meilleur moyen de conserver de l'autorité sur les hommes ? "

    $ estPasAthee = situation_.GetValCarac(religion.Religion.C_RELIGION) != religion.Atheisme.NOM
    menu:
        "Cherchez la personne dont les ancêtres sont les plus glorieux.":
            $ AjouterACaracIdentite(peuple.Peuple.C_CLASSE, 0.3)
        "Le plus fort doit régner":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.3)
        "Le plus riche doit régner. Lui seul aura l'influence nécessaire.":
            $ AjouterACaracIdentite(peuple.Peuple.C_ARGENT, 0.3)
        "Le roi doit être le préféré du peuple ou au moins des classes supérieures, et doit être alu par eux.":
            $ AjouterACaracIdentite(peuple.Peuple.C_LEGALISME, 0.3)
            $ AjouterACaracIdentite(peuple.Peuple.C_LIBERTE, 0.1)
        "Le roi est le serviteur de la divinité sur terre. Écoutez les prêtres et les oracles. Ce sont eux qui le trouveront." if estPasAthee:
            $ AjouterACaracIdentite(peuple.Peuple.C_SPIRITUALITE, 0.3)

    jump fin_cycle
