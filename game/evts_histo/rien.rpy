# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    # from religions import religion
    # from geographie import quartier
    from spe.civilisation import celtes

    def AjouterEvtsRienHisto():
        global selecteur_, situation_
        selecteurDEvenementVide_h = declencheur.Declencheur(1.0, "selecteurDEvenementVide_h")
        selecteurDEvenementVide_h.AjouterCondition(estEnModeHisto)
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide_h)

    def LancerEvtVideH(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = ["evtRien1_h", "evtRien2_h" ] # note : peut-être n'utiliser ces événements bidons que si on n'en a aps de plus intéressants ?

        # selon religion
        religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religionActuelle == religion.Christianisme.NOM:
            evtsVides_.append("evtRien_saints")
            evtsVides_.append("evtRien_Christianisme_1")

        # ------------------------------ selon civilisation dominante :
        civRef = situation_.GetCivilisationDeReference()
        if civRef.nom_ == celtes.Celte.NOM:
            evtsVides_.append("evtRien_devinCelte")

        # fond selon quartier
        # if sceneParDefaut == "":
        #     quartierCourant = situation.GetQuartier()
        #     if quartierCourant is not None:
        #         sceneParDefaut = quartierCourant.imageDeFond_

        if sceneParDefaut == "":
            sceneParDefaut = "bg vercingetorix"

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(sceneParDefaut)
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label selecteurDEvenementVide_h:
    $ LancerEvtVideH(situation_)

label evtRien1_h:
    with Dissolve(.5)
    "Et encore une journée de plus."
    jump fin_cycle

label evtRien2_h:
    with Dissolve(.5)
    "Les jours se suivent et se ressemblent."
    jump fin_cycle
