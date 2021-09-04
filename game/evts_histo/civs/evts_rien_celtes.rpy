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

label evtRien_celtes_devin:
    "Un devin itinérant réputé annonce après avoir observé le vol des oiseaux que la prochaine récolte sera excellente. Le peuple est soulagé."
    jump fin_cycle

label evtRien_celtes_moqueriesBarde:
    "Au cours d'un banquet un barde a chanté une poésie lyrique se moquant grassement des coutumes ancestrales de votre peuple."
    $ cohesion = situation_.GetValCaracInt(peuple.Peuple.C_COHESION)
    if cohesion > 0.5:
        "Il a été violemment hué par le peuple assemblé pour son manque de respect et du s'enfuir sous les projections de nourriture."
        "D'autres bardes ont alors pris sa place pour louer les traditions et les exploits des [nomPeuple] jusqu'à la fin du banquet."
    else:
        "Il a été applaudi et la soirée a tourné à l'étalage de critiques et de moqueries sur els traditions ancestrales."
    jump fin_cycle

label evtRien_celtes_spectaclePoesie:
    "Un grand spectacle de poésie est organisé dans l'oppidum voisin voisin et les bardes des environs viennent nombreux."
    $ creativite = situation_.GetValCaracInt(peuple.Peuple.C_CREATIVITE)
    $ violence = situation_.GetValCaracInt(peuple.Peuple.C_VIOLENCE)
    $ aventure = situation_.GetValCaracInt(peuple.Peuple.C_AVENTURE)
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomBarde = civRef.GenererPatronyme(True)
    if creativite > 0.5:
        "Les poètes des [nomPeuple] y sont grandement appréciés et la réputation du talent artistiques de ce peuple se répand."
    if violence > 0.5:
        "Beaucoup de poèmes épiques sont chantés et les récents exploits des guerriers [nomPeuple] sont rappelés à l'assemblée avec éloquence."
    if aventure > 0.5:
        "Les multiples voyages accomplis par les [nomPeuple] sont chantés par le barde [nomBarde] et apportent une belle touche d'exotisme à la fin de la représentation."
    jump fin_cycle

label evtRien_celtes_mauvaisPresages:
    "Les présages sont inquiétants. Les devins recommandent la plus grande prudence au chef de village."
    jump fin_cycle

label evtRien_celtes_ecoleDruides:
    "Aujourd'hui est un jour d'école religieuse. Les [nomPeuple] se groupent autour de leur druide qui leur explique le principe de l'immortalité des âmes par la métenpsychose, la réincarnation."
    jump fin_cycle

label evtRien_celtes_druideRenegat:
    "Un druide renégat d'une tribu voisine a écrit des vers sacrés en alphabet grec et cmptait les vendre à des étrangers."
    "Heureusement il a été démasqué et exécuté pour cet infâme sacrilège. Puis tous ses livres ont été brûlés."
    jump fin_cycle

label evtRien_celtes_nouveauDruide:
    $ civRef = situation_.GetCivilisationDeReference()
    $ nomDruide = civRef.GenererPatronyme(True)
    "Après de très longues études de plus de 10 ans [nomDruide], votre nouveau druide, rejoint les [nomPeuple]. Il connaît par coeur les milliers de vers qui communiquent avec les dieux et appaisent les hommes."
    jump fin_cycle

label evtRien_celtes_auguresGuerre:
    "Avant une bataille les soldats [nomPeuple] exigent qu'un devin interroge les dieux. Un prisonnier est amené et frappé d'un coup d'épée au thorax."
    "Le devin observe avec attention la manière dont le prisonnier tombe et se vide de son sang. Les spasmes sont formels : les dieux approuvent la guerre et aideront les [nomPeuple]."
    jump fin_cycle
