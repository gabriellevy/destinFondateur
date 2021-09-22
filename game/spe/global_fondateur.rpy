init -2 python:
    from abs import carac
    from spe import situation_fondateur
    from abs.humanite import trait
    # from geographie import quartier
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite.sante import pbsante
    from spe.peuple import peuple
    from spe.peuple import peuples
    from spe.region import region
    from spe.region import regions
    from spe.civilisation import civ
    from spe.civilisation import civs
    import random

    situation_ = situation_fondateur.SituationFondateur() # dictionnaire contenant toutes les caracs courantes de la partie
    filtre_ = filtres_action.FiltreAction() # objet contenant les préférences du joueur pour les actions à afficher ou cacher en priorité
    traits_ = trait.CollectionTraits()
    situation_.collectionTraits = traits_
    blessures_ = pbsante.CollectionBlessures()
    situation_.collectionBlessures = blessures_
    maladies_ = pbsante.CollectionMaladies()
    situation_.collectionMaladies = maladies_
    # quartiers_ = quartier.CollectionQuartiers()
    # situation_.collectionQuartiers = quartiers_
    metiers_ = metier.CollectionMetiers()
    situation_.collectionMetiers = metiers_
    peuples_ = peuples.CollectionPeuples()
    situation_.collectionPeuples = peuples_
    regions_ = regions.CollectionRegions()
    situation_.collectionRegions = regions_
    civs_ = civs.CollectionCivs()
    situation_.collectionCivs = civs_
    interfaceMode_ = 0
    nbInterfaceMode_ = 5

    def AjouterACaracInf1(caracId, num):
        global situation_
        val = situation_.GetValCaracInt(caracId) + float(num)
        if val > 1.0:
            situation_.SetValCarac(caracId, 1)
        else:
            situation_.AjouterACarac(caracId, num)
        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")

    def InterfaceSuivante():
        global interfaceMode_, nbInterfaceMode_
        interfaceMode_ = interfaceMode_ + 1
        if interfaceMode_ >= nbInterfaceMode_:
            interfaceMode_ = 0
        print(interfaceMode_)

    def RetirerAPopulationPourcent(pourcent):
        global situation_
        population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
        retraitPop = int(population/100) + 1
        RetirerACaracPos(peuple.Peuple.C_POP, retraitPop)

    def AjouterAPopulationPourcent(pourcent):
        global situation_
        population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
        ajoutPop = int(population/100) + 1
        AjouterACarac(peuple.Peuple.C_POP, ajoutPop)

    # -------------------------- fonctions de manipulation de caracs de civilisation (inclue les formules et systèmes de rééquilibrages)
    def AjouterACaracCiv(caracId, num):
        global situation_
        # déterminer l'actuelle civilisation de référence :
        civRefObj = situation_.GetCivilisationDeReference()

        # ne peut pas dépasser 1 et si c'est le cas tout est recalulé proportionellement pour la remettre à 1
        valCaracCiv = situation_.GetValCaracInt(caracId) + float(num)
        if valCaracCiv > 1.0:
            # cette civilisation est la principale du joueur et les autres sont rééquilibrées à partir de celle ci
            ratio = 1/valCaracCiv
            # toutes les vals de civ sont divisées par ce ratio :
            for civK in situation_.collectionCivs.lCivs_.keys():
                valCiv = situation_.GetValCaracInt(civK)
                if valCiv != "":
                    situation_.SetValCarac(civK, valCiv*ratio)
            situation_.SetValCarac(caracId, 1.0)
            situation_.caracs_[civ.Civ.C_CIV] = caracId
        else:
            situation_.AjouterACarac(caracId, num)

        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        nouvCivRefObj = situation_.GetCivilisationDeReference()

        if civRefObj.nom_ != nouvCivRefObj.nom_:
            # !! changement de civilisation de référence !!
            # petit nettoyage
            for civK in situation_.collectionCivs.lCivs_.keys():
                valCiv = situation_.GetValCaracInt(civK)
                if valCiv < 0.05:
                    situation_.SetValCarac(civK, 0)
            renpy.jump("changementCivRef")

    def AjouterACaracIdentite(caracId, num):
        global situation_
        # ne peut pas dépasser 1 et si c'est le cas tout est recalulé proportionellement pour la remettre à 1
        valCaracCiv = situation_.GetValCaracInt(caracId) + float(num)
        if valCaracCiv > 1.0:
            # cette identité est la principale du peuple et les autres sont rééquilibrées à partir de celle ci
            ratio = 1/valCaracCiv
            # toutes les identités sont divisées par ce ratio :
            for carac in situation_.listeCaracsIdentite_:
                valCiv = situation_.GetValCaracInt(carac)
                if valCiv != "":
                    nouvelleVal = valCiv/ratio
                    if nouvelleVal > 1:
                        nouvelleVal = 1
                    if nouvelleVal < 0:
                        nouvelleVal = 0
                    situation_.SetValCarac(carac, nouvelleVal)
            situation_.SetValCarac(caracId, 1.0)
        else:
            situation_.AjouterACarac(caracId, num)

        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.GetCivilisationDeReference()

    def AjouterACaracStructurePolitique(caracId, num):
        global situation_
        # ne peut pas dépasser 1 et si c'est le cas tout est recalulé proportionellement pour la remettre à 1
        valCarac = situation_.GetValCaracInt(caracId) + float(num)
        if valCarac > 1.0:
            # cette structure politique est la principale du peuple et les autres sont rééquilibrées à partir de celle ci
            ratio = 1/valCarac
            # toutes les identités sont divisées par ce ratio :
            for carac in situation_.listeCaracsStructurePolitique_:
                val = situation_.GetValCaracInt(carac)
                if val != "":
                    nouvelleVal = val/ratio
                    if nouvelleVal > 1:
                        nouvelleVal = 1
                    if nouvelleVal < 0:
                        nouvelleVal = 0
                    situation_.SetValCarac(carac, nouvelleVal)
            situation_.SetValCarac(caracId, 1.0)
        else:
            situation_.AjouterACarac(caracId, num)

        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.GetCivilisationDeReference()

    def RetirerACaracPos(caracId, num):
        """
        retire 'num' à la carac 'caracId' mais en restant 'positif'.
        donc si cela met le nombre en dessous de 0 il vaut 0
        """
        global situation_
        valCarac = situation_.GetValCaracInt(caracId) - float(num)
        if valCarac < 0:
            situation_.SetValCarac(caracId, 0)
        else:
            textChangtCarac = u"{} - {}".format(caracId, num)
            renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#e11", size=24, alpha=1.0)
            renpy.pause(time_)
            renpy.hide_screen("fading_text")
            situation_.RetirerACarac(caracId, num)
        situation_.GetCivilisationDeReference()
