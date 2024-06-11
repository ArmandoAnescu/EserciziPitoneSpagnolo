nomePlayer=""
puntiKarmici=0
print("Buongiorno giocaore sei pronto per inziare la tua avventura?")
print("Dimmi, qual'è il tuo nome giovane:")
nomePlayer=input("-->:")
print(f"Bene {nomePlayer}, benvenuto nella tua nuova vita")
print("     ")
def morteFulminante():
    print("Lek Appalle insdegnata ti lancia un incantesimo di uflmine contro che ti uccide all'istante")
    print("magari ricordai l'umiltà o le buone maniere")
def sulSerio():
    print("In quel momento arriva il padre")
    print("la ragazzaracconta al padre delle tue gesta, il padre non è molto convinto ma accetta")
    print("Ti sposi con la nobile hai 2 figli e vivi una vita normale")
    print("Non te l'aspettevi di finire così? Beh negli altri finali capitano di quelle robe,sfortunatamente la tua depravazione ha avuto la meglio")
def amicaElfa():
    print("L'elfa ti ringrazia del suo aiuto e ti dice che il suo nome è Lek Appalle, e vuole sapere il tuo nome")
    print("Ti dice che è rimasta da sola e ha perso i suoi amici e non ha più soldi. Non ha soldi per mangiare o dove dormire")
    print("allora tu:")
    print("A: Le offri di vivere a casa tua finche ne ha bisogno")
    print("B: Le offri di vivere a casa tua ma deve conribuire nel lavorare nei campi [NON come schiava]")
    print("C: La porti da una tua amica che la può ospitare ")
    print("D: le ridi in faccia e te ne vai")
    scelta=input()
    if scelta=="A":
        puntiKarmici+=3
    elif scelta=="B":
        puntiKarmici+=2
    elif scelta=="C":
        puntiKarmici+=0
    else:
        morteFulminante()
    print("L'elfa è grata del tuo aiuto e si offre di fare le pulizie e cucinare mentre tu non ci sei")
    print("Dopo 3 giorni mentre torni a casa da i campi arrivi davanti a casa quando")
    print("Un famoso bandito Smazzullo Aleandro decide di rapinarti ma lek Apalle usa un incatesimo anti morroni(I morroni sono le persone che vengono dal sud del continente, solitamente ladri)")
    print("Il bandito prova a scappare ma viene catturato lo sceriffo S.M.Elon, che ringrazia Lek per l'aiuto, c'è anche un uomo di mezza età altro quanto un tronco tagliato si chiama Splinter Tumiliano")
    print("Splinter ti chiede se hai mai visto una torta rossa e va in crisi isterica, S.M.Elon ride e fa una batuta orribile, ti cheidi come questi individui siano addetti della sicurezza")
def finaleNormale():
    print("hai passato la tua vita in tranquillità e hai avauto dei figli")
def Risveglio():
    print("Ti svegli dopo una sera passata a bere con i tuoi amici e decidi di:")
    print("A: continua a dormire")
    print("B: alzati e fai colazione")
    print("C: rimane nel letto a guardare il soffito mentre sei nei tuoi pensieri")
    print("D: urli")
    scelta=input()
    if scelta=="A" or scelta=="B":
        puntiKarmici+=1
    print("Dopo aver fatto colazione decidi di andare a fare un giro nel boschetto")
    print("Mentre te la chillavi e giocavi a palword GO senti una ragazzina urlare")
    print("La ragazzina è circondata da cani randagi, cosa fai:")
    print("A: La ignori e vai avanti")
    print("B: raccogli un bastone e vai ad aiutarla e sbarazzarti dei cani")
    print("C: decidi di fare left and right con i cani con i tuoi pugni")
    print("D: scappi e chiamiaiuto")
    scelta=input()
    if scelta=="A":
        puntiKarmici-=5
    elif scelta=="B" or scelta=="C":
        puntiKarmici+=3
    else:
        puntiKarmici+=1
    print("dopo aver salvato la ragazza lei ti viene a ringraziare")
    print("dalla discussion scopre che è la figlia di un nobile in città")
    print("Allora decidi di:")
    print("A: Chiederle soldi")
    print("B: Gli dici che hai fatto il tuo dovere")
    print("C: Decidi di chiederla in sposa")
    print("D: Gli chiedi di farti fare un viaggio nella capitale")
    scelta=input()
    if scelta=="A":
        puntiKarmici+=1
    elif scelta=="B":
        puntiKarmici+=2
    elif scelta=="D":
        puntiKarmici+=2
    else:
        sulSerio()
    print("Dopo aver ricevuto il tuo premio sei felice e decidi di fare un giro per la città")
    print("Incontri una ragazza elfa, sembra persa e sull'orlo di piangere, allora tu:")
    print("A: Vai da lei e decidi di consolarla e aiutarla")
    print("B: Guardi se qualcuno prova ad aiutarla ma decidi di falo tu")
    print("C: Chiami qualcuno per aiutarla")
    print("D: Hai ricevuto il tuo premio cosa ti interessa di lei")
    scelta=input()
    if scelta=="A":
        puntiKarmici+=3
        amicaElfa()
    elif scelta=="B":
        puntiKarmici+=2
        amicaElfa()
    elif scelta=="D":
        puntiKarmici-=1
        amicaElfa()
    else:
        finaleNormale()

Risveglio()
#
#A=3 punti karmici via eroica
#B=2 punti karmici via nobile
#C=0 punto karmico via neutra
#D=-1 punto karmico via infima
#E=-2 punti karmici via peggiore
#se i punti karmici sono maggiori di 50 finale vero eroe
#se <50 ma >35 finale eroo
#se <35 ma >15 finale neutro
#se <15 ma >0 finale lurido
#se <0 finale Incubo
#finali accidnetali, finali ottenuti in base alle scelte che si voglia fare de bene o del male o entrambi possono essere all'inizio o verso la fine della storia