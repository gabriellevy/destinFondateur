# Persos
define narrator = Character(color="#fafad8", what_italic=True)
define std = Character('Perso standard...', color="#B22222") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define std2 = Character('Perso standard2...', color="#9400D3") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define std3 = Character('Perso standard3...', color="#556B2F") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define std4 = Character('Perso standard4...', color="#191970") # personnage standard remplacé selon les situations. (son nom est mis à jour)
define std5 = Character('Perso standard5...', color="#2F4F4F") # personnage standard remplacé selon les situations. (son nom est mis à jour)

#transforms :
transform tout_a_droite:
    xpos 1500 xanchor 0.5 ypos 350 yanchor 0.5
    linear 1 xpos 1100
transform a_droite:
    xpos 1500 xanchor 0.5 ypos 350 yanchor 0.5
    linear 1 xpos 880
transform un_peu_a_droite:
    xpos 1500 xanchor 0.5 ypos 350 yanchor 0.5
    linear 1 xpos 650
transform a_gauche:
    xpos -100 xanchor 0.5 ypos 350 yanchor 0.5
    linear 1 xpos 240
transform tout_a_gauche:
    xpos -100 xanchor 0.5 ypos 350 yanchor 0.5
    linear 1 xpos 70

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
    AjouterEvtsMetiersF()
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
    # queue music [ epique_principale, conquetes ] # pseudo liste de lecture temporaire
    jump choix_peuple

label debut_cycle:
    scene bg village_celte # A FAIRE : fond de base selon culture, époque, et lieu dominants
    show screen valeurs_traits
    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    # "Fin d'un cycle."
    # jump batailleAlalia # tmp test

    # si aucune musique n'est sélectionnée, en prendre une au hasard dans la liste des musiques de la culture principale
    if renpy.music.get_playing() == None:
        $ civRef = situation_.GetCivilisationDeReference()
        $ musiques = civRef.GetMusiqueAJouer()
        $ renpy.music.queue(musiques,loop=False)

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
