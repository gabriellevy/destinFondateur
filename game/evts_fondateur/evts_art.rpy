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
    parurePasFait = condition.Condition("parure", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsArt():
        global selecteur_

        droitSculpture = declencheur.Declencheur(proba.Proba(0.1, True), "droitSculpture")
        droitSculpture.AjouterConditions([estEnModeFondateur, estPasAthee, droitSculpturePasFait])
        selecteur_.ajouterDeclencheur(droitSculpture)

        parure = declencheur.Declencheur(proba.Proba(0.1, True), "parure")
        parure.AjouterConditions([estEnModeFondateur, parurePasFait])
        selecteur_.ajouterDeclencheur(parure)

label parure:
    $ situation_.SetValCarac("parure", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ imgPerso = civRef.GenererImagePerso(True, 50, []) # homme de 50 ans
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomPerso)
    $ renpy.show(imgPerso, [right])
    with moveinright
    std "Pardonnez moi de vous ennuyer avec des futilités, [titreFondateur], mais une habitude se développe parmi nos jeunes gens surtout mais même parmi le peuple tout entier."
    std "Il s'agit de se décorer le corps avec des symboles et surtout des bijoux créés par des artisans."
    std "Cet art a un tel succès que l'ornement devient la principale activité de nos jeunes gens, au point que nous commençons à craindre qu'il les rende futiles et sans profondeur d'esprit."

    menu:
        "La beauté de nos créations est un hommage à celle de la nature. Cet art est noble en soit et doit être encouragé.":
            $ AjouterACaracIdentite(peuple.Peuple.C_CREATIVITE, 0.3)
        "L'excès de coquetterie mène à l'orgueuil et à la faiblesse. Un bijou doit se mériter, se gagner par un rite, et représenter la place de son possesseur dans la tribu.":
            $ AjouterACaracIdentite(peuple.Peuple.C_CREATIVITE, 0.1)
            $ AjouterACaracInf1(peuple.Peuple.C_COHESION, 0.2)
        "La parure est une marque d'orgueil ridicule.":
            $ RetirerACaracPos(peuple.Peuple.C_CREATIVITE, 0.2)
        "La parure est naturelle et compréhensible chez la jeune fille, mais ridicule ailleurs.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SEXISME, 0.3)

    jump fin_cycle

label droitSculpture:
    $ situation_.SetValCarac("droitSculpture", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPerso = civRef.GenererPatronyme(True)
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomPerso)
    std "Des gens inspirés façonnent la pierre avec des outils pour former des figures. Ils veulent honorer la divinité en la représentant mais n'osent le faire sans votre assentiment."

    menu:
        "C'est hors de question. Aucune figure humaine ou divine ne doit être représentée et encore moins vénérée.":
            $ RetirerACaracPos(peuple.Peuple.C_CREATIVITE, 0.1)
        "La divinité a des avatars humains parfaits que vous pouvez représenter.":
            $ RetirerACaracPos(peuple.Peuple.C_CREATIVITE, 0.3)

    jump fin_cycle
