import random
from spe.civilisation import civ

class Celte(civ.Civ):

    NOM = u"Celte"

    PRENOMS_M =["Acedillus","Acedilu","Adbitus","Adcanaunos","Adcomaros","Adebugi","Adebugius","Adgennus","Adgenus","Adginnius",
    "Adiatorix","Adiatumarus","Adietuanus","Adietumarus","Admatius","Adnamati","Adnamatius","Adnamatus","Adretilis","Adrotus",
    "Advorix","Aesarius","Agedilicus","Agedilio","Agedilios","Agedilli","Agedillus","Agedovirus","Agisilius","Agisillus","Aicovindo",
    "Aisus","Albic","Albius","Albus","Alebece","Allecnus","Allinus","Allobroxus","Allovico","Alluci","Allucius","Alpius","Alpus",
    "Ambadus","Ambaxius","Ambilli","Ambillus","Ambilo","Ambilos","Ambimogidus","Ambisauus","Ambisavus","Ambudsuilus","Andangi",
    "Andecarius","Andecarus","Andegalli","Andegasi","Andegasus","Andereseni","Andergi","Andergos","Andolatius","Andosion","Andosten",
    "Andosteni","Andosteno","Andoston","Andreine","Anducor","Annamatus","Annamoris","Annamus","Antedrigus","Anteremius","Areobindus",
    "Arimanus","Ateano","Atecilus","Atecurus","Ategnutis","Atepatus","Atepiccus","Ateponirus","Ateponius","Ateponus","Ateratos","Atesios","Atesmertus","Atesos","Atessatis","Atesso","Atestas","Ateuritus","Atgite","Atolisus","Atporix","Atrectius","Atrectus","Atregtius","Atrextus","Atrixtos","Attectius","Atuirus","Atusonius","Audatus","Audeti","Audoenus","Audoti","Aventinius","Aventinus","Balaesus","Balatonux","Balorix","Banni","Bannio","Banu","Banui","Banuillus","Banuo","Banuus","Bellognatus","Bilicedo","Biliureto","Billiccissioni","Billicedo","Birucatus","Bocontius","Bodenia","Bodocenos","Bodocenus","Boduogenus","Bogionius","Borili","Borillus","Boritus","Borso","Borsus","Boruonicus","Borvonicus","Boudillus","Bravecci","Brigomaglos","Britomartis","Britomartus","Brocchus","Broccius","Broccus","Bussumarius","Bussumarus","Busturo","Butiro","Buturo","Cabriabantos","Cabrus","Caccuso","Cacurio","Cacurius","Cambo","Cambulus","Cambus","Camerianus","Camerinus","Camulatucus","Camulixus","Camulorigi","Caracco","Caracus","Caraddounius","Caraddounus","Caramantius","Carantacus","Carantillo","Caranto","Carantorius","Carasius","Carathounus","Caratillus","Caratodius","Cariaus","Carigo","Carigus","Carino","Carisianus","Caritosus","Carix","Caromarus","Carominius","Carucenus","Carugenus","Carulirus","Cassicius","Cassicus","Cassitalus","Cassutus","Castonius","Catabar","Catacius","Catacus","Catamandus","Catamanus","Catavignus","Caterto","Cathirix","Caticorix","Catinius","Catlus","Catonianus","Catotigirni","Catoualos","Cattabbot","Cattabus","Cattabuttas","Cattaus","Cattedius","Cattulus","Cattuvir","Cattuvvir","Catuen","Catuenus","Caturicus","Caturo","Catusius","Caurius","Caurus","Cenalus","Cenicus","Cenno","Ceno","Cenocantus","Centugeni","Centus","Cicedu","Cimarius","Cimarus","Cinge","Cinges","Cingessus","Cingetoutus","Cingius","Cintio","Cinto","Cintu","Cintugenus","Cintumarus","Cintusminius","Coaeddus","Cobledulitauus","Cobledulitavus","Coimagni","Colomagni","Comanus","Comatullus","Combaromarus","Comnertus","Conbertius","Conbertus","Conconnetodumnus","Condarillus","Condercus","Coneddus","Congenno","Congonetiacus","Congonnetiacus","Conteddius","Contesilo","Contessilo","Contoutos","Convictolitavis","Corbagni","Corio","Cornutos","Coro","Corobus","Coteus","Cotilius","Cotillus","Cotilus","Cotis","Cotius","Cottalus","Cottilus","Cottio","Cottius","Cotto","Cottro","Cottus","Cotus","Cotusus","Couertomotul","Covertomotul","Covirius","Covirus","Criciro","Criciru","Cricirus","Crigiru","Cunegni","Cunigni","Cunovicodu","Curcagni","Curcagnus","Dacotoutus","Dagillus","Dagobius","Dagomarus","Dalagni","Dannonus","Dano","Dattovir","Deoratus","Dercillos","Dercillus","Deuus","Devus","Diddignatus","Diocaitus","Diorix","Diuicatus","Divicatus","Divos","Dobagni","Doninas","Donnadu","Donnedo","Donnius","Donnotaurus","Donnus","Dovagni","Drutalus","Dubnotalus","Dubnovellaun","Dubnovellaunos","Dumnobellaunus","Dumnovellaunos","Ebicatos","Ebredus","Eburianus","Eburio","Eburius","Eburo","Elusco","Elusconos","Endouellicus","Endovellicus","Epacus","Epasius","Epatus","Epetinus","Epo","Epomedius","Epos","Epotsiorouidus","Epotsorouidus","Eppo","Eqqegni","Ercaviccas","Escengolatis","Escincos","Esumagius","Excingillius","Excingomarus","Excingullus","Exscincious","Exsomnus","Gabrius","Gabrus","Gedilli","Genetlus","Genillus","Gennalo","Girgani","Gnatusius","Grimiggni","Haesus","Iantasio","Iantinus","Iantumalius","Iantumar","Iantumarus","Iatinius","Iccalus","Iccinus","Iccnus","Icomius","Ientinus","Ientius","Iliatus","Illiomarus","Indercillus","Iotobito","Isarnouallanos","Itavus","Itosius","Itotagi","Lanianus","Laniogaius","Latauis","Leucamulo","Licno","Licnos","Licnus","Litauus","Litavis","Litgenes","Litgenus","Litigius","Litugenius","Lituriri","Losagni","Lucterius","Lugetus","Lugius","Lugurix","Macareus","Macarius","Maccarus","Maccis","Magiacos","Maglagni","Magurio","Magurius","Mailagni","Malucnus","Mando","Maritalus","Martalos","Martilinus","Martoualus","Meddignatius","Meddugnatus","Megaravico","Melmandus","Mertoualus","Mesillus","Messillus","Metilius","Metillius","Miletumarus","Moddagni","Nantonos","Nertomaros","Netacari","Nisigni","Oclicno","Oclicnos","Ollocnus","Ollognus","Onalisus","Oppianicnos","Perrius","Perrus","Peruincus","Perus","Qasigni","Qenilocgni","Regenos","Regenus","Regininus","Reginius","Reginus","Remico","Remicus","Reovalis","Reticius","Reticus","Retomarus","Rextugeos","Rigalis","Ripcicnus","Ritogenus","Rittuvvecc","Rituvvecas","Rovicus","Sacrovir","Sacrovirus","Sagillius","Sagillus","Samaconius","Samalus","Samio","Samis","Samius","Sammio","Sammo","Sammus","Samo","Samocenus","Samocinus","Samogenus","Samognatius","Samus","Sancotalus","Sanicios","Scilagni","Segolatius","Segomaros","Senecio","Senecius","Senocarus","Senovir","Senucaris","Silanus","Smertulitanus","Sollouico","Sollovico","Suadinus","Suadugenus","Suadutto","Suratus","Talagni","Talavus","Talis","Talius","Tallius","Tallus","Tallutius","Talotius","Talussanus","Talutius","Tanco","Tanotalos","Tarbunus","Taruiacus","Tascius","Tascus","Tasgetios","Tasgetius","Tauratis","Tauri","Taurio","Taurocutius","Taurou","Teutagonus","Teuto","Teutomalius","Teutomus","Totavali","Toutio","Touto","Toutobocio","Toutobocios","Toutos","Toutus","Trenacatus","Trenaccatlo","Triti","Trito","Tritos","Tritus","Trogimarus","Trouceteius","Tuticanius","Tuticanus","Ulcagni","Ulccagni","Urogenonertus","Valatonius","Valis","Vallio","Vallius","Vallo","Vallus","Vebro","Vebru","Vecatus","Vecconius","Vecius","Vectimarius","Vectimarus","Vecto","Velagenius","Velagenus","Velenius","Velitas","Velitius","Vello","Velugni","Velugnius","Vendagni","Vendogni","Venecarus","Venedius","Venextos","Venicarus","Venixamus","Venixxamus","Vennenus","Vennonius","Venucius","Vepotalus","Veqreq","Vercatus","Vercombogio","Vercombogious","Vercombogus","Versicnos","Versignos","Verter","Verto","Vertos","Vertros","Veruecco","Veruico","Veugnus","Vicatus","Vicixtillus","Victi","Viction","Vindedo","Vindicatus","Vinicarus","Vinovaleius","Viranus","Virato","Viratus","Viri","Viriacius","Viriaicus","Virianto","Viriatis","Viriatius","Virici","Virico","Viriodacus","Virisimi","Virlus","Virocantus","Vironianus","Virotalus","Virotutus","Vitousurix","Vlatcani","Vlatos","Vlatucni","Vlatucnos","Vlatugni","Vocagni","Vocarantus","Vocorix","Vogitoutus","Voltodaga","Vopiscus","Voretouirius","Voretoviros","Vosegus","Vridolanos","Vrittakos"]

    PRENOMS_F = ["Abrezta","Acca","Acisillia","Adbugiouna","Adbugissa","Adginna","Adgonna","Adiania","Adianta","Admata","Adnama","Adnamata","Adnamatia",
    u"Adnamita","Adnamu","Adreticia","Aduorix","Advorix","Aesica","Aesiua","Agedia","Agisiaca","Agisilia","Agisilla","Aisa","Albina","Albisia","Albucia",
    u"Aleasiumara","Alla","Alleicea","Alleticia","Allia","Allouira","Allusa","Alpina","Alpinia","Alpinula","Alteurita","Ambada","Andaitia","Andarta",
    u"Andebrocirix","Andeca","Anderca","Anderica","Anderina","Anderitia","Andilia","Andoca","Andueia","Anduenna","Annama","Ariola","Arrotala","Arsulana",
    u"Atebodua","Atectorigiana","Ategenta","Ategnissa","Atepa","Atepu","Atessatia","Atestatia","Atestia","Ateurita","Atigenta","Atioxta","Atreba","Atrebia",
    u"Attisaga","Atturita","Auamacimaria","Audata","Audenta","Auentina","Aulricmara","Aventina","Avitianomara","Balatonaua","Ballatulla","Banna","Bannua",
    u"Banona","Betudaca","Bileseton","Bilisa","Billia","Bimottia","Bitudaga","Bora","Borissa","Boudenna","Boudilla","Boudinna","Brocchia","Brogimara",
    u"Buscilla","Bussia","Bussugnata","Cabrilla","Cabura","Caburena","Caccosa","Cacossa","Cacudia","Cambaria","Cambosa","Camelognata","Camolatia",
    u"Camoulatia","Camula","Camulata","Camulatia","Camuledu","Camulia","Camulilia","Camullia","Cantexta","Caraddouna","Caranta","Carantana","Carantia",
    u"Carantiana","Carantila","Carantilla","Carantina","Carantodia","Carantusa","Carata","Caratila","Caratilla","Caratulla","Careia","Carenta","Caretosa",
    u"Caria","Carina","Carisia","Carissa","Carosa","Carosia","Carrotala","Cartulla","Caruca","Caruiliena","Caruonia","Cassa","Cassia","Cassibodua","Cassicia",
    u"Cassimara","Cassiola","Casticia","Castina","Cata","Catalia","Catia","Catica","Catilia","Catilla","Catiola","Catnea","Catronia","Catta","Cattara",
    u"Cattea","Cattia","Cattira","Cattulla","Cattuviqqa","Catuallauna","Catucia","Catulla","Catullia","Caturica","Caturigia","Caturisa","Cauaria","Caura",
    u"Cauru","Cavaria","Cenia","Ceniuria","Cenos","Censonia","Centa","Centogenea","Centusmia","Cigemma","Cincia","Cincissa","Cingetissa","Cinia","Cintucra",
    u"Cintugena","Cintusma","Cintusmina","Cintussa","Cintussia","Cloutina","Clutamilla","Cobiatia","Coblanuo","Coblucia","Cobnerta","Cobromara","Cobronia",
    u"Cobruna","Comacia","Comatia","Comatimara","Comatulla","Combara","Comerta","Comiomara","Condexua","Congenetia","Congenncia","Consuadullia","Contessia",
    u"Corasia","Corobilla","Corrodu","Cotina","Cotira","Cotta","Cottia","Cottina","Cottira","Cottula","Cotu","Cotuconi","Cotulia","Counerta","Cricconia",
    u"Cubria","Cunacena","Dagania","Dania","Danissa","Dannia","Dannumaa","Danotala","Danu","Deiotariana","Derceia","Deuila","Deuillia","Deuognata",
    u"Devignata","Diona","Diorata","Diougenia","Diuilla","Diuuogna","Diuvogna","Diveca","Divogenia","Donilla","Donisia","Dubna","Dubnia","Dumnana","Dumnia",
    u"Eburia","Eburila","Eliomara","Elovissa","Elvissa","Emogenia","Epa","Epetina","Epia","Epilla","Epillia","Epiu","Eppa","Eppacta","Eppaxtia","Eppia",
    u"Epponina","Etiona","Etolugnia","Exapia","Excinga","Excingilla","Exobna","Exomna","Exouna","Fimmilene","Friagabi","Gabra","Genaca","Genetodia","Genna",
    u"Genobia","Genucia","Gnata","Gnatia","Gnatilla","Iantulla","Iantumara","Iatta","Iattossa","Ibliomaria","Iccia","Ilateuta","Inatura","Inderca","Indercilea",
    u"Isosae","Itta","Kareia","Karina","Lanpendia","Larma","Leuca","Leucena","Leucimara","Leucona","Leuconia","Litania","Litogena","Littiossa","Litu",
    u"Litua","Litucca","Lituccia","Litugena","Litullina","Loucita","Loucitta","Lugiola","Luppa","Macaria","Maccira","Maccirra","Magunia","Magunna","Magusatia",
    u"Mandelana","Manduilla","Manduissa","Marilla","Martidia","Martilia","Martiria","Martna","Mata","Mataura","Materiona","Matia","Maticia","Matidia","Matina",
    u"Matona","Matonia","Matta","Mattia","Mattosa","Mattua","Matua","Matucenia","Matucia","Matugena","Matugenia","Matullina","Matuna","Medilotamica","Medlotama",
    u"Meducena","Melicia","Meliginna","Messilia","Messilla","Metela","Metilia","Moria","Moriena","Mottu","Motuca","Motuidiaca","Nama","Namia","Namidia",
    u"Namiola","Namma","Nammia","Nammota","Namu","Namusa","Namuta","Nantia","Nantiorix","Nemetocena","Nemetogena","Nerta","Nertilla","Nertomaria","Netelia",
    u"Nitiogenna","Ollia","Olliadu","Olluna","Olugnia","Orbia","Orbiana","Orbissa","Origena","Oxidubna","Pera","Perra","Peruia","Perula","Rega","Regallia",
    u"Regina","Reginia","Regula","Rematia","Resia","Ressatu","Ressilla","Ressona","Resta","Restia","Reticiana","Rextugeniana","Riceina","Ricina","Ricua",
    u"Riguiru","Rikua","Ritomara","Ritulla","Ritumara","Rituscia","Rotama","Rotania","Sagila","Sagillia","Sama","Samacia","Samaxa","Samia","Samianta",
    u"Samicantu","Samicia","Saminia","Samma","Sammia","Sammiola","Sammola","Sammulla","Samuda","Sattomata","Sedata","Sedatia","Sedecennis","Sedia","Sedida",
    u"Segla","Segolia","Segusiaua","Senila","Senilla","Sennaucia","Senocenna","Senodona","Senodonna","Sila","Solimara","Suadugena","Suaduilla","Suadulla",
    u"Suagria","Suausia","Sucaria","Sueta","Sumaria","Sumela","Sumelia","Sumenu","Talauia","Talavica","Taliounia","Talisia","Talissa","Taluppa","Talussa",
    u"Tancina","Tancorix","Tascilla","Tasgilia","Tasgilla","Tauria","Taurica","Taurilla","Taurina","Teolugnia","Teuta","Teutalu","Teutana","Trita","Tritia",
    u"Trocina","Troucetissa","Troucisa","Troucissa","Valagenta","Valeia","Valicinia","Vallia","Vandania","Vebromara","Vebronara","Vebrumma","Veca","Vecticia",
    u"Vectinia","Velacena","Velacosta","Veleda","Velitia","Vellibia","Vena","Venaesia","Venia","Veniala","Venica","Venicia","Veniena","Venimara","Veninia",
    u"Venisama","Veniuallia","Venivallia","Venixama","Venixema","Venixiema","Venna","Vennonia","Venulanta","Venuleia","Verbronara","Verica","Verodumna",
    u"Vertia","Verucia","Vicana","Viccu","Viccus","Victisarana","Victulliena","Vindaina","Vindama","Vindauscia","Vindilla","Vindoinissa","Vindu","Viniuallia",
    u"Viralira","Viratia","Viriana","Viriata","Viricia","Viriciu","Viriola","Viriondaga","Virodu","Virotouta","Visurix","Vlattia","Vlattu","Vlatuna","Vocara",
    u"Vocontia","Volatia","Vritea","Vrittia","Vrogenia"]

    NOMS_PEUPLES = [u"Boïens", u"Lingons", u"Sénons", u"Rèmes", u"Santones", u"Ceutrones", u"Turones", u"Tricasses", u"Parisii", u"Carnutes", u"Meldes", u" Aulerques Brannovices", u"Bituriges Cubes", u"Éduens", u"Séquanes",
    u"Carni", u"Cénomans", u"Insubres", u"Taurins", u"Anares", u"Comasques", u"Laevi", u"Lépontiens", u"Libici", u"Marici", u"Orobiens", u"Salasses", u"Aduatuques", u"Ambiens",
    u"Atrebates", u"Bellovaques", u"Caeroesi", u"Calètes", u"Catalaunes", u"Catuslogues", u"Condruses", u"Éburons", u"Geidumnes", u"Leuques", u"Médiomatriques", u"Ménapiens", u"Morins", u"Nerviens", u"Pémanes",
    u"Rèmes", u"Sègnes", u"Silvanectes", u"Suessions", u"Tongres", u"Trévires", u"Tricasses", u"Viromanduens", u"Abrincates", u"Ambarres", u"Ambilatres" ,u"Ambivarètes" ,u"Andecaves", u"Aulerques Brannovices",
    u"Aulerques Cénomans", u"Aulerques Diablintes", u"Aulerques Éburovices", u"Bajocasses", u"Bituriges Cubes", u"Blannovii", u"Cadurques", u"Cénomans", u"Coriosolites", u"Éduens", u"Gabales", u"Helviens", u"Lémovices",
    u"Lexoviens,Lingons", u"Meldes", u"Mandubiens", u"Namnètes", u"Osismes", u"Parisii", u"Petrocores", u"Riedones", u"Rutènes", u"Santons", u"Ségusiaves", u"Sénons", u"Séquanes", u"Turons", u"Unelles", u"Vadicasses",
    u"Vellaves", u"Vénètes", u"Véliocasses", u"Viducasses", u"Agésinates", u"Arvernes", u"Bituriges Vivisques", u"Nitiobroges", u"Pictons ", u"Ausques", u"Bénéharnais", u"Biguerres", u"Boïates", u"Campanii",
    u"Cocosates", u"Consorans", u"Convènes", u"Elusates", u"Garoumnes", u"Gates", u"Llourais", u"Lactorates", u"Onesii", u"Oscidates", u"Ptianiens", u"Sotiates", u"Suburates", u"Tarbelles", u"Tarusates", u"Vocates", u"Vernani",
    u"Albiques", u"Allobroges", u"Atacini", u"Bodiontiques", u"Brigiani", u"Cambolectri Atlantici", u"Caturiges", u"Cavares", u"Ceutrons", u"Helviens", u"Médulles", u"Mémines", u"Salyens", u"Sardones", u"Segovellaunes",
    u"Tricastins", u"Vertamocores", u"Voconces", u"Volques Arécomiques", u"Volques Tectosages ", u"Rauraques", u"Ubiens", u"Breunes", u"Cotini", u"Eravisces", u"Helvètes", u"Hercuniates", u"Iapodes",
    u"Istriens", u"Latobices", u"Liburniens", u"Nantuates", u"Rhètes", u"Scordiques", u"Sédunes", u"Taurisques  Tulinges", u"Tylènes", u"Ubères", u"Vendéliques", u"Veragri", u" Ancalites", u"Atrebates",
    u"Belgae", u"Bibroques", u"Brigantes", u"Caereni", u"Caledones", u"Cantiaci", u"Carnonacae", u"Carvetii", u"Cassi", u"Catuvellauni", u"Corionototae", u"Coritani", u"Cornovii", u"Darini", u"Deceangli",
    u"Demetae", u"Dobunni", u"Dumnonii", u"Durotriges", u"Epidii", u"Gangani", u"Icènes", u"Lugi", u"Ordovices", u"Regnenses", u"Segontiaques", u"Selgovae", u"Setantii", u"Silures", u"Smertae", u"Taexali",
    u"Trinovantes", u"Vacomagi", u"Venicones", u"Votadini", u"Autini", u"Brigantes", u"Cauci", u"Coriondi", u"Cruithin", u"Darini", u"Domnainn", u"Eblani", u"Erdinii", u"Gangani", u"Iberni", u"Luceni", u"Menapii",
    u"Nagnate", u"Rhobogdi", u"Uterni", u"Velabri", u"Vennicni", u"Vodiae", u"Ulaid", u"Tectosages", u"Tolistobogiens", u"Trocmes"]

    def __init__(self):
        self.nom_ = Celte.NOM

    def GenererPrenom(self, masculin):
        if masculin:
            return random.choice(Celte.PRENOMS_M)
        return random.choice(Celte.PRENOMS_F)

    def GenererNomPeuple(self):
        return random.choice(Celte.NOMS_PEUPLES)

    def GenererImagePerso(self, masculin, age):
        if masculin:
            return "celte_m_20_50"
        else:
            return "celte_f_20_40"

    def GenererNom(self):
        return u""

    def GetTitreFondateur(self, situation):
        nom = civ.Civ.GetTitreFondateur(self, situation)
        return "Grand Druide {}".format(nom)
