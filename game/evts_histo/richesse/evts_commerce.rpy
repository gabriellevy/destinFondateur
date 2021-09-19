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
    from spe.richesse import richesse

    # caracs
    violencePlusQueUn = condition.Condition(peuple.Peuple.C_VIOLENCE, 0.1, condition.Condition.SUPERIEUR_EGAL)

    # richesse
    commercePlusQueTrois = condition.Condition(richesse.Richesse.C_COMMERCE, 0.3, condition.Condition.SUPERIEUR_EGAL)

    def AjouterEvtsSudFranceH():
        global selecteur_

        ramolissementDuAuCommerce = declencheur_fondateur.DeclencheurFondateur(proba.Proba(0.05, True), "ramolissementDuAuCommerce")
        # peut arriver plusieurs fois
        ramolissementDuAuCommerce.AjouterConditions( [violencePlusQueUn, commercePlusQueTrois])
        selecteur_.ajouterDeclencheur(ramolissementDuAuCommerce)

label ramolissementDuAuCommerce:
    "Les produits de luxe étrangers et l'appât du gain des commerçants de plus en plus nombreux a changé les [nomPeuple]."
    "Ils deviennent plus mous, moins belliqueux."
    $ AjouterACaracIdentite(peuple.Peuple.C_SENSUALITE, 0.05)
    $ AjouterACaracIdentite(peuple.Peuple.C_COOPERATION, 0.05)
    $ RetirerACaracPos(peuple.Peuple.C_ENDURANCE, 0.05)
    $ RetirerACaracPos(peuple.Peuple.C_VIOLENCE, 0.05)

    jump fin_cycle
