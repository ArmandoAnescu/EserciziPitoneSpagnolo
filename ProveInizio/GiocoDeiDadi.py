class Dado:
    nPunti=0
    def __init__(self,n):
        self.nFaccie=n
        self.facciausicita=0
    def generaFaccia(self):
        import random
        self.facciaUscita= random.randint(1,self.nFaccie)
def Gioco(p1,p2,nRound):
    while nRound>0:
        p1.generaFaccia()
        p2.generaFaccia()
        print(f"round{nRound}")
        print(f"Faccia giocatore 1:{p1.facciaUscita}")
        print(f"Faccia giocatore 2:{p2.facciaUscita}")
        if p1.facciaUscita>p2.facciaUscita:
            print("Vince giocatore 1")
            p1.nPunti+=1
        elif p2.facciaUscita>p1.facciaUscita:
            print("Vince giocatore 2")
            p2.nPunti+=1
        else:
            print("Pareggio")
            p1.nPunti+=1
            p2.nPunti+=1
        print("Premi invio per continuare!!!")
        input()
        nRound-=1

        

p1=Dado(n=6)
p2=Dado(n=6)
print("Quanti round volete fare??")
nRound=int(input())
Gioco(p1=p1,p2=p2,nRound=nRound)
if p1.nPunti>p2.nPunti:
    print("Vince la partita giocatore 1")
elif p2.nPunti>p1.nPunti:
    print("Vince la partita giocatore 2")
else:
    print("La partita è pareggio")