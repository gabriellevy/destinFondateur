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

    def AjouterEvtsMetiersF():
        global selecteur_

        metierLePlusImportant = declencheur.Declencheur(proba.Proba(0.1, True), "metierLePlusImportant")
        metierLePlusImportant.AjouterConditions([estEnModeFondateur])
        selecteur_.ajouterDeclencheur(metierLePlusImportant)

label metierLePlusImportant:
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)

    $ sexeVillageois1 = random.uniform(0, 1.0) > 0.5
    $ nomVillageois1 = civRef.GenererPatronyme(sexeVillageois1)
    $ std = Character(sexeVillageois1)
    $ imgVillageois1 = civRef.GenererImagePerso(sexeVillageois1, 15, [])

    $ sexeVillageois2 = random.uniform(0, 1.0) > 0.5
    $ nomVillageois2 = civRef.GenererPatronyme(sexeVillageois2)
    $ std2 = Character(sexeVillageois2)
    $ imgVillageois2 = civRef.GenererImagePerso(sexeVillageois2, 25, [imgVillageois1])

    $ sexeVillageois3 = random.uniform(0, 1.0) > 0.5
    $ nomVillageois3 = civRef.GenererPatronyme(sexeVillageois3)
    $ std3 = Character(sexeVillageois3)
    $ imgVillageois3 = civRef.GenererImagePerso(sexeVillageois3, 35, [imgVillageois1, imgVillageois2])

    $ sexeVillageois4 = random.uniform(0, 1.0) > 0.5
    $ nomVillageois4 = civRef.GenererPatronyme(sexeVillageois4)
    $ std4 = Character(sexeVillageois4)
    $ imgVillageois4 = civRef.GenererImagePerso(sexeVillageois4, 45, [imgVillageois1, imgVillageois2, imgVillageois3])

    $ sexeVillageois5 = random.uniform(0, 1.0) > 0.5
    $ nomVillageois5 = civRef.GenererPatronyme(sexeVillageois5)
    $ std5 = Character(sexeVillageois5)
    $ imgVillageois5 = civRef.GenererImagePerso(sexeVillageois5, 55, [imgVillageois1, imgVillageois2, imgVillageois3, imgVillageois4])

    "Une grande discussion anime les villageois depuis des heures au marche. Ils sont maintenant si échauffés qu'on demande votre venue sur place pour arbitrer."
    $ renpy.show(imgVillageois1, at_list=[tout_a_droite])
    std "Les paysans sont les gens les plus importants car sans la nourriture qu'ils produisent nous mourrions tous de faim."

    $ renpy.show(imgVillageois2, at_list=[a_gauche])
    std2 "Les paysans ont l'air fin quand l'ennemi attaque. Heureusement que nos guerriers sont là pour sauver la mise."

    $ renpy.show(imgVillageois3, at_list=[tout_a_gauche])
    std3 "Et comment le village survivrait-il sans les sages et érudits qui rendent la justice, guident le peuple, préservent le village du chaos ?"

    $ renpy.show(imgVillageois4, at_list=[a_droite])
    std4 "Certes tout celà est important mais à quoi bon vivre sans la poésie des bardes dont la voix est si enivrante lorsqu'ils chantent les exploits de nos ancêtres ?"

    $ renpy.show(imgVillageois5, at_list=[un_peu_a_droite])
    std5 "À quoi bon l'art et même la nourriture si els dieux sont contre nous ? Les prêtres sont les prmeiers des hommes."

    menu:
        "Quel est le métier le plus important ?"
        "L'artiste":
            $ AjouterACaracIdentite(peuple.Peuple.C_CREATIVITE, 0.2)
        "Le paysan":
            pass
        "Le soldat":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.2)
        "Le sage":
            $ AjouterACaracIdentite(peuple.Peuple.C_INTEL, 0.2)
        "Les prêtres":
            $ AjouterACaracIdentite(peuple.Peuple.C_SPIRITUALITE, 0.2)
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_THEOCRATIE, 0.2)

    jump fin_cycle
