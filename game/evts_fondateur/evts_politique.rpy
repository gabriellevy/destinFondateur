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

    siNonSouverain = condition.Condition(peuple.Peuple.C_SOUV, peuple.Peuple.MINORITE, condition.Condition.EGAL)
    siSouverain = condition.Condition(peuple.Peuple.C_SOUV, peuple.Peuple.MINORITE, condition.Condition.DIFFERENT)
    # simples marqueurs de fait/pas fait des événements
    choixRoiPasFait = condition.Condition("choixRoi", "1", condition.Condition.DIFFERENT)
    fideliteClanPeuplePasFait = condition.Condition("fideliteClanPeuple", "1", condition.Condition.DIFFERENT)
    def AjouterEvtsPouvoirF():
        global selecteur_

        choixRoi = declencheur.Declencheur(proba.Proba(0.1, True), "choixRoi")
        choixRoi.AjouterConditions([estEnModeFondateur, choixRoiPasFait, siNonSouverain])
        selecteur_.ajouterDeclencheur(choixRoi)

        fideliteClanPeuple = declencheur.Declencheur(proba.Proba(0.1, True), "fideliteClanPeuple")
        fideliteClanPeuple.AjouterConditions([estEnModeFondateur, fideliteClanPeuplePasFait, siSouverain])
        selecteur_.ajouterDeclencheur(fideliteClanPeuple)

label fideliteClanPeuple:
    $ situation_.SetValCarac("fideliteClanPeuple", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)

    $ nomPerso = civRef.GenererPatronyme(True)
    $ nomFamille = civRef.GenererNomPeuple()
    $ imgPerso = civRef.GenererImagePerso(True, 17, [])
    $ std = Character(nomPerso)
    $ renpy.show(imgPerso, [right])
    with moveinright
    "Tout le village est agité. Un membre de la puissante famille de [nomFamille] a tué traitreusement un des [nomPeuple]. On craint une feude entre clans."
    "[nomPerso], un cousin du meurtrier vient vous voir."
    std "[titreFondateur], je ne sais plus quoi faire. Mon devoir est de soutenir mon cousin, mais je ne parviens pas à approuver son acte et je n'ose agir."

    menu:
        "Ton devoir est de soutenir ta famille quoiqu'il arrive comme eux t'ont toujours protégé et te protégeront toujours.":
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_CLANIQUE, 0.3)
        "Seule une autorité supérieure peut résoudre ce conflit. Va prêter allégeance à celui que tu estimeras capable d'être ce juge et prête lui allégeance.":
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_FEODALE, 0.3)
        "Cherche ce que te disent ton coeur et ta tête et agis en conséquence.":
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_INDIVIDUALISME, 0.3)
        "Prie les dieux, ils guideront ton coeur.":
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_THEOCRATIE, 0.1)
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_INDIVIDUALISME, 0.1)

    jump fin_cycle

label choixRoi:
    $ situation_.SetValCarac("choixRoi", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    $ titreFondateur = civRef.GetTitreFondateur(situation_)
    $ estMale = random.uniform(0, 1.0) > 0.5
    $ nomPerso = civRef.GenererPatronyme(estMale)
    $ imgPerso = civRef.GenererImagePerso(estMale, 50, []) # homme de 50 ans
    $ std = Character(nomPerso)
    $ renpy.show(imgPerso, [right])
    with moveinright
    std "[titreFondateur], vous êtes notre Guide et nous suivons vos commandements, mais nous avons aussi besoin de l'autorité d'un roi qui nous mènera à la guerre et rendra la justice."
    std "Comment choisir qui sera digne de cet honneur ? Quel est le meilleur moyen de conserver de l'autorité sur les hommes ? "

    $ estPasAthee = situation_.GetValCarac(religion.Religion.C_RELIGION) != religion.Atheisme.NOM
    menu:
        "Cherchez la personne dont les ancêtres sont les plus glorieux.":
            $ AjouterACaracStructurePolitique(peuple.Peuple.C_CLASSE, 0.3)
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
