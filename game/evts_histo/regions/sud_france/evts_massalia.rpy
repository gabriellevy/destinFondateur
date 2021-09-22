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
    from spe.region import region
    from spe.region import sud_france
    from spe.science import science
    from spe.richesse import richesse
    from spe import declencheur_fondateur
    from spe.civilisation import romains
    from spe.civilisation import grecs

    # caracs
    cooperationPlusQueTrois = condition.Condition(peuple.Peuple.C_COOPERATION, 0.3, condition.Condition.SUPERIEUR_EGAL)

    # Massilia
    mauvaisRapportAvecMassalia = condition.Condition(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5, condition.Condition.INFERIEUR)
    RapportAvecMassaliaPasTropMauvais = condition.Condition(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.3, condition.Condition.SUPERIEUR)
    RapportAvecMassaliaExcellent = condition.Condition(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.8, condition.Condition.SUPERIEUR)
    # déclencheurs
    batailleAlaliaPasFait = condition.Condition("batailleAlalia", "1", condition.Condition.DIFFERENT)
    arriveeRenfortsPhoceenPasFait = condition.Condition("arriveeRenfortsPhoceen", "1", condition.Condition.DIFFERENT)
    plantationOliviersMassaliaPasFait = condition.Condition("plantationOliviersMassalia", "1", condition.Condition.DIFFERENT)
    developpementMassaliaPasFait = condition.Condition("developpementMassalia", "1", condition.Condition.DIFFERENT)
    introductionMonnaieMassaliaPasFait = condition.Condition("introductionMonnaieMassalia", "1", condition.Condition.DIFFERENT)
    creationVignesMassaliaPasFait = condition.Condition("creationVignesMassalia", "1", condition.Condition.DIFFERENT)
    prospectionCommerceMassaliaPasFait = condition.Condition("prospectionCommerceMassalia", "1", condition.Condition.DIFFERENT)
    apprentissageEcritureParMassiliaPasFait = condition.Condition("apprentissageEcritureParMassilia", "1", condition.Condition.DIFFERENT)
    rencontreMassilaPasFait = condition.Condition("rencontreMassila", "1", condition.Condition.DIFFERENT)
    guerreAvatiquesPhoceensPasFait = condition.Condition("guerreAvatiquesPhoceens", "1", condition.Condition.DIFFERENT)
    interventionRomeAMassaliaPasFait = condition.Condition("interventionRomeAMassalia", "1", condition.Condition.DIFFERENT)
    rencontreMassilaFait = condition.Condition("rencontreMassila", "1", condition.Condition.EGAL)
    # avatiques
    mauvaisRapportAvecAvatiques = condition.Condition(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.5, condition.Condition.INFERIEUR)

    # science
    niveauEcritureNul = condition.Condition(science.Science.C_ECRITURE, "0.3", condition.Condition.INFERIEUR)

    # base
    siSudFrance = condition.Condition(region.Region.C_REGION, sud_france.SudFrance.NOM, condition.Condition.EGAL)
    def AjouterEvtsSudFranceH():
        global selecteur_

        apprentissageEcritureParMassilia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.4, True), "apprentissageEcritureParMassilia")
        apprentissageEcritureParMassilia.AjouterConditions( [apprentissageEcritureParMassiliaPasFait,
            siSudFrance, rencontreMassilaFait, niveauEcritureNul])
        apprentissageEcritureParMassilia.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(apprentissageEcritureParMassilia)

        rencontreMassila = declencheur_fondateur.DeclencheurFondateur(proba.Proba(1.0, True), "rencontreMassila")
        # ENVIRON -600 AVANT jc
        rencontreMassila.AjouterConditions( [ rencontreMassilaPasFait, siSudFrance])
        rencontreMassila.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(rencontreMassila)

        prospectionCommerceMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.3, True), "prospectionCommerceMassalia")
        # ENVIRON -550 AVANT jc
        prospectionCommerceMassalia.AjouterConditions( [ prospectionCommerceMassaliaPasFait, siSudFrance])
        prospectionCommerceMassalia.EvtHistoArriveEntreDateAetB(-550, 0)
        selecteur_.ajouterDeclencheur(prospectionCommerceMassalia)

        arriveeRenfortsPhoceen = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "arriveeRenfortsPhoceen")
        # ENVIRON -546 AVANT jc
        arriveeRenfortsPhoceen.AjouterConditions( [ arriveeRenfortsPhoceenPasFait, siSudFrance])
        arriveeRenfortsPhoceen.EvtHistoArriveEntreDateAetB(-546, -530)
        selecteur_.ajouterDeclencheur(arriveeRenfortsPhoceen)

        batailleAlalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.2, True), "batailleAlalia")
        # ENVIRON -540 AVANT jc
        batailleAlalia.AjouterConditions( [ batailleAlaliaPasFait, siSudFrance])
        batailleAlalia.EvtHistoArriveEntreDateAetB(-540, -530)
        selecteur_.ajouterDeclencheur(batailleAlalia)

        introductionMonnaieMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "introductionMonnaieMassalia")
        # ENVIRON -470 AVANT jc
        introductionMonnaieMassalia.AjouterConditions( [ introductionMonnaieMassaliaPasFait, siSudFrance])
        introductionMonnaieMassalia.EvtHistoArriveEntreDateAetB(-470, 0)
        selecteur_.ajouterDeclencheur(introductionMonnaieMassalia)

        creationVignesMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "creationVignesMassalia")
        # ENVIRON -400 AVANT jc
        creationVignesMassalia.AjouterConditions( [ creationVignesMassaliaPasFait, siSudFrance])
        creationVignesMassalia.EvtHistoArriveEntreDateAetB(-400, 0)
        selecteur_.ajouterDeclencheur(creationVignesMassalia)

        developpementMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "developpementMassalia")
        # ENVIRON -380 AVANT jc
        developpementMassalia.AjouterConditions( [ developpementMassaliaPasFait, siSudFrance])
        developpementMassalia.EvtHistoArriveEntreDateAetB(-380, 0)
        selecteur_.ajouterDeclencheur(developpementMassalia)

        plantationOliviersMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "plantationOliviersMassalia")
        # ENVIRON -360 AVANT jc
        plantationOliviersMassalia.AjouterConditions( [ plantationOliviersMassaliaPasFait, siSudFrance])
        plantationOliviersMassalia.EvtHistoArriveEntreDateAetB(-360, 0)
        selecteur_.ajouterDeclencheur(plantationOliviersMassalia)

        guerreAvatiquesPhoceens = declencheur_fondateur.DeclencheurFondateur(proba.Proba(1.0, True), "guerreAvatiquesPhoceens")
        # ENVIRON -200 AVANT jc
        guerreAvatiquesPhoceens.AjouterConditions( [guerreAvatiquesPhoceensPasFait, siSudFrance, rencontreMassilaFait])
        guerreAvatiquesPhoceens.EvtHistoArriveEntreDateAetB(-210, -190)
        selecteur_.ajouterDeclencheur(guerreAvatiquesPhoceens)

        interventionRomeAMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.8, True), "interventionRomeAMassalia")
        # ENVIRON -180 AVANT jc
        interventionRomeAMassalia.AjouterConditions( [siSudFrance, rencontreMassilaFait, interventionRomeAMassaliaPasFait])
        interventionRomeAMassalia.EvtHistoArriveEntreDateAetB(-180, -140)
        selecteur_.ajouterDeclencheur(interventionRomeAMassalia)

        attaqueParMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "attaqueParMassalia")
        # peut arriver plusieurs fois
        attaqueParMassalia.AjouterConditions( [siSudFrance, mauvaisRapportAvecMassalia, rencontreMassilaFait])
        attaqueParMassalia.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(attaqueParMassalia)

        pillageMassaliaParAvatiques = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "pillageMassaliaParAvatiques")
        # peut arriver plusieurs fois
        pillageMassaliaParAvatiques.AjouterConditions( [siSudFrance, rencontreMassilaFait])
        pillageMassaliaParAvatiques.EvtHistoArriveEntreDateAetB(-600, 0)
        selecteur_.ajouterDeclencheur(pillageMassaliaParAvatiques)

        commerceAvecMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "commerceAvecMassalia")
        # peut arriver plusieurs fois
        commerceAvecMassalia.AjouterConditions( [siSudFrance, rencontreMassilaFait, RapportAvecMassaliaPasTropMauvais, cooperationPlusQueTrois])
        selecteur_.ajouterDeclencheur(commerceAvecMassalia)

        tresBonRapportsAvecMassalia = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "tresBonRapportsAvecMassalia")
        # peut arriver plusieurs fois
        tresBonRapportsAvecMassalia.AjouterConditions( [siSudFrance, rencontreMassilaFait, RapportAvecMassaliaExcellent, cooperationPlusQueTrois])
        selecteur_.ajouterDeclencheur(tresBonRapportsAvecMassalia)

label tresBonRapportsAvecMassalia:
    scene bg massalia
    "Les [nomPeuple] sont devenus très proches des Massaliottes. Non seulement ils commercent avec eux mais ils servent de plus en plus souvent d'intermédiaires avec les autres tribus gauloises."
    "Beaucoup de [nomPeuple] ont eu l'honneur de visiter la grande ville et d'entrer dans les temples. Le grec se répand ainsi que la curiosité pour l'étrange fonctionnement politique de cette ville."
    $ AjouterACaracCiv(grecs.Grecque.NOM, 0.1)
    $ AjouterACaracIdentite(peuple.Peuple.C_LEGALISME, 0.05)
    $ AjouterACaracIdentite(peuple.Peuple.C_ARGENT, 0.1)
    $ AjouterACaracStructurePolitique(peuple.Peuple.C_INDIVIDUALISME, 0.05)
    jump fin_cycle

label commerceAvecMassalia:
    scene bg massalia
    "Le port de Massalia est un excellent partenaire de commerce. Vos pouvez y échanger de l'ambre et de l'étain contre du vin et de la céramique de luxe."
    $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.1)
    $ AjouterACaracInf1(richesse.Richesse.C_COMMERCE, 0.1)
    $ AjouterACaracCiv(grecs.Grecque.NOM, 0.05)

    jump fin_cycle

label interventionRomeAMassalia:
    scene bg massalia
    $ situation_.SetValCarac("interventionRomeAMassalia", "1")
    "Après avoir subi des raids celtes réguliers les phocéens de Massalia décident de demander l'intervention des romains pour pacifier la région."
    "Pour la première fois les celtes Salyens et avatiques découvrent cet ennemi dangereux et discipliné. Ils résistent très bravement mais sont contraints à reculer et leur place forte est détruite."
    $ rapport_massalia = situation_.GetValCaracInt(sud_france.SudFrance.C_RAPPORT_MASSILIA)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    if rapport_massalia > 0.5 and violence < 0.5:
        "Les [nomPeuple] sont perçus comme non dangereux et parviennent à se tenir à l'écart des combats. Les autres celtes voient celà d'un très mauvais oeil mais ils sont trop affaiblis pour se venger dans l'immédiat."
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.1)
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_SALYENS, 0.1)
        $ situation_.SetValCarac(romains.Romain.C_RAPPORT_ROME, 0.3)
    else:
        "Les [nomPeuple] sont inévitablement entrainés dans la guerre aux côtés des autres celtes et sont durement défaits avec eux."
        $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.05)
        $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_SALYENS, 0.05)
        $ situation_.SetValCarac(romains.Romain.C_RAPPORT_ROME, 0.0)
        $ situation_.SetValCarac(romains.Romain.C_GUERRE, 1)
    jump fin_cycle

label pillageMassaliaParAvatiques:
    scene bg massalia
    "Les celtes avatiques s'enhardissent et pillent de plus en plus souvent les bateaux et convois des phocéens de Massalia."
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    if violence > 0.5:
        "Les [nomPeuple] sautent sur l'occasion et se joignent à leurs frères pour récolter un beau butin et de belles têtes tranchées comme trophée."
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.4)
        $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.05)
        $ AjouterACaracInf1(richesse.Richesse.C_TRIBUS, 0.3)
    else:
        "Les [nomPeuple] préfèrent ne pas s'en mêler ce qui leur attire le mépris des autres celtes."
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.05)

    jump fin_cycle

label guerreAvatiquesPhoceens:
    scene bg massalia
    $ situation_.SetValCarac("guerreAvatiquesPhoceens", "1")
    "L'expansion des phocéens de Massalia se heurte de plus en plus souvent aux peuples celtes des environs."
    "De leur côté les celtes avatiques sont de plus en plus tentés par le pillage de la riche Massalia. Cela va dégénérer en guerre ouverte."
    $ population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    $ rapport_massalia = situation_.GetValCaracInt(sud_france.SudFrance.C_RAPPORT_MASSILIA)
    $ rapport_avatiques = situation_.GetValCaracInt(sud_france.SudFrance.C_RAPPORT_AVATIQUES)

    if rapport_massalia > 0.6 and rapport_avatiques > 0.6:
        "Les [nomPeuple] ont de très bons rapports avec les deux camps et refusent de participer à la guerre dans quelque camps que ce soit."
        "Ils parviennent avec difficulté à le faire. Mais phocéens comme celtes attendaient leur aide et prennent très mal cette attitude."
        jump guerreAvatiquesPhoceens_neutralite
    elif rapport_massalia < 0.2:
        label guerreAvatiquesPhoceens_allies_avatiques:
            # allié aux avatiques
            "Le mépris des [nomPeuple] pour les grecs leur fait rejoindre leur frères celtes avatiques dans la guerre contre Massalia."
            "Malheureusement ces grecs ci sont disciplinés et bien armés et se cachent derrières des armures et des boucliers."
            "Les [nomPeuple] sont contraints de rester sur la défensive et voient leur village incendié par les envahisseurs."
            $ RetirerAPopulationPourcent(7)
            $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.2)
            $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.2)
            $ RetirerACaracPos(richesse.Richesse.C_TRIBUS, 0.1)
            jump guerreAvatiquesPhoceens_fin
    elif rapport_avatiques < 0.2:
        label guerreAvatiquesPhoceens_allies_massalia:
            # allié à Massalia
            "C'est l'occasion pour les [nomPeuple] de se venger de leurs frères avatiques détestés en s'alliant aux puissants marins grecs en armure."
            "Ils parviennent ainsi à participer à quelques pillages juteux."
            $ RetirerAPopulationPourcent(3)
            $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.2)
            $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.2)
            $ AjouterACaracInf1(richesse.Richesse.C_TRIBUS, 0.3)
            jump guerreAvatiquesPhoceens_fin
    elif violence < 0.2:
        "Les [nomPeuple] sont aussi pacifiques qu'on peut l'être et fuient les combats, quitte à fuir leur village temporairement."
        "Les avatiques et les phocéens ne font que les mépriser encore plus et pillent leurs terres."
        jump guerreAvatiquesPhoceens_neutralite
    elif rapport_avatiques > rapport_massalia:
        jump guerreAvatiquesPhoceens_allies_avatiques
    else:
        jump guerreAvatiquesPhoceens_allies_massalia

    label guerreAvatiquesPhoceens_neutralite:
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.1)
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_AVATIQUES, 0.1)
        jump guerreAvatiquesPhoceens_fin

    label guerreAvatiquesPhoceens_fin:
        "Après plusieurs mois de traque et d'escarmouches les phocéens de Massalia sortent vainqueurs mais ne sont pas arrivés à grand chose."
        "Ils ont brûlé le village de l'île des avatiques, tué des guerriers, pris des esclaves et montré leur supériorité mais les avatiques se sont réinstallés aussitôt après."
        $ RetirerAPopulationPourcent(2)

    jump fin_cycle

label introductionMonnaieMassalia:
    scene bg massalia
    $ situation_.SetValCarac("introductionMonnaieMassalia", "1")
    show monnaie_massalia at truecenter
    with dissolve
    "Les Massaliottes ont créé quelque chose d'incroyable. Ils façonnent de petits disques de métal précieux avec un symbole gravé dessus et s'en servent comme système de valeur pour les échanges commerciaux."
    $ argent = situation_.GetValCaracInt(peuple.Peuple.C_ARGENT)
    $ cooperation = situation_.GetValCaracInt(peuple.Peuple.C_COOPERATION)
    if argent > 0.3 or cooperation > 0.3:
        "Les [nomPeuple] sont très entousiastes et adoptent vite ce système esthétique et ingénieux."
        $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.1)
    jump fin_cycle

label batailleAlalia:
    scene bg massalia
    $ situation_.SetValCarac("batailleAlalia", "1")
    scene bg galere
    "Un commerçant de retour d'un long voyage en mer régale tout le village de ses histoires exotiques."
    "Une d'entre elle est particulièrement intéressante. Il raconte avoir récemment vu de ses yeux une énorme bataille navale entre des dizaines de navires grecs, étrusques et phéniciens près d'Alalia en Corse."
    "Apparemment les grecs, qui incluaient beaucoup de Massaliottes, ont été vaincus et ont du abandonner cette île. Ils sont néanmoins encore nombreux et puissants et continuent à contrôler vos rivages."
    "De l'avis du marchand le temps des grecs est compté. Les phéniciens de Carthage sont bien plus puissants et meilleurs marins. Mais seul le temps le dira. De votre point de vue les Massaliottes restent redoutables, surtout sur mer."
    jump fin_cycle

label arriveeRenfortsPhoceen:
    scene bg massalia
    $ situation_.SetValCarac("arriveeRenfortsPhoceen", "1")
    "Les grecs de Massalia étaient jusqu'à maintenant peu nombreux mais cela a changé récemment. Beaucoup de bateau chargés d'autres grecs y ont accosté."
    "Ils prétendent qu'ils ont été chassés de leur ville d'origine par des barabres lointains et veulent s'installer avec leurs frères grecs. Si les Massaliottes acceptent ils vont devenir très nombreux et un danger potentiel."
    jump fin_cycle

label developpementMassalia:
    scene bg massalia
    $ situation_.SetValCarac("developpementMassalia", "1")
    $ nomBarde = civRef.GenererPatronyme(True)
    $ imgBarde = civRef.GenererImagePerso(True, 35, [])
    $ std = Character(nomBarde)
    $ renpy.show(imgBarde, [right])
    with moveinright
    "[nomBarde], un de vos meilleurs barde, a joué à Massalia. Il en a rapporté une description impressionnante."
    std "Massalia est située sur un terrain rocheux. Son port se trouve au pied d’une falaise en amphithéâtre qui regarde vers le midi."
    std "Elle est solidement fortifiée, de même que l’ensemble de la ville dont la dimension est considérable. Sur l’acropole sont fondés l’Ephésion et le sanctuaire d’Apollon Delphinien."
    std "L’Ephésion est le temple réservé à l’Artémis d’Éphèse. En effet, alors que les Phocéens partaient de leur patrie, un oracle, dit-on, leur tomba du ciel qui disait de prendre pour chef de leur navigation un guide reçu d’Artémis d’Éphèse."
    $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.05)
    jump fin_cycle

label prospectionCommerceMassalia:
    scene bg massalia
    $ situation_.SetValCarac("prospectionCommerceMassalia", "1")
    "Les Massaliottes prospectent dans toutes les directions et créent  des contrats commerciaux sur toute la côte et jusqu'en amont du Rhône."
    "Ils achètent surtout l'ambre et l'étain et vendent de la vaisselle, de la céramique, et du vin."
    $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.1)
    jump fin_cycle

label plantationOliviersMassalia:
    scene bg massalia
    $ situation_.SetValCarac("plantationOliviersMassalia", "1")
    "Les massaliottes avaient déjà fait goûter aux [nomPeuple] leur précieuse huile d'olive qu'ils vendent à prix d'or. Mais c'est longtemps après qu'ils ont révélé que les arbres noueux qu'ils plantaient sur les coteaux qui bordent leur ville sont des oliviers."
    "Cette plante inconnue par ici leur permettra de produire leur huile d'olive localement, de la vendre aux [nomPeuple], voire même de l'exporter !"
    $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.04)
    jump fin_cycle

label creationVignesMassalia:
    scene bg massalia
    $ situation_.SetValCarac("creationVignesMassalia", "1")
    "Après leurs succès contre les ligures, les Massaliottes possèdent maintenant des coteaux et on dit qu'ils ont l'intention de faire posser du raison pour faire du vin !"
    $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.1)
    jump fin_cycle

label rencontreMassila:
    scene bg massalia
    $ situation_.SetValCarac("rencontreMassila", "1")
    "Une rumeur est venue jusqu'aux [nomPeuple] : des étrangers au langage et aux coutumes inconnues se sont installés en bordure de la mer à l'embouchure du Rhône, à moins de 100 lieux de leur village."
    "Les habitations qu'ils construisent sont d'un style étrange, de toute évidence lointain. Et on dit qu'ils appartiennent au lointain peuple des grecs et qu'ils ont été banni jusqu'à ces rivages."
    "En tout cas leurs navires sont nombreux et impressionnants et d'un type que vous n'aviez jamais vu."
    "D'autres celtes sont déjà entrés en contact avec eux et ont commencé à commercer. Ces étrangers sont très friands de l'artisanat et des fourrures locales et les expédient par delà les mers."
    "Ils ont baptisé leur cité naissante 'Massalia' et nul doute que vous les verrez de près tôt ou tard."
    jump fin_cycle

label apprentissageEcritureParMassilia:
    scene bg massalia
    $ situation_.SetValCarac("apprentissageEcritureParMassilia", "1")
    $ civRef = situation_.GetCivilisationDeReference()
    "Vos voisins phocéens de Massila parlent et surtout écrivent en grec. Comme vous commercez avec eux ils décident d'initier les [nomPeuple] car c'est un art très pratique pour tenir les comptes."
    $ intellectualisme = situation_.GetValCarac(peuple.Peuple.C_INTEL)
    $ curiosite = situation_.GetValCarac(peuple.Peuple.C_AVENTURE)
    if curiosite < 0.5 and intellectualisme < 0.2:
        "Mais les [nomPeuple] les repoussent. Ils ont toujours bien vécu sans se compliquer la vie avec ça et continueront."
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
    else:
        "Plusieurs commerçants [nomPeuple] s'y intéressent essentiellement pour tenir leurs comptes."
        $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
        $ AjouterACaracCiv(grecs.Grecque.NOM, 0.1)
        $ AjouterACaracIdentite(peuple.Peuple.C_INTEL, 0.1)
        $ AjouterACaracInf1(science.Science.C_ECRITURE, 0.3)
    jump fin_cycle

label attaqueParMassalia:
    scene bg massalia
    "Les rapports des [nomPeuple] avec les phocéens de Massalia sont devenus très mauvais et ceux-ci décident de lancer un raid contre leur village pour les chasser des environs."
    $ population = situation_.GetValCaracInt(peuple.Peuple.C_POP)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    if population > 4000 and violence > 0.3:
        "Les guerriers [nomPeuple] tiennent bon et parviennent à tendre une embuscade aux phocéens qui préfèrent négocier un traité que de prendre le risque de se battre."
        "Les [nomPeuple] conservent leurs terres et recevront un tribu régulier contre la promesse de respecter les commerçants phocéens."
        $ AjouterACaracInf1(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.5)
        $ AjouterACaracInf1(richesse.Richesse.C_TRIBUS, 0.5)
        $ RetirerAPopulationPourcent(2)
    else:
        "Les [nomPeuple] sont vaincus et leur village détruit. Les phocéens ne tentent cependant pas de les exterlminer. Ils veulent juste s'étendre en volant leurs terres."
        "Les [nomPeuple] se réinstallent donc à bonne distance, affaiblis mais furieux et décidés à ne pas se laisser encore surprendre."
        $ AjouterACaracIdentite(peuple.Peuple.C_VIOLENCE, 0.1)
        $ RetirerACaracPos(sud_france.SudFrance.C_RAPPORT_MASSILIA, 0.3)
        $ RetirerAPopulationPourcent(10)

    jump fin_cycle
