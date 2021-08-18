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
    droitSculpturePasFait = condition.Condition("droitSculpture", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsArt():
        global selecteur_

        droitSculpture = declencheur.Declencheur(proba.Proba(0.1, True), "droitSculpture")
        droitSculpture.AjouterCondition(estEnModeFondateur)
        droitSculpture.AjouterCondition(estPasAthee)
        droitSculpture.AjouterCondition(droitSculpturePasFait)
        selecteur_.ajouterDeclencheur(droitSculpture)

label droitSculpture:
    $ situation_.SetValCarac("droitSculpture", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomPerso)
    std "Des gens inspirés façonnent la pierre avec des outils pour former des figures. Ils veulent honorer la divinité en la représentant mais n'osent le faire sans votre assentiment."

    menu:
        "C'est hors de question. Aucune figure humaine ou divine ne doit être représentée et encore moins vénérée.":
            $ AjouterAAffinite(civ.Juive.NOM, 0.3)
            $ AjouterAAffinite(civ.Arabe.NOM, 0.3)
            $ RetirerACarac(peuple.Peuple.C_CREATIVITE, -0.1)
        "La divinité a des avatars humains parfaits que vous pouvez représenter.":
            $ AjouterAAffinite(civ.Grecque.NOM, 0.3)
            $ RetirerACarac(peuple.Peuple.C_CREATIVITE, 0.3)

    jump fin_cycle
