NUM_MIN_COLOR=0
NUM_MAX_COLOR=4
class Carta:
    colore=""
    num=0
    csimb=""
    def __init__(self):
        import random
        valore=random.randint(NUM_MIN_COLOR,NUM_MAX_COLOR)#se 0 nero, 1=rosso 2=blu 3=verde 4=giallo
        options = [0,1, 2, 3, 4, 5,6,7,8,9,"+2", "stop", "change rotation"]
        if valore==0:
            self.colore="nero"
        elif valore==1:
            self.colore="rosso"
        elif valore==2:
            self.colore="blu"
        elif valore==3:
            self.colore="verdes"
        elif valore==4:
            self.colore="giallo"
        if self.colore!= "nero":
            self.num=random.choice(options)
        else:
            self.csimb=random.choice(["+4","+2","cambio colore"])
def GeneraCarteInizio():
    carte=[]
    for i in range(7):
        cartePlayer.append(Carta())
    for i in range(7):
        carteNemico.append(Carta())
def PescaCarta():
    carta=Carta()
    return carta
def Gioco():
    cartaInizio=Carta()
    turnoNemico=False
    while cartaInizio.colore=="nero":
        cartaInizio=Carta()
########################################################
    while len(cartePlayer) !=0 or len(carteNemico!=0):
        print("Scegli una carta dal tuo mazzo")
        print("carta sul campo=",cartaInizio.colore,cartaInizio.num)
        turnoGiocatore=True
        while turnoGiocatore:
            for i in range(len(cartePlayer)):
                if cartePlayer[i].num!=0:
                    print(f"{i}",cartePlayer[i].colore,cartePlayer[i].num)
                else:
                    print(f"{i}",cartePlayer[i].colore,cartePlayer[i].csimb)
            print(f"{len(cartePlayer)} Pesca")
            scelta=int(input("-->"))
            if scelta>=0 and scelta<len(cartePlayer):
                if cartePlayer[scelta].colore==cartaInizio.colore or cartePlayer[scelta].colore=="nero":
                    cartaInizio=cartePlayer.pop(scelta)
                    turnoGiocatore=False
                    turnoNemico=True
                else:
                    print("Carta non valida riprova")
            else:
                cartePlayer.append(Carta())
##########################################################
        while turnoNemico:
            import random
            scelta=random.randint(0,len(carteNemico))
            if scelta>=0 and scelta<len(cartePlayer):
                if carteNemico[scelta].colore==cartaInizio.colore or carteNemico[scelta].colore=="nero":
                    cartaInizio=carteNemico.pop(scelta)
                    turnoGiocatore=True
                    turnoNemico=False
                else:
                    print("Carta non valida riprova")
            else:
                carteNemico.append(Carta())
##########################################################
cartePlayer=[]
carteNemico=[]
GeneraCarteInizio()
Gioco()