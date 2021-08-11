import random

class Civ:
    C_CIV = u"Civilisation"

    def __init__(self):
        self.nom_ = u"pas de nom de civilisation, doit être overridé"

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return u"Civilisation : {}".format(self.nom_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return u"{}".format(self.nom_)

    def GenererPrenom(self, masculin):
        if masculin:
            return u"Pas de prénom masculin, doit être overridé"
        return u"Pas de prénom féminin, doit être overridé"

    def GenererNom(self):
        return u"Pas de nom, doit être overridé"

    def GenererPatronyme(self, masculin):
        prenom = self.GenererPrenom(masculin)
        return "{} {}".format(prenom, self.GenererNom())

class Celte(Civ):

    NOM = u"Celte"

    PRENOMS_M =["Acedillus","Acedilu","Adbitus","Adcanaunos","Adcomaros","Adebugi","Adebugius","Adgennus","Adgenus","Adginnius",
    "Adiatorix","Adiatumarus","Adietuanus","Adietumarus","Admatius","Adnamati","Adnamatius","Adnamatus","Adretilis","Adrotus",
    "Advorix","Aesarius","Agedilicus","Agedilio","Agedilios","Agedilli","Agedillus","Agedovirus","Agisilius","Agisillus","Aicovindo",
    "Aisus","Albic","Albius","Albus","Alebece","Allecnus","Allinus","Allobroxus","Allovico","Alluci","Allucius","Alpius","Alpus",
    "Ambadus","Ambaxius","Ambilli","Ambillus","Ambilo","Ambilos","Ambimogidus","Ambisauus","Ambisavus","Ambudsuilus","Andangi",
    "Andecarius","Andecarus","Andegalli","Andegasi","Andegasus","Andereseni","Andergi","Andergos","Andolatius","Andosion","Andosten",
    "Andosteni","Andosteno","Andoston","Andreine","Anducor","Annamatus","Annamoris","Annamus","Antedrigus","Anteremius","Areobindus",
    "Arimanus","Ateano","Atecilus","Atecurus","Ategnutis","Atepatus","Atepiccus","Ateponirus","Ateponius","Ateponus","Ateratos","Atesios","Atesmertus","Atesos","Atessatis","Atesso","Atestas","Ateuritus","Atgite","Atolisus","Atporix","Atrectius","Atrectus","Atregtius","Atrextus","Atrixtos","Attectius","Atuirus","Atusonius","Audatus","Audeti","Audoenus","Audoti","Aventinius","Aventinus","Balaesus","Balatonux","Balorix","Banni","Bannio","Banu","Banui","Banuillus","Banuo","Banuus","Bellognatus","Bilicedo","Biliureto","Billiccissioni","Billicedo","Birucatus","Bocontius","Bodenia","Bodocenos","Bodocenus","Boduogenus","Bogionius","Borili","Borillus","Boritus","Borso","Borsus","Boruonicus","Borvonicus","Boudillus","Bravecci","Brigomaglos","Britomartis","Britomartus","Brocchus","Broccius","Broccus","Bussumarius","Bussumarus","Busturo","Butiro","Buturo","Cabriabantos","Cabrus","Caccuso","Cacurio","Cacurius","Cambo","Cambulus","Cambus","Camerianus","Camerinus","Camulatucus","Camulixus","Camulorigi","Caracco","Caracus","Caraddounius","Caraddounus","Caramantius","Carantacus","Carantillo","Caranto","Carantorius","Carasius","Carathounus","Caratillus","Caratodius","Cariaus","Carigo","Carigus","Carino","Carisianus","Caritosus","Carix","Caromarus","Carominius","Carucenus","Carugenus","Carulirus","Cassicius","Cassicus","Cassitalus","Cassutus","Castonius","Catabar","Catacius","Catacus","Catamandus","Catamanus","Catavignus","Caterto","Cathirix","Caticorix","Catinius","Catlus","Catonianus","Catotigirni","Catoualos","Cattabbot","Cattabus","Cattabuttas","Cattaus","Cattedius","Cattulus","Cattuvir","Cattuvvir","Catuen","Catuenus","Caturicus","Caturo","Catusius","Caurius","Caurus","Cenalus","Cenicus","Cenno","Ceno","Cenocantus","Centugeni","Centus","Cicedu","Cimarius","Cimarus","Cinge","Cinges","Cingessus","Cingetoutus","Cingius","Cintio","Cinto","Cintu","Cintugenus","Cintumarus","Cintusminius","Coaeddus","Cobledulitauus","Cobledulitavus","Coimagni","Colomagni","Comanus","Comatullus","Combaromarus","Comnertus","Conbertius","Conbertus","Conconnetodumnus","Condarillus","Condercus","Coneddus","Congenno","Congonetiacus","Congonnetiacus","Conteddius","Contesilo","Contessilo","Contoutos","Convictolitavis","Corbagni","Corio","Cornutos","Coro","Corobus","Coteus","Cotilius","Cotillus","Cotilus","Cotis","Cotius","Cottalus","Cottilus","Cottio","Cottius","Cotto","Cottro","Cottus","Cotus","Cotusus","Couertomotul","Covertomotul","Covirius","Covirus","Criciro","Criciru","Cricirus","Crigiru","Cunegni","Cunigni","Cunovicodu","Curcagni","Curcagnus","Dacotoutus","Dagillus","Dagobius","Dagomarus","Dalagni","Dannonus","Dano","Dattovir","Deoratus","Dercillos","Dercillus","Deuus","Devus","Diddignatus","Diocaitus","Diorix","Diuicatus","Divicatus","Divos","Dobagni","Doninas","Donnadu","Donnedo","Donnius","Donnotaurus","Donnus","Dovagni","Drutalus","Dubnotalus","Dubnovellaun","Dubnovellaunos","Dumnobellaunus","Dumnovellaunos","Ebicatos","Ebredus","Eburianus","Eburio","Eburius","Eburo","Elusco","Elusconos","Endouellicus","Endovellicus","Epacus","Epasius","Epatus","Epetinus","Epo","Epomedius","Epos","Epotsiorouidus","Epotsorouidus","Eppo","Eqqegni","Ercaviccas","Escengolatis","Escincos","Esumagius","Excingillius","Excingomarus","Excingullus","Exscincious","Exsomnus","Gabrius","Gabrus","Gedilli","Genetlus","Genillus","Gennalo","Girgani","Gnatusius","Grimiggni","Haesus","Iantasio","Iantinus","Iantumalius","Iantumar","Iantumarus","Iatinius","Iccalus","Iccinus","Iccnus","Icomius","Ientinus","Ientius","Iliatus","Illiomarus","Indercillus","Iotobito","Isarnouallanos","Itavus","Itosius","Itotagi","Lanianus","Laniogaius","Latauis","Leucamulo","Licno","Licnos","Licnus","Litauus","Litavis","Litgenes","Litgenus","Litigius","Litugenius","Lituriri","Losagni","Lucterius","Lugetus","Lugius","Lugurix","Macareus","Macarius","Maccarus","Maccis","Magiacos","Maglagni","Magurio","Magurius","Mailagni","Malucnus","Mando","Maritalus","Martalos","Martilinus","Martoualus","Meddignatius","Meddugnatus","Megaravico","Melmandus","Mertoualus","Mesillus","Messillus","Metilius","Metillius","Miletumarus","Moddagni","Nantonos","Nertomaros","Netacari","Nisigni","Oclicno","Oclicnos","Ollocnus","Ollognus","Onalisus","Oppianicnos","Perrius","Perrus","Peruincus","Perus","Qasigni","Qenilocgni","Regenos","Regenus","Regininus","Reginius","Reginus","Remico","Remicus","Reovalis","Reticius","Reticus","Retomarus","Rextugeos","Rigalis","Ripcicnus","Ritogenus","Rittuvvecc","Rituvvecas","Rovicus","Sacrovir","Sacrovirus","Sagillius","Sagillus","Samaconius","Samalus","Samio","Samis","Samius","Sammio","Sammo","Sammus","Samo","Samocenus","Samocinus","Samogenus","Samognatius","Samus","Sancotalus","Sanicios","Scilagni","Segolatius","Segomaros","Senecio","Senecius","Senocarus","Senovir","Senucaris","Silanus","Smertulitanus","Sollouico","Sollovico","Suadinus","Suadugenus","Suadutto","Suratus","Talagni","Talavus","Talis","Talius","Tallius","Tallus","Tallutius","Talotius","Talussanus","Talutius","Tanco","Tanotalos","Tarbunus","Taruiacus","Tascius","Tascus","Tasgetios","Tasgetius","Tauratis","Tauri","Taurio","Taurocutius","Taurou","Teutagonus","Teuto","Teutomalius","Teutomus","Totavali","Toutio","Touto","Toutobocio","Toutobocios","Toutos","Toutus","Trenacatus","Trenaccatlo","Triti","Trito","Tritos","Tritus","Trogimarus","Trouceteius","Tuticanius","Tuticanus","Ulcagni","Ulccagni","Urogenonertus","Valatonius","Valis","Vallio","Vallius","Vallo","Vallus","Vebro","Vebru","Vecatus","Vecconius","Vecius","Vectimarius","Vectimarus","Vecto","Velagenius","Velagenus","Velenius","Velitas","Velitius","Vello","Velugni","Velugnius","Vendagni","Vendogni","Venecarus","Venedius","Venextos","Venicarus","Venixamus","Venixxamus","Vennenus","Vennonius","Venucius","Vepotalus","Veqreq","Vercatus","Vercombogio","Vercombogious","Vercombogus","Versicnos","Versignos","Verter","Verto","Vertos","Vertros","Veruecco","Veruico","Veugnus","Vicatus","Vicixtillus","Victi","Viction","Vindedo","Vindicatus","Vinicarus","Vinovaleius","Viranus","Virato","Viratus","Viri","Viriacius","Viriaicus","Virianto","Viriatis","Viriatius","Virici","Virico","Viriodacus","Virisimi","Virlus","Virocantus","Vironianus","Virotalus","Virotutus","Vitousurix","Vlatcani","Vlatos","Vlatucni","Vlatucnos","Vlatugni","Vocagni","Vocarantus","Vocorix","Vogitoutus","Voltodaga","Vopiscus","Voretouirius","Voretoviros","Vosegus","Vridolanos","Vrittakos"]

    PRENOMS_F=["Abrezta","Acca","Acisillia","Adbugiouna","Adbugissa","Adginna","Adgonna","Adiania","Adianta","Admata","Adnama","Adnamata","Adnamatia","Adnamita","Adnamu","Adreticia","Aduorix","Advorix","Aesica","Aesiua","Agedia","Agisiaca","Agisilia","Agisilla","Aisa","Albina","Albisia","Albucia","Aleasiumara","Alla","Alleicea","Alleticia","Allia","Allouira","Allusa","Alpina","Alpinia","Alpinula","Alteurita","Ambada","Andaitia","Andarta","Andebrocirix","Andeca","Anderca","Anderica","Anderina","Anderitia","Andilia","Andoca","Andueia","Anduenna","Annama","Ariola","Arrotala","Arsulana","Atebodua","Atectorigiana","Ategenta","Ategnissa","Atepa","Atepu","Atessatia","Atestatia","Atestia","Ateurita","Atigenta","Atioxta","Atreba","Atrebia","Attisaga","Atturita","Auamacimaria","Audata","Audenta","Auentina","Aulricmara","Aventina","Avitianomara","Balatonaua","Ballatulla","Banna","Bannua","Banona","Betudaca","Bileseton","Bilisa","Billia","Bimottia","Bitudaga","Bora","Borissa","Boudenna","Boudilla","Boudinna","Brocchia","Brogimara","Buscilla","Bussia","Bussugnata","Cabrilla","Cabura","Caburena","Caccosa","Cacossa","Cacudia","Cambaria","Cambosa","Camelognata","Camolatia","Camoulatia","Camula","Camulata","Camulatia","Camuledu","Camulia","Camulilia","Camullia","Cantexta","Caraddouna","Caranta","Carantana","Carantia","Carantiana","Carantila","Carantilla","Carantina","Carantodia","Carantusa","Carata","Caratila","Caratilla","Caratulla","Careia","Carenta","Caretosa","Caria","Carina","Carisia","Carissa","Carosa","Carosia","Carrotala","Cartulla","Caruca","Caruiliena","Caruonia","Cassa","Cassia","Cassibodua","Cassicia","Cassimara","Cassiola","Casticia","Castina","Cata","Catalia","Catia","Catica","Catilia","Catilla","Catiola","Catnea","Catronia","Catta","Cattara","Cattea","Cattia","Cattira","Cattulla","Cattuviqqa","Catuallauna","Catucia","Catulla","Catullia","Caturica","Caturigia","Caturisa","Cauaria","Caura","Cauru","Cavaria","Cenia","Ceniuria","Cenos","Censonia","Centa","Centogenea","Centusmia","Cigemma","Cincia","Cincissa","Cingetissa","Cinia","Cintucra","Cintugena","Cintusma","Cintusmina","Cintussa","Cintussia","Cloutina","Clutamilla","Cobiatia","Coblanuo","Coblucia","Cobnerta","Cobromara","Cobronia","Cobruna","Comacia","Comatia","Comatimara","Comatulla","Combara","Comerta","Comiomara","Condexua","Congenetia","Congenncia","Consuadullia","Contessia","Corasia","Corobilla","Corrodu","Cotina","Cotira","Cotta","Cottia","Cottina","Cottira","Cottula","Cotu","Cotuconi","Cotulia","Counerta","Cricconia","Cubria","Cunacena","Dagania","Dania","Danissa","Dannia","Dannumaa","Danotala","Danu","Deiotariana","Derceia","Deuila","Deuillia","Deuognata","Devignata","Diona","Diorata","Diougenia","Diuilla","Diuuogna","Diuvogna","Diveca","Divogenia","Donilla","Donisia","Dubna","Dubnia","Dumnana","Dumnia","Eburia","Eburila","Eliomara","Elovissa","Elvissa","Emogenia","Epa","Epetina","Epia","Epilla","Epillia","Epiu","Eppa","Eppacta","Eppaxtia","Eppia","Epponina","Etiona","Etolugnia","Exapia","Excinga","Excingilla","Exobna","Exomna","Exouna","Fimmilene","Friagabi","Gabra","Genaca","Genetodia","Genna","Genobia","Genucia","Gnata","Gnatia","Gnatilla","Iantulla","Iantumara","Iatta","Iattossa","Ibliomaria","Iccia","Ilateuta","Inatura","Inderca","Indercilea","Isosae","Itta","Kareia","Karina","Lanpendia","Larma","Leuca","Leucena","Leucimara","Leucona","Leuconia","Litania","Litogena","Littiossa","Litu","Litua","Litucca","Lituccia","Litugena","Litullina","Loucita","Loucitta","Lugiola","Luppa","Macaria","Maccira","Maccirra","Magunia","Magunna","Magusatia","Mandelana","Manduilla","Manduissa","Marilla","Martidia","Martilia","Martiria","Martna","Mata","Mataura","Materiona","Matia","Maticia","Matidia","Matina","Matona","Matonia","Matta","Mattia","Mattosa","Mattua","Matua","Matucenia","Matucia","Matugena","Matugenia","Matullina","Matuna","Medilotamica","Medlotama","Meducena","Melicia","Meliginna","Messilia","Messilla","Metela","Metilia","Moria","Moriena","Mottu","Motuca","Motuidiaca","Nama","Namia","Namidia","Namiola","Namma","Nammia","Nammota","Namu","Namusa","Namuta","Nantia","Nantiorix","Nemetocena","Nemetogena","Nerta","Nertilla","Nertomaria","Netelia","Nitiogenna","Ollia","Olliadu","Olluna","Olugnia","Orbia","Orbiana","Orbissa","Origena","Oxidubna","Pera","Perra","Peruia","Perula","Rega","Regallia","Regina","Reginia","Regula","Rematia","Resia","Ressatu","Ressilla","Ressona","Resta","Restia","Reticiana","Rextugeniana","Riceina","Ricina","Ricua","Riguiru","Rikua","Ritomara","Ritulla","Ritumara","Rituscia","Rotama","Rotania","Sagila","Sagillia","Sama","Samacia","Samaxa","Samia","Samianta","Samicantu","Samicia","Saminia","Samma","Sammia","Sammiola","Sammola","Sammulla","Samuda","Sattomata","Sedata","Sedatia","Sedecennis","Sedia","Sedida","Segla","Segolia","Segusiaua","Senila","Senilla","Sennaucia","Senocenna","Senodona","Senodonna","Sila","Solimara","Suadugena","Suaduilla","Suadulla","Suagria","Suausia","Sucaria","Sueta","Sumaria","Sumela","Sumelia","Sumenu","Talauia","Talavica","Taliounia","Talisia","Talissa","Taluppa","Talussa","Tancina","Tancorix","Tascilla","Tasgilia","Tasgilla","Tauria","Taurica","Taurilla","Taurina","Teolugnia","Teuta","Teutalu","Teutana","Trita","Tritia","Trocina","Troucetissa","Troucisa","Troucissa","Valagenta","Valeia","Valicinia","Vallia","Vandania","Vebromara","Vebronara","Vebrumma","Veca","Vecticia","Vectinia","Velacena","Velacosta","Veleda","Velitia","Vellibia","Vena","Venaesia","Venia","Veniala","Venica","Venicia","Veniena","Venimara","Veninia","Venisama","Veniuallia","Venivallia","Venixama","Venixema","Venixiema","Venna","Vennonia","Venulanta","Venuleia","Verbronara","Verica","Verodumna","Vertia","Verucia","Vicana","Viccu","Viccus","Victisarana","Victulliena","Vindaina","Vindama","Vindauscia","Vindilla","Vindoinissa","Vindu","Viniuallia","Viralira","Viratia","Viriana","Viriata","Viricia","Viriciu","Viriola","Viriondaga","Virodu","Virotouta","Visurix","Vlattia","Vlattu","Vlatuna","Vocara","Vocontia","Volatia","Vritea","Vrittia","Vrogenia"]

    def __init__(self):
        self.nom_ = Celte.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return random.choice(Celte.PRENOMS_M)
        return random.choice(Celte.PRENOMS_F)

    def GenererNom(self):
        return u""

class CollectionCivs:

    def __init__(self):
        self.lCivs_ = dict()

        celte = Celte()
        self.SetCiv(Celte.NOM, celte)

    def __getitem__(self, idCiv):
        # assert not idPeuple in self.lPeuples_, u"Pas de peuple '{}'".format(idPeuple)
        return self.lCivs_[idCiv]

    def __setitem__(self, idCiv, civ):
        self.SetCiv(idCiv, civ)

    def SetCiv (self, idCiv, civ):
        self.lCivs_[idCiv] = civ

    def __len__(self):
        return len(self.lCivs_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lCivs_) == 0:
            return "Aucune civilisation."
        str = u"Liste de toutes les civilisations : "
        for civ in self.lCivs_:
            str = str + civ + ","
        return str
