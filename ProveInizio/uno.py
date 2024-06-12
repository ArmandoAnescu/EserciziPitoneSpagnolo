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
            self.num=random.choice(["+4","cambio colore"])
def pesca(num,list):
  for i in range(num):
      list.append(Carta())
def GeneraCarteInizio():
    carte=[]
    for i in range(7):
        cartePlayer.append(Carta())
    for i in range(7):
        carteNemico.append(Carta())
def Gioco():
    cartaInizio=Carta()
    turnoNemico=False
    while cartaInizio.colore=="nero":
        cartaInizio=Carta()
########################################################
    while len(cartePlayer) !=0 and len(carteNemico)!=0:
        print("Scegli una carta dal tuo mazzo")
        print("carta sul campo=",cartaInizio.colore,cartaInizio.num)
        turnoGiocatore=True
        notStopPlayer=True
        notStopNemico=True
        while turnoGiocatore and notStopPlayer:
            for i in range(len(cartePlayer)):
                if isinstance(cartePlayer[i].num,int):
                    print(f"{i}",cartePlayer[i].colore,cartePlayer[i].num)
                else:
                    print(f"{i}",cartePlayer[i].colore,cartePlayer[i].num)
            print(f"{len(cartePlayer)} Pesca")
            scelta=int(input("-->"))
            if scelta>=0 and scelta<len(cartePlayer):
                if cartePlayer[scelta].colore==cartaInizio.colore or cartePlayer[scelta].colore=="nero" or cartaInizio.colore=="nero":
                    if isinstance(cartePlayer[scelta].num,int):
                        notStopNemico=True
                    elif cartePlayer[scelta].num=="+2" or cartePlayer[scelta].num=="+4":
                        pesca(num=int(cartePlayer[i].csimb.replace("+"," ")),list=carteNemico)
                        notStopNemico=True
                    elif cartePlayer[scelta].num=="stop":
                        notStopNemico=False
                    cartaInizio=cartePlayer.pop(scelta)
                    turnoGiocatore=False
                    turnoNemico=True
                else:
                    print("Carta non valida riprova")
            elif scelta==len(cartePlayer):
                cartePlayer.append(Carta())
                
##########################################################
        while turnoNemico and notStopNemico:
            import random
            scelta=random.randint(0,len(carteNemico))
            if scelta>=0 and scelta<len(cartePlayer):
                if carteNemico[scelta].colore==cartaInizio.colore or carteNemico[scelta].colore=="nero" or cartaInizio.colore=="nero":
                    if isinstance(cartePlayer[scelta].num,int):
                        notStopNemico=True
                    elif cartePlayer[scelta].num=="+2" or cartePlayer[scelta].num=="+4":
                        pesca(num=int(carteNemico[scelta].csimb.replace("+"," ")),list=carteNemico)
                        notStopNemico=True
                    elif cartePlayer[scelta].num=="stop":
                        notStopPlayer=False
                    turnoGiocatore=True
                    turnoNemico=False
                    cartaInizio=carteNemico.pop(scelta)
                    turnoGiocatore=True
                    turnoNemico=False
            else:
                carteNemico.append(Carta())
##########################################################
cartePlayer=[]
carteNemico=[]
GeneraCarteInizio()
Gioco()
