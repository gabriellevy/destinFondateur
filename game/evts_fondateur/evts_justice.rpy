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
    from spe.civilisation import celtes
    from spe.region import geo

    def AjouterEvtsJusticeF():
        global selecteur_

        ruseEtForce = declencheur.Declencheur(proba.Proba(0.1, True), "ruseEtForce")
        ruseEtForce.AjouterConditions([ estEnModeFondateur])
        selecteur_.ajouterDeclencheur(ruseEtForce)

        enlevementEtViol = declencheur.Declencheur(proba.Proba(0.1, True), "enlevementEtViol")
        enlevementEtViol.AjouterConditions([ estEnModeFondateur])
        selecteur_.ajouterDeclencheur(enlevementEtViol)

        punitionMeurtre = declencheur.Declencheur(proba.Proba(0.1, True), "punitionMeurtre")
        punitionMeurtre.AjouterConditions([ estEnModeFondateur])
        selecteur_.ajouterDeclencheur(punitionMeurtre)

        jugementPourDette = declencheur.Declencheur(proba.Proba(0.1, True), "jugementPourDette")
        jugementPourDette.AjouterConditions([ estEnModeFondateur])
        selecteur_.ajouterDeclencheur(jugementPourDette)

        choixDesJuges = declencheur.Declencheur(proba.Proba(0.1, True), "choixDesJuges")
        choixDesJuges.AjouterConditions([ estEnModeFondateur, siTribue])
        selecteur_.ajouterDeclencheur(choixDesJuges)

label choixDesJuges:
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)

    "[titreFondateur], de nombreuses personnes revendiquent le droit de juger les délits commis et de prononcer les punitions."
    "C'est particulièrement ennuyeux quand les plaignants ne sont pas du même clan. Après vous, qui devrait avoir la plus haute autorité de juge ?"
    $ estPasAthee = situation_.GetValCarac(religion.Religion.C_RELIGION) != religion.Atheisme.NOM
    menu:
        "les prêtres sont les juges de dernier recours, les dieux parleront à travers eux." if estPasAthee:
            $ AjouterACaracIdentite(peuple.Peuple.C_INTEL, 0.1)
            $ AjouterACaracIdentite(peuple.Peuple.C_SPIRITUALITE, 0.1)

        "Les nobles car leur force militaire seule fera que leurs décisions seront respectées":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.1)

        "Les juges doivent être choisis par le peuple. Ainsi il acceptera mieux les sentences.":
            $ AjouterACaracIdentite(peuple.Peuple.C_LEGALISME, 0.1)
            $ AjouterACaracIdentite(peuple.Peuple.C_LIBERTE, 0.1)
            $ AjouterACaracIdentite(peuple.Peuple.C_COOPERATION, 0.1)

        "Les grands propriétaires doivent prononcer les jugements car leur richesse est preuve de leur discernement.":
            $ AjouterACaracIdentite(peuple.Peuple.C_ARGENT, 0.1)
            $ AjouterACaracIdentite(peuple.Peuple.C_INTEL, 0.1)

    jump fin_cycle

label jugementPourDette:
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)

    $ nomCriminel = civRef.GenererPatronyme(True)
    $ nomRapporteur = civRef.GenererPatronyme(True)
    $ imgRapporteur = civRef.GenererImagePerso(True, 40, [])
    $ std = Character(nomRapporteur)
    $ renpy.show(imgRapporteur, [right])
    with moveinright
    std "[titreFondateur], je suis désemparé. [nomCriminel] me doit trois têtes de bétail et refuse de me les rendre."
    std "Il sait qu'il est plus puissant et plus respecté que moi dans le clan, et que personne ne m'aidera contre lui. Que faire ?"
    menu:
        "Affronte le face à face en guerrier.":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.2)

        "Va devant sa porte et jeûne au vu et au su de tout le village. Il devra intervenir pour téviter la mort ou verra son honneur terni pour toujours.":
            $ AjouterACaracIdentite(peuple.Peuple.C_ENDURANCE, 0.2)

    jump fin_cycle

label punitionMeurtre:
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ nomCriminel = civRef.GenererPatronyme(True)
    $ imgCriminel = civRef.GenererImagePerso(True, 40, [])
    $ nomVictime = civRef.GenererPatronyme(False)
    $ nomClanVictime = civRef.GenererNomPeuple()
    $ nomRapporteur = civRef.GenererPatronyme(True)
    $ imgRapporteur = civRef.GenererImagePerso(True, 40, [imgCriminel])
    $ std = Character(nomRapporteur)
    $ renpy.show(imgRapporteur, [right])
    with moveinright
    std "[titreFondateur], un grave crime a eu lieu. [nomCriminel] a pénétré chez les [nomClanVictime] pour les voler."
    std "Et quand il a été surpris par la vieille [nomClanVictime] il l'a frappée avec un vase et s'est enfui. La malheureuse vient de mourir de ses blessures."
    std "[nomCriminel] a été capturé peu après par la famille de la victime qui réclame justice mais a préféré attendre votre approbation avant d'agir."

    $ std2 = Character(nomCriminel)
    $ renpy.show(imgCriminel, [left])
    with moveinleft
    std2 "Pitié je voulais simplement voler de quoi nourrir mes enfants. Je n'ai jamais voulu faire de mal à qui que ce soit."
    std "Silence [nomCriminel], tu seras peut-être autorisé à parler quand [titreFondateur] aura rendu sa sentence."
    std2 "..."
    menu:
        "Oeil pour oeil dent pour dent. Éxécutez le.":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.1)
            $ AjouterACaracIdentite(peuple.Peuple.C_ENDURANCE, 0.1)

        "Cet homme est maintenant l'esclave de la famille de la victime. Il travaillera pour réparer le mal qu'il a fait.":
            $ RetirerACaracPos(peuple.Peuple.C_LIBERTE, 0.1)
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_CLANIQUE, 0.4)

        "Je ne peux juger seul. Une assemblée de sages déterminera sa punition.":
            $ AjouterACaracIdentite(peuple.Peuple.C_LEGALISME, 0.3)

        "Je lui pardonne son erreur. Dieu le jugera.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SPIRITUALITE, 0.1)

        "[nomCriminel] doit payer l'amende pour homicide convenue à la famille de [nomVictime]":
            $ AjouterACaracIdentite(peuple.Peuple.C_ARGENT, 0.3)

    jump fin_cycle

label enlevementEtViol:
    # NOTE : un joueur standard pensera à la prison. Mais cela n'existait pas à l'époque. Ajouter un choix couteux de ce genre ? Expliqueur ce détail d'une manière détournée ?
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomEnleveur = civRef.GenererPatronyme(True)
    $ nomEnlevee = civRef.GenererPatronyme(False)
    $ nomRapporteur = civRef.GenererPatronyme(True)
    $ imgRapporteur = civRef.GenererImagePerso(True, 50, [])
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ std = Character(nomRapporteur)
    $ renpy.show(imgRapporteur, [right])
    with moveinright
    std "[nomEnleveur] a enlevé la jeune [nomEnlevee] et l'a déshonorée. La famille est furieuse et nous sommes au bord d'un règlement de compte sanglant entre clans."
    std "Quel est le meilleur moyen de régler la situation ?"
    menu:
        "Exécuter le ravisseur.":
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.2)
            # A FAIRE : ajouter une deuxième partie au dialogue où il se révèle qu'elle était consentente et est-ce que ça change quelque chose ?
        "Forcer le ravisseur à épouser la victime.":
            $ AjouterACaracIdentite(peuple.Peuple.C_SEXISME, 0.3)
            $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.1)
        "Obliger le ravisseur à payer un lourd dédommagement à la famille de la victime.":
            $ AjouterACaracIdentite(peuple.Peuple.C_ARGENT, 0.2)

    jump fin_cycle

label ruseEtForce:
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomPersoTueur = civRef.GenererPatronyme(True)
    $ nomPersoJuge = civRef.GenererPatronyme(True)
    $ nomPersoVictime = civRef.GenererPatronyme(True)
    $ nomPersoTueurImg = civRef.GenererImagePerso(True, 30, [])
    $ nomPersoJugeImg = civRef.GenererImagePerso(True, 30, [nomPersoTueurImg])
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    "[nomPersoTueur] et [nomPersoJuge] débattent depuis des heures d'une grave affaire de morale."
    $ renpy.show(nomPersoJugeImg, [left])
    with moveinleft
    $ renpy.show(nomPersoTueurImg, [right])
    with moveinright
    $ std = Character(nomPersoJuge)
    $ std2 = Character(nomPersoTueur)
    std "D'accord, [nomPersoVictime] t'avais volé et offensé et tu étais en droit de te venger mais l'empoisonner est traître et déloyal. Un homme se doit de défier son ennemi en face."
    std2 "En plus d'être malhonnête et cruel [nomPersoVictime] était un puissant guerrier et m'aurait à coup sûr battu. Seule la ruse pouvait me permettre de restaurer mon honneur."
    std "Peu importe ton avis, [titreFondateur] décidera de ta punition."
    menu:
        "L'honneur réside dans la force et le courage. [nomPersoTueur] a eu tort et sera puni.":
            $ RetirerACaracPos(peuple.Peuple.C_VIOLENCE, 0.3)
        "Seule la réussite compte. [nomPersoTueur] était dans son droit et a bien agi.":
            $ AjouterACaracIdentite(peuple.Peuple.C_INTEL, 0.3)
        "Nul ne doit se venger sans consulter un sage qui déterminera les fautes et les punitions. [nomPersoTueur] sera jugé pour son crime.":
            $ AjouterACaracIdentite(peuple.Peuple.C_LEGALISME, 0.3)

    jump fin_cycle
