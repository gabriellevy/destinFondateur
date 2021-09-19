from abs.humanite import identite

class Civ:
    C_CIV = u"Civilisation"

    def __init__(self):
        self.nom_ = u"pas de nom de civilisation, doit être overridé"

    def MiseEnPlaceCaracsDepart(self, situation):
        pass

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return u"Civilisation : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{}".format(self.nom_)

    def GetPolice(self):
        """
        police à afficher quand cette civ est la civ dominante
        """
        # germanique par défaut pour l'instant
        return u"gui/polices/CloisterBlack.ttf"

    def GenererPrenom(self, masculin):
        if masculin:
            return u"Pas de prénom masculin, doit être overridé"
        return u"Pas de prénom féminin, doit être overridé"

    def GetMusiqueAJouer(self):
        """
        renvoie un tableau de chemins de musiques à jouer dans le style de la civilisation en question
        """
        return []

    def GenererNomPeuple(self):
        return u"Pas de nom de peuple, doit être overridé"

    def GenererNom(self):
        return u"Pas de nom, doit être overridé"

    def GenererPatronyme(self, masculin):
        prenom = self.GenererPrenom(masculin)
        return "{} {}".format(prenom, self.GenererNom())

    def GenererImagePerso(self, masculin, age, tabImagesInterdites):
        # if masculin:
        return "à overrider GenererImagePerso pour votre civ"

    def GenererImageGuerrier(self, masculin, age,tabImagesInterdites):
        """
        tabImagesInterdites list des images qui ne peuvent pas être sélectionnées
        """
        # if masculin:
        return "à overrider GenererImageGuerrier pour votre civ"

    def GetTitreFondateur(self, situation):
        nom = situation.GetValCarac(identite.Identite.C_NOM)
        return nom

class Juive(Civ):
    NOM = u"Juive"

    def __init__(self):
        self.nom_ = Juive.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Juive PAS FAIT"
        return u"prénom féminin Juive PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Juive PAS FAIT"

    def GenererNom(self):
        return u"nom Juive PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Rabbin {}".format(nom)

class Arabe(Civ):
    NOM = u"Arabe"

    def __init__(self):
        self.nom_ = Arabe.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Arabe PAS FAIT"
        return u"prénom féminin Arabe PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Arabe PAS FAIT"

    def GenererNom(self):
        return u"nom Arabe PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Imam {}".format(nom)

class Phenicien(Civ):
    NOM = u"Phénicien"

    def __init__(self):
        self.nom_ = Phenicien.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Phenicien PAS FAIT"
        return u"prénom féminin Phenicien PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Phenicien PAS FAIT"

    def GenererNom(self):
        return u"nom Phenicien PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Chef {}".format(nom)

class Nordique(Civ):
    NOM = u"Nordique"

    def __init__(self):
        self.nom_ = Nordique.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Nordique PAS FAIT"
        return u"prénom féminin Nordique PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Nordique PAS FAIT"

    def GenererNom(self):
        return u"nom Nordique PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Jarl {}".format(nom)

class Germanique(Civ):
    NOM = u"Germanique"

    def __init__(self):
        self.nom_ = Germanique.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Germanique PAS FAIT"
        return u"prénom féminin Germanique PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Germanique PAS FAIT"

    def GenererNom(self):
        return u"nom Germanique PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Jarl {}".format(nom)

class Francais(Civ):
    NOM = u"Français"

    def __init__(self):
        self.nom_ = Francais.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Francais PAS FAIT"
        return u"prénom féminin Francais PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Francais PAS FAIT"

    def GenererNom(self):
        return u"nom Francais PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Cher {}".format(nom)

class Christianisme(Civ):
    NOM = u"Chrétien"

    def __init__(self):
        self.nom_ = Christianisme.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Christianisme PAS FAIT"
        return u"prénom féminin Christianisme PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Christianisme PAS FAIT"

    def GenererNom(self):
        return u"nom Christianisme PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Saint {}".format(nom)

class Russe(Civ):
    NOM = u"Russe"

    def __init__(self):
        self.nom_ = Russe.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Russe PAS FAIT"
        return u"prénom féminin Russe PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Russe PAS FAIT"

    def GenererNom(self):
        return u"nom Russe PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "??? {}".format(nom)

class Mongol(Civ):
    NOM = u"Mongol"

    def __init__(self):
        self.nom_ = Mongol.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return u"prénom masculin Mongol PAS FAIT"
        return u"prénom féminin Mongol PAS FAIT"

    def GenererNomPeuple(self):
        return u"nom peuple Mongol PAS FAIT"

    def GenererNom(self):
        return u"nom Mongol PAS FAIT"

    def GetTitreFondateur(self, situation):
        nom = Civ.GetTitreFondateur(self, situation)
        return "Khan {}".format(nom)
