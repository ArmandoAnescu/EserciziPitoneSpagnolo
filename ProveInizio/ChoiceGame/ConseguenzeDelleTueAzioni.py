nomePlayer=""
puntiKarmici=0
print("Buongiorno giocaore sei pronto per inziare la tua avventura?")
print("Dimmi, qual'è il tuo nome giovane:")
nomePlayer=input("-->:")
print(f"Bene {nomePlayer}, benvenuto nella tua nuova vita")
print("     ")
def sulSerio():
    print("In quel momento arriva il padre")
    print("la ragazzaracconta al padre delle tue gesta, il padre non è molto convinto ma accetta")
    print("Ti sposi con la nobile hai 2 figli e vivi una vita normale")
    print("Non te l'aspettevi di finire così? Beh negli altri finali capitano di quelle robe,sfortunatamente la tua depravazione ha avuto la meglio")
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