init -2 python:
    from abs import carac
    from spe import situation_fondateur
    from abs.humanite import trait
    # from geographie import quartier
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite.sante import pbsante
    from spe.peuple import peuple
    from spe.region import region
    from spe.civilisation import civ
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
    peuples_ = peuple.CollectionPeuples()
    situation_.collectionPeuples = peuples_
    regions_ = region.CollectionRegions()
    situation_.collectionRegions = regions_
    civs_ = civ.CollectionCivs()
    situation_.collectionCivs = civs_
    interfaceMode_ = 3
    nbInterfaceMode_ = 4

    def AjouterAAffinite(idCiv, num):
        """
        affecte l'affinité entre les civilisation c'est à dire est-ce que quand elles se rencontreront ces deux civilisation se ressembleront
        (et auront plus de chance de s'allier, fusionner, ou s'affronter)
        """
        global situation_
        id = u"affinite{}".format(idCiv)
        situation_.AjouterACarac(id, num)

    def InterfaceSuivante():
        global interfaceMode_, nbInterfaceMode_
        interfaceMode_ = interfaceMode_ + 1
        if interfaceMode_ >= nbInterfaceMode_:
            interfaceMode_ = 0
        print(interfaceMode_)
