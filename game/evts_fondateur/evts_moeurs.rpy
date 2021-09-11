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
    from spe.civilisation import romains

    # simples marqueurs de fait/pas fait des événements
    habillementEtDecencePasFait = condition.Condition("habillementEtDecence", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsMoeursF():
        global selecteur_

        habillementEtDecence = declencheur.Declencheur(proba.Proba(0.1, True), "habillementEtDecence")
        habillementEtDecence.AjouterConditions([estEnModeFondateur, habillementEtDecencePasFait])
        selecteur_.ajouterDeclencheur(habillementEtDecence)

label habillementEtDecence:
    $ situation_.SetValCarac("habillementEtDecence", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomVieilleDame = civRef.GenererPatronyme(False)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomVieilleDame)
    $ imgVieilleDame = civRef.GenererImagePerso(False, 50)
    $ renpy.show(imgVieilleDame, [right])
    with moveinright
    std "[titreFondateur], les gens et particulièrement les jeunes s'habillent et se comportent de manière particulièrement indécente."
    std "Cette vulgarité et ce manque de modestie a déjà causé des incidents, et cela insupporte de plus en plus de gens."
    menu:
        "Le corps humain est magnifique et nous devrions le montrer  avec fierté et le regarder sans honte.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SENSUALITE, 0.3)
            $ AjouterACaracIdentite(peuple.Peuple.C_LIBERTE, 0.3)
        "Les gens peuvent s'habiller comme bon leur semble.":
            $ AjouterACaracIdentite(peuple.Peuple.C_LIBERTE, 0.4)
        "Les gens peuvent s'habiller comme ils le souhaitent mais doivent faire preuve de pudeur dans les lieux de culte et d'enseignement.":
            pass
        "Hommes comme femmes se doivent d'être habillés dignement et avec pudeur.":
            $ RetirerACaracPos(peuple.Peuple.C_LIBERTE, 0.1)
            $ RetirerACaracPos(peuple.Peuple.C_SENSUALITE, 0.1)
        "Les femmes en particulier doivent faire preuve de plus de pudeur. Cela suffira à calmer les tensions.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SEXISME, 0.2)
            $ RetirerACaracPos(peuple.Peuple.C_LIBERTE, 0.1)
            $ RetirerACaracPos(peuple.Peuple.C_SENSUALITE, 0.1)

    jump fin_cycle
