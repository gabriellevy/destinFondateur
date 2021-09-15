# Persos
define narrator = Character(color="#fafad8", what_italic=True)
define std = Character('Perso standard...', color="#009900") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define std2 = Character('Perso standard2...', color="#009900") # personnage standard remplacé selon les situations. (son nom est mis à jour)

# Musiques
define audio.epique_principale = "musique/epique_principale.ogg"
define audio.conquetes = "musique/conquetes.ogg"

init -10 python:
    from abs import selecteur
    from spe import situation_fondateur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from spe import situation_fondateur
    import random

    selecteur_ = selecteur.Selecteur()
    estEnModeFondateur = condition.Condition(situation_fondateur.SituationFondateur.C_MODE, situation_fondateur.SituationFondateur.C_MODE_FONDATEUR, condition.Condition.EGAL)
    estEnModeHisto = condition.Condition(situation_fondateur.SituationFondateur.C_MODE, situation_fondateur.SituationFondateur.C_MODE_HISTORIQUE, condition.Condition.EGAL)
    def determinationEvtCourant(situation):
        global selecteur_
        return selecteur_.determinationEvtCourant(situation)

init -1 python:
    from abs import selecteur
    import random

    # fondateurs
    AjouterEvtsFamilleF()
    AjouterEvtsReligieux()
    AjouterEvtsAventure()
    AjouterEvtsJusticeF()
    AjouterEvtsArt()
    AjouterEvtsRienFondateur()
    AjouterEvtsVieillesseF()
    AjouterEvtsPeuples()
    AjouterEvtsScience()
    AjouterEvtsGuerreF()
    AjouterEvtsGuerreF()
    AjouterEvtsMoeursF()
    AjouterEvtsPouvoirF()
    # AjouterEvtsMaladies()
    # ------------------ historique --------------------
    AjouterEvtsRienHisto()
    AjouterEvtsReligieuxH()
    AjouterEvtsSudFranceH()
    # *** civs
    AjouterEvtsCeltesH()

# Le jeu commence ici
label start:
    scene bg village_celte
    # play music musique_menu
    queue music [ epique_principale, conquetes ] # pseudo liste de lecture temporaire
    jump choix_peuple

label debut_cycle:
    show screen valeurs_traits
    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    # "Fin d'un cycle."
    # jump combat_avant_garde # tmp test

    $ situation_.TourSuivant()
    
    jump debut_cycle

label mort:
    $ situation_[situation_fondateur.SituationFondateur.C_MODE] = situation_fondateur.SituationFondateur.C_MODE_HISTORIQUE
    "Le fondateur est mort. L'histoire de votre peuple commence."
    jump debut_cycle

label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"

label probaAbsoluesSup100:
    "Le total des probas absolues dépasse 100%% !"
